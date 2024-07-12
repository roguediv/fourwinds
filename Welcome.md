This is your new *vault*.

Make a note of something, [[create a link]], or try [the Importer](https://help.obsidian.md/Plugins/Importer)!

When you're ready, delete this note and make the vault your own.
- [ ] test note #test #makeready


## Filter by page
```dataviewjs
const tag = '#makeready'
const query = `
not done
${"(path includes " + dv.pagePaths(tag).join(') OR (path includes ') + ")"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```
## Filter by tags
```tasks
(tags include makeready) OR (tags include test)
```