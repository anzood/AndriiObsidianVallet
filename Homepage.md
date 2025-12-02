# 🏠 Home Base

## 🧭 Main Spheres
| [[Health]] | [[Family]] | [[Career]] | [[Wealth]] | [[Play]] | [[Growth]] | [[Admin]] | [[Social]] |
## 📝 Daily notes to process
```dataviewjs
function toLocalDate(d) {
    return new Date(d.getFullYear(), d.getMonth(), d.getDate());
}

const today = toLocalDate(new Date());
const pages = dv.pages('"journals"')
    .where(p => p.file.tags?.includes("#type/journal") &&
                p.file.tags?.includes("#status/raw") &&
                // filter by file name as date before today
                (() => {
                    const fileDate = new Date(p.file.name);
                    if (isNaN(fileDate)) return false; // skip invalid file names
                    return toLocalDate(fileDate) < today;
                })()
            )
    .sort(p => p.file.name, 'desc');

const lines = [];

function escapeForMd(text) {
    if (!text) return "";
    return text
        .replace(/\\/g, "\\\\")   // backslash
        .replace(/\|/g, "\\|")    // pipe
        .replace(/\[/g, "\\[")    // [
        .replace(/\]/g, "\\]")    // ]
        .replace(/\*/g, "\\*")    // *
        .replace(/`/g, "\\`");    // inline code backtick
}

for (let page of pages) {
    const content = await dv.io.load(page.file.path);
    const linesArr = content.split("\n");

    // Find the “## 📝 Notes” heading (exact start)
    const startIndex = linesArr.findIndex(l => l.trim().startsWith("## 📝 Notes"));

    let extracted = "";
    let hadMore = false;

    if (startIndex !== -1) {
        // Extract lines until the next "## " heading
        let section = [];

        for (let i = startIndex + 1; i < linesArr.length; i++) {
            const line = linesArr[i];

            // Stop on next H2 (## ) heading
            if (line.trim().startsWith("## ")) break;

            section.push(line);
        }

        // Clean: trim, drop empty lines
        const cleanedAll = section.map(l => l.trim()).filter(l => l.length > 0);

        if (cleanedAll.length > 5) {
            hadMore = true;
        }

        const cleaned = cleanedAll.slice(0, 5);
        extracted = cleaned.join(" ");
    }

    let previewText = extracted ? escapeForMd(extracted.trim()) : "_(no notes)_";
    if (hadMore) previewText += " …";

    const link = `[[${page.file.path}|${page.file.name}]]`;
    lines.push(`- **${link}**: ${previewText}`);
}

// Render as markdown so obsidian will parse wikilinks and show hover previews
dv.el("div", lines.join("\n"));
```
## 📥 Recent Thoughts
```dataview
LIST WITHOUT ID link(file.link, file.name) + " (" + default(lang, "en") + ")"
FROM "pages"
SORT file.mtime DESC
LIMIT 5
```
## 🧠 Knowledge Garden
[[Map of Content|Master MOC]] - _Entry point to all knowledge_
[[Tag System]] - _The tag system_

## ⚡ Quick Actions
- [[Inbox]]
- [[Tasks]]
