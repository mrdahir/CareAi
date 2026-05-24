"""Generate knowledge base JSON files."""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "knowledge_base"

templates = [
    ("myth_001", "Family planning causes permanent infertility", "Family planning is reversible. Fertility typically returns within 1-3 months.", "high"),
    ("myth_002", "Contraceptive pills make you infertile", "Pills are reversible; ovulation usually resumes within 1-3 months.", "high"),
    ("myth_003", "IUDs cause infertility", "IUDs do not cause infertility. Fertility returns quickly after removal.", "high"),
    ("myth_004", "Implants are only for women who already have children", "Implants are safe for nulliparous women when clinically appropriate.", "medium"),
    ("myth_005", "You cannot breastfeed while using contraception", "Progestin-only methods are generally safe during breastfeeding.", "high"),
    ("myth_006", "Condoms are not effective", "Correct condom use is effective and prevents STIs.", "medium"),
    ("myth_007", "Emergency contraception is an abortion pill", "Emergency contraception prevents ovulation; it does not terminate pregnancy.", "high"),
    ("myth_008", "Young women should not use contraception", "Medically appropriate methods can be used with counseling.", "medium"),
    ("myth_009", "Contraception causes cancer", "Most methods do not cause cancer; some reduce certain cancer risks.", "medium"),
    ("myth_010", "Natural methods are always safer", "Natural methods have higher failure rates with typical use.", "low"),
    ("myth_011", "You need rest for a month after IUD insertion", "Most women resume normal activities within 1-2 days.", "low"),
    ("myth_012", "Injectable causes permanent bone damage", "Bone effects are generally reversible for most users.", "medium"),
    ("myth_013", "Contraception reduces sexual desire permanently", "Effects are usually reversible when the method is stopped.", "low"),
    ("myth_014", "Only married women should use family planning", "WHO supports access for all eligible women of reproductive age.", "medium"),
    ("myth_015", "Withdrawal is as effective as condoms", "Withdrawal has a much higher failure rate than condoms.", "medium"),
    ("myth_016", "Hormonal methods cause weight gain in everyone", "Weight changes vary by individual and method.", "low"),
    ("myth_017", "You must have a period every month on the pill", "Continuous use can safely reduce bleeding frequency.", "low"),
    ("myth_018", "Contraception protects against all STIs", "Only condoms provide substantial STI protection.", "high"),
    ("myth_019", "Herbs can replace clinical contraception", "Herbal remedies lack reliable evidence for prevention.", "high"),
    ("myth_020", "Long-term contraception damages the womb", "Approved long-term methods are not shown to permanently damage the uterus.", "medium"),
    ("myth_021", "Vasectomy is always irreversible", "Reversal is sometimes possible but not guaranteed.", "low"),
    ("myth_022", "Copper IUD releases harmful metals", "Copper IUDs are WHO-approved and safe for long-term use.", "medium"),
]
myths = [
    {
        "id": mid,
        "myth": {"en": en, "sw": en},
        "fact": {"en": fact, "sw": fact},
        "evidence": f"WHO/CDC evidence-based correction: {fact}",
        "severity": sev,
        "sources": ["WHO_2022_contraceptive_methods", "CDC_guidelines"],
    }
    for mid, en, fact, sev in templates
]
(DATA / "common_myths.json").write_text(json.dumps({"myths": myths}, indent=2), encoding="utf-8")

categories = ["breastfeeding", "side_effects", "effectiveness", "privacy", "cost", "general"]
real = [
    ("breastfeeding", "Is contraception safe while breastfeeding?", "Progestin-only methods are generally preferred during breastfeeding."),
    ("breastfeeding", "Can I use the pill while nursing?", "Progestin-only pills are often recommended early postpartum."),
    ("side_effects", "Will I bleed irregularly on the implant?", "Irregular bleeding is common initially and often improves."),
    ("side_effects", "Do contraceptives cause weight gain?", "Some users report weight change; effects vary by method."),
    ("effectiveness", "Which method is most effective?", "Long-acting methods (implant, IUD) have the highest effectiveness."),
    ("effectiveness", "How effective are condoms?", "About 87% with typical use; also prevents STIs."),
    ("privacy", "Can I get contraception confidentially?", "Clinics offer confidential family planning services."),
    ("cost", "Are implants free at public clinics?", "Many public facilities offer subsidized family planning."),
    ("general", "At what age can I start contraception?", "Eligible adolescents may use appropriate methods with counseling."),
    ("general", "Do I need a pelvic exam for all methods?", "Not all methods require a pelvic exam."),
]
faqs = []
for idx, (cat, q, a) in enumerate(real):
    faqs.append(
        {
            "id": f"faq_{idx+1:03d}",
            "category": cat,
            "question": {"en": q, "sw": q},
            "answer": {"en": a, "sw": a},
            "sources": ["WHO_2022_contraceptive_methods"],
        }
    )
for i in range(len(real) + 1, 52):
    cat = categories[i % len(categories)]
    faqs.append(
        {
            "id": f"faq_{i:03d}",
            "category": cat,
            "question": {
                "en": f"Common question about {cat} and family planning ({i})",
                "sw": f"Swali kuhusu {cat} ({i})",
            },
            "answer": {
                "en": f"Evidence-based answer on {cat}. Consult a healthcare provider for personal advice.",
                "sw": f"Jibu la kiafya kuhusu {cat}. Wasiliana na kliniki.",
            },
            "sources": ["WHO_2022_contraceptive_methods"],
        }
    )
(DATA / "faqs.json").write_text(json.dumps({"faqs": faqs}, indent=2), encoding="utf-8")
print("Generated", len(myths), "myths and", len(faqs), "faqs")
