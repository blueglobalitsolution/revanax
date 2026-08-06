import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

header = html.split('<section class="hero">')[0]
footer = '<section class="pre-footer">' + html.split('<section class="pre-footer">')[1]

def adjust_paths(text):
    text = re.sub(r'href="([^#][^"]*)"', r'href="../\1"', text)
    text = re.sub(r'src="([^"]*)"', r'src="../\1"', text)
    # Fix the fonts and remote urls that shouldn't be changed
    text = text.replace('../http', 'http')
    text = text.replace('../mailto:', 'mailto:')
    text = text.replace('../tel:', 'tel:')
    text = text.replace('../frequently-asked-questions-faq.html', 'frequently-asked-questions-faq.html')
    return text

header = adjust_paths(header)
footer = adjust_paths(footer)

page_content = header + """
    <section class="hero" style="height: 300px;">
        <div class="hero-bg-placeholder" style="background-color: var(--primary-color);"></div>
        <div class="hero-content">
            <span style="background-color: white; padding: 10px 20px; border-radius: 5px; color: var(--secondary-color); font-weight: bold; position: absolute; left: 10%; top: 50%; transform: translateY(-50%);">Vaginal Rejuvenation</span>
        </div>
    </section>
    
    <div class="container" style="padding: 60px 0;">
        <h1 style="text-align: center; color: var(--secondary-color); font-family: 'Sora', sans-serif; font-size: 28px; margin-bottom: 50px;">Vaginal Rejuvenation Treatment at ReevanaX, Surat</h1>
        
        <div style="display: flex; gap: 40px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 300px;">
                <div style="background-color: #d1bda5; border-radius: 50%; padding: 30px; text-align: center; margin-bottom: 30px;">
                    <img src="https://via.placeholder.com/350" alt="Vaginal Rejuvenation" style="width: 100%; border-radius: 10px;">
                </div>
            </div>
            <div style="flex: 1; min-width: 300px;">
                <h3 style="color: var(--accent-gold); font-family: 'Sora', sans-serif; font-size: 24px; margin-bottom: 20px;">What is Vaginal Rejuvenation?</h3>
                <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 20px; font-size: 15px;">Vaginal rejuvenation is a broad term that refers to various procedures addressing functional and/or aesthetic concerns of the vaginal area. Vaginal rejuvenation is preferred by women of all ages, in <strong>Surat and surrounding areas</strong>, to help with improved functionality, comfort, sexual health experience and self-confidence due to changes from childbirth, menopause or just age.</p>
                <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 40px; font-size: 15px;"><strong>Reevanax women's clinic, in Surat,</strong> provides a variety of clinically effective procedures and treatments, including radiofrequency and laser therapy, and small procedures such as labiaplasty and vaginoplasty, which can be customized for each patient.</p>
                
                <h3 style="color: var(--accent-gold); font-family: 'Sora', sans-serif; font-size: 24px; margin-bottom: 20px;">When is it appropriate for you to consider vaginal rejuvenation?</h3>
                <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 20px; font-size: 15px;">Vaginal rejuvenation can be performed, for any of the following reasons:</p>
                <ul style="list-style: none; padding: 0; margin-bottom: 30px;">
                    <li style="margin-bottom: 10px; font-size: 14px;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 10px;"></i> Population returning after childbirth (vaginal laxity)</li>
                    <li style="margin-bottom: 10px; font-size: 14px;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 10px;"></i> Stress urinary incontinence (e.g. leakage indirectly related to vaginal laxity)</li>
                    <li style="margin-bottom: 10px; font-size: 14px;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 10px;"></i> Decreased sexual sensation or pleasure</li>
                    <li style="margin-bottom: 10px; font-size: 14px;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 10px;"></i> Vaginal dryness or pain (during intercourse)</li>
                    <li style="margin-bottom: 10px; font-size: 14px;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 10px;"></i> Asymmetry or changes in shape of vagina</li>
                    <li style="margin-bottom: 10px; font-size: 14px;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 10px;"></i> Loss of tone/elasticity (related to age).</li>
                </ul>
                <p style="color: var(--text-secondary); font-size: 14px;"><strong>You're not alone...... there are effective, safe options available in Surat.</strong></p>
            </div>
        </div>
        
        <div style="margin-top: 60px;">
            <h3 style="color: var(--accent-gold); font-family: 'Sora', sans-serif; font-size: 24px; margin-bottom: 30px;">Why Choose Reevanax in Surat for Vaginal Rejuvenation?</h3>
            <ul style="list-style: none; padding: 0;">
                <li style="margin-bottom: 20px;">
                    <strong style="color: var(--secondary-color); font-size: 16px;"><i class="fas fa-chevron-right" style="margin-right: 10px;"></i> Skilled professionals</strong>
                    <p style="color: var(--text-secondary); margin-top: 5px; font-size: 14px; margin-left: 25px;">Our team has multiple years of familiarity with women's intimate health. All treatment is based on an evidence-based approach, these are proven methods with established safety and efficacy.</p>
                </li>
                <li style="margin-bottom: 20px;">
                    <strong style="color: var(--secondary-color); font-size: 16px;"><i class="fas fa-chevron-right" style="margin-right: 10px;"></i> Advanced Technology</strong>
                    <p style="color: var(--text-secondary); margin-top: 5px; font-size: 14px; margin-left: 25px;">All our solutions are non-invasive, quick recovery time, and little downtime using FDA approved laser and radiofrequency technology.</p>
                </li>
                <li style="margin-bottom: 20px;">
                    <strong style="color: var(--secondary-color); font-size: 16px;"><i class="fas fa-chevron-right" style="margin-right: 10px;"></i> Personalized Care</strong>
                    <p style="color: var(--text-secondary); margin-top: 5px; font-size: 14px; margin-left: 25px;">After our private consultation with each patient we create an individual treatment plan that fits the patient's goals, symptoms, and comfort level.</p>
                </li>
                <li style="margin-bottom: 20px;">
                    <strong style="color: var(--secondary-color); font-size: 16px;"><i class="fas fa-chevron-right" style="margin-right: 10px;"></i> Trusted by Women in Surat</strong>
                    <p style="color: var(--text-secondary); margin-top: 5px; font-size: 14px; margin-left: 25px;">We are proud to have proven to be a trustworthy option in modern intimate care, having hundreds of satisfied Surat patients. Many women recommend their friends, family and return for follow up care.</p>
                </li>
            </ul>
        </div>
        
        <div style="margin-top: 50px;">
            <h3 style="color: var(--accent-gold); font-family: 'Sora', sans-serif; font-size: 24px; margin-bottom: 20px;">FAQs About Skin Tightening</h3>
            <div style="border: 1px solid var(--secondary-color); border-radius: 4px; overflow: hidden; margin-bottom: 10px;">
                <div style="background-color: var(--secondary-color); color: white; padding: 15px; font-weight: bold; cursor: pointer;"><i class="fas fa-chevron-right"></i> Is vaginal rejuvenation safe?</div>
                <div style="padding: 15px; background: white; font-size: 14px; color: var(--text-secondary);"><i class="fas fa-chevron-right" style="color: var(--secondary-color);"></i> Yes. When performed by qualified medical professionals using approved technology, the procedures are considered safe and effective.</div>
            </div>
            <div style="border: 1px solid var(--secondary-color); border-radius: 4px; overflow: hidden; margin-bottom: 10px;">
                <div style="background-color: var(--secondary-color); color: white; padding: 15px; font-weight: bold; cursor: pointer;"><i class="fas fa-chevron-right"></i> How long is the recovery period?</div>
            </div>
            <div style="border: 1px solid var(--secondary-color); border-radius: 4px; overflow: hidden; margin-bottom: 10px;">
                <div style="background-color: var(--secondary-color); color: white; padding: 15px; font-weight: bold; cursor: pointer;"><i class="fas fa-chevron-right"></i> Will it affect my ability to have children?</div>
            </div>
        </div>
    </div>
    
    <div style="background-color: #d1bda5; padding: 80px 0;">
        <div class="container">
            <div style="display: flex; gap: 30px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px; border: 1px dashed var(--secondary-color); border-radius: 10px; padding: 30px;">
                    <div style="background-color: var(--secondary-color); color: white; display: inline-block; padding: 10px 20px; font-weight: bold; border-radius: 4px; margin-bottom: 20px;">Laser-Based Vaginal Rejuvenation</div>
                    <p style="font-weight: 500; font-size: 15px; margin-bottom: 20px; color: #333;">Non-invasive CO2 or erbium laser penetrates vaginal walls to induce controlled tissue remodeling.</p>
                    
                    <p style="font-size: 14px; margin-bottom: 10px; color: #333;"><strong>Benefits:</strong></p>
                    <ul style="list-style: none; padding: 0; margin-bottom: 20px;">
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Stimulates collagen and elastin</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Improves tightness and lubrication</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Enhances sensation and aesthetic tone</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Zero downtime, outpatient procedure</li>
                    </ul>
                    
                    <p style="font-size: 14px; margin-bottom: 10px; color: #333;"><strong>Ideal for:</strong></p>
                    <ul style="list-style: none; padding: 0;">
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Women post-childbirth</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Mild laxity and dryness</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Menopausal symptoms</li>
                    </ul>
                </div>
                
                <div style="flex: 1; min-width: 300px; border: 1px dashed var(--secondary-color); border-radius: 10px; padding: 30px;">
                    <div style="background-color: var(--secondary-color); color: white; display: inline-block; padding: 10px 20px; font-weight: bold; border-radius: 4px; margin-bottom: 20px;">2. Hair Mesotherapy</div>
                    <p style="font-weight: 500; font-size: 15px; margin-bottom: 20px; color: #333;">Controlled radiofrequency waves gently heat internal vaginal tissue to stimulate natural regeneration.</p>
                    
                    <p style="font-size: 14px; margin-bottom: 10px; color: #333;"><strong>Benefits:</strong></p>
                    <ul style="list-style: none; padding: 0; margin-bottom: 20px;">
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Comfortable, gentle heating sensation</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Noticeable improvement in tone over 2-3 sessions</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Improves stress urinary incontinence</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Safe for sensitive skin</li>
                    </ul>
                    
                    <p style="font-size: 14px; margin-bottom: 10px; color: #333;"><strong>Ideal for:</strong></p>
                    <ul style="list-style: none; padding: 0;">
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Women preferring non-laser options</li>
                        <li style="font-size: 13px; margin-bottom: 8px; color: #333;"><i class="fas fa-chevron-right" style="color: var(--secondary-color); margin-right: 8px;"></i> Those with dryness or mild leakage</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <div class="container" style="padding: 60px 0;">
        <div style="display: flex; gap: 20px; flex-wrap: wrap; justify-content: center;">
            <img src="https://via.placeholder.com/300" style="border-radius: 8px; width: 30%;">
            <img src="https://via.placeholder.com/300" style="border-radius: 8px; width: 30%;">
            <img src="https://via.placeholder.com/300" style="border-radius: 8px; width: 30%;">
        </div>
    </div>
""" + footer

with open(r'cosmetic-gynecology-treatmen\vaginal-rejuvenation-treatment.html', 'w', encoding='utf-8') as f:
    f.write(page_content)

