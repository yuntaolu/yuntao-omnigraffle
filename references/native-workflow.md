# Tested native workflow

Verified in OmniGraffle 7.26 on macOS. Consult **Automation → API Reference** for the installed version. The reference window's export icon can save API documentation locally; do not guess property names or redistribute the entire vendor manual in a skill.

## Application console

Open **Automation → Show Console**. The active document's first canvas is:

```javascript
const c = document.portfolio.canvases[0];
```

`document.canvases` is not the OmniGraffle 7.26 API. A new document can be created with `Document.makeNewAndShow()`; reopen its own console before executing a drawing script so the script acts on the intended document.

A reviewed local JavaScript file may be loaded through a system file picker:

```javascript
new FilePicker().show()
  .then(urls => eval(FileWrapper.fromURL(urls[0]).contents.toString()))
  .catch(e => console.log(String(e), e.stack));
```

Select only the script prepared and reviewed for the task. This intentionally executes code inside OmniGraffle. Do not apply it to an untrusted downloaded file. Direct `URL.fromPath(path, false)` reads can fail because the macOS application sandbox has not received access; choose the file through `FilePicker` rather than changing permissions or disabling protections. Catch Promise failures so a silent asynchronous error is not mistaken for success.

For the Codex Computer Use runtime tested here, setting the console text field through `setValue` preserved long scripts. `KP_Enter` executed the console command and confirmed Go to Folder paths when `Return` failed to behave as expected. This is a runtime-specific fallback, not a universal keyboard mapping. Use fresh accessibility IDs. In path dialogs prefer `setValue` over long simulated typing; verify the full path before continuing.

## Minimal native drawing example

Run only on a new, empty canvas:

```javascript
(() => {
  const c = document.portfolio.canvases[0];
  if (c.graphics.length) throw Error('Use an empty canvas.');
  c.canvasSizingMode = CanvasSizingMode.Fixed;
  c.canvasSizeIsMeasuredInPages = false;
  c.size = new Size(300, 100);
  c.background.fillColor = Color.RGB(1, 1, 1);
  const boxes = [20, 180].map((x, i) => {
    const s = c.newShape();
    s.geometry = new Rect(x, 30, 100, 40);
    s.text = ['Input', 'Review'][i];
    s.fontName = 'TimesNewRomanPSMT';
    s.textSize = 10;
    s.textHorizontalAlignment = HorizontalTextAlignment.Center;
    s.textVerticalPlacement = VerticalTextPlacement.Middle;
    s.fillColor = Color.RGB(0.86, 0.95, 1);
    s.strokeColor = Color.RGB(0.42, 0.49, 0.57);
    s.strokeThickness = 0.65;
    s.shadowColor = null;
    s.cornerRadius = 2;
    s.magnets = [new Point(-1, 0), new Point(1, 0)];
    return s;
  });
  const line = c.connect(boxes[0], boxes[1]);
  line.tailMagnet = 2; line.headMagnet = 1;
  line.headType = 'FilledArrow'; line.headScale = 0.6;
  line.strokeThickness = 0.65;
  if (c.graphics.filter(g => g instanceof Line).length !== 1)
    throw Error('Unexpected connector count.');
})();
```

Magnets are indexed from 1; 0 means no specific magnet. For a bent line, set `lineType = LineType.Straight` and provide the successive `points` while keeping `tail`/`head` attached. `StrokeDash.Dash2on2off` and `StrokeDash.Solid` are real dash settings. Separate title/detail text shapes can be grouped with their panel using `new Group([panel, title, detail])`.

## Save and export

- **File → Save As…** saves the native `.graffle`. Verify the resulting document URL; macOS may otherwise autosave an untitled document to iCloud.
- Reopen the saved local file and use **Fit in Window** to inspect every object. Select one node; verify its label and native properties.
- **File → Export… → PDF → Current Canvas → 100%** exports the whole fixed canvas. **All Objects** crops differently and can change insertion geometry.
- Keep notes excluded. Check PDF author metadata when the target package must be anonymous; embedded figure metadata and final manuscript metadata are separate checks.
- Exporting is complete only after the target file exists, its PDF dimensions and text are verified, and the rebuilt paper shows the intended figure.
