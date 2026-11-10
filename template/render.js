// Usage: node template/render.js <input.html> <output.png>
// Renders a 1080x1350 Deal Signal image and fails if any block overlaps the footer or leaves the canvas.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.resolve(inp));
  await p.waitForTimeout(500);
  const problems = await p.evaluate(() => {
    const foot = document.querySelector('.foot');
    const footTop = foot ? foot.getBoundingClientRect().top : 1350;
    const bad = [];
    document.querySelectorAll('.wrap > *').forEach(e => {
      const r = e.getBoundingClientRect();
      if (r.bottom > footTop - 12) bad.push('overlaps footer: ' + (e.className || e.tagName));
      if (r.right > 1080) bad.push('off canvas: ' + (e.className || e.tagName));
    });
    document.querySelectorAll('*').forEach(e => {
      if (e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).overflow === 'hidden') bad.push('clipped: ' + (e.className || e.tagName));
    });
    return bad;
  });
  await p.screenshot({ path: out });
  await b.close();
  if (problems.length) { console.error('LAYOUT FAIL\n' + problems.join('\n')); process.exit(1); }
  console.log('OK ' + out);
})();
