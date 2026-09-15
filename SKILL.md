---
name: yuntao-omnigraffle
description: Draw and revise editable academic diagrams in macOS OmniGraffle, matching supplied Graffle examples and exporting vector figures for LaTeX. Use for method, architecture, workflow and system diagrams; retain the user's separate plotting workflow for experimental charts.
---

# Yuntao OmniGraffle

Produce a native `.graffle` source and a corresponding vector PDF using OmniGraffle. Match supplied examples without copying their scientific claims.

## Scope and intake

1. Read the figure's source, caption and surrounding manuscript text. Inventory `includegraphics`, TikZ and figure inputs; respect excluded chapters or figures.
2. Inspect the user's `.graffle` examples visually and structurally. `scripts/inspect_graffle.py` reads native shape counts, fonts, colors and attached connectors without modifying the document. For the default personal style, see [references/style.md](references/style.md).
3. Record the required labels, directed edges, grouping, legend meanings and final insertion size. Preserve distinctions such as implemented versus proposed mechanisms. A redraw is not permission to change results or add claims.

## Draw in OmniGraffle

Use the available Computer Use integration for native UI actions. In Codex, use `cua_repl`; follow its current documentation and refresh the accessibility state after actions. Do not substitute OS-level event injection when Computer Use is required.

For small edits use the inspectors. For repeatable multi-object diagrams, run reviewed JavaScript through OmniGraffle's own Automation Console. This creates real native shapes, groups, editable text and attached connectors. Read [references/native-workflow.md](references/native-workflow.md) for the tested API and export sequence.

- Start from a new empty canvas, or duplicate an existing document before substantial changes. Never clear a user's existing canvas as a setup step.
- Use a fixed canvas in points when the publication has a fixed figure size. Set text at its final printed size; avoid enlarging the canvas and shrinking it in LaTeX.
- Group a panel's background and labels. Attach connectors to shapes with explicit magnets. Check arrow direction and bends after connecting; approximate line placement is insufficient.
- Preserve real dashed/solid semantics and readable contrast. Do not use color as the only indication of a route or state.
- Save the native source in the user's requested `fig/src/` or equivalent directory. Keep previous draw.io/TikZ files unless their deletion was requested; identify the current editable source clearly.

## Export and verify

1. Save and reopen the `.graffle` file. Select a node or group and confirm editability and retained connector attachments.
2. Select the intended figure objects, then export **PDF → Selection (Current Canvas) → 100%**. Enable **Transparent background** and leave **Include margin** disabled with its value at **0 px**. Exclude notes and non-printing layers. Do not export the entire canvas unless the user explicitly requests it. Preserve the prior export before replacing it.
3. Inspect the PDF at publication size: all labels, arrowheads, line breaks, legends and margins. Confirm selected-object export dimensions and embedded font sizes. A PNG preview may be rendered from this PDF; it is not the paper's vector source.
4. Rebuild the manuscript after replacing the figure. Check references, overfull boxes, page budget and the placement of the figure. Keep an explicit author-requested format separate from venue compliance.
5. If delivery copies exist, refresh their PDF, Word previews and source ZIP. Include `.graffle` and the native drawing script in the source package; avoid publishing private research files merely to distribute this skill.
6. Report native source, exported figure, rebuilt manuscript, unchanged excluded files and checks performed. File existence alone does not prove a correct export.

## Portability

Requires macOS and a working OmniGraffle installation with the needed automation capabilities. The inspection helper uses Python's standard library and does not require OmniGraffle. Tool availability differs between Claude Code and Codex; use the installed native Computer Use interface and do not claim to have opened or exported a file without application evidence.
