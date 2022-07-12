const path = require('path')
const fs = require('fs')
const indexes = []
const asmDocDir = 'asm_doc_html'
const xhtmlDir = path.join(__dirname, 'public', asmDocDir)
fs.readdirSync(xhtmlDir).forEach(file => {
  console.log(file)
  if (!file.endsWith('.html')) return
  const content = fs.readFileSync(path.join(xhtmlDir, file), { encoding: 'utf-8' })
  if (!/(?<=<h1>)(.*)/.test(content)) return
  const t = RegExp.$1.trim()
  console.log(t)
  if (!/(.+)(?=<\/h1>)/.test(content)) return
  indexes.push({ t, p: asmDocDir + '/' + file, d: RegExp.$1.trim() })
})
fs.writeFileSync(path.join(__dirname, 'public', 'indexes.json'), JSON.stringify(indexes))
