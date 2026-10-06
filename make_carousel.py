import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the Channels section grid
match = re.search(r'<div class="max-w-5xl mx-auto grid grid-cols-4 md:grid-cols-7 gap-y-10 gap-x-6 items-center justify-items-center opacity-80 filter grayscale hover:grayscale-0 transition duration-500 px-4 text-\[#111\]">(.*?)</div>', html, re.DOTALL)

if not match:
    print("Could not find the channels grid")
    exit(1)

content = match.group(1)

# we need to make sure every item has `shrink-0`
# add shrink-0 to each top-level div inside content
# A simple way is to replace class="..." with class="... shrink-0"
# Wait, some items have class="font-black text-2xl tracking-tighter border-2 border-[#111] rounded-full w-12 h-12 flex items-center justify-center"
# Actually, the container can just be flex. We don't even need `shrink-0` if we put `shrink-0` on children or just let flex handle it if `w-max` is used on parent.
# Wait, `animate-marquee` uses `display: flex; width: max-content;`
# So children won't shrink by default in `width: max-content` anyway, but adding `shrink-0` is safer.

new_content = re.sub(r'class="([^"]+)"', r'class="\1 shrink-0"', content)

carousel_html = f'''<div class="w-full relative opacity-80 filter grayscale hover:grayscale-0 transition duration-500 overflow-hidden">
                <div class="animate-marquee flex items-center gap-16 px-8 text-[#111]">
                    <!-- Set 1 -->
                    {new_content}
                    
                    <!-- Set 2 -->
                    {new_content}
                </div>
            </div>'''

# also add overflow-hidden relative to the section
html = html.replace('<section id="channels" class="py-16 text-center border-t border-gray-200">', '<section id="channels" class="py-16 text-center border-t border-gray-200 overflow-hidden relative">')

html = html.replace(match.group(0), carousel_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Channels updated to carousel successfully!")
