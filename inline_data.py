import json

def get_berita_html():
    with open('data/berita.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = []
    for item in data['items']:
        img_html = f'<img src="{item["image"]}" alt="{item["title"]}" class="news-img" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\';">\n                 <div class="news-img-fallback" style="display:none;"></div>' if item.get("image") else '<div class="news-img-fallback"></div>'
        html.append(f'''          <article class="news-card fade-up visible">
            <div class="news-img-wrap">
              {img_html}
            </div>
            <div class="news-content">
              <div class="news-date">{item["date"]}</div>
              <h3 class="news-title">{item["title"]}</h3>
              <p class="news-body">{item["body"]}</p>
            </div>
          </article>''')
    return '\n'.join(html)

def get_umkm_html():
    with open('data/umkm.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = []
    for item in data['items']:
        wa_link = f'https://wa.me/{item["contact"].replace("+", "")}'
        html.append(f'''          <div class="umkm-card fade-up visible">
            <div class="umkm-img-wrap">
              <img src="{item.get('image', '')}" alt="{item['name']}" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
              <div class="umkm-img-fallback" style="display:none;">🛍️</div>
            </div>
            <div class="umkm-body">
              <h3 class="umkm-name">{item['name']}</h3>
              <p class="umkm-desc">{item['desc']}</p>
              <a href="{wa_link}" target="_blank" class="btn solid umkm-btn">Pesan via WhatsApp</a>
            </div>
          </div>''')
    return '\n'.join(html)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace UMKM container
umkm_start = content.find('<div class="umkm-grid" id="umkm-container">')
if umkm_start != -1:
    umkm_end = content.find('</div>', umkm_start) + 6
    new_umkm = f'<div class="umkm-grid" id="umkm-container">\n{get_umkm_html()}\n        </div>'
    content = content[:umkm_start] + new_umkm + content[umkm_end:]

# Replace Berita container
news_start = content.find('<div class="news-grid" id="news-container">')
if news_start != -1:
    news_end = content.find('</div>', news_start) + 6
    new_news = f'<div class="news-grid" id="news-container">\n{get_berita_html()}\n        </div>'
    content = content[:news_start] + new_news + content[news_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML successfully updated with hardcoded data!")
