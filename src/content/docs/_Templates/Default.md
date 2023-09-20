<%*
let filename = await tp.system.prompt("Note Title")
await tp.file.rename(filename)
-%>
---

title: <% filename %>
tags: []
---

<% tp.file.cursor() %>

## Anhänge
