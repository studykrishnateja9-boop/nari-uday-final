from flask import Flask, render_template

app = Flask(__name__)

# Mock Data
HERO_STATS = [
    {"label": "Women onboarded", "value": "14,202", "sub": "across 8 divisions"},
    {"label": "Children kept in school", "value": "12,840", "sub": "this academic year"},
    {"label": "Weekly earnings", "value": "৳ 42.5M", "sub": "via micro-business hub"},
    {"label": "School retention", "value": "98.2%", "sub": "in active hubs"},
]

INCOME_GROWTH = [
    {"month": "M1", "income": 1800, "attendance": 62},
    {"month": "M2", "income": 2400, "attendance": 68},
    {"month": "M3", "income": 3300, "attendance": 74},
    {"month": "M4", "income": 4100, "attendance": 82},
    {"month": "M5", "income": 5200, "attendance": 89},
    {"month": "M6", "income": 6800, "attendance": 94},
    {"month": "M7", "income": 7900, "attendance": 96},
    {"month": "M8", "income": 9100, "attendance": 98},
]

PROBLEM_STATS = [
    {"label": "Rural female labor force participation", "value": "36%", "source": "World Bank, 2023"},
    {"label": "Children 5–17 in child labor", "value": "1.07M", "source": "BBS / ILO survey"},
    {"label": "Primary completion (rural girls)", "value": "78%", "source": "UNICEF Bangladesh"},
    {"label": "Mobile penetration", "value": "84%", "source": "BTRC, 2024"},
    {"label": "Mobile internet users", "value": "77M+", "source": "BTRC, 2024"},
    {"label": "MFS accounts (bKash/Nagad/Rocket)", "value": "220M+", "source": "Bangladesh Bank"},
]

COURSES = [
    {"title": "Tailoring & Stitching", "bn": "সেলাই", "level": "Beginner", "hours": 18, "learners": 4210, "tag": "Handicraft"},
    {"title": "Nakshi Kantha Embroidery", "bn": "নকশী কাঁথা", "level": "Intermediate", "hours": 22, "learners": 1820, "tag": "Handicraft"},
    {"title": "Food Processing & Pickle", "bn": "খাদ্য প্রক্রিয়াজাত", "level": "Beginner", "hours": 14, "learners": 2310, "tag": "Agro"},
    {"title": "Poultry & Dairy Basics", "bn": "পশুপালন", "level": "Beginner", "hours": 12, "learners": 1750, "tag": "Agro"},
    {"title": "Digital Marketing for Sellers", "bn": "ডিজিটাল মার্কেটিং", "level": "Intermediate", "hours": 16, "learners": 980, "tag": "Digital"},
    {"title": "Online Selling on Daraz/Facebook", "bn": "অনলাইন বিক্রয়", "level": "Beginner", "hours": 10, "learners": 1640, "tag": "Digital"},
    {"title": "Freelancing 101", "bn": "ফ্রিল্যান্সিং", "level": "Intermediate", "hours": 24, "learners": 720, "tag": "Digital"},
    {"title": "Graphic Design with Canva", "bn": "গ্রাফিক ডিজাইন", "level": "Beginner", "hours": 14, "learners": 540, "tag": "Digital"},
    {"title": "AI Basics in Bangla", "bn": "এআই পরিচিতি", "level": "Beginner", "hours": 8, "learners": 1120, "tag": "Digital"},
    {"title": "Data Entry & MS Office", "bn": "ডেটা এন্ট্রি", "level": "Beginner", "hours": 12, "learners": 880, "tag": "Digital"},
    {"title": "Customer Support (Bangla/EN)", "bn": "কাস্টমার সাপোর্ট", "level": "Intermediate", "hours": 14, "learners": 410, "tag": "Service"},
    {"title": "Local Business Bookkeeping", "bn": "হিসাব রক্ষা", "level": "Beginner", "hours": 10, "learners": 690, "tag": "Business"},
]

JOBS = [
    {"title": "Garment QC (Remote)", "org": "Aarong Supply", "type": "Remote", "pay": "৳ 14,000/mo", "district": "Dhaka"},
    {"title": "Nakshi Kantha Artisan", "org": "Jaago Foundation", "type": "Piece-rate", "pay": "৳ 220/piece", "district": "Rangpur"},
    {"title": "Data Annotation (Bangla)", "org": "GigaTech NGO", "type": "Remote", "pay": "৳ 18,000/mo", "district": "Any"},
    {"title": "Customer Support — Bangla", "org": "Daraz BD", "type": "Remote PT", "pay": "৳ 9,500/mo", "district": "Any"},
    {"title": "Poultry Cluster Lead", "op": "Govt Poultry Scheme", "type": "Field", "pay": "৳ 16,500/mo", "district": "Mymensingh"},
    {"title": "Tailoring Cluster Worker", "org": "BRAC SME", "type": "Hybrid", "pay": "৳ 12,000/mo", "district": "Khulna"},
    {"title": "School Liaison Volunteer", "org": "Save the Children", "type": "Field PT", "pay": "৳ 6,500/mo", "district": "Sylhet"},
    {"title": "Pickle Production Helper", "org": "Pran-RFL", "type": "On-site", "pay": "৳ 11,000/mo", "district": "Chattogram"},
]

STORIES = [
    {
        "name": "Rahima Khatun",
        "age": 32,
        "district": "Bogura",
        "bn": "রহিমা খাতুন",
        "role": "Tailor & online seller",
        "quote": "My daughter is the first in our family to study science — while I run my orders from the porch.",
        "metric": "৳ 9,200/mo · 2 children in school",
    },
    {
        "name": "Sufia Begum",
        "age": 41,
        "district": "Satkhira",
        "bn": "সুফিয়া বেগম",
        "role": "Nakshi kantha cluster lead",
        "quote": "Sutara helped 14 women in our village. None of our children dropped out this year.",
        "metric": "৳ 12,800/mo · cluster of 14",
    },
    {
        "name": "Morjina Akter",
        "age": 27,
        "district": "Rangpur",
        "bn": "মর্জিনা আক্তার",
        "role": "Data annotation (Bangla)",
        "quote": "I work two hours a day on my phone. My son is in class 5 now — top of his class.",
        "metric": "৳ 7,500/mo · 1 child in school",
    },
]

PARTNERS = ["BRAC", "UNICEF", "ILO", "World Bank", "a2i", "PKSF", "Grameen", "Aarong"]

@app.route("/")
def index():
    return render_template("index.html", stats=HERO_STATS, problem_stats=PROBLEM_STATS, stories=STORIES, partners=PARTNERS)

@app.route("/training")
def training():
    return render_template("training.html", courses=COURSES)

@app.route("/jobs")
def jobs():
    return render_template("jobs.html", jobs=JOBS)

@app.route("/impact")
def impact():
    return render_template("impact.html", income_growth=INCOME_GROWTH)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
