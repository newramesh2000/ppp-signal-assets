# Deal Signal: house standard (approved 10 Nov 2026)

Approved sample: images/2026/11/2026-11-10-sabic-hospital.png (built from template/deal-signal-template.html).

## Image (1080 x 1350 PNG)
Keep the template's frame, colours, fonts (Lora headings, Inter body), masthead, footer and evidence codes exactly. Only the content changes.
1. Masthead: "PPP ARCHITECTURE SERIES" + "DEAL SIGNAL · <COUNTRY CODE> · <SECTOR>".
2. Kicker: project name · city/country.
3. Headline: one testable claim, two lines max, second line italic teal.
4. Sub-line: scale · contract model and term · latest dated stage.
5. Hero visual: ONE mechanism. Pick the form that fits the lens: number decoder (template ladder), capital stack, procurement clock/timeline, or risk split. Same colour ramp as the template.
6. "The lender question" box (one question) and "Not yet disclosed" box (4-6 gaps).
7. Footer: dated sources; V = official notice or regulatory filing, R = reputable press, E = author arithmetic with method; "Not investment advice."; "Ramesh Radhakrishnaraja, FCA".
Render with: node template/render.js <file.html> <file.png>  (must print OK), then view the PNG before upload.

## Hook standard (set by Ramesh, 27 Nov 2026)
Model post: Taweelah C IPP, Abu Dhabi, published 25 Nov 2026 (images/2026/11/2026-11-25-taweelah-c.png; https://linkedin.com/feed/update/urn:li:share:7531266302275969024). It went viral. Every Deal Signal now uses its hook pattern: one named player, two numbers that contradict each other, and what that split means for the money.
- Image headline: two short, parallel sentences that set one number against another for the same named player, at most two lines. Line 1 is the expected fact ("TAQA owns 60%."). Line 2, in italic teal, is the contradiction ("It runs only 40%.").
- Caption line 1: the contrast in one plain sentence, naming the player and both numbers ("TAQA owns 60% of Abu Dhabi's Taweelah C plant, but only 40% of the company that runs it."). No icon on line 1.
- Caption line 2: "🔑 " + one short sentence saying who gets which cash or carries which risk because of the split ("Dividends and operating fees go to different hands.") + " 👇".
- Good contrasts to look for: equity vs O&M or EPC share, headline value vs cash, debt vs equity, award date vs cash date, capacity vs payment, owner vs operator, public vs private share.
- Both numbers must be [V] or [R], or an [E] figure built from them that the hero visual shows. The contradiction must be stated by the sources, not inferred. No hype words, no question in the hook, no claim the sources do not support. The evidence rules still win: if no true contrast exists, use the plainest true version.
- The rest of the caption keeps the Taweelah C order: facts with icons, "Decode it", "Why it matters", "Not yet public", one question, three hashtags, "Soli Deo Gloria".

## Caption
Hook per the hook standard above, then a blank line. Icon at the start of every line. Facts, then "Decode it" or the mechanism, then why it matters to lenders/sponsors, then what is not public. One question to the audience. Exactly three hashtags (#PPP #Vision2030 #ProjectFinance unless the deal is outside the Gulf, then swap #Vision2030 for the country or sector tag). Close with "Soli Deo Gloria". Under 1,300 characters.

## First comment
"Sources" then each source: publisher, what it confirms, date, full URL. Then the [E] arithmetic written out. End with "Not investment advice."

## Evidence rules
- Every fact confirmed by two independent organisations (e.g. ministry + press, or regulator + listed-company filing). Fetch them on the day; never rely on memory.
- Every number carries V, R or E. No figure without a source or a stated method.
- If two independent sources cannot be confirmed, do not post that day. Fail closed.

## Selection
- Source pool: the Global PPP Intelligence sheet (DEAL_REGISTER, PRIORITY_BOARD, CHANGE_EVENTS, SOURCE_EVIDENCE, EDITORIAL_QUEUE), plus fresh dated news on those projects.
- Geography mix: about 60% Saudi/GCC, the rest UAE, Middle East and global deals with a Saudi lesson.
- No project or angle repeated within the last 30 posts (check PUBLICATION_LOG).
- Employer firewall: Sharakat/SWPC water assets (reservoirs, IWPs, ISTPs, transmission) are facts-only with no verdict or lender question; prefer other deals.

## Release
Image to images/YYYY/MM/ in this repo; Metricool brand 7080378, LinkedIn only, 11:00 Asia/Riyadh, autoPublish true, draft false, first comment set.
