import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove VIEW FULL CHANNEL LIST
html = re.sub(r'<a href="https://wa\.me/447988577652" class="inline-block mt-16[^>]+>VIEW FULL CHANNEL LIST</a>', '', html)

# 2. Update REQUEST FREE TRIAL link (only the first instance or matching text)
html = html.replace(
    '<a href="https://wa.me/447988577652" class="hidden md:flex bg-primary text-black px-6 py-2.5 rounded-full font-black text-xs uppercase tracking-widest hover:bg-yellow-500 transition items-center gap-2">\n                REQUEST FREE TRIAL\n            </a>',
    '<a href="https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20request%20a%20free%20trial." class="hidden md:flex bg-primary text-black px-6 py-2.5 rounded-full font-black text-xs uppercase tracking-widest hover:bg-yellow-500 transition items-center gap-2">\n                REQUEST FREE TRIAL\n            </a>'
)

# 3. Add IDs and default text to Pricing buttons
# We need to replace the 3 CHOOSE PLAN buttons
# Button 1 (1 Month)
html = html.replace(
    '<a href="https://wa.me/447988577652" class="block w-full text-center border border-gray-600 text-white py-3 rounded-full font-bold text-xs tracking-widest hover:border-primary hover:text-primary transition uppercase">CHOOSE PLAN</a>',
    '<a id="btn-1mo" href="https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20subscribe%20to%20the%201%20Month%20plan%20for%201%20Device." class="block w-full text-center border border-gray-600 text-white py-3 rounded-full font-bold text-xs tracking-widest hover:border-primary hover:text-primary transition uppercase">CHOOSE PLAN</a>',
    1 # only the first one
)

# Button 2 (12 Months)
html = html.replace(
    '<a href="https://wa.me/447988577652" class="block w-full text-center bg-primary text-black py-4 rounded-full font-black text-xs tracking-widest hover:bg-yellow-500 transition shadow-[0_10px_20px_rgba(255,171,0,0.2)] uppercase">CHOOSE PLAN</a>',
    '<a id="btn-12mo" href="https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20subscribe%20to%20the%2012%20Months%20plan%20for%201%20Device." class="block w-full text-center bg-primary text-black py-4 rounded-full font-black text-xs tracking-widest hover:bg-yellow-500 transition shadow-[0_10px_20px_rgba(255,171,0,0.2)] uppercase">CHOOSE PLAN</a>'
)

# Button 3 (6 Months)
html = html.replace(
    '<a href="https://wa.me/447988577652" class="block w-full text-center border border-gray-600 text-white py-3 rounded-full font-bold text-xs tracking-widest hover:border-primary hover:text-primary transition uppercase">CHOOSE PLAN</a>',
    '<a id="btn-6mo" href="https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20subscribe%20to%20the%206%20Months%20plan%20for%201%20Device." class="block w-full text-center border border-gray-600 text-white py-3 rounded-full font-bold text-xs tracking-widest hover:border-primary hover:text-primary transition uppercase">CHOOSE PLAN</a>'
)

# 4. Update Javascript for Pricing Device Selector
js_replacement = """        function setDevices(num, btn) {
            // Update button styles
            const buttons = document.querySelectorAll('.device-btn');
            buttons.forEach(b => {
                b.classList.remove('bg-primary', 'text-black', 'font-black', 'shadow');
                b.classList.add('text-gray-400', 'font-bold');
            });
            btn.classList.remove('text-gray-400', 'font-bold');
            btn.classList.add('bg-primary', 'text-black', 'font-black', 'shadow');

            // Update price values with fade animation
            const p1 = document.getElementById('price-1mo');
            const p6 = document.getElementById('price-6mo');
            const p12 = document.getElementById('price-12mo');

            // Quick fade out/in effect
            [p1, p6, p12].forEach(el => el.style.opacity = 0);
            
            setTimeout(() => {
                p1.innerHTML = pricing[num].p1 + '<span class="text-sm text-gray-400 align-top font-bold tracking-widest">/mo</span>';
                p6.innerHTML = pricing[num].p6 + '<span class="text-sm text-gray-400 align-top font-bold tracking-widest">/6mo</span>';
                p12.innerHTML = pricing[num].p12 + '<span class="text-sm text-gray-400 align-top font-bold tracking-widest">/yr</span>';
                
                [p1, p6, p12].forEach(el => {
                    el.style.transition = 'opacity 0.3s ease';
                    el.style.opacity = 1;
                });
            }, 150);

            // Update WhatsApp links
            const deviceText = num === 1 ? '1 Device' : num + ' Devices';
            document.getElementById('btn-1mo').href = `https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20subscribe%20to%20the%201%20Month%20plan%20for%20${deviceText}.`;
            document.getElementById('btn-6mo').href = `https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20subscribe%20to%20the%206%20Months%20plan%20for%20${deviceText}.`;
            document.getElementById('btn-12mo').href = `https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20subscribe%20to%20the%2012%20Months%20plan%20for%20${deviceText}.`;
        }"""

html = re.sub(r'function setDevices\(num, btn\).*?}, 150\);\s*\}', js_replacement, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update setup.html
with open('setup.html', 'r', encoding='utf-8') as f:
    setup_html = f.read()

setup_html = setup_html.replace(
    '<a href="https://wa.me/447988577652" class="hidden md:flex bg-primary text-black px-6 py-2.5 rounded-full font-black text-xs uppercase tracking-widest hover:bg-yellow-500 transition items-center gap-2">\n                REQUEST FREE TRIAL\n            </a>',
    '<a href="https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20would%20like%20to%20request%20a%20free%20trial." class="hidden md:flex bg-primary text-black px-6 py-2.5 rounded-full font-black text-xs uppercase tracking-widest hover:bg-yellow-500 transition items-center gap-2">\n                REQUEST FREE TRIAL\n            </a>'
)

setup_html = setup_html.replace(
    '<a href="https://wa.me/447988577652" class="text-primary font-bold text-[11px] tracking-widest uppercase hover:underline flex items-center gap-1">Contact Support &rarr;</a>',
    '<a href="https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20need%20some%20support%20getting%20set%20up." class="text-primary font-bold text-[11px] tracking-widest uppercase hover:underline flex items-center gap-1">Contact Support &rarr;</a>'
)

setup_html = setup_html.replace(
    '<a href="https://wa.me/447988577652" class="whatsapp-float">',
    '<a href="https://wa.me/447988577652?text=Hello%20NIXATV%2C%20I%20need%20some%20support%20getting%20set%20up." class="whatsapp-float">'
)

with open('setup.html', 'w', encoding='utf-8') as f:
    f.write(setup_html)

print("Updates completed successfully.")
