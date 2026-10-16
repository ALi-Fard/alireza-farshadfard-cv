"""Builds the resume site (GitHub Pages). Edit DATA below, run `python3 build.py`, commit the generated .html files."""
import json, html, os, shutil
H = html.escape
OUT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://ali-fard.github.io/alireza-farshadfard-cv/"
SITE = "https://gaiasystems.ca"

P = {
    "name": "Ali Reza Farshad Fard", "alt": "Alireza Farshadfard",
    "headline": "AI Systems Architect · Founder & Head of AI Platform, GaiaSystems™ (GaiaLink AI)",
    "tagline": "LLM platforms · AI agents · MLOps · Responsible AI",
    "location": "Greater Vancouver, British Columbia, Canada",
    "email": "alireza.farshadfard@gmail.com",
    "linkedin": "https://www.linkedin.com/in/a-farshadfard/",
    "company": SITE,
    "summary": "AI systems engineer and platform leader with 4+ years building and operating production-grade LLM and agent infrastructure on AWS and Azure, and more than a decade in digital growth, content and marketing automation before that. Hands-on with AWS Bedrock, Azure OpenAI, RAG pipelines, multi-agent orchestration, CI/CD, observability and IAM/security, with delivery across Fortune 500 healthcare, SaaS and infrastructure domains. Founder of GaiaLink AI (GaiaSystems™), which builds early-warning, explainable AI for cities, schools and enterprise teams.",
    "about": [
        "I build systems that help people notice what is coming early enough to act: AI that is explainable, keeps humans in charge, and runs reliably in production.",
        "Today I lead GaiaSystems™ (Gaialink Intelligence Systems Inc.), the company I founded in Surrey, British Columbia in 2024 and incorporated in May 2025. Before that I led AI platform and automation work in healthcare communications, consulted on multi-agent LLM systems for B2B SaaS clients, and spent years on data, growth and brand strategy at large digital businesses.",
    ],
}

SKILLS = [
    ("AI & LLM platforms", "AWS Bedrock, Azure AI Foundry, Azure OpenAI, Claude API, GPT-4, RAG systems, LLM orchestration, AI agent frameworks, prompt engineering, MLOps"),
    ("Cloud & infrastructure", "AWS (EC2, S3, Lambda, IAM, VPC), Azure (AKS, App Service, AD, Key Vault), Terraform, Docker, Kubernetes (familiarity), GitLab CI/CD, Harbor"),
    ("Observability & security", "Grafana, DORA metrics, IAM / RBAC, enterprise SSO, secrets management, audit logging, responsible AI and governance"),
    ("Data & integration", "ETL/ELT pipelines, Databricks, Microsoft Fabric, Power BI, REST API design, SQL, event-driven architectures, enterprise webhooks"),
    ("Platforms & tooling", "HubSpot, NetSuite, Make.com, Zapier, Power Automate, GitHub Actions"),
    ("Growth & marketing", "SEO, PPC (Google & Meta Ads), content strategy, A/B testing, analytics, marketing automation, brand strategy"),
]

EXP = [
    ("Founder & Head of AI Platform", "Gaialink Intelligence Systems Inc. (GaiaSystems™ / GaiaLink AI)", "Vancouver, BC", "Jun 2025 – Present", [
        "Designed and deployed a production AI/agent platform on AWS using Bedrock for LLM orchestration and GitLab CI/CD with Terraform-managed infrastructure; cut release cycles 40% and accelerated go-to-market 50%.",
        "Built multi-agent systems with event-driven coordination, tool use and memory layers, integrated with enterprise data sources through REST APIs and secure webhook pipelines.",
        "Implemented an observability stack (Grafana dashboards, structured logging, DORA metrics) and IAM/RBAC governance across platform services for 5 enterprise pilot clients.",
        "Led a 6-person cross-functional team; owned full P&L and extended operational runway 20% through data-driven resource planning."]),
    ("Director, AI Platform & Automation", "Lampyon Health Communications", "Toronto, ON", "Mar 2025 – Jun 2025", [
        "Engineered a production-grade, medically safe RAG system on Azure OpenAI deployed across Fortune 500 pharmacy chains for surgeons and pharmacists; improved retrieval accuracy 40% and content engagement 400%.",
        "Designed secure enterprise integrations with IAM-controlled access, audit trails and compliance-aligned data handling for regulated healthcare environments.",
        "Authored an AI implementation and governance playbook that reduced project development cycles 30% across the organization."]),
    ("AI & Cloud Infrastructure Consultant", "Independent practice", "Vancouver, BC", "Jul 2024 – Mar 2025", [
        "Deployed custom multi-agent LLM systems on AWS and Azure for B2B SaaS clients; increased conversion rates 40% and reduced client integration time 60% through API-first architecture.",
        "Designed AI-driven data workflows with CI/CD pipelines, secrets management and role-based access controls aligned with enterprise security standards.",
        "Expanded qualified pipeline volume 35% in six months by automating lead scoring, enrichment and CRM sync workflows."]),
    ("Senior Data & Automation Strategist", "Digikala Co.", "Tehran, Iran", "Jan 2022 – Jun 2024", [
        "Built BI and analytics infrastructure (Power BI, SQL) and automated reporting pipelines; improved operational visibility and drove a 20% conversion uplift through data-driven experimentation.",
        "Led cross-functional alignment between engineering, product and marketing on automation tooling and data workflow delivery."]),
    ("Digital Marketing & Brand Manager", "IranKhodro", "", "Jun 2019 – Dec 2021", [
        "Developed and ran digital strategies across SEO, PPC and social media for B2B audiences, working with external agencies and advanced analytics.",
        "Improved click-through rates 25% and conversion rates 15% through A/B testing and keyword analysis."]),
    ("Content Marketing Specialist", "SOKAN Technology Solutions LLC", "", "Mar 2016 – May 2019", [
        "Led SaaS content and SEO strategy; increased organic search visibility 30% through keyword analysis and on-page optimization.",
        "Produced blogs, case studies and technical whitepapers aligned with buyer personas."]),
]

DELIVERABLES = [
    ("Production LLM agent platform (AWS Bedrock)", "Multi-agent orchestration with tool use, RAG retrieval, memory and a secure API gateway, serving 5 enterprise clients in production."),
    ("Healthcare RAG system (Azure OpenAI)", "HIPAA-aligned retrieval pipeline with role-based access, audit logging and clinical content governance for Fortune 500 healthcare."),
    ("CI/CD & MLOps infrastructure", "GitLab pipelines with Docker, Terraform, Harbor registry, model versioning and Grafana observability; release cycles cut 40%."),
    ("Enterprise AI integration layer", "REST API-first connectors linking LLM agents to CRMs (HubSpot, NetSuite), ERPs and data warehouses (Databricks, Fabric) with IAM-enforced access."),
]

EDU = [
    ("Postgraduate Certificate, Business Administration", "The University of Manchester (Manchester Business School), UK", "2013"),
    ("Bachelor's Degree, Computer Software", "Islamic Azad University, Shiraz, Iran", "2006"),
]

CERT = {
    "title": "Agent Architect", "kind": "Certificate of Completion", "issuer": "Founderz Business School", "year": "Class of 2026",
    "text": "Founderz Business School certifies that Ali Reza Farshad Fard has successfully completed all academic and practical requirements of the Agent Architect program.",
    "signed": "Eloi Noya, Academic Director, Founderz AI Business School, Barcelona, Spain",
    "hash": "f4216a02453e57ae2d634c421df44d38d85b11e2",
    "url": "https://learn.founderz.com/certificate/agent-architect/bf5f643f-2c78-4635-800e-7f9ace03aea6",
}

PROJECTS = [
    ("EarthOS™", "AI decision intelligence for infrastructure: forecasts when roads, bridges and water systems will cross their failure thresholds, with confidence ranges, climate stress as an input and human review built in.", SITE + "/earthos"),
    ("GaiaThinker™", "Privacy-first, explainable AI for schools and campuses, with educator review gates and climate literacy lessons built from city data.", SITE + "/gaiathinker"),
    ("CivicOS™", "Decision support for civic leaders that brings service demand, climate risk and community outcomes into council-ready briefings.", SITE + "/civicos"),
    ("SalesOS™", "Sales forecasting and explainable opportunity scoring for forklift and industrial equipment dealers.", SITE + "/salesos"),
    ("Gaia, the website AI assistant", "Multilingual assistant on gaiasystems.ca built on the Claude API, with Turnstile-verified sessions, rate limiting, prompt-injection and leak filters, and a subscriber-only AI business assessment that generates PDF reports.", SITE + "/?gaia=1"),
    ("Healthcare RAG system", "Medically safe retrieval for pharmacists and surgeons on Azure OpenAI, with audit logging and role-based access (Lampyon Health Communications).", ""),
]
RESEARCH = ["Q-Wind RailSense™: wind estimation for rail safety without GPS or 5G", "Decentralized rail and bus routing that keeps working offline",
            "WildfireSense AI: early wildfire warning from micro-sensors and satellite data", "Watershed and salmon habitat intelligence for BC rivers",
            "Climate stress forecasting for drought, flood and ecosystem instability", "MindNest BC: calm technology rooted in nature"]

ARTICLES = json.load(open(os.path.join(OUT, "articles.json"), encoding="utf-8"))

NAV = [("index.html", "Home"), ("resume.html", "Resume"), ("projects.html", "Projects"), ("contact.html", "Contact")]


def shell(fname, title, desc, body, ld=None):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    lds = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ""
    canon = BASE + ("" if fname == "index.html" else fname)
    return f'''<!DOCTYPE html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H(title)}</title>
<meta name="description" content="{H(desc)}">
<meta name="author" content="{P["name"]}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#100C2B">
<meta property="og:type" content="profile">
<meta property="og:title" content="{H(title)}">
<meta property="og:description" content="{H(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/montserrat.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css">
{lds}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap row">
  <a class="brand" href="index.html"><img src="assets/mark.svg" width="30" height="30" alt="">{P["name"]}</a>
  <nav aria-label="Main">{nav}</nav>
</div></header>
<main id="main">{body}</main>
<footer class="foot"><div class="wrap row">
  <span>© 2026 {P["name"]} · <a href="{SITE}">GaiaSystems™</a></span>
  <span><a href="{P["linkedin"]}" rel="me noopener">LinkedIn</a> · <a href="mailto:{P["email"]}">Email</a> · <a href="contact.html">Contact</a></span>
</div></footer>
<script src="assets/site.js" defer></script>
</body>
</html>'''


person_ld = {
    "@context": "https://schema.org", "@type": "Person", "@id": BASE + "#person", "name": P["name"], "alternateName": [P["alt"]],
    "url": BASE, "image": BASE + "assets/portrait-720.webp", "jobTitle": "Founder & Head of AI Platform",
    "worksFor": {"@type": "Organization", "name": "GaiaSystems", "legalName": "Gaialink Intelligence Systems Inc.", "alternateName": "GaiaLink AI", "url": SITE + "/"},
    "address": {"@type": "PostalAddress", "addressRegion": "BC", "addressCountry": "CA"},
    "email": "mailto:" + P["email"], "sameAs": [P["linkedin"], SITE + "/about#founder"],
    "alumniOf": [{"@type": "CollegeOrUniversity", "name": "The University of Manchester"}, {"@type": "CollegeOrUniversity", "name": "Islamic Azad University"}],
    "hasCredential": {"@type": "EducationalOccupationalCredential", "name": CERT["title"], "credentialCategory": CERT["kind"],
                      "recognizedBy": {"@type": "Organization", "name": CERT["issuer"]}, "url": CERT["url"]},
    "knowsAbout": ["AI systems architecture", "AI agents", "LLM platforms", "AWS Bedrock", "Azure OpenAI", "RAG", "MLOps", "Responsible AI", "SEO", "Marketing automation"],
}

# ---------- Home
home = f'''
<section class="hero"><div class="wrap hero-g">
  <div>
    <p class="kicker">{H(P["tagline"])}</p>
    <h1>I build AI systems that help people <em>act in time.</em></h1>
    <p class="lead">{H(P["headline"])}. Based in {H(P["location"])}.</p>
    <div class="ctas"><a class="btn btn-p" href="resume.html">View resume →</a><a class="btn btn-o" href="projects.html">Projects</a><a class="btn btn-o" href="{P["linkedin"]}" rel="me noopener">LinkedIn</a></div>
  </div>
  <div class="portrait"><img src="assets/portrait-720.webp" srcset="assets/portrait-400.webp 400w, assets/portrait-720.webp 720w" sizes="(max-width:800px) 280px, 360px" width="720" height="720" alt="Portrait of {P["name"]}"></div>
</div></section>
<section class="band"><div class="wrap">
  <h2>About me</h2>
  {"".join(f"<p>{H(t)}</p>" for t in P["about"])}
  <div class="stats">
    <div><b>10+ years</b><span>in digital, data and AI</span></div>
    <div><b>AWS · Azure</b><span>production LLM and agent platforms</span></div>
    <div><b>Founder</b><span>GaiaSystems™ / GaiaLink AI</span></div>
    <div><b>Agent Architect</b><span>Founderz Business School, 2026</span></div>
  </div>
</div></section>
<section><div class="wrap">
  <h2>Latest writing</h2>
  <div class="cards">{"".join(f'<a class="card" href="{SITE}/insights/{a["slug"]}"><span class="meta">{a["date"][:7]}</span><b>{H(a["title"])}</b></a>' for a in ARTICLES[:3])}</div>
  <p><a class="more" href="resume.html#publications">All publications →</a></p>
</div></section>
'''

# ---------- Resume
exp_html = "".join(f'''<article class="job"><div class="job-h"><div><h3>{H(t)}</h3><p class="org">{H(o)}{" · " + H(l) if l else ""}</p></div><span class="when">{H(d)}</span></div>
<ul>{"".join(f"<li>{H(x)}</li>" for x in pts)}</ul></article>''' for t, o, l, d, pts in EXP)
resume = f'''
<section class="hero sm"><div class="wrap">
  <p class="kicker">Resume</p>
  <h1>{P["name"]}</h1>
  <p class="lead">{H(P["headline"])}</p>
  <p class="contact-line">{H(P["location"])} · <a href="mailto:{P["email"]}">{P["email"]}</a> · <a href="{P["linkedin"]}" rel="me noopener">linkedin.com/in/a-farshadfard</a> · <a href="{SITE}">gaiasystems.ca</a></p>
  <div class="ctas no-print"><a class="btn btn-p" href="assets/Ali_Reza_Farshad_Fard_Resume.pdf" download>Download PDF</a><button class="btn btn-o" type="button" data-print>Print</button><a class="btn btn-o" href="contact.html">Contact me</a></div>
</div></section>
<section><div class="wrap cv">
  <h2>Professional summary</h2><p>{H(P["summary"])}</p>
  <h2>Certification</h2>
  <div class="cert">
    <div class="seal" aria-hidden="true">✓</div>
    <div><h3>{CERT["title"]}</h3><p class="org">{CERT["kind"]} · {CERT["issuer"]} · {CERT["year"]}</p>
    <p>{H(CERT["text"])}</p><p class="small">Signed by {H(CERT["signed"])}<br>Certificate hash: <code>{CERT["hash"]}</code></p>
    <a class="btn btn-o sm-btn no-print" href="{CERT["url"]}" rel="noopener" target="_blank">Verify certificate →</a></div>
  </div>
  <h2>Experience</h2>{exp_html}
  <h2>Key technical deliverables</h2>
  <ul class="del">{"".join(f"<li><b>{H(t)}.</b> {H(d)}</li>" for t, d in DELIVERABLES)}</ul>
  <h2>Technical skills</h2>
  <dl class="skills">{"".join(f"<dt>{H(k)}</dt><dd>{H(v)}</dd>" for k, v in SKILLS)}</dl>
  <h2>Education</h2>
  {"".join(f'<div class="edu"><div><h3>{H(d)}</h3><p class="org">{H(s)}</p></div><span class="when">{y}</span></div>' for d, s, y in EDU)}
  <h2 id="publications">Publications</h2>
  <p class="print-only">45+ articles on AI, climate resilience and digital strategy. Selected articles: gaiasystems.ca/insights. Certificate verification: {CERT["url"]}</p>
  <p class="no-print">Selected articles, republished on gaiasystems.ca. More than 45 articles on <a href="{P["linkedin"]}recent-activity/articles/" rel="noopener">LinkedIn</a>.</p>
  <ul class="pubs no-print">{"".join(f'<li><a href="{SITE}/insights/{a["slug"]}">{H(a["title"])}</a> <span class="when">{a["date"][:7]}</span></li>' for a in ARTICLES)}</ul>
</div></section>
'''

# ---------- Projects
projects = f'''
<section class="hero sm"><div class="wrap"><p class="kicker">Projects</p><h1>What I am building</h1>
<p class="lead">Products and platforms from GaiaSystems™ (GaiaLink AI) and earlier work.</p></div></section>
<section><div class="wrap">
  <div class="cards two">{"".join(f'<div class="card"><b>{H(t)}</b><p>{H(d)}</p>{f"<a class=more href={u!r}>Learn more →</a>" if u else ""}</div>' for t, d, u in PROJECTS)}</div>
  <h2>Research directions at GaiaLink AI</h2>
  <ul class="del">{"".join(f"<li>{H(x)}</li>" for x in RESEARCH)}</ul>
  <p class="small">Research directions are early-stage concepts and are not product claims.</p>
</div></section>
'''

# ---------- Contact
contact = f'''
<section class="hero sm"><div class="wrap"><p class="kicker">Contact</p><h1>Let's talk</h1>
<p class="lead">For AI platform roles and contracts, speaking, or partnerships with GaiaSystems™.</p></div></section>
<section><div class="wrap contact">
  <a class="card" href="mailto:{P["email"]}"><b>Email</b><span>{P["email"]}</span></a>
  <a class="card" href="{P["linkedin"]}" rel="me noopener"><b>LinkedIn</b><span>linkedin.com/in/a-farshadfard</span></a>
  <a class="card" href="{SITE}/contact"><b>GaiaSystems™</b><span>Demos, partnerships and investor enquiries</span></a>
  <a class="card" href="{SITE}/about#founder"><b>Founder story</b><span>Why I started GaiaSystems™</span></a>
</div></section>
'''

pages = [
    ("index.html", f"{P['name']} | AI Systems Architect & Founder, GaiaSystems™", "Ali Reza Farshad Fard (Alireza Farshadfard): AI systems architect, founder of GaiaSystems™ (GaiaLink AI), LLM platforms, AI agents and MLOps in Vancouver, BC.", home, person_ld),
    ("resume.html", f"Resume: {P['name']}, AI Systems Architect", "Resume of Ali Reza Farshad Fard: AI platform leadership, AWS Bedrock and Azure OpenAI, AI agents, MLOps, Agent Architect certification, education and publications.", resume, person_ld),
    ("projects.html", f"Projects: {P['name']}", "Projects by Ali Reza Farshad Fard: EarthOS, GaiaThinker, CivicOS, SalesOS and AI platforms built at GaiaSystems (GaiaLink AI).", projects, None),
    ("contact.html", f"Contact {P['name']}", "Contact Ali Reza Farshad Fard for AI platform roles, contracts, speaking and partnerships with GaiaSystems.", contact, None),
]
for f, t, d, b, ld in pages:
    open(os.path.join(OUT, f), "w", encoding="utf-8").write(shell(f, t, d, b, ld))
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE}{'' if f == 'index.html' else f}</loc></url>\n" for f, *_ in pages) + "</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
print("built", [p[0] for p in pages])
