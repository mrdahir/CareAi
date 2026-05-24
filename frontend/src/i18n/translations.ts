import type { Language } from "../types/common";

export type TranslationKey =
  | "nav.home"
  | "nav.chat"
  | "nav.recommend"
  | "nav.myth"
  | "nav.about"
  | "home.title"
  | "home.subtitle"
  | "home.cta"
  | "home.feature.chat.title"
  | "home.feature.chat.desc"
  | "home.feature.recommend.title"
  | "home.feature.recommend.desc"
  | "home.feature.myth.title"
  | "home.feature.myth.desc"
  | "about.title"
  | "about.p1"
  | "about.p2"
  | "chat.title"
  | "chat.clear"
  | "chat.disclaimer"
  | "chat.placeholder"
  | "chat.send"
  | "myth.title"
  | "myth.intro"
  | "myth.placeholder"
  | "myth.submit"
  | "myth.isMyth"
  | "myth.factCheck"
  | "myth.severity"
  | "myth.fact"
  | "myth.sources"
  | "recommend.title"
  | "recommend.surveyTitle"
  | "recommend.back"
  | "recommend.next"
  | "recommend.submit"
  | "recommend.age"
  | "recommend.goals"
  | "recommend.goals.space"
  | "recommend.goals.prevent"
  | "recommend.goals.flexible"
  | "recommend.breastfeeding"
  | "recommend.health"
  | "recommend.duration"
  | "recommend.duration.short"
  | "recommend.duration.medium"
  | "recommend.duration.long"
  | "recommend.region"
  | "error.generic"
  | "notFound"
  | "programme.title"
  | "programme.visits"
  | "programme.counselled"
  | "programme.counties"
  | "programme.topMethod";

type Dict = Record<TranslationKey, string>;

const en: Dict = {
  "nav.home": "Home",
  "nav.chat": "Chat",
  "nav.recommend": "Recommend",
  "nav.myth": "Myth Buster",
  "nav.about": "About",
  "home.title": "CareApp",
  "home.subtitle":
    "Reproductive health education for Sub-Saharan Africa — multilingual, private, and evidence-based.",
  "home.cta": "Start chatting",
  "home.feature.chat.title": "Health Chat",
  "home.feature.chat.desc": "Ask questions about contraception in your language.",
  "home.feature.recommend.title": "Get Recommendations",
  "home.feature.recommend.desc": "Personalized method suggestions based on your profile.",
  "home.feature.myth.title": "Myth Buster",
  "home.feature.myth.desc": "Verify common myths with evidence-based facts.",
  "about.title": "About CareApp",
  "about.p1":
    "CareApp is a reproductive health education assistant designed for Sub-Saharan Africa. It supports English, Kiswahili, Amharic, French, and Somali, and works on low-bandwidth mobile connections.",
  "about.p2":
    "Information is sourced from WHO and CDC guidelines. CareApp does not replace professional medical care.",
  "chat.title": "Health Chat",
  "chat.clear": "Clear",
  "chat.disclaimer":
    "Not a doctor. For emergencies, visit your nearest health facility.",
  "chat.placeholder": "Type your question...",
  "chat.send": "Send",
  "myth.title": "Myth Buster",
  "myth.intro":
    "Enter a statement you have heard about contraception or family planning.",
  "myth.placeholder": 'e.g. "Family planning causes infertility"',
  "myth.submit": "Check fact",
  "myth.isMyth": "This is a common myth",
  "myth.factCheck": "Fact check",
  "myth.severity": "Severity",
  "myth.fact": "Fact",
  "myth.sources": "Sources",
  "recommend.title": "Contraceptive recommendations",
  "recommend.surveyTitle": "Tell us about your needs",
  "recommend.back": "Back",
  "recommend.next": "Next",
  "recommend.submit": "Get recommendations",
  "recommend.age": "Your age (15-49)",
  "recommend.goals": "Pregnancy goals",
  "recommend.goals.space": "Space children",
  "recommend.goals.prevent": "Prevent pregnancy",
  "recommend.goals.flexible": "Flexible / not sure",
  "recommend.breastfeeding": "Currently breastfeeding",
  "recommend.health": "Health conditions (if any)",
  "recommend.duration": "Preferred duration",
  "recommend.duration.short": "Short term",
  "recommend.duration.medium": "Medium (months-years)",
  "recommend.duration.long": "Long term",
  "recommend.region": "Region",
  "error.generic": "Something went wrong",
  "notFound": "Page not found",
  "programme.title": "Western Kenya programme data",
  "programme.visits": "Client visits",
  "programme.counselled": "Counselled",
  "programme.counties": "Counties",
  "programme.topMethod": "Top method",
};

const sw: Dict = {
  ...en,
  "nav.home": "Nyumbani",
  "nav.chat": "Mazungumzo",
  "nav.recommend": "Mapendekezo",
  "nav.myth": "Ukweli wa Ngono",
  "nav.about": "Kuhusu",
  "home.subtitle":
    "Elimu ya afya ya uzazi kwa Afrika ya Kusini mwa Jangwa — lugha nyingi, faragha, na msingi wa ushahidi.",
  "home.cta": "Anza mazungumzo",
  "home.feature.chat.desc": "Uliza maswali kuhusu uzazi wa mpango kwa lugha yako.",
  "home.feature.recommend.desc": "Mapendekezo ya njia kulingana na wasifu wako.",
  "home.feature.myth.desc": "Thibitisha hadithi za kawaida kwa ukweli.",
  "about.title": "Kuhusu CareApp",
  "about.p1":
    "CareApp ni msaidizi wa elimu ya afya ya uzazi kwa Afrika ya Kusini mwa Jangwa. Inasaidia Kiingereza, Kiswahili, Kiamhari, Kifaransa, na Kisomali.",
  "about.p2":
    "Taarifa zinatoka kwa miongozo ya WHO na CDC. CareApp haibadili huduma ya kitaalamu.",
  "chat.title": "Mazungumzo ya Afya",
  "chat.clear": "Futa",
  "chat.disclaimer":
    "Si daktari. Kwa dharura, tembelea kituo cha afya kilicho karibu.",
  "chat.placeholder": "Andika swali lako...",
  "myth.title": "Ukweli wa Ngono",
  "myth.intro":
    "Andika kauli uliyosikia kuhusu uzazi wa mpango au kinga ya mimba.",
  "myth.placeholder": 'mf. "Uzazi wa mpango husababisha tasa"',
  "myth.submit": "Angalia ukweli",
  "myth.isMyth": "Hii ni hadithi ya kawaida",
  "myth.factCheck": "Ukaguzi wa ukweli",
  "myth.fact": "Ukweli",
  "myth.sources": "Vyanzo",
  "recommend.title": "Mapendekezo ya kinga ya mimba",
  "recommend.surveyTitle": "Tuambie mahitaji yako",
  "recommend.back": "Rudi",
  "recommend.next": "Ifuatayo",
  "recommend.submit": "Pata mapendekezo",
  "recommend.age": "Umri wako (15-49)",
  "recommend.goals": "Malengo ya ujauzito",
  "recommend.goals.space": "Panga watoto",
  "recommend.goals.prevent": "Zuia ujauzito",
  "recommend.goals.flexible": "Sijui / kubadilika",
  "recommend.breastfeeding": "Nanyonyesha sasa",
  "recommend.health": "Hali za kiafya (ikiwa zipo)",
  "recommend.duration": "Muda unaopendelea",
  "recommend.duration.short": "Muda mfupi",
  "recommend.duration.medium": "Wastani (miezi-miaka)",
  "recommend.duration.long": "Muda mrefu",
  "recommend.region": "Eneo",
  "error.generic": "Kuna hitilafu",
  "notFound": "Ukurasa haupatikani",
};

const fr: Dict = {
  ...en,
  "nav.home": "Accueil",
  "nav.chat": "Discussion",
  "nav.recommend": "Conseils",
  "nav.myth": "Mythes",
  "nav.about": "À propos",
  "home.subtitle":
    "Éducation en santé reproductive pour l'Afrique subsaharienne — multilingue et fondée sur des preuves.",
  "home.cta": "Commencer",
  "home.feature.chat.desc":
    "Posez vos questions sur la contraception dans votre langue.",
  "home.feature.recommend.desc":
    "Suggestions personnalisées selon votre profil.",
  "home.feature.myth.desc":
    "Vérifiez les idées reçues avec des faits.",
  "about.title": "À propos de CareApp",
  "about.p1":
    "CareApp est un assistant d'éducation en santé reproductive pour l'Afrique subsaharienne (anglais, swahili, amharique, français, somali).",
  "about.p2":
    "Informations issues des directives OMS et CDC. Ne remplace pas un médecin.",
  "chat.title": "Discussion santé",
  "chat.clear": "Effacer",
  "chat.disclaimer":
    "Pas un médecin. En urgence, consultez un centre de santé.",
  "chat.placeholder": "Tapez votre question...",
  "myth.title": "Chasseur de mythes",
  "myth.intro":
    "Entrez une affirmation entendue sur la contraception ou la planification familiale.",
  "myth.placeholder": 'ex. « La contraception cause l\'infertilité »',
  "myth.submit": "Vérifier",
  "myth.isMyth": "C'est un mythe courant",
  "myth.factCheck": "Vérification",
  "myth.fact": "Fait",
  "myth.sources": "Sources",
  "recommend.title": "Recommandations contraceptives",
  "recommend.surveyTitle": "Parlez-nous de vos besoins",
  "recommend.back": "Retour",
  "recommend.next": "Suivant",
  "recommend.submit": "Obtenir des recommandations",
  "recommend.age": "Votre âge (15-49)",
  "recommend.goals": "Objectifs de grossesse",
  "recommend.goals.space": "Espacer les enfants",
  "recommend.goals.prevent": "Éviter une grossesse",
  "recommend.goals.flexible": "Flexible / pas sûr",
  "recommend.breastfeeding": "J'allaite actuellement",
  "recommend.health": "Conditions de santé (le cas échéant)",
  "recommend.duration": "Durée préférée",
  "recommend.duration.short": "Court terme",
  "recommend.duration.medium": "Moyen (mois-années)",
  "recommend.duration.long": "Long terme",
  "recommend.region": "Région",
  "error.generic": "Une erreur s'est produite",
  "notFound": "Page introuvable",
};

const so: Dict = {
  ...en,
  "nav.home": "Guriga",
  "nav.chat": "Sheeko",
  "nav.recommend": "Talo",
  "nav.myth": "Halyeey",
  "nav.about": "Ku saabsan",
  "home.subtitle":
    "Waxbarashada caafimaadka taranka ee Afrika ka hooseysa Saxaraha — luqado badan, gaar ah, caddayn ku salaysan.",
  "home.cta": "Bilow sheekada",
  "home.feature.chat.desc":
    "Su'aalo ka weydii ka hortagga uurka luqaddaada.",
  "home.feature.recommend.desc":
    "Talooyin habab ku salaysan xogtaada.",
  "home.feature.myth.desc":
    "Xaqiiji halyeeyada caadiga ah.",
  "about.title": "Ku saabsan CareApp",
  "about.p1":
    "CareApp waa kaaliyaha waxbarashada caafimaadka taranka ee Afrika. Waxaa lagu taageeraa Ingiriisi, Kiswahili, Amxaari, Faransiis, iyo Soomaali.",
  "about.p2":
    "Macluumaadka wuxuu ka yimaadaa WHO iyo CDC. CareApp ma beddelo daryeelka caafimaad.",
  "chat.title": "Sheeko Caafimaad",
  "chat.clear": "Tirtir",
  "chat.disclaimer":
    "Ma aha dhakhtar. Xaalad degdeg ah, tag xarunta caafimaadka ugu dhow.",
  "chat.placeholder": "Qor su'aashaada...",
  "myth.title": "Halyeeyada",
  "myth.intro":
    "Geli hadal aad ka maqashay ka hortagga uurka ama qorshaynta qoyska.",
  "myth.placeholder": 'tusaale "Qorshaynta qoyska waxay keentaa madhalaysnimo"',
  "myth.submit": "Hubi xaqiiqda",
  "myth.isMyth": "Tani waa halyeey caadi ah",
  "myth.factCheck": "Hubinta xaqiiqda",
  "myth.fact": "Xaqiiqo",
  "myth.sources": "Ilaha",
  "recommend.title": "Talooyinka ka hortagga uurka",
  "recommend.surveyTitle": "Noo sheeg baahiyahaaga",
  "recommend.back": "Dib",
  "recommend.next": "Xiga",
  "recommend.submit": "Hel talooyin",
  "recommend.age": "Da'daada (15-49)",
  "recommend.goals": "Ujeeddooyinka uurka",
  "recommend.goals.space": "Kala fogee carruurta",
  "recommend.goals.prevent": "Ka hortag uurka",
  "recommend.goals.flexible": "Ma hubo / dabacsan",
  "recommend.breastfeeding": "Hadda naasnuujinaya",
  "recommend.health": "Xaaladaha caafimaadka (haddii ay jiraan)",
  "recommend.duration": "Muddada aad doorbidayso",
  "recommend.duration.short": "Muddo gaaban",
  "recommend.duration.medium": "Dhexdhexaad (bilood-sano)",
  "recommend.duration.long": "Muddo dheer",
  "recommend.region": "Gobol",
  "error.generic": "Wax baa khaldamay",
  "notFound": "Bogga lama helin",
};

const am: Dict = {
  ...en,
  "nav.home": "መነሻ",
  "nav.chat": "ውይይት",
  "nav.recommend": "ምክር",
  "nav.myth": "አፈ ታሪክ",
  "nav.about": "ስለ",
  "home.subtitle":
    "የወሊድ ጤና ትምህርት ለሰሃራ በታች አፍሪካ — ብዙ ቋንቋ፣ የግል፣ በማስረጃ የተደገፈ።",
  "home.cta": "ውይይት ጀምር",
  "home.feature.chat.desc": "በቋንቋዎ ስለ መከላከያ ጥያቄ ይጠይቁ።",
  "home.feature.recommend.desc": "በመገለጫዎ ላይ የተመሠረተ ምክር።",
  "home.feature.myth.desc": "የተለመዱ አፈ ታሪኮችን ያረጋግጡ።",
  "about.title": "ስለ CareApp",
  "about.p1":
    "CareApp ለሰሃራ በታች አፍሪካ የወሊድ ጤና ትምህርት ረዳት ነው። እንግሊዝኛ፣ Kiswahili፣ አማርኛ፣ ፈረንሳይኛ እና ሶማሊ ይደገፋል።",
  "about.p2":
    "መረጃ ከ WHO እና CDC መመሪያዎች ይመጣል። CareApp ሙያዊ ሕክምና አይተካም።",
  "chat.title": "የጤና ውይይት",
  "chat.clear": "አጽዳ",
  "chat.disclaimer":
    "ዶክተር አይደለም። በአስቸኳይ፣ ወደ ቅርብ የጤና ተቋም ይሂዱ።",
  "chat.placeholder": "ጥያቄዎን ይፃፉ...",
  "myth.title": "አፈ ታሪክ መፈታት",
  "myth.intro": "ስለ መከላከያ ወይም የቤተሰብ እቅድ የሰማዎትን አስተያየት ያስገቡ።",
  "myth.placeholder": 'ለምሳሌ «የቤተሰብ እቅድ መናን ያስከትላል»',
  "myth.submit": "አረጋግጥ",
  "myth.isMyth": "ይህ የተለመደ አፈ ታሪክ ነው",
  "myth.factCheck": "የእውነት ምርመራ",
  "myth.fact": "እውነት",
  "myth.sources": "ምንጮች",
  "recommend.title": "የመከላከያ ምክሮች",
  "recommend.surveyTitle": "ስለ ፍላጎትዎ ይንገሩን",
  "recommend.back": "ተመለስ",
  "recommend.next": "ቀጣይ",
  "recommend.submit": "ምክሮችን ያግኙ",
  "recommend.age": "ዕድሜዎ (15-49)",
  "recommend.goals": "የእርግዝና ግቦች",
  "recommend.goals.space": "ልጆችን ማራቅ",
  "recommend.goals.prevent": "እርግዝና መከላከል",
  "recommend.goals.flexible": "እርግጠኛ አይደለም",
  "recommend.breastfeeding": "አሁን እየጠበቅኩ ነው",
  "recommend.health": "የጤና ሁኔታዎች (ካሉ)",
  "recommend.duration": "የሚመረጠው ጊዜ",
  "recommend.duration.short": "አጭር ጊዜ",
  "recommend.duration.medium": "መካከለኛ",
  "recommend.duration.long": "ረጅም ጊዜ",
  "recommend.region": "ክልል",
  "error.generic": "ስህተት ተከስቷል",
  "notFound": "ገጹ አልተገኘም",
};

export const translations: Record<Language, Dict> = { en, sw, am, fr, so };

export function t(lang: Language, key: TranslationKey): string {
  return translations[lang]?.[key] ?? translations.en[key] ?? key;
}
