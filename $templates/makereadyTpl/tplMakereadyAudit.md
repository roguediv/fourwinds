### General
- [?] Carpet #floor
- [?] laminate #floor

### [[kitchen]]
```dataviewjs
const query = `
${"(path includes " + dv.current().file.folder + "/kitchen)"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```

### [[living]]
```dataviewjs
const query = `
${"(path includes " + dv.current().file.folder + "/living)"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```

### [[bath 1]]
```dataviewjs
const query = `
${"(path includes " + dv.current().file.folder + "/bath 1)"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```

### [[bath 2]]
```dataviewjs
const query = `
${"(path includes " + dv.current().file.folder + "/bath 2)"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```

### [[bed 1]]
```dataviewjs
const query = `
${"(path includes " + dv.current().file.folder + "/kitchen)"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```
### [[bed 2]]
```dataviewjs
const query = `
${"(path includes " + dv.current().file.folder + "/bed 2)"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```
### [[bed 3]]
```dataviewjs
const query = `
${"(path includes " + dv.current().file.folder + "/bed 3)"}
`;
dv.paragraph('```tasks\n' + query + '\n```')
```

