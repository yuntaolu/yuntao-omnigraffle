#!/usr/bin/env python3
"""Summarize native OmniGraffle structure without modifying the source."""
import argparse
import collections
import json
import plistlib
import tempfile
import zipfile
from pathlib import Path


def inspect(path):
    path = Path(path)
    if path.is_dir():
        raw = (path / 'data.plist').read_bytes()
    elif zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as archive:
            raw = archive.read('data.plist')
    else:
        raw = path.read_bytes()
    data = plistlib.loads(raw)
    sheets = data.get('Sheets', [data])
    graphics = []
    def walk(items):
        for item in items:
            graphics.append(item)
            walk(item.get('Graphics', []))
    for sheet in sheets:
        walk(sheet.get('GraphicsList', []))
    classes = collections.Counter(g.get('Class', 'Unknown') for g in graphics)
    fills = collections.Counter()
    fonts = collections.Counter()
    for g in graphics:
        fill = g.get('Style', {}).get('fill', {})
        color = fill.get('Color', {})
        if fill.get('Draws') != 'NO' and all(k in color for k in ('r', 'g', 'b')):
            rgb = [round(float(color[k]) * 255) for k in ('r', 'g', 'b')]
            fills['#' + ''.join(f'{max(0, min(255, v)):02X}' for v in rgb)] += 1
        f = g.get('FontInfo', {})
        if f.get('Font'):
            fonts[f"{f['Font']} @ {f.get('Size', '?')}pt"] += 1
    lines = [g for g in graphics if g.get('Class') == 'LineGraphic']
    return {
        'canvases': len(sheets), 'native_objects_recursive': len(graphics),
        'classes': dict(classes),
        'attached_lines': sum(bool(g.get('Head', {}).get('ID')) and bool(g.get('Tail', {}).get('ID')) for g in lines),
        'rgb_fills': dict(fills.most_common()), 'font_info': dict(fonts.most_common()),
        'note': 'FontInfo is a summary; rich-text runs and PDF fonts need separate checks. RGB tokens do not normalize ICC profiles or alpha compositing.'
    }


def self_test():
    data = {'Sheets': [{'GraphicsList': [
        {'Class': 'Group', 'Graphics': [{'Class': 'ShapedGraphic', 'ID': 1}, {'Class': 'ShapedGraphic', 'ID': 2}]},
        {'Class': 'LineGraphic', 'Head': {'ID': 1}, 'Tail': {'ID': 2}},
        {'Class': 'LineGraphic'}]}]}
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp); raw = plistlib.dumps(data)
        (p/'flat.graffle').write_bytes(raw)
        (p/'bundle.graffle').mkdir(); (p/'bundle.graffle/data.plist').write_bytes(raw)
        with zipfile.ZipFile(p/'zip.graffle', 'w') as z: z.writestr('data.plist', raw)
        results = [inspect(p/name) for name in ['flat.graffle', 'bundle.graffle', 'zip.graffle']]
        assert results[0] == results[1] == results[2]
        assert results[0]['native_objects_recursive'] == 5
        assert results[0]['attached_lines'] == 1
    print('PASS: flat, package and zipped files; recursive groups; attached/free lines.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test: self_test()
    elif args.path: print(json.dumps(inspect(args.path), indent=2))
    else: parser.error('provide a .graffle path or --self-test')
