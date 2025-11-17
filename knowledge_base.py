"""
The Treatment Knowledge Base for the Farmer's AI Assistant.

This file stores structured, expert-written, pre-translated advice for all
plant diseases. The backend (app.py) will query this dictionary to build
custom responses in the user's selected language.

Your task is to fill in the "..." placeholders with the correct translations
for 'kn' (Kannada), 'te' (Telugu), and 'hi' (Hindi).
"""
SAFETY_NOTE = {

    'en': ("**Important Safety Note:** I am not a certified agricultural extension officer... "

           "Always follow the pesticide/product label, local regulations, safety instructions (PPE), "

           "and consult your local agricultural extension service."),

    'kn': ("**ಪ್ರಮುಖ ಸುರಕ್ಷತಾ ಸೂಚನೆ:** ನಾನು ಪ್ರಮಾಣೀಕೃತ ಕೃಷಿ ವಿಸ್ತರಣಾ ಅಧಿಕಾರಿಯಲ್ಲ... "

           "ಯಾವಾಗಲೂ ಕೀಟನಾಶಕ/ಉತ್ಪನ್ನದ ಲೇಬಲ್, ಸ್ಥಳीय ನಿಯಮಗಳು, ಸುರಕ್ಷತಾ ಸೂಚನೆಗಳನ್ನು (ಪಿಪಿಇ) ಅನುಸರಿಸಿ, "

           "ಮತ್ತು ಅಂತಿಮ ನಿರ್ಧಾರಗಳಿಗಾಗಿ ನಿಮ್ಮ ಸ್ಥಳೀಯ ಕೃಷಿ ವಿಸ್ತರಣಾ ಸೇವೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ."),

    'te': ("**ముఖ్య గమనిక:** నేను ధృవీకరింపబడిన వ్యవసాయ విస్తరణ అధికారి కాదు... "

           "ఎల్లప్పుడూ పురుగుమందు/ఉత్పత్తి లేబుల్, స్థానిక నియమాలు, భద్రత సూచనలు (PPE) పాటించండి, "

           "మరియు తుది నిర్ణయాల కోసం మీ స్థానిక వ్యవసాయ విస్తరణ సేవను సంప్రదించండి."),

    'hi': ("**महत्वपूर्ण सुरक्षा नोट:** मैं एक प्रमाणित कृषि विस्तार अधिकारी नहीं हूँ... "

           "हमेशा कीटनाशक/उत्पाद लेबल, स्थानीय नियमों, सुरक्षा निर्देशों (पीपीई) का पालन करें, "

           "और अंतिम निर्णयों के लिए अपनी स्थानीय कृषि विस्तार सेवा से परामर्श करें।")

}



treatment_kb = {



    # -------------------------

    # APPLE

    # -------------------------

    'Apple___Apple_scab': {

        'soils': {

            'red': {

                'en': "Risk increases in poorly drained red soils—improve drainage, avoid overhead irrigation.",

                'hi': "खराब जल निकासी वाली लाल मिट्टी में जोखिम बढ़ता है—जल निकासी सुधारें, ओवरहेड सिंचाई से बचें।",

                'kn': "ಪುರుగు ಒಳಚರಂಡಿ ಇರುವ ಕೆಂಪು ಮಣ್ಣಿನಲ್ಲಿ ಅಪಾಯ ಹೆಚ್ಚಾಗುತ್ತದೆ — ಒಳಚರಂಡಿ ಸುಧಾರಿಸಿ, ಓವರ್‌ಹೆಡ್ ನೀರಾವರಿ ತಪ್ಪಿಸಿ.",

                'te': "చెడు డ్రైనేజీ కలిగిన ఎర్ర నేలలలో ప్రమాదం పెరుగుతుంది — డ్రైనేజ్ మెరుగుపరచండి, ఓవర్‌హెడ్ నీరు నివారించండి."

            },

            'black': {

                'en': "High moisture retention; thin canopy and improve airflow to reduce leaf wetness.",

                'hi': "उच्च नमी बनी रहती है; पत्तियों की सूखने के लिए कैनोपी पतला करें और वायु-संचालन बढ़ाएं।",

                'kn': "ಹೆಚ್ಚಿನ ತೇವಾಂಶದ ತೊಂದರೆ—ಕ canopy ಅನ್ನು ತೆಳುವಾಗಿಸಿ ಮತ್ತು ಗಾಳಿ ಹರಿವು ಹೆಚ್ಚಿಸಿ.",

                'te': "అధిక తేమ నిల్వ; ఆకుల ఒడిగుడ్డును తగ్గించడానికి క్యానోపీని పిండి చేయండి."

            },

            'alluvial': {

                'en': "Generally better drainage; maintain spray schedules during wet spells.",

                'hi': "आम तौर पर अच्छी निकासी; गीले समय में स्प्रे अनुसूची बनाए रखें।",

                'kn': "ಸಾಮಾನ್ಯವಾಗಿ ಉತ್ತಮ ಒಳಚರಂಡಿ — ತೇವಾವಧಿಯಲ್ಲಿ ಸ್ಪ್ರೇ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಪಾಲಿಸಿ.",

                'te': "సాధారణంగా మంచి డ్రైనేజ్ — తడి కాలంలో స్ప్రే షెడ్యూల్ పాటించండి."

            },

            'general': {

                'en': "Avoid prolonged leaf wetness; sanitation (remove fallen leaves) is key.",

                'hi': "लंबे समय तक पत्ती गीली रहने से बचें; स्वच्छता (गिरी पत्तियों को हटाना) महत्वपूर्ण है।",

                'kn': "ಉದ್ದ ಕಾಲ ಗಿಡದ ಇಲೆಗಳ ತೇವಾಂಶ ತಪ್ಪಿಸಿ; ಸ್ವಚ್ಛತಾ (ಬಿದ್ದ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ) ಮುಖ್ಯ.",

                'te': "పొడవుగా ఆకులు తడి ఉండకూడదు; శుభ్రత (పడి ఉన్న ఆకులను తీసేయండి) ముఖ్యం."

            }

        },

        'seasons': {

            'monsoon': {

                'en': "Highest risk. Protect new growth at bud-break. Repeat sprays every 7–14 days in wet periods.",

                'hi': "सबसे उच्च जोखिम। कली फूटने पर नई बढ़त रक्षा करें। गीले समय में 7–14 दिनों पर स्प्रे दोहराएं।",

                'kn': "ಅತಿ ಅಪಾಯದ ಅವಧಿ. ಮೊಗ್ಗು ಮುಗಿಸಿದಾಗ ಹೊಸ ಬೆಳವಣಿಗೆಯನ್ನು ರಕ್ಷಿಸಿ. ತೇವಾವಧಿಯಲ್ಲಿ ಪ್ರತಿ 7-14 ದಿನಕ್ಕೆ ಸ್ಪ್ರೇ ಮಾಡಿ.",

                'te': "అత్యధిక ప్రమాదం. పెదవుల విప్పిడిలో కొత్త వృద్ధిని రక్షించండి. తడిగా ఉన్న సమయంలో ప్రతి 7–14 రోజులకు స్ప్రే చేయండి."

            },

            'summer': {

                'en': "Lower risk but monitor irrigation; keep canopy open.",

                'hi': "जोखिम कम लेकिन सिंचाई पर निगरानी रखें; कैनोपी खुला रखें।",

                'kn': "ಅಲ್ಪ ಅಪಾಯ — ಶೋಧನೆ ಮತ್ತು ಓವರ್‌ಹೆಡ್ ನೀರಾವರಿಯನ್ನು ಕಡಿಮೆ ಮಾಡಿ.",

                'te': "కొందటి ప్రమాదం — నీటివ్వడంపై గమనించండి, క్యానోపీని ఓపెన్ ఉంచండి."

            },

            'winter': {

                'en': "Cool dry periods reduce disease; skip unnecessary sprays.",

                'hi': "शीतल शुष्क अवधि रोग कम करती है; गैर-जरूरी स्प्रे न करें।",

                'kn': "ತಣಿವೆ ಮತ್ತು ಒಣ ಕಾಲDisease ಕಡಿಮೆ—ಅವಶ್ಯದಿಲ್ಲದ ಸ್ಪ್ರೇಗಳನ್ನು ತಪ್ಪಿಸಿ.",

                'te': "చలి మరియు పొడి కాలంలో వ్యాధి తగ్గుతుంది; అవసరం లేని స్ప్రేలను చేయవద్దు."

            },

            'general': {

                'en': "Monitor during warm, humid windows and after rains.",

                'hi': "गर्म, नम परिस्थितियों और बारिश के बाद निगरानी करें।",

                'kn': "ಬೆಚ್ಚಗಿನ ಮತ್ತು ಆರ್ದ್ರ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಮತ್ತು ಮಳೆಯ ನಂತರ ಗಮನಿಸಿ.",

                'te': "వేయి ఉష్ణోగ్రతలు, తేమ ఉన్న సమయంలో మరియు వర్షాల తర్వాత గమనించండి."

            }

        },

        'action_plan': {

            'cultural': {

                'en': ("Sanitation: collect & destroy fallen leaves; prune for airflow; avoid overhead irrigation; "

                       "thin fruit to reduce humidity."),

                'hi': ("स्वच्छता: गिरी पत्तियाँ इकट्ठा कर नष्ट करें; वायु संचार के लिए छंटाई करें; ओवरहेड सिंचाई से बचें; "

                       "नमी कम करने हेतु फलों को पतला करें।"),

                'kn': ("ಸ್ವಚ್ಛತೆ: ಬಿದ್ದ ಎಲೆಗಳನ್ನು ಸೇರ್ಪಡೆ ಮಾಡಿ ನಾಶಮಾಡಿ; ಗಾಳಿ ಹರಿವಿಗಾಗಿ ಕತ್ತರಿಸಿ; ಓವರ್‌ಹೆಡ್ ನೀರಾವರಿಯನ್ನು ತಪ್ಪಿಸಿ; "

                       "ಆರ್ಡ್ರತೆ ಕಡಿಮೆ ಮಾಡಲು ಹಣ್ಣುಗಳನ್ನು ತೆಳ್ಳಗೊಳಿಸಿ."),

                'te': ("శుభ్రత: పడిపోయిన ఆకులను సేకరించి నిర్మూలించండి; గాలి ప్రసరణ కొరకు చెట్లు కొట్టండి; ఓవర్‌హెడ్ నీటివివిధి నివారించండి; "

                       "తేమ తగ్గించడానికి పండ్లను తక్కువగా ఉంచండి.")

            },

            'organic': {

                'en': ("Copper-based (organic-approved) sprays as protectants; lime-sulfur at dormant stage if permitted; "

                       "use Bacillus subtilis (commercial formulations) as foliar biocontrol; ensure thorough coverage."),

                'hi': ("कॉपper-आधारित (ऑर्गैनिक-स्वीकृत) स्प्रे सुरक्षात्मक; निष्क्रिय अवस्था में चूना-सल्फर (यदि अनुमति हो); "

                       "Bacillus subtilis वाणिज्यिक फॉर्मुलेशन के रूप में प्रयोग करें; अच्छी कवरेज सुनिश्चित करें।"),

                'kn': ("ಕಾಪರ್ ಆಧಾರಿತ (ಆರ್ಗ್ಯಾನಿಕ್ ಅನುಮೋದಿತ) ಸ್ಪ್ರೇಗಳು; ಡಾರ್ಮೆಂಟ್ ಹಂತದಲ್ಲಿ ಲೈಮ್-ಸಲ್ಫರ್ (ಅನುಮತಿ ಇದ್ದರೆ); "

                       "Bacillus subtilis ವಾಣಿಜ್ಯ ಉತ್ಪನ್ನಗಳನ್ನು ಬಳಸಿ; ಸಂಪೂರ್ಣ ಆವರಣೆ ಖಚಿತಗೊಳಿಸಿ."),

                'te': ("కాపర్ ఆధారిత (సేంద్రియ అనుమతిపొంది) స్ప్రేలు; డార్మెంట్ దశలో లైమ్-సల్ఫర్ (అనుమతి ఉంటే); "

                       "Bacillus subtilis వాణిజ్య రూపంలో ఉపయోగించండి; సమగ్ర కవర్ అవసరం.")

            },

            'chemical': {

                'en': ("Use protectant fungicides: copper oxychloride or copper hydroxide (typical spray conc. 0.2–0.3% w/v) "

                       "or multi-site protectants like mancozeb (follow label). Apply at bud-break and repeat every 7–14 days during high risk. "

                       "Do not exceed label dose; rotate modes of action to prevent resistance. ALWAYS follow label and local regulations."),

                'hi': ("रक्षात्मक कवकनाशक: तांबे ऑक्सीक्लोराइड या हाइड्रॉक्साइड (आम स्प्रे सांद्रता 0.2–0.3% w/v) या मैनकोजेब जैसे मल्टी-साइट प्रोटेक्टेंट। "

                       "कली फूटने पर और उच्च जोखिम में 7–14 दिनों पर दोहराएं। लेबल से अधिक मात्रा न करें; रोधक तंत्र बदलें। लेबल और स्थानीय नियमों का पालन करें।"),

                'kn': ("ರಕ್ಷಕ ಫಂಗಿಸೈಡ್‍ಗಳು: ಕಾಪರ್ ಓಕ್ಸಿಕ್ಲೋರೈಡ್/ಹೈಡ್ರಾಕ್ಸೈಡ್ (ಸಾಧಾರಣ ಕಾಂಸೆ. 0.2–0.3% w/v) ಅಥವಾ ಮ್ಯಾಂಕೋಝೆಬ್. "

                       "ಬಡ್-ಬ್ರೇಕ್‌ನಲ್ಲಿ ಅನ್ವಯಿಸಿ ಮತ್ತು ಉತ್ತಮ ಅಪಾಯದಲ್ಲಿ ಪ್ರತಿ 7–14 ದಿನಗಳಿಗೆ ಪುನರಾವರ್ತಿಸಿ. ಲೇಬಲ್ ಪಾಲಿಸಿ."),

                'te': ("రక్షక ఫంగిసైడ్స్: కాపర్ ఆక్సీక్లోరైడ్ లేదా కాపర్ హైడ్రాక్‌సైడ్ (సాధారణ కాంస్ 0.2–0.3% w/v) లేదా మాన్కోజెబ్ లాంటి మల్టీ-సైట్ ప్రొటెక్టెంట్లు. "

                       "బడ్-బ్రేక్‌లో అప్లై చేసి తడి కాలంలో ప్రతి 7–14 రోజులకు పునరావృతం చేయండి. లేబల్‌ను పాటించండి.")

            }

        }

    },



    'Apple___Black_rot': {

        'soils': {

            'red': {

                'en': "Warm wet pockets in red soils increase risk—promote airflow and remove infected fruit.",

                'hi': "लाल मिट्टी के गीले गरम हिस्से जोखिम बढ़ाते हैं—हवा का संचार बढ़ाएं और संक्रमित फल हटाएं।",

                'kn': "ಕೆಂಪು ಮಣ್ಣುಗಳಲ್ಲಿ ತೇವ ಮತ್ತು ತಾಪಮಾನ ಹೆಚ್ಚಿದರೆ ಅಪಾಯ ಹೆಚ್ಚಾಗುತ್ತದೆ — ಹಣ್ಣುಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಗಾಳಿ ಹರಿವು ಹೆಚ್ಚಿಸಿ.",

                'te': "ఎర్ర మడతల్లో తడి, వేడి ప్రాంతాలు ప్రమాదాన్ని పెంచుతాయి — संक्रमित పండ్లను తీసివేయండి."

            },

            'black': {

                'en': "Retains moisture; remove mummified fruit and prune to open canopy.",

                'hi': "नमी बनी रहती है; मम्मी हुए फल हटाएं और कैनोपी खोलने के लिए छंटाई करें।",

                'kn': "ತೇವಾಂಶ ಉಳಿಯುತ್ತದೆ; ಸಾಂಕ್ರಾಮಿಕ ಹಣ್ಣುಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಕ್ಯಾನೊಪಿಯನ್ನು ತೆಗೆಯಿರಿ.",

                'te': "తేమ నిలవుతుంది; మమ్మిఫైడ్ పండ్లను తొలగించండి."

            },

            'alluvial': {

                'en': "Manage irrigation to avoid prolonged leaf/fruit wetness; remove sources of inoculum.",

                'hi': "लंबे समय तक पत्ती/फल गीले न रखें; संक्रमण स्रोत हटाएं।",

                'kn': "ಇಲೆ/ಫಲ ಬಹುಮಾನವಾಗಿ ತೇವದಲ್ಲಿ ಇರದಂತೆ ಸರಿಯಾದ ನೀರು ನಿರ್ವಹಣೆ ಮಾಡಿ.",

                'te': "అవసరమైనంత మంటలు నివారించడానికి నీటిపారుదలను నిర్వహించండి."

            },

            'general': {

                'en': "Sanitation to remove overwintering mummies and infected debris is important.",

                'hi': "संक्रमित मम्मी और मलबे को हटाना महत्वपूर्ण है।",

                'kn': "ಅನೇಕ ಕಾಲದ ಮಮ್ಮಿಗಳನ್ನು ತೆಗೆದುಹಾಕುವುದು ಮುಖ್ಯ.",

                'te': "మమ్మిఫైడ్ పిండులను తొలగించడం ముఖ్యం."

            }

        },

        'seasons': {

            'monsoon': {

                'en': "High risk—treat newly infected fruit and maintain protective sprays.",

                'hi': "उच्च जोखिम—नए संक्रमित फलों का उपचार करें और सुरक्षात्मक स्प्रे बनाए रखें।",

                'kn': "ಎಚ್ಚರಿಕೆ ಅವಧಿ — ಹೊಸ ಸೋಂಕಾಗಿರುವ ಹಣ್ಣುಗಳನ್ನು ಚಿಕಿತ್ಸೆ ನೀಡಿ.",

                'te': "అత్యధిక ప్రమాదం — కొత్తగా సంక్రమించిన పండ్లపై చికిత్స చేయండి."

            },

            'summer': {

                'en': "Moderate risk; reduce irrigation frequency to limit wet hours.",

                'hi': "मध्यम जोखिम; गीले घंटों को कम करने के लिए सिंचाई घटाएं।",

                'kn': "ಮಧ್ಯಮ ಅಪಾಯ; ನೀರು ನೀಡುವ ಅವಧಿಯನ್ನು ಕಡಿಮೆ ಮಾಡಿ.",

                'te': "సగటున ప్రమాదం; నీటివాయు తగ్గించండి."

            },

            'winter': {

                'en': "Lower disease activity; clean up mummies before dormancy break.",

                'hi': "कम गतिविधि; निष्क्रियता से पहले मम्मी साफ करें।",

                'kn': "ಕಡಿಮೆ ರೋಗ ಚಟುವಟಿಕೆ — ಡಾರ್ಮೆಂಟ್ ಮುಂಚೆ ಕ್ಲೀನ್ ಅಪ್ ಮಾಡಿ.",

                'te': "తక్కువ వ్యాధి చర్య; డార్మంట్ ముందు శుభ్రపరచండి."

            }

        },

        'action_plan': {

            'cultural': {

                'en': "Remove mummified and rotting fruit; prune to improve air; do not leave fruit on ground.",

                'hi': "मम्मी और सड़े हुए फल हटाएं; हवा बढ़ाने के लिए छंटाई करें; फल जमीन पर न रखें।",

                'kn': "ಮಮ್ಮಿ ಮತ್ತು ಕೊಳೆಯುತ್ತಿರುವ ಹಣ್ಣನ್ನು ತೆಗೆದುಹಾಕಿ; ಹವೆಯನ್ನು ಸುಧಾರಿಸಲು ಕತ್ತರಿಸಿರಿ.",

                'te': "మమ్మీ మరియు తోడుకుపోతున్న పండ్లను తొలగించండి; గాలి ప్రవాహాన్ని మెరుగుపరచండి."

            },

            'organic': {

                'en': "Use copper formulations or biologicals (Bacillus spp.) as protective sprays; remove inoculum sources.",

                'hi': "तांबे या जैविक (Bacillus spp.) स्प्रे का उपयोग करें; संक्रमण स्रोत हटाएं।",

                'kn': "ಕಾಪರ್ ಅಥವಾ ಬ್ಯಾಕ್ಟೀರಿಯಾ ಆಧಾರಿತ ಬಯೋಪ್ರೊಡಕ್ಟ್‍ಗಳು ಬಳಸಿ.",

                'te': "కాపర్ లేదా బయోఫార్ములేషన్స్ ఉపయోగించండి."

            },

            'chemical': {

                'en': ("Protectants: mancozeb or chlorothalonil (follow label). For active infections consider systemic fungicide rotations "

                       "with different modes of action. Typical protectant spray spacing 7–14 days in wet weather."),

                'hi': ("प्रोटेक्टेंट: मैनकोजेब या क्लोरोथलोनिल (लेबल का पालन करें)। सक्रिय संक्रमण में सिस्टमिक फंगिसाइड रोटेशन अपनाएं।"),

                'kn': ("ರಕ್ಷಕ: ಮ್ಯಾಂಕೋಝೆಬ್ ಅಥವಾ ಕ್ಲೋರೊಥಲೋನಿಲ್. ಆಕ್ಷನ್ ಮೋಡ್‌ಗಳನ್ನು ರೋಟೇಟ್ ಮಾಡಿ."),

                'te': ("రక్షకాలు: మాంకోజెబ్ లేదా క్రోరోథాలోనిల్; అవసరమైతే సిస్టమిక్ రొటేషన్లు చేయండి.")

            }

        }

    },



    'Apple___Cedar_apple_rust': {

        'soils': {

            'red': {'en': "Wet microclimates favor disease; remove nearby alternate hosts if possible.", 'hi': "गीले सूक्ष्मजलवायु रोग को बढ़ावा देते हैं; निकटवर्ती वैकल्पिक होस्ट हटाएं।", 'kn': "ತೇವವಾದ ಪರಿಸ್ಥಿತಿ ರೋಗಕ್ಕೆ ಯೋಗ್ಯವಾಗಿದೆ; ಹತ್ತಿರದ ವಿಚಿತ್ರ ಹೋಸ್ಟ್‌ಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.", 'te': "తడి సూక్ష్మకాలుష్యాలు వ్యాధిని ప్రోత్సహిస్తాయి; సమీప ప్రత్యామ్నాయ యజమానులను తొలగించండి."},

            'black': {'en': "High moisture areas need canopy management.", 'hi': "उच्च नमी वाले क्षेत्रों में कैनोपी प्रबंधन आवश्यक है।", 'kn': "ಹೆಚ್ಚಿನ ತೇವಾಂಶ ಇರುವ ಪ್ರದೇಶಗಳಿಗೆ ಕ್ಯಾನೊಪಿ ನಿರ್ವಹಣೆ ಅಗತ್ಯ.", 'te': "తేమ ఎక్కువగా ఉన్న ప్రాంతాల్లో క్యానోపీ నిర్వహణ అవసరం."},

            'alluvial': {'en': "Manage windbreaks and remove junipers if feasible.", 'hi': "विंडब्रेक्स प्रबंधित करें और संभव हो तो जुनिपर हटाएं।", 'kn': "ಗಾಳಿ ತಡೆಯಲು ಮತ್ತು ಜೂನಿಪರ್‍ನ್ನು ತೆಗೆದುಹಾಕಲು ಪ್ರಯತ್ನಿಸಿ.", 'te': "వింట్ బ్రేక్స్ నిర్వహించండి మరియు జూనిపర్ లు ఉంటే తొలగించండి."},

            'general': {'en': "Alternate host (cedar/juniper) proximity is major factor—manage or remove.", 'hi': "वैकल्पिक होस्ट (सीडर) की निकटता प्रमुख कारक है—प्रबंधित या हटाएं।", 'kn': "ಬದಲಿ ಯಜಮಾನ ಬಳಿಯಿರುವುದು ಪ್ರಮುಖದು — ನಿರ್ವಹಿಸಿ ಅಥವಾ ತೆಗೆದುಹಾಕಿ.", 'te': "వికల్పిక యజమాని సమీపత ప్రధాన అంశం—నియంత్రించండి లేదా తీసివేయండి."}

        },

        'seasons': {

            'monsoon': {'en': "Spore release and infection peaks—protectant sprays before leaf emergence.", 'hi': "स्पोर रिलीज़ चरम पर—पत्ती उगने से पहले सुरक्षात्मक स्प्रे।", 'kn': "ಸ್ಪೋರ್ ಬಿಡುಗಡೆಯು ಉಚ್ಛ—is before leaf emergence.", 'te': "స్పోర్ విడుదల అధికం—ఆకులు వచ్చే ముందు రక్షక స్ప్రేలను చేయండి."},

            'summer': {'en': "Monitor and treat young leaves if infection observed.", 'hi': "युवा पत्ता संक्रमित दिखे तो उपचार करें।", 'kn': "ಯುವ ಎಲೆಗೆ ಸೋಂಕು ಕಂಡುಬಂದರೆ ಚಿಕಿತ್ಸೆ ನೀಡಿ.", 'te': "యువ ఆకులపై సంక్రమణ ఉంటే చికిత్స చేయండి."},

            'winter': {'en': "Disease activity low; focus on pruning and alternate host removal.", 'hi': "गतिविधि कम; छंटाई और वैकल्पिक होस्ट हटाने पर ध्यान दें।", 'kn': "ಕಡಿಮೆ ಚಟುವಟಿಕೆ; ಕತ್ತರಿಸುವುದು ಮತ್ತು ಬದಲಿ ಯಜಮಾನ ತೆಗೆದುಹಾಕುವುದು ಮುಖ್ಯ.", 'te': "కనిష్ట చర్య—కత్తరించి ప్రత్యామ్నాయ యజమానులను తొలగించండి."},

            'general': {'en': "Coordinate control of cedar/juniper nearby and orchard sprays.", 'hi': "सीडर/जुनिपर नियंत्रण और बाग़ स्प्रे समन्वय करें।", 'kn': "ವಚಿತ ಜೂನಿಪರ್ ನಿಯಂತ್ರಣೆ ಮತ್ತು ತೆಂಗು ಸ್ಪ್ರೇ ಗಳು ಸಮನ್ವಯಗೊಳಿಸಿ.", 'te': "సమీప జూనిపర్లు మరియు ఆర్డర్చ్ స్ప్రేలను సమన్వయించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Remove alternate hosts (junipers) near orchards; prune and improve airflow.", 'hi': "नजदीकी वैकल्पिक होस्ट हटाएं; छंटाई करें।", 'kn': "ಸಮೀಪದ ಜೂನಿಪರ್‍ಗಳನ್ನು ತೆಗೆದುಹಾಕಿ; ಕತ್ತರಿಸಿ.", 'te': "నెగడైన యజమానులను తొలగించండి; చెట్లను కత్తరించండి."},

            'organic': {'en': "Copper protectants; keep area around trees tidy. Biologicals may reduce inoculum.", 'hi': "कॉपर प्रोटेक्टेंट्स; आस-पास साफ रखें।", 'kn': "ಕಾಪರ್ ರಕ್ಷಕಗಳು; ವಾತಾವರಣವನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", 'te': "కాపర్ బేస్డ్ స్ప్రేలు; పరిసరాలను శుభ్రంగా ఉంచండి."},

            'chemical': {'en': "Protectant sprays (copper, mancozeb) at bud break and early leaf stage; repeat as label directs.", 'hi': "बड-ब्रेक पर और शुरुआती पत्ती चरण में प्रोटेक्टेंट स्प्रे (कॉपper, मैनकोजेब)।", 'kn': "ಬಡ್‌ಬ್ರೇಕ್‌ನಲ್ಲಿ ಕಾಪರ್/ಮ್ಯಾಂಕೋಝೆಬ್ ಸ್ಪ್ರೇ ಮಾಡಿ.", 'te': "బడ్-బ్రేక్‌లో కాపర్/మాంకోజెబ్ స్ప్రే చేయండి."}

        }

    },



    'Apple___healthy': {

        'soils': {

            'red': {'en': "Maintain drainage and good nutrition.", 'hi': "जल निकासी और पोषण बनाए रखें।", 'kn': "ಒಳ್ಳೆಯ ಒಳಚರಂಡಿ ಮತ್ತು ಪೋಷಣೆಯನ್ನು ಕಾಪಾಡಿ.", 'te': "డ్రైనేజ్ మరియు పోషకాలను పర్యవేక్షించండి."},

            'black': {'en': "Avoid waterlogging and manage fertility.", 'hi': "जलभराव से बचें और उर्वरक प्रबंधन करें।", 'kn': "ನೆನೆದಿರಬೇಡಿ ಮತ್ತು ಗೊಬ್ಬರವನ್ನು ವನ್ನು ನಿರ್ವಹಿಸಿ.", 'te': "నీటి నిల్వను నివారించండి; ఫర్టిలిటీ నిర్వహించండి."},

            'alluvial': {'en': "Normal care—monitor for pests & diseases.", 'hi': "सामान्य देखभाल—कीट व रोग देखें।", 'kn': "ಸಾರ್ವಜನಿಕ ಕಾಳಜಿ—ಹಾನಿಕಾರಕಗಳು ಮತ್ತು ರೋಗಗಳನ್ನು ಗಮನಿಸಿ.", 'te': "సాధారణ శ్రద్ధ—పొడవైన పంటలను గమనించండి."},

            'general': {'en': "Routine monitoring, pruning, balanced fertilization and irrigation scheduling.", 'hi': "नियमित निगरानी, छंटाई, संतुलित उर्वरन और सिंचाई शेड्यूल।", 'kn': "ಸಾಧಾರಣ ಸರಣಿ — ಶೋಧನೆ, ಕತ್ತರಿಸಿ, ಸಮತೋಲಿತ ಎೂರಿಕರಣ.", 'te': "నియమిత తనిఖీ, కత్తిరింపు, సమతుల్య ఎరువుల వినియోగం."}

        },

        'seasons': {'monsoon': {'en': "Increase monitoring for fungal disease.", 'hi': "फफूंदी रोग की निगरानी बढ़ाएं।", 'kn': "ಹವಾಮಾನಕ್ಕೆ ತಕ್ಕಂತೆ ರೋಗದ ಮೇಲ್ವಿಚಾರಣೆ ಹೆಚ್ಚಿಸಿ.", 'te': "ఫుంగల్ వ్యాధులపై పర్యవేక్షణ పెంచండి."},

                    'summer': {'en': "Watch for heat stress & irrigation scheduling.", 'hi': "गर्मी से सुरक्षा और सिंचाई तालिका देखें।", 'kn': "ಬಿಸಿಲಿನ ಒತ್ತಡ ಮತ್ತು ನೀರು ನೀರ್ ಪಟ್ಟಿ ಗಮನಿಸಿ.", 'te': "వేడితో సంబంధించిన పర్యవేక్షణ, నీరు షెడ్యూల్ పరిశీలన."},

                    'winter': {'en': "Dormant pruning and orchard sanitation.", 'hi': "निष्क्रिय छंटाई और बाग सैनिटेशन।", 'kn': "ಡಾರ್ಮೆಂಟ್ ಕತ್ತರಿಸುವ ಕಾರ್ಯ ಮತ್ತು ಸ್ವಚ್ಛತೆ.", 'te': "డార్మంట్ కత్తిరింపు మరియు శుభ్రపరచడం."},

                    'general': {'en': "Follow nutrient plan, monitor pests and disease, calibrate sprayers.", 'hi': "पोषण योजना पालन करें, कीट व रोग देखें, स्प्रेयर कैलिब्रेट करें।", 'kn': "ಪೋಷಕ ಯೋಜನೆ ಅನುಸರಿಸಿ, ಕೀಟಗಳು/ರೋಗಗಳ ಮೇಲೆ ಗಮನ ಇಡಿ.", 'te': "పోషక ప్రణాళిక పాటించండి, పర్యవేక్షణ కొనసాగించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Routine sanitation, pruning, balanced fertilization and irrigation.", 'hi': "नियमित सफाई, छंटाई, संतुलित उर्वरन और सिंचाई।", 'kn': "ನಿಯಮಿತ ಸ್ವಚ್ಛತೆ, ಕತ್ತರಿಸುವುದು, ಸಮತೋಲಿತ ಗೊಬ್ಬರ.", 'te': "సామాన్య శుభ్రత, కత్తిరింపు, సమతుల్య ఎరువుల వాడకం."},

            'organic': {'en': "Soil health: compost, biofertilizers; foliar biocontrols if needed.", 'hi': "मिट्टी स्वास्थ्य: कंपोस्ट, बायोफर्टिलाइज़र; जरूरत पर पर्णचर जैव नियंत्रण।", 'kn': "ನೇರಗೊಳ್ಳು: ಕಾಂಪೋಸ್ಟ್ ಮತ್ತು ಬಯೋ ಫರ್ಟಿಲೈಜರ್.", 'te': "మట్టిని ఆరోగ్యంగా ఉంచండి: కంపోస్ట్, బయో ఫర్టిలైజర్లు."},

            'chemical': {'en': "No chemical action if healthy; follow preventive copper sprays only if local advisories suggest.", 'hi': "यदि स्वस्थ है तो रासायनिक कार्रवाई आवश्यक नहीं; स्थानीय सलाह पर ही रोकथाम हेतु कॉपर स्प्रे।", 'kn': "ಆರೋಗ್ಯವಾಗಿದ್ದರೆ ರಾಸಾಯನಿಕಗಳನ್ನು ಬಳಸಬೇಡಿ.", 'te': "ఆరోగ్యంగా ఉంటే రసాయనాలు అవసరం లేదు."}

        }

    },




    # -------------------------

    # BLUEBERRY

    # -------------------------

    'Blueberry___healthy': {

        'soils': {

            'red': {'en': "Blueberry prefers acidic, well-drained soils; maintain pH 4.5–5.5.", 'hi': "ब्लूबेरी एसिडिक, अच्छी जल निकासी वाली मिट्टी पसंद करती है; pH 4.5–5.5 रखें।", 'kn': "ಬ್ಲೂಬೆರಿ ಆಸಿಡ್ ಮಣ್ಣನ್ನು ಇಷ್ಟಪಡುತ್ತದೆ; pH 4.5–5.5 ವಂದ್ರಿಸಿ.", 'te': "బ్లూబెర్రీ ఆమ్ల నెత్తెర ఆధారిత నేలలను ఇష్టపడుతుంది; pH 4.5–5.5."},

            'black': {'en': "Black soils high in salts may be unsuitable—monitor EC and amend.", 'hi': "लवण उच्च होने पर काली मिट्टी अनुपयुक्त हो सकती है—EC मॉनिटर करें।", 'kn': "ಕಪ್ಪು ಮಣ್ಣು ಉಪ್ಪಿನ ಪ್ರಮಾಣ ಹೆಚ್ಚಿದ್ದರೆ ಅನుకೂಲವಿಲ್ಲ.", 'te': "నల్ల నేలలో ఉప్పు ఎక్కువైతే అనుకూలం కాదు—EC గమనించండి."},

            'alluvial': {'en': "Ensure acidity & organic matter; good drainage.", 'hi': "अम्लता और जैविक पदार्थ सुनिश्चित करें; अच्छी जल निकासी।", 'kn': "ಆಮ್ಲತೆ ಮತ್ತು ಕಾರ್ಬೋನಿಕ್ ವಿಷಯವನ್ನು ಖಾತ್ರಿಪಡಿಸಿ.", 'te': "ఆమ్లితనం మరియు సేంద్రీయ పదార్థం ఉంచండి."},

            'general': {'en': "Blueberry entries: maintain acidity, mulching, and regular irrigation without waterlogging.", 'hi': "ब्लूबेरी: अम्लता, मल्चिंग और नियमित सिंचाई पर ध्यान रखें।", 'kn': "ಬ್ಲೂಬೆರಿ: ಆಸಿಡ್, ಮಲ್ಚಿಂಗ್, ಸರಿಯಾದ ನೀರು ನೀಡಲು ಗಮನಿಸಿ.", 'te': "బ్లూబెర్రీ: ఆమ్లితనం, మార్యాథి, సరైన నీరు."}

        },

        'seasons': {

            'monsoon': {'en': "Watch root rot in poorly drained soils; avoid waterlogging.", 'hi': "खराब निकासी में रूट रॉट देखें; जलभराव से बचें।", 'kn': "ತೇವದ ಮಣ್ಣುಗಳಲ್ಲಿ ರೂಟ್ ರಾಟ್ ಮೇಲೆ ಗಮನಿಸಿ.", 'te': "తడి నేలలో రూట్ రాట్ కు జాగ్రత్త."},

            'summer': {'en': "Irrigate to avoid drought stress; mulch to keep roots cool.", 'hi': "सूखा तनाव से बचने के लिए सिंचाई; जड़ों को ठंडा रखने के लिए मल्च करें।", 'kn': "ಬಿರುಕು ಬೇಡಿಕೆ ಇದ್ದರೆ ನೀರು ನೀಡಿ; ಮಲ್ಚ್ ಮಾಡಿ.", 'te': "వానపాటు తగ్గకుండా నీరు ఇవ్వండి; మల్చ్ చేయండి."},

            'winter': {'en': "Protect from late frosts if susceptible; reduce irrigation.", 'hi': "अगर संवेदनशील हो तो देर से पड़ने वाली ठंडी से बचाएं; सिंचाई कम करें।", 'kn': "ಹಿಮ ಕಡಿಮೆಯಾದಲ್ಲಿ రక్షణ ನೀಡಿ.", 'te': "తరువాతి చల్లబడే సమయంలో రక్షించండి."},

            'general': {'en': "Maintain soil pH and organic matter; fertilize per local recommendations.", 'hi': "मिट्टी pH और जैविक पदार्थ बनाए रखें; स्थानीय सिफारिशों के अनुसार उर्वरक दें।", 'kn': "ಮಣ್ಣು pH ಮತ್ತು ಕಾರ್ಬೋನಿಕ್ ವಿಷಯ ನೀರಾವರಿ ಮಾಡಿ.", 'te': "మట్టి pH మరియు ఆర్గానిక్ matter నిర్వహించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Mulch, maintain acidic pH, avoid waterlogging, good drainage.", 'hi': "मल्च, अम्लता बनाए रखें, जलभराव से बचें।", 'kn': "ಮಲ್ಚ್ ಮಾಡಿ, pH ಕಾಪಾಡಿ, ನೀರು ನಿಲ್ಲಿಸಬೇಡಿ.", 'te': "మల్చ్ చేయండి, pH నిర్వహించండి."},

            'organic': {'en': "Use composted organic matter; mycorrhizae inoculants may help root health.", 'hi': "कम्पोस्टेड जैविक पदार्थ उपयोग करें; मायकोराइजा जड़ स्वास्थ्य में मदद कर सकता है।", 'kn': "ಕಂಪೋಸ್ಟ್ ಮತ್ತು ಮೈಕೊರಿಜಾ ಬಳಸಿ.", 'te': "కంపోస్ట్ వాడండి; మైకోరైజా ఉపయోగించండి."},

            'chemical': {'en': "If needed, use fungicides labelled for blueberry root/foliar diseases — consult label & extension.", 'hi': "यदि आवश्यक हो तो ब्लूबेरी के लिए लेबल वाले फंगिसाइड का प्रयोग करें—लेबल और विस्तार सेवा से परामर्श करें।", 'kn': "ಆವಶ್ಯಕತೆ ಇದ್ದರೆ ಲೇಬಲ್ ಹೊಂದಿರುವ ಫಂಗಿಸೈಡ್ ಬಳಸಿ.", 'te': "అవసరమైతే లేబుల్ ఉన్న ఫంగిసైడ్ ఉపయోగించండి."}

        }

    },



    # -------------------------

    # CHERRY

    # -------------------------

    'Cherry___Powdery_mildew': {

        'soils': {

            'red': {'en': "Powdery mildew often worse in warm, sheltered microclimates; maintain air flow.", 'hi': "गर्म, सुरक्षित क्षेत्रों में पाउडरी मिल्ड्यू अधिक होता है; वायु प्रवाह बनाए रखें।", 'kn': "ಬಿಸಿಲಿನ ಮತ್ತು ಸಂರಕ್ಷಿತ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಹೆಚ್ಚಿನದು — ಗಾಳಿ ಹರಿವು ಇರಿಸಿಕೊಳ್ಳಿ.", 'te': "వేడిగా, రహదారి ప్రాంతాల్లో ఎక్కువగా ఉంటుంది — గాలి ప్రవాహం ఉంచండి."},

            'black': {'en': "High canopy humidity in black soils can favor mildew—prune to open canopy.", 'hi': "काली मिट्टी में उच्च कैनोपी आर्द्रता मिल्ड्यू को बढ़ाती है—छंटाई करें।", 'kn': "ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲಿ ಕ್ಯಾನೊಪಿ ತೇವಾಂಶ ಹೆಚ್ಚಾಗುತ್ತದೆ — ಕತ್ತರಿಸಿ.", 'te': "నల్ల నేలలో క్యానోపీ తేమ ఎక్కువైతే శుద్ధి చేయండి."},

            'alluvial': {'en': "Manage irrigation to reduce leaf wetness in evenings.", 'hi': "शाम के समय पत्ती गीली न हो—सिंचाई प्रबंधित करें।", 'kn': "ಸಂಜೆ ಎಲೆ ತೇವಾಂಶ ಕಡಿಮೆ ಮಾಡಲು ನೀರು ನಿಯಂತ್ರಿಸಿ.", 'te': "సాయంకాలంలో ఆకుల తేమ తగ్గించడానికి నీటిపారుదల నిర్వహించండి."},

            'general': {'en': "Avoid excessive nitrogen which favors tender new growth susceptible to mildew.", 'hi': "अत्यधिक नाइट्रोजन नया नाज़ुक विकास बढ़ाता है — इससे बचें।", 'kn': "ಅತಿಯಾದ ನೈಟ್ರೋಜನ್ ನವೀಕರಣವನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ — ತಪ್ಪಿಸಿ.", 'te': "అధిక నైట్రోజన్ కొత్త కోమల వృద్ధిని ప్రోత్సహిస్తుంది — జాగ్రత్త."}

        },

        'seasons': {

            'monsoon': {'en': "Humidity increases risk—protect new shoots, repeat sprays every 10–14 days if needed.", 'hi': "नमी बढ़ने पर जोखिम—नए शुट्स की रक्षा करें, 10–14 दिनों पर स्प्रे।", 'kn': "ತೇವಾಂಶ ಹೆಚ್ಚಿದರೆ 10–14 ದಿನಗಳಿಗೊಮ್ಮೆ ಸ್ಪ್ರೇ ಮಾಡಿ.", 'te': "తేమ పెరిగితే 10–14 రోజులకొకసారి స్ప్రే చేయండి."},

            'summer': {'en': "Warm dry weather may reduce outbreaks but monitor shaded areas.", 'hi': "गर्म शुष्क मौसम कम कर सकता है पर छायादार क्षेत्रों की निगरानी करें।", 'kn': "ಬೆಚ್ಚಗಿನ ಒಣ ಹವಾಮಾನ ಕಡಿಮೆ ಮಾಡಬಹುದು — ಛಾಯಾಗ್ರಸ್ತ ಪ್ರದೇಶಗಳನ್ನು ಗಮನಿಸಿ.", 'te': "వేడిగా పొడిగా ఉండి తక్కువగా ఉంటుంది — చాయల్లో గమనించండి."},

            'winter': {'en': "Dormant sprays (sulfur/lime-sulfur if permitted) can reduce inoculum.", 'hi': "निष्क्रिय स्प्रे (सल्फर/लाइम-सल्फर) संक्रमण घटा सकते हैं।", 'kn': "ಡಾರ್ಮೆಂಟ್ ಸರ್ಪೇ (ಸಲ್ಫರ್) ಬಳಸಿ.", 'te': "డార్మెంట్ సమయంలో సల్ఫర్ స్ప్రే చేయవచ్చు."},

            'general': {'en': "Monitor shaded & low-airflow parts of canopy closely.", 'hi': "छायादार और कम वायु वाले हिस्सों की निगरानी करें।", 'kn': "ಛಾಯಾದ ಪ್ರದೇಶಗಳನ್ನು ಸಮೀಪದಿಂದ ಗಮನಿಸಿ.", 'te': "చాయలో ఉన్న భాగాలను గమనించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Prune to open canopy, remove infected shoots, avoid excess nitrogen.", 'hi': "कैनोपी खोलने के लिए छंटाई करें, संक्रमित शुट्स हटाएं, अतिरिक्त नाइट्रोजन से बचें।", 'kn': "ಕನೋಪಿಯನ್ನು ತೆರವುಮಾಡಿ, ಸೋಂಕಿತ ಶೂಟ್‌ಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.", 'te': "క్యానోపీని తెరవండి, సంక్రమిత కాండాలను తీసివేయండి."},

            'organic': {'en': "Use sulfur-based sprays or potassium bicarbonate where approved; biocontrols (Ampelomyces) in some formulations.", 'hi': "सर्व मंज़ूर होने पर सल्फर या पोटेशियम बिकार्बोनेट का प्रयोग; कुछ बायोकंट्रोल उत्पाद।", 'kn': "ಸಲ್ಫರ್ ಅಥವಾ ಪೊಟಾಷಿಯಂ ಬಿಕಾರ್ಬೊನೆಟ್ ಬಳಸಬಹುದು.", 'te': "సల్ఫర్ లేదా పొటాషియం బయోకార్బోనేట్ వాడండి."},

            'chemical': {'en': "Use DMIs (e.g., triazoles) or QoI fungicides per label and rotate MoAs; protectant sprays every 10–14 days in high-risk periods.", 'hi': "डीएमआई या क्यूओआई फंगिसाइड, मोड़ बदलें; उच्च जोखिम में 10–14 दिन पर स्प्रे।", 'kn': "DMIs ಅಥವಾ QoI ಗಳನ್ನು ಲೇಬಲ್ ಪ್ರಕಾರ ಬಳಸಿ.", 'te': "DMIs లేదా QoI ఫంగిసైడ్స్ లేబుల్ ప్రకారం వాడండి."}

        }

    },



    'Cherry___healthy': {

        'soils': {

            'red': {'en': "Ensure good drainage; cherries dislike waterlogging.", 'hi': "अच्छी निकासी सुनिश्चित करें; चेरी जलभराव पसंद नहीं करती।", 'kn': "ಒಳ್ಳೆಯ ಒಳಚರಂಡಿ ಇಲ್ಲದೆ ಚೆರಿ ಬೆಳೆ नसುತ್ತೇ.", 'te': "మంచి డ్రైనేజ్ ఉంచండి; చెర్రీ నీరు నిలవకుండా ఉండదు."},

            'black': {'en': "Manage irrigation; avoid root saturation.", 'hi': "सिंचाई प्रबंधित करें; जड़ों को संतृप्त न रखें।", 'kn': "ನೀರಿನ ಭರಿತ ಸ್ಥಿತಿಯಿಂದ ತಪ್ಪಿಸಿಕೊಳ್ಳಿ.", 'te': "రూట్ సాచ్యురేషన్ నివారించండి."},

            'alluvial': {'en': "Maintain pH and fertility per local recommendations.", 'hi': "स्थानीय सुझाव के अनुसार pH और उर्वरक सुरक्षित रखें।", 'kn': "ಸ್ಥಳೀಯ ಸಲಹೆ ಅನುಸಾರ pH ಉಳಿಸಿ.", 'te': "ప్రాంతీయ సూచనల ప్రకారం pH నిర్వహించండి."},

            'general': {'en': "Routine pruning, pest monitoring and appropriate fertilization.", 'hi': "नियमित छंटाई, कीट निगरानी और उचित उर्वरक।", 'kn': "ನಿಯಮಿತ ಕತ್ತರಿಸುವುದು ಮತ್ತು ಕೀಟಗಳ ಮೇಲ್ವಿಚಾರಣೆ.", 'te': "నియమితగా పర్యవేక్షించండి."}

        },

        'seasons': {

            'monsoon': {'en': "Watch for fungal issues in humid spells.", 'hi': "नम मौसम में फफूंदी देखें।", 'kn': "ತೇವಾವಧಿಯಲ್ಲಿ ಫಂಗಸ್ ಸಮಸ್ಯೆಗಳಿಗೆ ಗಮನಿಸಿ.", 'te': "తడిగా ఉన్నప్పుడు ఫంగల్ బాధ్యత."},

            'summer': {'en': "Irrigate as needed; protect from heat stress.", 'hi': "आवश्यकतानुसार सिंचाई करें; गर्मी से बचाएं।", 'kn': "ಅವಶ್ಯಕತೆ ಇದ್ದರೆ ನೀರು ನೀಡಿರಿ.", 'te': "వేడిని నివారించండి."},

            'winter': {'en': "Dormant pruning and sanitation.", 'hi': "निष्क्रिय छंटाई और स्वच्छता।", 'kn': "ಡಾರ್ಮೆಂಟ್ ಕತ್ತರಿ.", 'te': "డార్మంట్ సమయంలో శుభ్రపరచండి."},

            'general': {'en': "Calibrate sprayers and follow IPM.", 'hi': "स्प्रेयर कैलिब्रेट करें और IPM अपनाएं।", 'kn': "ಸ್ಪ್ರೇಯರ್‌ಗಳನ್ನು ಕ್ಯಾಲಿಬ್ರೇಟ್ ಮಾಡಿ.", 'te': "స్ప్రేయర్‌లు పరీక్షించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Good sanitation, fruit removal, pruning to improve airflow.", 'hi': "स्वच्छता, फल हटाना और छंटाई।", 'kn': "ಸ್ವಚ್ಛತೆ ಮತ್ತು ಕತ್ತರಿಸುವುದು.", 'te': "శుభ్రత మరియు కత్తిరింపు."},

            'organic': {'en': "Use organic soil conditioners and biocontrols as necessary.", 'hi': "ऑर्गेनिक कंडीशनर और बायोकंट्रोल्स का उपयोग करें।", 'kn': "ಆರ್ಗ್ಯಾನ್ಯಿಕ್ ಉತ್ಪನ್ನಗಳನ್ನು ಬಳಸಿ.", 'te': "సేంద్రీయ పద్ధతులు వాడండి."},

            'chemical': {'en': "Only if disease occurs — use label-approved fungicides and follow safety rules.", 'hi': "रोग होने पर ही उपयोग करें — लेबल-अनुमोदित फंगिसाइड प्रयोग करें।", 'kn': "ರೋಗ ಹೊತ್ತರೆ ಮಾತ್ರ ರಾಸಾಯನಿಕ ಬಳಸಿ.", 'te': "వ్యాధి వస్తే మాత్రమే రసాయనాలు వాడండి."}

        }

    },



    # -------------------------

    # CORN (MAIZE)

    # -------------------------

    'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot': {

        'soils': {

            'red': {'en': "Warm, humid pockets favor Cercospora—manage residue and crop rotation.", 'hi': "गर्म, नम क्षेत्रों में सर्कोस्पोरा पसंद करती है—अवशेष प्रबंधन और फसल चक्र।", 'kn': "ಬಿಸಿಲು ಮತ್ತು ತೇವ ಇರುವಲ್ಲಿ ಹೆಚ್ಚು—ಅವಶೇಷ ನಿರ್ವಹಣೆ ಮಾಡಿ.", 'te': "వేడి తేమా ప్రాంతాల్లో ఎక్కువగా ఉంటుంది — రెసిడ్యూ నిర్వహించండి."},

            'black': {'en': "Residue retention increases inoculum—manage tillage and residue.", 'hi': "अवशेष संक्रमण बढ़ाते हैं—टिलेज और अवशेष प्रबंधित करें।", 'kn': "ಅವಶೇಷ ಹೆಚ್ಚಾಗಿರುವುದು ಸೋಂಕು ಕಾರಣ.", 'te': "రెసిడ్యూ ఎక్కువైతే సోకింపు ఎక్కువ."},

            'alluvial': {'en': "Ensure good drainage; avoid dense planting which increases humidity.", 'hi': "अच्छी निकासी सुनिश्चित करें; घना रोपण न करें।", 'kn': "ಉತ್ತಮ ಒಳಚರಂಡಿ ಸಿಗಲಿ; ದಟ್ಟ ಸಂಯೋಜನೆ ತಪ್ಪಿಸಿ.", 'te': "మంచి డ్రైనేజ్ కలిగి ఉండండి; మ densely విత్తించడం చేయవద్దు."},

            'general': {'en': "Crop rotation away from host crops and residue management reduces disease.", 'hi': "फसल चक्र और अवशेष प्रबंधन रोग को कम करता है।", 'kn': "ಕ್ರಾಪ್ ರೊಟೇಷನ್ ಮತ್ತು ಅವಶೇಷ ನಿರ್ವಹಣೆ ರೋಗ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.", 'te': "ఫలితంగా మార్పులు మరియు రెసిడ్యూ నిర్వహణ అవసరం."}

        },

        'seasons': {

            'monsoon': {'en': "Rainy periods increase spread—apply protectants during prolonged wetness.", 'hi': "बारिश फैलाव बढ़ाती है—लंबे समय तक गीले होने पर प्रोटेक्टेंट।", 'kn': "ಮಳೆಯ ಸಮಯದಲ್ಲಿ ಸ್ಪ್ರೆ ಮಾಡಿ.", 'te': "వర్షకాలంలో రక్షకాలు వాడండి."},

            'summer': {'en': "Warm dry spells may reduce severity but monitor irrigation events.", 'hi': "गर्म सूखे समय में कम गंभीरता हो सकती है—सिंचाई पर निगरानी रखें।", 'kn': "ಬೆಚ್ಚಗಿನ ಒಣಾವಧಿಯಲ್ಲಿ ತೀವ್ರತೆ ಕಡಿಮೆಯಾಗಬಹುದು.", 'te': "వేడిగా పొడిగా ఉంటే తక్కువగా ఉంటుంది."},

            'winter': {'en': "Low activity—manage residues before next season.", 'hi': "कम गतिविधि—अगले सीजन से पहले अवशेष साफ करें।", 'kn': "ಕಡಿಮೆ ಚಟುವಟಿಕೆ—ಮುನ್ನೂ ಅವಶೇಷ ಸರಿಪಡಿಸಿ.", 'te': "తక్కువ చర్య—రెసిడ్యూ నిర్వహించండి."},

            'general': {'en': "Monitor lower canopy where humidity is higher.", 'hi': "जहां नमी अधिक हो वहाँ निचले हिस्से की निगरानी करें।", 'kn': "ಕೆಳಗಿನ ಕ್ಯಾನೋಪಿ ಗಮನಿಸಿ.", 'te': "కనిష్ట క్యానోపీని పరిశీలించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Residue management, crop rotation, avoid dense stands, improve drainage.", 'hi': "अवशेष प्रबंधन, फसल घुमाव, घना रोपण न करें।", 'kn': "ಅವಶೇಷ ನಿರ್ವಹಣೆ, ರೊಟೇಷನ್ ಮಾಡಿ.", 'te': "రెసిడ్యూ నిర్వహణ చేయండి."},

            'organic': {'en': "Use Trichoderma/compost teas on residue where available; improve soil health", 'hi': "त्रायकೋಡರ್ಮा/कम्पोस्ट चाय का उपयोग करें; मिट्टी स्वास्थ्य सुधारें।", 'kn': "ಟ್ರಿಕೋಡರ್ಮಾ ಅಥವಾ ಕಾಂಪೋಸ್ಟ್ ಬಳಸಿ.", 'te': "ట్రికోడర్మా మరియు కంపోస్ట్ వాడండి."},

            'chemical': {'en': "Fungicides labelled for Cercospora (strobilurins, triazoles) as per label; rotate MoAs; apply at disease onset.", 'hi': "लेबल अनुसार स्टोबिलुरिन/ट्रायाजोल्स; मोड बदलें।", 'kn': "ಲೇಬಲ್ ಪ್ರಕಾರ ಸ್ಟ್ರೋಬಿಲುರಿನ್/ಟ್ರೈಅಜೋಲ್ ಬಳಸಿ.", 'te': "లేబుల్ ప్రకారం స్ట్రోబిలురిన్లు లేదా ట్రయజోలు వాడండి."}

        }

    },



    'Corn_(maize)___Common_rust': {

        'soils': {

            'red': {'en': "Favors humid conditions—monitor and select resistant hybrids when available.", 'hi': "नम परिस्थितियां पसंद; प्रतिरोधी हाइब्रिड चुनें।", 'kn': "ತೇವವಿರುವಲ್ಲಿ ಹೆಚ್ಚು—ಪ್ರತಿರೋಧಕ ಜಾತಿಗಳು ಆಯ್ಕೆ ಮಾಡಿ.", 'te': "తేమ ఉన్న చోటలు ప్రాధాన్యం—ప్రతిరోధక జాతులు ఎంచుకోండి."},

            'black': {'en': "High humidity zones favor rust—manage plant density.", 'hi': "उच्च आर्द्रता जड़ी को बढ़ावा देती है—घनत्व प्रबंधित करें।", 'kn': "ಹೆಚ್ಚಿನ ತೇವಾಂಶದಲ್ಲಿ ರಸ್ಟ್ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "తేమ ఎక్కువైతే రస్ట్ ఎక్కువ."},

            'alluvial': {'en': "Ensure airflow and avoid overhead irrigation at night.", 'hi': "वायु प्रवाह सुनिश्चित करें; रात में ओवरहेड सिंचाई न करें।", 'kn': "ಗಾಳಿ ಪ್ರವಾಹ ಖಚಿತಪಡಿಸಿ; ರಾತ್ರಿ ಓವರ್‌ಹೆಡ್ ನೀರಾವರಿ ತಪ್ಪಿಸಿ.", 'te': "గాలి ప్రవాహాన్ని నిర్థారించండి; రాత్రి నీరు ఇవ్వకండి."},

            'general': {'en': "Use rust-resistant hybrids and plant spacing to reduce severity.", 'hi': "रस्ट-प्रतिरोधी हाइब्रिड और रोपण स्थान का उपयोग करें।", 'kn': "ರಸ್ಟ್-ಪ್ರತಿರೋಧಕ ಜಾತಿಗಳನ್ನು ಬಳಸಿರಿ.", 'te': "రస్ట్ నిరోధక జాతులను వాడండి."}

        },

        'seasons': {

            'monsoon': {'en': "High risk—monitor and apply protectants if outbreaks begin.", 'hi': "उच्च जोखिम—निगरानी करें और प्रोटेक्टेंट लगाएं।", 'kn': "ತೇವದಲ್ಲಿ ಅಪಾಯ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "తడి కాలంలో జాగ్రత్త."},

            'summer': {'en': "Lower risk but check shaded lower leaves.", 'hi': "जोखिम कम पर छायादार पत्तियों की जाँच करें।", 'kn': "ಕಡಿಮೆ ಅಪಾಯ — ಕೆಳಗಿನ ಎಲೆಗಳನ್ನು ಗಮನಿಸಿ.", 'te': "తక్కువ ప్రమాదం—ఈ తరహాలో చూడండి."},

            'winter': {'en': "Low activity—clean residues.", 'hi': "कम गतिविधि—अवशेष साफ करें।", 'kn': "ಕಡಿಮೆ ಚಟುವಟಿಕೆ — ಅವಶೇಷ ತೆರವುಗೊಳಿಸಿ.", 'te': "తక్కువ క్రియాశీలత—రెసిడ్యూ తీసివేయండి."},

            'general': {'en': "Monitor and favor resistant varieties.", 'hi': "निगरानी और प्रतिरोधी किस्मों का प्रयोग।", 'kn': "ನಿಗದಿತ ನೋಟೊ ಮಾಡಿ.", 'te': "మారక varieties ని ఎంచుకోండి."}

        },

        'action_plan': {

            'cultural': {'en': "Use resistant hybrids, adjust planting date/spacing, remove volunteer maize.", 'hi': "प्रतिरोधी हाइब्रिड, रोपण तिथि/घनत्व समायोजित करें।", 'kn': "ಪ್ರತಿರೋಧಕ ಜಾತಿಗಳನ್ನು ಬಳಸಿ.", 'te': "రెసిస్టెంట్ హైబ్రిడ్లు వాడండి."},

            'organic': {'en': "Increase air flow and use biological seed treatments where available.", 'hi': "वायु प्रवाह बढ़ाएं; बायोलॉजिकल बीज उपचार उपयोग करें।", 'kn': "ಗಾಳಿ ಹರಿವು ಹೆಚ್ಚಿಸಿ; ಬಯೋಬೀಜ್ ಚಿಕಿತ್ಸೆ ಬಳಸಿ.", 'te': "గాలి ప్రవాహాన్ని పెంచండి; బియ్యానికి బయో ట్రీట్ చేయండి."},

            'chemical': {'en': "Apply fungicides labelled for rust (triazoles, strobilurins) at early pustule stage; follow label.", 'hi': "प्रारम्भिक अवस्था में लेबल वाले फंगिसाइड लगाएं।", 'kn': "ಆರಂಭಿಕದಲ್ಲಿ ಫಂಗಿಸೈಡ್ ಬಳಸಿ.", 'te': "చెప్పిన ప్రకారమే ఫంగిసైడ్స్ వాడండి."}

        }

    },



    'Corn_(maize)___Northern_Leaf_Blight': {

        'soils': {

            'red': {'en': "Favors long wet periods—improve drainage and avoid excessive irrigation.", 'hi': "लंबे गीले समय में बढ़ता है—ड्रेन करें।", 'kn': "ತಂಪಾದ ತೇವಾವಧಿಯಲ್ಲಿ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "తడి ఎక్కువగా ఉన్నప్పుడే ఉంటుంది."},

            'black': {'en': "Residues help carry inoculum—manage crop residue.", 'hi': "अवशेष संक्रमण बढ़ाते हैं—प्रबंध करें।", 'kn': "ಅವಶೇಷ ನಿರ್ವಹಣೆ ಮಾಡಿರಿ.", 'te': "రెసిడ్యూ నిర్వహించండి."},

            'alluvial': {'en': "Use resistant hybrids and manage irrigation.", 'hi': "प्रतिरोधी हाइब्रिड और सिंचाई प्रबंधित करें।", 'kn': "ಪ್ರತಿರೋಧಕ ಜಾತಿಗಳನ್ನು ಬಳಸಿ.", 'te': "రెసిస్టెంట్ జాయింట్లు ఎంచుకోండి."},

            'general': {'en': "Crop rotation and residue management reduce disease pressure.", 'hi': "फसल चक्र और अवशेष प्रबंधन से दबाव कम होता है।", 'kn': "ಕ್ರಾಪ್ ರೊಟೇಷನ್ ಉಪಯುಕ್ತ.", 'te': "ఫలితం మార్చండి."}

        },

        'seasons': {

            'monsoon': {'en': "High risk during rainy periods—protect young plants.", 'hi': "बारिश में अधिक जोखिम—युवा पौधों को सुरक्षा दें।", 'kn': "ಮಳೆಯ ಸಮಯದಲ್ಲಿ ಅಪಾಯ ಹೆಚ್ಚಾಗಬಹುದು.", 'te': "వానకాలంలో జాగ్రత్త."},

            'summer': {'en': "Warm conditions may increase spread—monitor fields.", 'hi': "गर्म परिस्थितियों में फैलाव बढ़ सकता है—निगरानी करें।", 'kn': "ಬೆಚ್ಚಗಿನ ಅವಧಿಯಲ್ಲಿ ಗಮನಿಸಿ.", 'te': "వేడి సమయంలో గమనించండి."},

            'winter': {'en': "Low activity—plan residue clearance.", 'hi': "कम गतिविधि—अवशेष साफ करें।", 'kn': "ಕಡಿಮೆ ಚಟುವಟಿಕೆ — ಅವಶೇಷ ಗುರ್ತಿಸಿ.", 'te': "తక్కువ కార్యాచరణ—రెసిడ్యూ తీసివేయండి."},

            'general': {'en': "Inspect lower canopy and older leaves first.", 'hi': "पहले निचली पत्तियों की जाँच करें।", 'kn': "ಕೆಳಗಿರುವ ಎಲೆಗಳನ್ನು ಮೊದಲು ಪರೀಕ್ಷಿಸಿ.", 'te': "కనిష్ట ఆకులను ముందుగా తనిఖీ చేయండి."}

        },

        'action_plan': {

            'cultural': {'en': "Deep ploughing to bury residue, rotate crops away from maize, reduce irrigation at night.", 'hi': "अवशेष दबाने के लिए गहरी जुताई, फसल चक्र बदलें।", 'kn': "ಅವಶೇಷ ಮರುವಳಿಗೆ ನುಗ್ಗಿಸುವ ಕೆಲಸ ಮಾಡಿರಿ.", 'te': "రెసిడ్యూ దాగండి."},

            'organic': {'en': "Promote soil health; Trichoderma-based treatments on residue if available.", 'hi': "मिट्टी स्वास्थ्य बढ़ाएं; ट्रिकोडर्मा उपयोग।", 'kn': "ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಹೆಚ್ಚಿಸಿ.", 'te': "మట్టి ఆరోగ్యం పెంచండి."},

            'chemical': {'en': "Use fungicides approved for NLB (QoI, DMI) as per label and rotate to prevent resistance.", 'hi': "NLB के लिए अनुमोदित फंगिसाइड का उपयोग करें; मोड रोटेट करें।", 'kn': "ನೇorthern leaf blight ಗೆ ಲೇಬಲ್ ಪ್ರಕಾರ ಫಂಗಿಸೈಡ್ ಬಳಸಿ.", 'te': "లేబుల్ ప్రకారం ఫంగిసైడ్స్ వాడండి."}

        }

    },



    'Corn_(maize)___healthy': {

        'soils': {

            'red': {'en': "Maintain fertility and drainage.", 'hi': "उर्वरता और निकासी बनाए रखें।", 'kn': "ಪೋಷಣೆ ಮತ್ತು ಒಳಚರಂಡಿ ಕಾಪಾಡಿ.", 'te': "పోషకాల్నీ నిర్వహించండి."},

            'black': {'en': "Avoid waterlogging and salinity issues.", 'hi': "जलभराव और लवणता की जाँच करें।", 'kn': "ಒಣಗಿಡದ ಸಮಸ್ಯೆ ತಡೆಯಿರಿ.", 'te': "నీటి నిల్వ నివారించండి."},

            'alluvial': {'en': "Balanced fertilization and irrigation scheduling.", 'hi': "संतुलित उर्वरक और सिंचाई।", 'kn': "ಸಮತೋಲಿತ ಗೊಬ್ಬರ ಮತ್ತು ನೀರು.", 'te': "సమతుల్య ఎరువులు మరియు నీరు."},

            'general': {'en': "IPM: monitoring, resistant hybrids, calibrated spray equipment.", 'hi': "IPM: निगरानी, प्रतिरोधी हाइब्रिड, कैलिब्रेटेड स्प्रे।", 'kn': "IPM: ನಿಗಾ, ಪ್ರತಿರೋಧಕ ಜಾತಿ, ಸ್ಪ್ರೆ ಕಲೆ.", 'te': "IPM పాటించండి."}

        },

        'seasons': {

            'monsoon': {'en': "Increase surveillance for foliar diseases.", 'hi': "पर्ण रोगों की निगरानी बढ़ाएं।", 'kn': "ಲಿಷ್ಠ ರೋಗಗಳ ಮೇಲೆ ಕಣ್ಣಿಟ್ಟಿ.", 'te': "ఆకుల వ్యాధులపై పర్యవేక్షణ పెంచండి."},

            'summer': {'en': "Manage irrigation to avoid stress.", 'hi': "सिंचाई से तनाव न होने दें।", 'kn': "ನೀರು ನೀಡುವ ನಿಯಂತ್ರಣ ಇರಲಿ.", 'te': "నీటి ఒత్తిడిని తగ్గించండి."},

            'winter': {'en': "Clean residues and plan rotations.", 'hi': "अवशेष साफ करें और रोटेशन योजना बनाएं।", 'kn': "ಅವಶೇಷ ತೊළಗಿಸು.", 'te': "రొటేషన్ ప్లాన్ చేయండి."},

            'general': {'en': "Maintain balanced nutrition and pest scouting.", 'hi': "संतुलित पोषण और कीट जाँच।", 'kn': "ಸಮತೋಲಿತ ಜವಳಿ.", 'te': "పోషకాలు సరిచూడండి."}

        },

        'action_plan': {

            'cultural': {'en': "Good agronomy, rotation and residue management.", 'hi': "अच्छा कृषि अभ्यास, फसल चक्र और अवशेष प्रबंधन।", 'kn': "ಒಳ್ಳೆಯ ಕೃಷಿ ಕ್ರಮಗಳು.", 'te': "ముందస్తు నిర్వహణ."},

            'organic': {'en': "Use organic matter to improve soil structure.", 'hi': "जैविक पदार्थ से मिट्टी संरचना सुधारें।", 'kn': "ಆರ್ಗ್ಯಾನಿಕ್ ವಿಷಯ ಬಳಸಿ.", 'te': "సేంద్రీయ పదార్థం వాడండి."},

            'chemical': {'en': "Apply inputs only as needed per scouting and label.", 'hi': "निगरानी अनुसार ही रसायन इस्तेमाल करें।", 'kn': "ತಪಾಸಣೆ ಇದ್ದರೆ ಮಾತ್ರ ರಾಸಾಯನಿಕ ಬಳಸಿ.", 'te': "పర్యవేక్షణ ప్రకారం మాత్రమే రసాయనాలు వాడండి."}

        }

    },



    # -------------------------

    # GRAPE

    # -------------------------

    'Grape___Black_rot': {

        'soils': {

            'red': {'en': "Warm humid pockets increase risk—ensure good airflow and avoid overhead irrigation.", 'hi': "गर्म नम स्थान जोखिम बढ़ाते—अच्छी हवा और ओवरहेड सिंचाई से बचें।", 'kn': "ಬಿಸಿಲು ಮತ್ತು ತೇವ ಹೊಂದಿದ ಸ್ಥಳಗಳಲ್ಲಿನ ಅಪಾಯ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "తడి, వేడి ప్రాంతాల్లో ఎక్కువగా ఉంటుంది."},

            'black': {'en': "Canopy exfoliation and pruning reduce humidity; remove infected clusters.", 'hi': "छंटाई व संक्रमित गुच्छे हटाएं।", 'kn': "ಕ್ಯಾನೊಪಿ ತೆಳಗೆ ಮಾಡಿ ಮತ್ತು ಸೋಂಕಿತ ಗುಚ್ಛಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.", 'te': "క్యానోపీని తగ్గించండి; సంక్రమిత క్లస్టర్లు తొలగించండి."},

            'alluvial': {'en': "Ensure drainage and avoid water splashing clusters.", 'hi': "नाली बनाए रखें और फलों पर पानी न सोखे।", 'kn': "ನೆರೆಯನ್ನು తగ్గಿಸಿ ಮತ್ತು ಕ್ಲಸ್ಟರ್ ಮೇಲೆ ನೀರು ತಿರುಗದಂತೆ ನೋಡಿಕೊಳ್ಳಿ.", 'te': "డ్రైన్ ఏర్పాటు చేయండి; క్లస్టర్లపై నీరు తాకకుండా చూడండి."},

            'general': {'en': "Sanitation: remove mummified berries and infected canes.", 'hi': "सफाई: मम्मी बेरी और संक्रमित डंठल हटाएं।", 'kn': "ಸ್ವಚ್ಛತೆ: ಸಾಂಕ್ರಾಮಿಕ ಬೆರಿಗಳು ಮತ್ತು ಕ್ಯಾಂಸ್ ತೆಗೆದುಹಾಕಿ.", 'te': "శుభ్రత: సంక్రమిత బెరీస్ తొలగించండి."}

        },

        'seasons': {

            'monsoon': {'en': "High risk—apply protectants at bunch closure and pre-rain spray every 7–14 days.", 'hi': "उच्च जोखिम—बंच क्लोजर पर और बारिश से पहले 7–14 दिनों में स्प्रे।", 'kn': "ಮಳೆಗಿಂತ ಮುನ್ನ ಪ್ರತಿ 7-14 ದಿನಕ್ಕೆ ಸ್ಪ್ರೇ ಮಾಡಿ.", 'te': "వర్షానికి ముందు 7-14 రోజులకు ఒకసారి స్ప్రే చేయండి."},

            'summer': {'en': "Monitor clusters in shaded zones.", 'hi': "छायादार क्षेत्रों में गुच्छों की निगरानी करें।", 'kn': "ಛಾಯಾದ ಭಾಗಗಳಲ್ಲಿನ ಗುಚ್ಛಗಳನ್ನು ಗಮನಿಸಿ.", 'te': "చాయల్లో ఉన్న క్లస్టర్లను పర్యవేక్షించండి."},

            'winter': {'en': "Prune and remove overwintering inoculum.", 'hi': "छंटाई और संक्रमण स्रोत हटाएं।", 'kn': "ಓವರ್‌윈್ಟರ್ ಮಾಡುವ ಸೂತ್ರಗಳನ್ನು ತೆಗೆಯಿರಿ.", 'te': "సంక్రమిత మూలాలను తొలగించండి."},

            'general': {'en': "Protectant sprays during wet spells; canopy management essential.", 'hi': "गीले समय में प्रोटेक्टेंट स्प्रे; कैनोपी प्रबंधन आवश्यक।", 'kn': "ತೇವಾವಧಿಯಲ್ಲಿ ರಕ್ಷಕ ಸ್ಪ್ರೇಗಳು ಮಾಡಿ.", 'te': "తడి సమయంలో రక్షక స్ప్రేలు చేయండి."}

        },

        'action_plan': {

            'cultural': {'en': "Sanitation, canopy opening, remove infected clusters, avoid fruit contact with ground.", 'hi': "सफाई, कैनोपी खोलना, संक्रमित गुच्छे हटाना।", 'kn': "ಸ್ವಚ್ಛತೆ ಮತ್ತು ಕ್ಯಾನೊಪಿ ತೆಗೆಯಿರಿ.", 'te': "శుభ్రత మరియు క్యానోపీ ని తెరవండి."},

            'organic': {'en': "Use copper or sulphur-based protectants; biologicals may reduce inoculum.", 'hi': "कॉपर/सल्फर प्रोटेक्टेंट; बायोप्रोडक्ट।", 'kn': "ಕಾಪರ್ ಅಥವಾ ಸಲ್ಫರ್ ಉಪಯೋಗಿಸಿ.", 'te': "కాపర్ లేదా సల్ఫర్ బేస్డ్ స్ప్రేలు వాడండి."},

            'chemical': {'en': "Use protectants (mancozeb, chlorothalonil) at bunch closure and systemic fungicides for severe outbreaks—follow label & rotate MoAs.", 'hi': "बंच क्लोजर पर प्रोटेक्टेंट और गंभीर स्थिति में सिस्टमिक फंगिसाइड—लेबल पढ़ें।", 'kn': "ಬಂಚ್ ಕ್ಲೋಜರ್‌ನಲ್ಲಿ ರಕ್ಷಕಗಳನ್ನು ಬಳಸಿ.", 'te': "బంచ్ క్లోజర్ వద్ద రక్షక స్ప్రేలు చేయండి."}

        }

    },



    'Grape___Esca_(Black_Measles)': {

        'soils': {

            'red': {'en': "Wood-inhabiting pathogens—avoid injuries to trunk; improve drainage.", 'hi': "लकड़ी पर रहने वाले रोग—तने को चोट से बचाएं; जल निकासी सुधारें।", 'kn': "ಗೊಂಬೆ ಆಗುವ ಹಾನಿ — ಮರದ ತಾಣವನ್ನು ಕಾಪಾಡಿ.", 'te': "మరపు సంబంధ వ్యాధులు—దిగినప్పుడే సంరక్షించండి."},

            'black': {'en': "Reduce vine stress; maintain balanced nutrition.", 'hi': "लताओं पर तनाव घटाएं; संतुलित पोषण रखें।", 'kn': "ಬೆಂಕಿ ತಾಪಮಾನ ಕಡಿಮೆ ಮಾಡಿ.", 'te': "వైన్ ఒత్తిడి తగ్గించండి."},

            'alluvial': {'en': "Avoid waterlogging stress; manage vine vigor.", 'hi': "जलभराव से बचें; लता की तीव्रता प्रबंधित करें।", 'kn': "ನೀರಿನ ತಣ್ಣನೆಯವಸ್ತು ತಪ್ಪಿಸಿ.", 'te': "నీటి నిల్వ నివారించండి."},

            'general': {'en': "Esca is complex—avoid trunk wounds, maintain sanitation and remove severely affected vines.", 'hi': "एस्का जटिल है—तने की चोट से बचें; संक्रमित लताओं को हटाएं।", 'kn': "Esca ಸಂಕೀರ್ಣ—ಸಂಕ್ರಾಮಕ ಗಳನ್ನು ತೆಗೆಯಿರಿ.", 'te': "ఎస్కా సంక్లిష్టం—చిరునది జాగ్రత్తగా ఉంచండి."}

        },

        'seasons': {

            'monsoon': {'en': "Stress and wood decay can progress—prune and remove symptomatic wood.", 'hi': "तनाव व लकड़ी सड़ना बढ़ सकता—संकेतित लकड़ी हटाएं।", 'kn': "ತೇವದಲ್ಲಿ ಗಡಿಬಿಡಿ ಹೆಚ್ಚಾಗಬಹುದು.", 'te': "తడి సమయంలో లక్షణాలున్న భాగాలను తొలగించండి."},

            'summer': {'en': "Monitor vine vigor and berry quality.", 'hi': "लता की शक्ति व फल की गुणवत्ता देखें।", 'kn': "ವೈನ್ ಶಕ್ತಿ ಮತ್ತು ಗುಣಮಟ್ಟ ನೋಡಿ.", 'te': "వైన్ శక్తి పర్యవేక్షించండి."},

            'winter': {'en': "Prune out dead wood and burn if regulation allows.", 'hi': "मृत लकड़ी हटाएँ और जलाएँ (नियम अनुमति दें)।", 'kn': "ಚಡ್ಡಿ ಮರವನ್ನು ತೆಗೆದುಹಾಕಿ.", 'te': "సంక్రమిత కలకాలం తీసివేయండి."},

            'general': {'en': "Maintain vine health, consider rootstock selection and sanitation.", 'hi': "लताओं का स्वास्थ्य बनाए रखें; उपयुक्त जड़ चयन पर विचार करें।", 'kn': "ವೈನ್ ಆರೋಗ್ಯ ಕಾಪಾಡಿ.", 'te': "వైన్ ఆరోగ్యం పర్యవేక్షించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Prune dead wood, manage vigor (balanced N), avoid trunk wounds.", 'hi': "मृत लकड़ी छंटाई, संतुलित N, तने की चोट से बचें।", 'kn': "ಮೃತ ಮರವನ್ನು ಕತ್ತರಿಸಿ.", 'te': "డెడ్ వుడ్ తొలగించండి."},

            'organic': {'en': "Improve soil drainage and organic matter; biological wound treatments where available.", 'hi': "मिट्टी की निकासी व जैविक पदार्थ बढ़ाएं; घाव उपचार।", 'kn': "ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಹೆಚ್ಚಿಸಿ.", 'te': "మట్టిని ఆరోగ్యంగా ఉంచండి."},

            'chemical': {'en': "No reliable curative chemical—preventive sanitation & management are primary. Follow local extension guidance for trunk treatments.", 'hi': "कोई विश्वसनीय रासायनिक उपचार नहीं—प्रमुख रोकथाम स्वच्छता व प्रबंधन।", 'kn': "ರಾಸಾಯನಿಕಕ್ಕೆ ನಿರ್ಧಿಷ್ಟ ಪರಿಹಾರ ಇಲ್ಲ.", 'te': "రసాయనిక మందులు సాధారణంగా పనికిరావు."}

        }

    },



    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {

        'soils': {

            'red': {'en': "Warm wet microclimates increase severity—open canopy and remove infected leaves.", 'hi': "गर्म, नम क्षेत्र गंभीरता बढ़ाते—कैनोपी खोलें।", 'kn': "ಬಿಸಿಲು ಮತ್ತು ತೇವ ಅವಧಿಯಲ್ಲಿ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "వేడిగా తడి ఉన్నప్పుడు ఎక్కువగా ఉంటుంది."},

            'black': {'en': "Reduce humidity in canopy and remove fallen debris.", 'hi': "कैनोपी में नमी घटाएँ और गिरे हुए तत्व हटाएँ।", 'kn': "ಕ್ಯಾನೋಪಿ ತೇವಾಂಶ ಬದಲಾಗಿಸಿರಿ.", 'te': "క్యానోపీ తేమ తగ్గించండి."},

            'alluvial': {'en': "Watch for splashed inoculum—avoid wetting clusters.", 'hi': "छिड़काव से फैलता है—फलों को गीला न करें।", 'kn': "ಸ್ಪ್ಲ್ಯಾಶ್ ಆದ ಸೋಂಕುಗಳು ಇರುವುದನ್ನು ನೋಡಿರಿ.", 'te': "పూత ద్వారా వ్యాప్తి ఉంటుంది—ఫలాలపై నీరు పడనివ్వండి."},

            'general': {'en': "Sanitation and canopy management reduce disease load.", 'hi': "स्वच्छता व कैनोपी प्रबंधन रोग घटाते।", 'kn': "ಸ್ವಚ್ಛತೆ ಮತ್ತು ಕ್ಯಾನೋಪಿ ನಿರ್ವಹಣೆ ಮುಖ್ಯ.", 'te': "శుభ్రత మరియు క్యానోపీ నిర్వహణ."}

        },

        'seasons': {

            'monsoon': {'en': "High risk—protectants and good canopy sprays at 7–14 day intervals.", 'hi': "उच्च जोखिम—प्रोटेक्टेंट हर 7–14 दिन पर।", 'kn': "ತೇವದಲ್ಲಿ 7–14 ದಿನಕ್ಕೆ ಸ್ಪ್ರೇ ಮಾಡಿ.", 'te': "తడి సమయంలో 7–14 రోజులకోసారి స్ప్రే చేయండి."},

            'summer': {'en': "Monitor shaded rows.", 'hi': "छायादार पंक्तियों पर निगरानी।", 'kn': "ಛಾಯಾದ ಸಾಲಿಗೆ ಗಮನಿಸಿ.", 'te': "చాయగా ఉన్న వరుసలను గమనించండి."},

            'winter': {'en': "Reduce inoculum by leaf removal during pruning.", 'hi': "छंटाई में पत्तियाँ हटाकर संक्रमण कम करें।", 'kn': "ಕತ್ತರಿಸುವಾಗ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.", 'te': "కత్తిరించేటప్పుడు ఆకులు తీసివేయండి."},

            'general': {'en': "Spray coverage must reach undersides of leaves and inner canopy.", 'hi': "स्प्रे पत्ती के नीचे और अंदरूनी कैनोपी तक पहुँचना चाहिए।", 'kn': "ಸ್ಪ್ರೇ ಆಮ್ಲವೊಂದಕ್ಕೂ ತಲುಪಬೇಕು.", 'te': "స్ప్రే ఆకుల కిందికి కూడా చేరాలి."}

        },

        'action_plan': {

            'cultural': {'en': "Prune to improve airflow, remove infected leaves & debris, avoid overhead irrigation.", 'hi': "हवा के लिए छंटाई, संक्रमित पत्तियां हटाएं।", 'kn': "ಗಾಳಿ ಪ್ರವೇಶವಾಗುವಂತೆ ಕತ್ತರಿಸಿ.", 'te': "గాలి పనితీరును మెరుగుపరచండి."},

            'organic': {'en': "Copper protectants, neem-based sprays may reduce severity.", 'hi': "कापर, नीम-आधारित स्प्रे मदद कर सकते हैं।", 'kn': "ಕಾಪರ್ ಅಥವಾ ನೀಮ್ ಸ್ಪ್ರೇ ಬಳಸಿ.", 'te': "కాపర్ లేదా నిర్ణయ బేస్డ్ స్ప్రేలు వాడండి."},

            'chemical': {'en': "Use protectant fungicides (mancozeb/chlorothalonil) and systemic fungicides if severe—rotate MoAs; follow label.", 'hi': "प्रोटेक्टेंट और सिस्टमिक फंगिसाइड का उपयोग—लेबल पढ़ें।", 'kn': "ರಕ್ಷಕ ಮತ್ತು ಸಿಸ್ಟಮಿಕ್ ಫಂಗಿಸೈಡ್ ಬಳಸಿ.", 'te': "రక్షక మరియు సిస్టమిక్ ఫంగిసైడ్స్ వాడండి."}

        }

    },



    'Grape___healthy': {

        'soils': {

            'red': {'en': "Balance fertility and maintain drainage; mulching helps soil moisture.", 'hi': "उर्वरता संतुलित रखें; ड्रेन करें।", 'kn': "ಪೋಷಣೆ ಸಮತೋಲನೆ ಮಾಡಿ.", 'te': "పోషకాలు సమతుల్యం చేయండి."},

            'black': {'en': "Avoid waterlogging; manage vine vigor.", 'hi': "जलभराव से बचें; लता की वृद्धि नियंत्रित करें।", 'kn': "ನೀರು ನಿರ್ವಹಣೆ ಮಾಡಿ.", 'te': "నీటి నిల్వ నివారించండి."},

            'alluvial': {'en': "Ensure good drainage and organic matter.", 'hi': "अच्छी निकासी और कार्बनिक पदार्थ।", 'kn': "ಉತ್ತಮ ಒಳಚರಂಡಿ ಮತ್ತು ಆರ್ಗ್ಯಾನಿಕ್ ವಸ್ತು.", 'te': "మంచి డ్రైనేజ్ మరియు ఆర్గానిక్ మెటర్."},

            'general': {'en': "Routine canopy management, pest monitoring and nutrition balance.", 'hi': "नियमित कैनोपी प्रबंधन और पोषण संतुलन।", 'kn': "ನಿಯಮಿತ ಕ್ಯಾನೋಪಿ ನಿರ್ವಹಣೆ.", 'te': "నియమిత క్యానోపీ నిర్వహణ."}

        },

        'seasons': {

            'monsoon': {'en': "Increase surveillance for foliar diseases.", 'hi': "पर्ण रोगों की निगरानी बढ़ाएं।", 'kn': "ತೇವಾವಧಿಯಲ್ಲಿ ಗಮನವಿಡಿ.", 'te': "పర్ణ వ్యాధులపై పర్యవేక్షణ పెంచండి."},

            'summer': {'en': "Manage irrigation and heat stress.", 'hi': "सिंचाई और गर्मी का प्रबंधन करें।", 'kn': "ನೀరు ಮತ್ತು ತಾಪಮಾನ ನಿರ್ವಹಣೆ.", 'te': "నీటి నిర్వహణ మరియు ఎండ నుంచి రక్షణ."},

            'winter': {'en': "Dormant pruning & sanitation.", 'hi': "निष्क्रिय छंटाई और सफाई।", 'kn': "ಡಾರ್ಮೆಂಟ್ ಕತ್ತರಿಸಿ.", 'te': "డార్మంట్ కత్తరించండి."},

            'general': {'en': "Follow IPM: resistant rootstocks, calibrated sprays, sanitation.", 'hi': "IPM अपनाएं: प्रतिरोधी रूटस्टॉक और स्वच्छता।", 'kn': "IPM ಅನುಸರಿಸಿ.", 'te': "IPM పాటించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Prune for airflow, manage vigor, remove diseased parts.", 'hi': "हवा के लिए छंटाई करें, वृद्धि नियंत्रित करें।", 'kn': "ಗಾಳಿಗೆ ಕತ್ತರಿಸಿ.", 'te': "గాలి ప్రవాహం కోసం కత్తిరించండి."},

            'organic': {'en': "Use compost, organic mulches and biocontrols where available.", 'hi': "कम्पोस्ट और जैविक मल्च का उपयोग।", 'kn': "ಕಂಪೋಸ್ಟ್ ಮತ್ತು ಆರ್ಗ್ಯಾನಿಕ್ ಮಲ್ಚ್ ಬಳಸಿ.", 'te': "కంపోస్ట్ మరియు సేంద్రీయ మల్చ్ వాడండి."},

            'chemical': {'en': "No treatment if healthy; follow preventive sprays only when advised.", 'hi': "यदि स्वस्थ है तो उपचार आवश्यक नहीं; केवल सलाह पर स्प्रे।", 'kn': "ಆರೋಗ್ಯವಾಗಿದ್ದರೆ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.", 'te': "ఆరోగ్యంగా ఉంటే ట్రీట్不要."}

        }

    },



# -------------------------
    # ORANGE
    # -------------------------
    'Orange___Haunglongbing_(Citrus_greening)': {
        'soils': {
            'red': {'en': "Soil type less critical—focus on tree vigor and psyllid control; improve drainage in waterlogged red soils.", 'hi': "मिट्टी का प्रकार कम महत्वपूर्ण—पेड़ की शक्ति और साइलिड नियंत्रण पर ध्यान दें।", 'kn': "ಮಣ್ಣು ಪ್ರಕಾರ ಕಡಿಮೆ — ಮರದ ಶಕ್ತಿ ಮತ್ತು ಸೈಲಿಡ್ ನಿರ್ವಹಣೆ ಮುಖ್ಯ.", 'te': " నేల తక్కువ ప్రాధాన్యం—ట్రీ ఆరోగ్యం మరియు సైల్లిడ్ నియంత్రణ ముఖ్యం."},
            'black': {'en': "Avoid waterlogging; maintain root health and nutrition.", 'hi': "जलभराव से बचें; जड़ स्वास्थ्य बनाये रखें।", 'kn': "ನೀರು ನಿಲ್ಲದಂತಿರುವುದನ್ನು ತಪ್ಪಿಸಿ.", 'te': "నీటి నిల్వ నివారించండి; వేరుసదుపాయాలు ఉంచండి."},
            'alluvial': {'en': "Ensure balanced nutrition and control psyllid vectors.", 'hi': "संतुलित पोषण और साइलिड नियंत्रण सुनिश्चित करें।", 'kn': "ಸಂತುಲನ ಪೋಷಣೆಯೊಂದಿಗೆ ಸೈಲಿಡ್ ನಿಯಂತ್ರಣ.", 'te': "సమతుల్య పోషణ మరియు సైల్లిడ్ నియంత్రణ."},
            'general': {'en': "HLB is systemic and often incurable; emphasis on vector control (Asian citrus psyllid), rogueing infected trees and strict sanitation; replant with disease-free stock.", 'hi': "HLB प्रणालीगत और अक्सर अयोग्य; साइलिड नियंत्रण, संक्रमित पेड़ों को हटाना और सफाई प्राथमिकता।", 'kn': "HLB ಸಿಸ್ಟಮಿಕ್ ಮತ್ತು ಸುಧಾರಣೆ ಕಡಿಮೆ—ವ್ಯಕ್ತಿಗತ ನಿಯಂತ್ರಣ ಮುಖ್ಯ.", 'te': "HLB ఒక వ్యవస్థాగత వ్యాధి; వ్యాక్టర్ నియంత్రణ మరియు సంక్రమిత చెట్లను తీసివేయడం ముఖ్యం."}
        },
        'seasons': {
            'monsoon': {'en': "Psyllid populations may increase after rains—monitor and control vectors aggressively.", 'hi': "बारिश के बाद साइलिड बढ़ सकते हैं—तीव्र नियंत्रण।", 'kn': "ಮಳೆಯ ನಂತರ ಸೈಲ್ಲಿಡ್ ಹೆಚ್ಚಬಹುದು.", 'te': "వర్షాల తర్వాత సైల్లిడ్ పెరుగుతాయి—నియంత్రణ చేయండి."},
            'summer': {'en': "Active vector periods—apply integrated vector management.", 'hi': "सक्रिय साइलिड अवधि—इंटीग्रेटेड कंट्रोल।", 'kn': "ಸಕ್ರಿಯ ಕಾಲದಲ್ಲಿ ನಿಯಂತ್ರಣ ಮಾಡಿ.", 'te': "వేడితో కూడిన కాలాల్లో ఇన్‌టిగ్రేటెడ్ పద్ధతులు అమలు చేయండి."},
            'winter': {'en': "Lower vector activity in cold months—prune and remove infected wood.", 'hi': "ठंड में कम गतिविधि—संक्रमित लकड़ी हटाएं।", 'kn': "ಚಳಿಯಲ್ಲಿ ಸಕ್ರಿಯತೆಯು ಕಡಿಮೆ.", 'te': "చలి సమయాల్లో వ్యాధి ప్రభావం తక్కువగా ఉంటుంది."},
            'general': {'en': "Year-round vector scouting & use of disease-free planting material is critical.", 'hi': "साल-दर-साल साइलिड जाँच और रोग-मुक्त पौधा महत्त्वपूर्ण।", 'kn': "ವರ್ಷವರಿ ಸ್ಕೌಟಿಂಗ್ ಮತ್ತು ರೋಗ ರಹಿತ ಕೊಂಡಿಕೆ ಅತ್ಯಾವಶ್ಯಕ.", 'te': "సంవత్సరం పొడవునా స్కౌటింగ్ మరియు వ్యాధి-రహిత విత్తనాలు అవసరం."}
        },
        'action_plan': {
            'cultural': {'en': "Rogue (remove & destroy) HLB-positive trees promptly; sanitize tools; plant certified disease-free nursery stock; maintain tree vigor.", 'hi': "HLB-पॉज़िटिव पेड़ जल्दी हटाएं; उपकरण सेंचित करें; रोग-मुक्त स्टॉक लगाएँ।", 'kn': "HLB-ಸಕಾರಾತ್ಮಕ ಮರಗಳನ್ನು ತಕ್ಷಣ ತೆಗೆದುಹಾಕಿ.", 'te': "HLB సంక్రమిత చెట్లను తొలగించండి; సాధారణ శుభ్రత పాటించండి."},
            'organic': {'en': "Kaolin clay sprays can reduce vector landing; encourage natural enemies (parasitoids), maintain tree vigor with organic manures.", 'hi': "कॉलಿನ್ क्ले स्प्रे साइलिड कम कर सकते हैं; जैविक खाद से पेड़ की शक्ति बढ़ाएँ।", 'kn': "ಕಾಲಿನ್ ಸ್ಫ್ರೇಗಳೇ ಹಾನಿಕರರನ್ನು ಕಡಿಮೆ ಮಾಡಬಹುದು.", 'te': "కాయలిన్ స్ప్రేలు వ్యాక్టర్లను తగ్గిస్తాయి; సహజ శత్రువులను ప్రోత్సహించండి."},
            
            # --- THIS SECTION IS NOW CORRECT ---
            'chemical': {
                'en': ("Vector control: use pyrethroids, neonicotinoids or insect growth regulators (as per local registration) for psyllid control; apply according to scouting thresholds and label. "
                       "Systemic cures for HLB do not exist; trunk injections with antibiotics are controversial/regulated — consult extension & regulations before any such use."),
                'hi': ("साइलिड नियंत्रण: पायरेथ्रोइड्स/नियोनिकोटिनॉयड/इंटेक्ट ग्रोथ रेगुलेटर्स का उपयोग करें; लेबल व नियमों का पालन करें। "
                       "HLB के लिए कोई सिस्टमिक इलाज नहीं है; ट्रंक इंजेक्शन विवादास्पद है — विस्तार सेवा से परामर्श करें।"),
                'kn': "ಸೈಲಿಡ್ ನಿಯಂತ್ರಣಕ್ಕೆ ಪೈರೇತ್ರಾಯ್ಡ್/ನಿಯೋನಿಕೋಟಿನಾಯ್ಡ್/IGRs ಬಳಸಿ; ಲೇಬಲ್ ಪಾಲಿಸಿ. HLBಗೆ ನಿಖರ ಚಿಕಿತ್ಸೆಯಿಲ್ಲ.",
                'te': "సైలిడ్ నియంత్రణకు అనుమతినిచ్చిన ఇన్‌సెక్టిసైడ్‌లు వాడండి; లేబుల్‌ను పాటించండి."
            }
            # --- END OF FIX ---
        }
    },



    # -------------------------

    # PEACH

    # -------------------------

    'Peach___Bacterial_spot': {

        'soils': {

            'red': {'en': "Warm wet conditions in red soils increase bacterial spread—avoid overhead irrigation.", 'hi': "लाल मिट्टी में गीले गर्म हालात बैक्टीरिया फैलाव बढ़ाते—ओवरहेड सिंचाई से बचें।", 'kn': "ತೇವವುಳ್ಳ ಕೆಂಪು ಮಣ್ಣಿನಲ್ಲಿ ಬ್ಯಾಕ್ಟೀರಿಯಾ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "ఎర్ర నేలల్లో తడి, వేడి పరిస్థితులు బ్యాక్టీరియా పెరగడానికి అనుకూలం."},

            'black': {'en': "High moisture retention favors spread; prune and sanitize.", 'hi': "ऊँची नमी फैलाव बढ़ाती; छंटाई व स्वच्छता रखें।", 'kn': "ತೇವಾಂಶ ಬಹಳಿದ್ದರೆ ಕತ್ತರಿಸಿ ಮತ್ತು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", 'te': "తేమ ఎక్కువైతే చెట్లను కత్తిరించండి."},

            'alluvial': {'en': "Avoid wetting foliage; maintain tree vigor.", 'hi': "पत्तियों को गीला न करें; पेड़ की शक्ति बनाए रखें।", 'kn': "ಎಲೆಗಳನ್ನು ತುತ್ತಿದಂತೆ ಮಾಡಬೇಡಿ; ಮರದ ಆರೋಗ್ಯ ಕಾಪಾಡಿ.", 'te': "ఆకులను తడిగా పెట్టవద్దు; ట్రీ శక్తిని కాపాడండి."},

            'general': {'en': "Bacterial pathogens spread in splashing water and tools—sanitation is key.", 'hi': "बैक्टीरिया पानी और उपकरणों से फैलते हैं—स्वच्छता महत्वपूर्ण।", 'kn': "ಬಾಕ್ಟೀರಿಯಾ ತಣ್ಣನೆಯ ನೀರು ಮತ್ತು ಉಪಕರಣಗಳಿಂದ ಹರಡುತ್ತದೆ.", 'te': "బ్యాక్టీరియా నీరు మరియు సాధనాల ద్వారా వ్యాపిస్తాయి."}

        },

        'seasons': {

            'monsoon': {'en': "High spread—minimize leaf wetness and perform copper sprays at early infection.", 'hi': "उच्च फैलाव—पत्ती गीली न होने दें; शुरुआती कंन में कॉपर स्प्रे।", 'kn': "ಮಳೆಯ ಸಮಯದಲ್ಲಿ ಪ್ರತಿ 7-14 ದಿನದಲ್ಲಿ ಕಾಪರ್ ಸ್ಪ್ರೇ ಮಾಡಿ.", 'te': "తడి సమయంలో కాపర్ స్ప్రే చేయండి."},

            'summer': {'en': "Lower risk if dry—avoid overhead irrigation.", 'hi': "सूखा होने पर जोखिम कम—ओवरहेड सिंचाई से बचें।", 'kn': "ಒಣ ವರ್ಷದಲ್ಲಿ ಅಪಾಯ ಕಡಿಮೆ.", 'te': "పొడి వాతావరణంలో ప్రమాదం తక్కువ."},

            'winter': {'en': "Low activity—prune infected shoots during dry window.", 'hi': "कम गतिविधि—सूखे समय में संक्रमित शाखाओं को छांटें।", 'kn': "ಕಡಿಮೆ ಚಟುವಟಿಕೆ — ಒಣಗಿದ ಸಮಯದಲ್ಲಿ ಕತ್ತರಿಸಿ.", 'te': "తక్కువ క్రియాశీలత—చెట్లను కత్తిరించండి."},

            'general': {'en': "Avoid tool-mediated spread; copper applications as preventive measure.", 'hi': "उपकरण से फैलाव न हो—रोकथाम के लिए कॉपर।", 'kn': "ಉಪಕರಣದಿಂದ ಹರಡುವಿಕೆಯನ್ನು ತಡೆಯಿರಿ.", 'te': "సాధనాలద్వారా వ్యాప్తి కోసమే జాగ్రత్త."}

        },

        'action_plan': {

            'cultural': {'en': "Sanitation, avoid overhead irrigation, prune and burn infected material where permitted.", 'hi': "स्वच्छता, ओवरहेड सिंचाई से बचें, संक्रमित भाग हटाएं।", 'kn': "ಸ್ವಚ್ಛತೆ ಮತ್ತು ಓವರ್‌ಹೆಡ್ ನೀರಾವರಿ ತಪ್ಪಿಸಿ.", 'te': "శుభ్రత మరియు తొలగింపు."},

            'organic': {'en': "Copper-based organic sprays at early stages; use of ASM (acibenzolar-S-methyl) in some regions as plant activator (follow regs).", 'hi': "प्रारम्भिक अवस्था में तांबे आधारित स्प्रे; कुछ जगह ASM का उपयोग—नियम देखें।", 'kn': "ಕಾಪರ್ ಬಯೋಸ್ಪ್ರೇಗಳು ಬಳಸಬಹುದು.", 'te': "కాపర్ ఆధారిత స్ప్రేలు వాడండి."},

            'chemical': {'en': "Copper bactericides (copper hydroxide/oxychloride) as per label (typical conc. 0.2–0.3%); systemic options limited—follow extension guidance.", 'hi': "कॉपper बेक्टिसाइड लेबल अनुसार (0.2–0.3%)।", 'kn': "ಕಾಪರ್ ಮೂಲಾಧಾರಿತ ಬೆಕ್ಟೀರಾಸೈಡ್ ಬಳಸಿ.", 'te': "కాపర్ బేస్డ్ బాక్టీరిసైడ్స్ లేబుల్ ప్రకారం వాడండి."}

        }

    },



    'Peach___Healthy': {

        'soils': {

            'red': {'en': "Maintain drainage, balanced N to avoid excessive succulent growth.", 'hi': "ड्रेन और संतुलित N रखें।", 'kn': "ಒಳ್ಳೆಯ ಒಳಚರಂಡಿ ಮತ್ತು ಸಮತೋಲಿತ ನೈಟ್ರೋಜನ್.", 'te': "మంచి డ్రైనేజ్ మరియు సమతుల్య N."},

            'black': {'en': "Avoid waterlogging; manage fertility.", 'hi': "जलभराव न करें; उर्वरक संतुलित रखें।", 'kn': "ನೀರು ನಿಲ್ಲದಂತೆ ತಡೆಗಟ್ಟಿ.", 'te': "నీటి నిల్వను నిరోధించండి."},

            'alluvial': {'en': "Follow local fertilization schedule; mulch to conserve moisture.", 'hi': "स्थानीय उर्वरक अनुसूची का पालन करें; मल्च करें।", 'kn': "ಸ್ಥಳೀಯ ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಅನುಸರಿಸಿ.", 'te': "ప్రాంతీయ సిఫార్సులు పాటించండి."},

            'general': {'en': "Routine IPM, pruning, and nutrient management.", 'hi': "नियमित IPM और पोषण।", 'kn': "IPM ಹಾಗೂ ಪೋಷಕ ನಿರ್ವಹಣೆ.", 'te': "IPM పద్ధతులు పాటించండి."}

        },

        'seasons': {

            'monsoon': {'en': "Watch for fungal diseases; maintain canopy airflow.", 'hi': "फफूंदियों की जाँच करें।", 'kn': "ತೇವಾವಧಿಯಲ್ಲಿ ವಿಮರ್ಶಿಸಿ.", 'te': "ఫంగల్ వ్యాధుల పర్యవేక్షణ."},

            'summer': {'en': "Protect from fruit sunburn and water stress.", 'hi': "फल की धूप से रक्षा करें।", 'kn': "ಹಣಬಿಲ್ నుంచి ರಕ್ಷಿಸಿ.", 'te': "పండ్లను సూర్యాడు వేసినప్పుడు రక్షించండి."},

            'winter': {'en': "Dormant pruning and sanitation.", 'hi': "निष्क्रिय छंटाई।", 'kn': "ಡಾರ್ಮೆಂಟ್ ಕುತೃಪ್ತ.", 'te': "డార్మంట్ సమయంలో కత్తిరించండి."},

            'general': {'en': "Keep records of pest/disease history and rotate sprays.", 'hi': "कीट/रोग का रिकॉर्ड रखें।", 'kn': "ರೋಗದ ದಾಖಲೆ ಇಡಿ.", 'te': "పరిస్థితుల రికార్డులు ఉంచండి."}

        },

        'action_plan': {

            'cultural': {'en': "Prune, sanitation, balanced nutrition and irrigation timing.", 'hi': "छंटाई, स्वच्छता और संतुलित पोषण।", 'kn': "ಕತ್ತರಿಸಿ ಮತ್ತು ಸ್ವಚ್ಛತೆ.", 'te': "కత్తిరించి శుభ్రపరచండి."},

            'organic': {'en': "Compost, mycorrhizae and biocontrol for soil health.", 'hi': "कम्पोस्ट और जैविक उपचार।", 'kn': "ಕಂಪೋಸ್ಟ್ ಮತ್ತು ಬಯೋಟ್.", 'te': "కంపోస్ట్ మరియు బయోకంట్రోల్ వాడండి."},

            'chemical': {'en': "Use pesticides only when scouting thresholds reached and follow label directions.", 'hi': "सिर्फ जरूरत पर उपयोग करें।", 'kn': "ತಪಾಸಣೆ ನಂತರ ಮಾತ್ರ ರಸಾಯನಿಕ ಬಳಸಿ.", 'te': "పర్యవేక్షణ తర్వాత మాత్రమే రసాయనాలు."}

        }

    },



    # -------------------------

    # BELL PEPPER

    # -------------------------

    'Pepper,_bell___Bacterial_spot': {

        'soils': {

            'red': {'en': "Moist warm periods favor spread—avoid leaf wetting and sanitize.", 'hi': "गर्म गीले माहौल फैलाव बढ़ाते—पत्ती गीली न करें।", 'kn': "ತೇವವಿರುವ ಪರಿಸ್ಥಿತಿ ಹರಡುತ್ತದೆ.", 'te': "తడిగా ఉన్నప్పుడు వ్యాప్తి ఉంటుంది."},

            'black': {'en': "Drainage and residue removal important.", 'hi': "नाली और अवशेष हटाना आवश्यक।", 'kn': "ನೆರೆಯನ್ನು ಸರಿಹೊಂದಿಸಿ.", 'te': "టలపాటు నిర్వహించండి."},

            'alluvial': {'en': "Avoid overhead irrigation; rotate capsicum crops.", 'hi': "ओवरहेड सिंचाई से बचें; फसल परिवर्तन करें।", 'kn': "ಓವರ್‌ಹೆಡ್ ನೀರಾವರಿ ತಪ್ಪಿಸಿ.", 'te': "ఓవరిహెడ్ నీరు ఇవ్వకండి."},

            'general': {'en': "Sanitation: remove infected fruits and avoid tool-mediated spread.", 'hi': "सफाई महत्वपूर्ण।", 'kn': "ಸ್ವಚ್ಛತೆ ಮುಖ್ಯ.", 'te': "శుభ్రత ముఖ్యమైనది."}

        },

        'seasons': {

            'monsoon': {'en': "High risk—apply copper protectants at transplant and during wet spells.", 'hi': "उच्च जोखिम—ट्रांसप्लांटिंग पर कॉपर लगाएं।", 'kn': "ಟ್ರಾನ್ಸ್ಪ್ಲಾಂಟ್‌ನಲ್ಲಿ ಕಾಪರ್ ಸ್ಪ್ರೇ ಮಾಡಿ.", 'te': "ట్రాన్స్‌ప్లాంట్ వేళ కాపర్ స్ప్రే చేయండి."},

            'summer': {'en': "Lower risk; avoid overhead watering during evening.", 'hi': "जोखिम कम—शाम को ओवरहेड पानी से बचें।", 'kn': "ಸಂಜೆ ಓವರ್‌ಹೆಡ್ ನೀರು ನಿಲ್ಲಿಸಿ.", 'te': "సాయంకాలం నీరు ఇవ్వకండి."},

            'winter': {'en': "Low activity—clean field and remove volunteers.", 'hi': "कम गतिविधि—खेत साफ रखें।", 'kn': "ಕಡಿಮೆ ಚಟುವಟಿಕೆ — ಭೂಮಿಯನ್ನು ತೊಳೆದುಹಾಕಿ.", 'te': "తక్కువ చర్య—వాలంటీయర్లను తొలగించండి."},

            'general': {'en': "Use certified seedlings and rotate Solanaceae crops.", 'hi': "प्रमाणित पौधे इस्तेमाल करें।", 'kn': "ಪ್ರಮಾಣೀಕೃತ ಸೀಡಿಂಗ್ ಬಳಸಿ.", 'te': "సర్టిఫైడ్ సీడ్లింగ్ వాడండి."}

        },

        'action_plan': {

            'cultural': {'en': "Use certified transplants, remove infected plants, avoid overhead irrigation.", 'hi': "प्रमाणित पौधे, संक्रमित हटाएँ।", 'kn': "ವೈದ್ಯರ ಸೂಚನೆ ಅನುಸರಿಸಿ.", 'te': "సర్టిఫైడ్ మొక్కలు వాడండి."},

            'organic': {'en': "Copper bactericides permitted in organic systems; biocontrol seed treatments may help.", 'hi': "कापर बायोउत्पाद प्रयोग करें।", 'kn': "ಕಾಪರ್ ಆಧಾರಿತ ಉತ್ಪನ್ನಗಳು ಬಳಸಬಹುದು.", 'te': "కాపర్ బేస్డ్ ఉత్పత్తులను వాడండి."},

            'chemical': {'en': "Copper hydroxide/oxychloride as per label (typical conc. 0.2–0.3%); follow re-entry and pre-harvest intervals.", 'hi': "कॉपper लेबल अनुसार (0.2–0.3%) और रिहाज़/हार्वेस्ट अंतर पालन करें।", 'kn': "ಲೇಬಲ್ ಪ್ರಕಾರ ಕಾಪರ್ ಬಳಸಿ.", 'te': "లేబుల్ ప్రకారం కాపర్ వాడండి."}

        }

    },



    'Pepper,_bell___healthy': {

        'soils': {

            'red': {'en': "Balance fertility, keep good drainage.", 'hi': "संतुलित उर्वरक और निकासी।", 'kn': "ಸಮತೋಲಿತ ಪೋಷಣೆ.", 'te': "సమతుల్య పోషణ."},

            'black': {'en': "Avoid waterlogging; mulch where needed.", 'hi': "जलभराव से बचें; मल्च करें।", 'kn': "ನೀರು ನಿಲ್ಲದಂತೆ ಮಾಡಿ.", 'te': "నీటి నిల్వ నివారించండి."},

            'alluvial': {'en': "Follow local recommendations for Capsicum nutrition.", 'hi': "स्थानीय सिफारिशों का पालन करें।", 'kn': "ಪ್ರಾದೇಶಿಕ ಸೂಚನೆ ಅನುಸರಿಸಿ.", 'te': "ప్రాంతీయ సూచనలు పాటించండి."},

            'general': {'en': "IPM, certified seedlings and rotation with non-Solanaceae.\"", 'hi': "IPM और प्रमाणित पौधे इस्तेमाल करें।", 'kn': "IPM ಬಳಸಿ.", 'te': "IPM విధానాలు పాటించండి."}

        },

        'seasons': {

            'monsoon': {'en': "Monitor for fungal/bacterial problems.", 'hi': "फफूंदी/बैक्टीरियल की जांच करें।", 'kn': "ತೇವಾವಧಿಯಲ್ಲಿ ಗಮನಿಸಿ.", 'te': "తడిగా ఉన్నప్పుడు జాగ్రత్త."},

            'summer': {'en': "Protect from sunburn and heat stress.", 'hi': "धूप से बचाएं।", 'kn': "ಸೂರ್ಯರಶ್ಮಿ ದೂರ.", 'te': "వేడి నుంచి రక్షించండి."},

            'winter': {'en': "Ensure pest sanitation.", 'hi': "कीट नियंत्रण रखें।", 'kn': "ಕೀಟದ ನಿರ್ವಹಣೆ.", 'te': "పసుపు ప్రయత్నం."},

            'general': {'en': "Maintain records and follow scouting thresholds for spray decisions.", 'hi': "रिकॉर्ड रखें और स्प्रे निर्णय लें।", 'kn': "ದಾಖಲೆ ಇಟ್ಟುಕೊಳ್ಳಿ.", 'te': "రికార్డ్స్ నిర్వహించండి."}

        },

        'action_plan': {

            'cultural': {'en': "Use certified transplants, rotate crops, good drainage and sanitation.", 'hi': "प्रमाणित पौधे, फसल घुमाव और ड्रेन।", 'kn': "ಸ್ಪಷ್ಟ ನೀರು ನಿರ್ವಹಣೆ.", 'te': "సర్టిఫైడ్ మొక్కలు వాడండి."},

            'organic': {'en': "Compost and biocontrol seed treatments.", 'hi': "कम्पोस्ट और बायोसीड उपचार।", 'kn': "ಕಂಪೋಸ್ಟ್ ಬಳಸಿ.", 'te': "కంపోస్టు ఉపయోగించండి."},

            'chemical': {'en': "Apply pesticides only when scouting shows threshold exceedance; follow label.", 'hi': "लेबल के अनुसार ही उपयोग।", 'kn': "ಲೇಬಲ್ ಪ್ರಕಾರ ಮಾತ್ರ.", 'te': "లేబుల్ ని పాటించండి."}

        }

    },


# -------------------------
    # POTATO
    # -------------------------
    'Potato___Early_blight': {  
        'soils': {
            'red': {'en': "Warm humid pockets favor early blight—manage canopy and rotation with non-solanaceous crops.", 'hi': "गर्म नम हिस्से शुरुआती संक्रमण बढ़ाते—कैनोपी प्रबंध और फसल परिवर्तन करे।", 'kn': "ತೇವದ ಬಿಸಿಲು ಭಾಗಗಳು ಹೆಚ್ಚು ಸಾಂಕ್ರಾಮಿಕ.", 'te': "తడి, వేడి ప్రాంతాలు రోగానికి అనుకూలం."},
            'black': {'en': "Residues and tuber exposure favor pathogen—bury volunteers and remove residues.", 'hi': "अवशेष और प्रमुख ट्यूबर जोखिम बढ़ाते—अवशेष हटाएं।", 'kn': "ಅವಶೇಷ ಮತ್ತು ಗುಡ್ಡಿ ಪರಿಹರಿಸಿಕೊಳ್ಳಿ.", 'te': "రెసిడ్యూ నిర్వహణ చేయండి."},
            'alluvial': {'en': "Good drainage reduces tuber rot risk; rotate crops.", 'hi': "अच्छी निकासी ट्यूबर रॉट कम करती है; रोटेट करें।", 'kn': "ಉತ್ತಮ ಒಳಚರಂಡಿ ಟ್ಯೂಬರ್ ರಾಟ್ ಕಡಿಮೆ.", 'te': "మంచి డ్రైనేజ్ ఉంచండి."},
            'general': {'en': "Use certified seed, avoid continuous potato cropping; sanitation essential.", 'hi': "प्रमाणित बीज प्रयोग करें; लगातार आलू की फसल न लगाए।", 'kn': "ಸೆರ್ಟಿಫೈಡ್ ಬೀಜ ಬಳಸಿ.", 'te': "సర్టిఫైడ్ వీటీలు వాడండి."}
        },
        'seasons': {
            'monsoon': {'en': "High risk—protectant sprays and good ventilation; 7-14 day spray intervals when wet.", 'hi': "उच्च जोखिम—प्रोटेक्टेंट और वेंटिलेशन; गीले में 7-14 दिन पर स्प्रे।", 'kn': "ತೇವಾದಿಯಲ್ಲಿ 7–14 ದಿನಕ್ಕೆ ಸ್ಪ್ರೇ.", 'te': "తడి సమయంలో 7–14 రోజులకు స్ಪ್ರే చేయండి."},
            'summer': {'en': "Reduce irrigation frequency to limit leaf wetness at night.", 'hi': "नींद में पत्तियों को गीला होने से बचाने हेतु सिंचाई घटाएं।", 'kn': " ರಾತ್ರಿ ತೇವಾಂಶ ಕಡಿಮೆ ಮಾಡಿರಿ.", 'te': "రాత్రి నీరు తగ్గించండి."},
            'winter': {'en': "Lower activity—plan seed selection and residue clearance.", 'hi': "कम गतिविधि—बीज और अवशेष व्यवस्था।", 'kn': "ಕಡಿಮೆ ಚಟುವಟಿಕೆ — ಬೀಯೂಸಿ ಆರಿಸಿ.", 'te': "తక్కువ వ్యాధి - సీడ్ యాజమాన్యం."},
            'general': {'en': "Watch lower leaves first and manage haulm removal before harvest.", 'hi': "निचली पत्तियों को पहले देखें और हार्वेस्ट से पहले हॉल्म हटाएँ।", 'kn': "ಕೆಳಗಿನ ಎಲೆಗಳನ್ನು ಮೊದಲು ಪರಿಶೀಲಿಸಿ.", 'te': "కిందివాటిని ముందుగా చూడండి."}
        },
        'action_plan': {
            'cultural': {'en': "Crop rotation, remove infected debris, avoid potato-on-potato sequences, good irrigation scheduling.", 'hi': "फसल चक्र, संक्रमित अवशेष हटाएँ, उचित सिंचाई।", 'kn': "ರೋಟೇಷನ್ ಮಾಡಿ ಮತ್ತು ಅವಶೇಷ ತೆಗೆದುಹಾಕಿ.", 'te': "రొటేషన్ నిర్వహించండి."},
            'organic': {'en': "Use Trichoderma-treated seed tubers, compost teas, and copper protectants as cultural-biological measures.", 'hi': "ट्राइकೋಡर्मा उपचारित बीज, कम्पोस्ट चाय और कॉपर प्रोटेक्टेंट का उपयोग।", 'kn': "ಟ್ರಿಕೋಡರ್ಮಾ ಪರಿಹಾರ ಬಳಸಿ.", 'te': "ట్రికోడర్మా ద్వారా ట్రీటెడ్ సీడ్లు వాడండి."},
            'chemical': {'en': "Use protectants (mancozeb) and systemics for severe outbreaks (e.g., azoxystrobin/fluazinam depending on label); rotate MoAs. Typical protectant conc. per label; 7–14 day repeat in wet spells.", 'hi': "मैनकोजेब जैसे प्रोटेक्टेंट और गंभीर स्थिति में सिस्टमिक—लेबल अनुसार।", 'kn': "ಮ್ಯಾಂಕೋಝೆಬ್ ಮತ್ತು ಸಿಸ್ಟಮಿಕ್ ಆಗಿರಬಹುದು.", 'te': "మాంకోజెబ్ వంటి రక్షకాలు మరియు అవసరమైతే సిస్టమిక్ ఫంగిసైడ్స్."}
        }
    },

'Potato___Late_blight': {
        'soils': {
            'red': {'en': "Oomycete (Phytophthora infestans) favored by cool wet conditions—ensure rapid drainage and avoid overhead irrigation.", 'hi': "फाइटोफ्थोरा ठंडे गीले में बढ़ता—तुरंत निकासी दें।", 'kn': "ಶೀತಲ ತೇವಾವಧಿಯಲ್ಲಿ oomycete ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "చల్లని తడి వాతావరణంలో విస్తరిస్తుంది."},
            'black': {'en': "High moisture retention increases tuber infection risk—avoid waterlogging.", 'hi': "उच्च नमी ट्यूबर संक्रमण जोखिम बढ़ाती—जलभराव से बचें।", 'kn': "ತೇವ ಹೆಚ್ಚಾದರೆ ಟ್ಯೂಬರ್ ಸೋಂಕು ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "తేమ ఎక్కువైతే ట్యూబర్ సోకుతుంది."},
            'alluvial': {'en': "Manage irrigation to avoid prolonged leaf wetness.", 'hi': "लंबे समय तक पत्ती गीली न रखें।", 'kn': "ಎಲೆಗಳ ತೀವ್ರ ತೇವಾಂಶ ಇಲ್ಲದಂತೆ ಮಾಡಿರಿ.", 'te': "పొడవుగా ఆకులు తేమగా ఉండనివ్వకండి."},
            'general': {'en': "Use certified seed, rapid removal of symptomatic plants, and fungicide programs focused on oomycete control.", 'hi': "प्रमाणित बीज, लक्षण दिखने पर तुरंत हटाएं; ओमाइसाइट नियंत्रण केंद्रित ఫंगिसाइड।", 'kn': "ಸೆರ್ಟಿಫೈಡ್ ಸೀಡ್ಗಳು ಬಳಸಿ.", 'te': "సర్టిఫైడ్ సీడ్లు వాడండి."}
        },
        'seasons': {
            'monsoon': {'en': "Very high risk—protectants and systemic (metalaxyl, mefenoxam) or phosphite sprays (potassium phosphite) as per label; repeat frequently during wet windows.", 'hi': "बहुत उच्च जोखिम—प्रोटेक्टेंट और सिस्टमिक/फॉसफाइट स्प्रे; बार-बार स्प्रे करें।", 'kn': "ತೇವಾವಧಿಯಲ್ಲಿ ಹೆಚ್ಚು ಅಪಾಯ.", 'te': "తడి సమయంలో తరచుగా స్ప్రే చేయండి."},
            'summer': {'en': "Warmer dry weather reduces activity but irrigations can cause local outbreaks—monitor.", 'hi': "गर्म शुष्क मौसम में कमी पर सिंचाई से स्थानीय फट सकती है।", 'kn': "ಒಣ ಹವಾಮಾನದಲ್ಲಿ ಕಡಿಮೆ.", 'te': "వేడితో ఉంటే తగ్గిపోతుంది కానీ నీటివ్వడం వల్ల వస్తుంది."},
            'winter': {'en': "Cool wet winter can also maintain inoculum—manage residues.", 'hi': "ठंडे गीले सर्दी में भी संक्रमण रह सकता—अवशेष प्रबंधित करें।", 'kn': "ಚಳಿಯಲ್ಲಿ ಕೂಡ ಇನೊಕ್ಯುಲಂ ಉಳಿಯಬಹುದು.", 'te': "చలి రోజుల్లో కూడా జాగ్రత్త."},
            'general': {'en': "Monitor for lesions on leaves, stems and tubers; removal and destruction reduce spread.", 'hi': "पत्तियों, तनों और ट्यूबरों पर घाव देखें; हटाना फैलाव घटाता है।", 'kn': "ಎಲೆಗಳು, ಕಾಂಡಗಳು ಮತ್ತು ಗೆಡ್ಡೆಗಳ ಮೇಲೆ ಗಾಯಗಳನ್ನು ಗಮನಿಸಿ; ತೆಗೆದುಹಾಕುವುದು ಹರಡುವಿಕೆಯನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.", 'te': "ఆకులు, కాండాలు మరియు దుంపలపై గాయాలను గమనించండి; తీసివేత వ్యాప్తిని తగ్గిస్తుంది."}
        },
        'action_plan': {
            'cultural': {'en': "Use certified seed, remove symptomatic plants promptly, avoid tuber exposure and reduce canopy wetness.", 'hi': "प्रमाणित बीज, रोगी पौधों को हटाएँ, ट्यूबर उजागर न करें।", 'kn': "ಸೆರ್ಟಿಫೈಡ್ ಬೀಜ ಬಳಸಿ, ರೋಗಲಕ್ಷಣಗಳಿರುವ ಸಸ್ಯಗಳನ್ನು ತಕ್ಷಣ ತೆಗೆದುಹಾಕಿ, ಗೆಡ್ಡೆಗಳು ಒಡ್ಡಿಕೊಳ್ಳುವುದನ್ನು ತಪ್ಪಿಸಿ.", 'te': "సర్టిఫైడ్ సీడ్ వాడండి; సంక్రమిత మొక్కలను తొలగించండి."},
            'organic': {'en': "Use potassium phosphite sprays as plant defense boosters (where registered) and biological soil amendments to improve drainage/soil health.", 'hi': "पोटेशियम फॉस्फाइट (जहाँ अनुमति हो) और जैविक मिट्टी सुधारक।", 'kn': "ಪೋಟಾಸಿಯಂ ಫಾಸ್ಫೈಟ್ ಬಳಸಬಹುದು (ನಿಯಮಾನುಸಾರ).", 'te': "పొటాసియం ఫాస్ఫైట్ వాడండి (నియమాల ప్రకారం)."},
            
            # --- THIS SECTION IS NOW CORRECT ---
            'chemical': {
                'en': ("Use oomycete-active fungicides (metalaxyl/mefenoxam, dimethomorph, fluopicolide) and protectants (mancozeb) as integrated program—follow label, rotate MoAs. "
                       "Typical strategy: protectants + systemic/curatives at onset; repeat 7–10 days in rainy windows. ALWAYS follow label & extension guidance."),
                'hi': "ओमाइसाइट-एक्टिव फंगिसाइड (metalaxyl/मेफेनॉक्सैम) और प्रोटेक्टेंट (मैनकोजेब) का संयोजन—लेबल का पालन करें।",
                'kn': "oomycete ಗಾಗಿ ಆಕ್ಟಿವ್ ಫಂಗಿಸೈಡ್ ಮತ್ತು ರಕ್ಷಕಗಳನ್ನು ಬಳಸಿ.",
                'te': "oomycete మందులను లేబుల్ ప్రకారం వాడండి."
            }
            # --- END OF FIX ---
        }
    },


    'Potato___healthy': { 
        'soils': {
            'red': {'en': "Avoid compaction and waterlogging; rotate crops.", 'hi': "कम्पैक्शन और जलभराव से बचें; रोटेशन करें।", 'kn': "ನಿಗದಿತ ಮಣ್ಣು ಸಂಯೋಜನೆ ತಪ್ಪಿಸಿ.", 'te': "గట్టిపడటం మరియు నీటి స్తబ్దతను నివారించండి; పంటలను మార్చండి."},
            'black': {'en': "Monitor for nematodes and tuber storage conditions.", 'hi': "नेमाटोड और ट्यूबर भंडारण देखें।", 'kn': "ನಿಮ್ಯಾಟೋಡ್ ಪರೀಕ್ಷೆ.", 'te': "నిమాటోడ్ పర్యవేక్షణ."},
            'alluvial': {'en': "Good drainage and certified seed prevent many problems.", 'hi': "अच्छी निकासी और प्रमाणित बीज कई समस्याएं रोकते हैं।", 'kn': "ಉತ್ತಮ ಒಳಚರಂಡಿ ಮತ್ತು ಸೆರ್ಟಿಫೈಡ್ ಬೀಜ.", 'te': "మంచి డ్రైనేజ్ మరియు సర్టిఫైడ్ సీడ్."},
            'general': {'en': "Maintain balanced N and K for tuber quality.", 'hi': "ट्यूबर गुणवत्ता के लिए संतुलित N और K।", 'kn': "ಟ್ಯೂಬರ್ ಗುಣಮಟ್ಟಕ್ಕೆ ಸಮತೋಲಿತ ಪೋಷಣೆ.", 'te': "ట్యూబర్ నాణ్యత కోసం సమతుల్య పోషణ."}
        },
        'seasons': {
            'monsoon': {'en': "High foliar disease risk—use protectant sprays in wet spells.", 'hi': "पर्ण रोग जोखिम अधिक—स्प्रे करें।", 'kn': "ಮಳೆಯ ಸಮಯದಲ್ಲಿ ರೋಗದ ಅಪಾಯ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "ఆకుల వ్యాధులపై జాగ్రత్త."},
            'summer': {'en': "Manage irrigation to avoid tuber cracking.", 'hi': "ट्यूबर दरार से बचाने हेतु सिंचाई प्रबंधित करें।", 'kn': "ಟ್ಯೂಬರ್ ಮುರಿದುಹೋಗದಂತೆ ನೀರು ಸಮತೋಲಗೊಳಿಸಿ.", 'te': "ట్యూబర్ పగుళ్లకు నిరోధకంగా నీరు ఇవ్వండి."},
            'winter': {'en': "Cure tubers properly for storage and remove residues.", 'hi': "ट्यूबर को सही ढंग से स्टोर करें।", 'kn': "ಟ್ಯೂಬರ್ ಸರಿಯಾಗಿ ಸಂಗ್ರಹಿಸಿ.", 'te': "ట్యూబర్ నిల్వ చేయండి."},
            'general': {'en': "Monitor pests (Colorado potato beetle, aphids) and apply IPM.", 'hi': "कीटों की निगरानी करें और IPM अपनाएं।", 'kn': "ಕೀಟದ ಪರಿಶೀಲನೆ ಮಾಡಿ.", 'te': "కీటక పర్యవేక్షణ."}
        },
        'action_plan': {
            'cultural': {'en': "Use certified seed, rotate away from solanaceous hosts, manage irrigation and haulm removal before harvest.", 'hi': "प्रमाणित बीज, फसल परिवर्तन और सही सिंचाई।", 'kn': "ಸೆರ್ಟಿಫೈಡ್ ಬೀಜ ಬಳಸಿ.", 'te': "సర్టిఫైడ్ వీతీలు వాడండి."},
            'organic': {'en': "Compost, Trichoderma seed treatments and soil health improvement.", 'hi': "कम्पोस्ट, ट्रायकೋडर्मा।", 'kn': "ಕಂಪೋಸ್ಟ್ ಮತ್ತು ಟ್ರಿಕೋಡರ್ಮಾ.", 'te': "కంపోస్ట్ మరియు ట్రికోడర్మా వాడండి."},
            'chemical': {'en': "Use pesticides only as per scouting and label; rotate MoAs to avoid resistance.", 'hi': "निगरानी और लेबल के अनुसार ही।", 'kn': "ತಪಾಸಣೆ ನಂತರ ಮಾತ್ರ ರಾಸಾಯನಿಕ ಬಳಸಿ.", 'te': "పర్యవేక్షణ తరువాత మాత్రమే రసాయనాలు వాడండి."}
        }
    },

    'Potato___healthy': {

        'soils': {

            'red': {'en': "Avoid compaction and waterlogging; rotate crops.", 'hi': "कम्पैक्शन और जलभराव से बचें; रोटेशन करें।", 'kn': "ನಿಗದಿತ ಮಣ್ಣು ಸಂಯೋಜನೆ ತಪ್ಪಿಸಿ.", 'te': "నిలిపివేయకండి."},

            'black': {'en': "Monitor for nematodes and tuber storage conditions.", 'hi': "नेमाटोड और ट्यूबर भंडारण देखें।", 'kn': "ನಿಮ್ಯಾಟೋಡ್ ಪರೀಕ್ಷೆ.", 'te': "నిమాటోడ్ పర్యవేక్షణ."},

            'alluvial': {'en': "Good drainage and certified seed prevent many problems.", 'hi': "अच्छी निकासी और प्रमाणित बीज कई समस्याएं रोकते हैं।", 'kn': "ಉತ್ತಮ ಒಳಚರಂಡಿ ಮತ್ತು ಸೆರ್ಟಿಫೈಡ್ ಬೀಜ.", 'te': "మంచి డ్రైనేజ్ మరియు సర్టిఫైడ్ సీడ్."},

            'general': {'en': "Maintain balanced N and K for tuber quality.", 'hi': "ट्यूबर गुणवत्ता के लिए संतुलित N और K।", 'kn': "ಟ್ಯೂಬರ್ ಗುಣಮಟ್ಟಕ್ಕೆ ಸಮತೋಲಿತ ಪೋಷಣೆ.", 'te': "ట్యూబర్ నాణ్యత కోసం సమతుల్య పోషణ."}

        },

        'seasons': {

            'monsoon': {'en': "High foliar disease risk—use protectant sprays in wet spells.", 'hi': "पर्ण रोग जोखिम अधिक—स्प्रे करें।", 'kn': "ಮಳೆಯ ಸಮಯದಲ್ಲಿ ರೋಗದ ಅಪಾಯ ಹೆಚ್ಚಾಗುತ್ತದೆ.", 'te': "దెబ్బతిన్న ఆకుల వ్యాధులపై జాగ్రత్త."},

            'summer': {'en': "Manage irrigation to avoid tuber cracking.", 'hi': "ट्यूबर दरार से बचाने हेतु सिंचाई प्रबंधित करें।", 'kn': "ಟ್ಯೂಬರ್ٛ ಮುರಿದುಹೋಗದಂತೆ ನೀರು ಸಮತೋಲಗೊಳಿಸಿ.", 'te': "ట్యూబర్ పగుళ్లకు నిరోధకంగా నీరు ఇవ్వండి."},

            'winter': {'en': "Cure tubers properly for storage and remove residues.", 'hi': "ट्यूबर को सही ढंग से स्टोर करें।", 'kn': "ಟ್ಯೂಬರ್ ಸರಿಯಾಗಿ ಸಂಗ್ರಹಿಸಿ.", 'te': "ట్యూబర్ నిల్వ చేయండి."},

            'general': {'en': "Monitor pests (Colorado potato beetle, aphids) and apply IPM.", 'hi': "कीटों की निगरानी करें और IPM अपनाएं।", 'kn': "ಕೀಟದ ಪರಿಶೀಲನೆ ಮಾಡಿ.", 'te': "కీట్స్ పర్యవేక్షణ."}

        },

        'action_plan': {

            'cultural': {'en': "Use certified seed, rotate away from solanaceous hosts, manage irrigation and haulm removal before harvest.", 'hi': "प्रमाणित बीज, फसल परिवर्तन और सही सिंचाई।", 'kn': "ಸೆರ್ಟಿಫೈಡ್ ಬೀಜ ಬಳಸಿ.", 'te': "సర్టిఫైడ్ వీతీలు వాడండి."},

            'organic': {'en': "Compost, Trichoderma seed treatments and soil health improvement.", 'hi': "कम्पोस्ट, ट्रायकೋडर्मा।", 'kn': "ಕಂಪೋಸ್ಟ್ ಮತ್ತು ಟ್ರಿಕೋಡರ್ಮಾ.", 'te': "కంపోస్ట్ మరియు ట్రికోడర్మా వాడండి."},

            'chemical': {'en': "Use pesticides only as per scouting and label; rotate MoAs to avoid resistance.", 'hi': "निगरानी और लेबल के अनुसार ही।", 'kn': "ತ್ಯಾಖಾನದ ನಂತರ ಮಾತ್ರ ರಾಸಾಯನಿಕ ಬಳಸಿ.", 'te': "పర్యవేక్షణ తరువాత మాత్రమే రసాయనాలు వాడండి."}

        }

    },

# -------------------------
    # RASPBERRY
    # -------------------------
    'Raspberry___healthy': {
        'soils': {
            'red': {'en': "Prefer well-drained, slightly acid soils; avoid heavy compaction.", 'hi': "अच्छी निकासी और हल्का अम्लीय मिट्टी पसंद।", 'kn': "ಒಳ್ಳೆಯ ಒಳಚರಂಡಿ ಹಾಗೂ ಸ್ವಲ್ಪ ಆಮ್ಲ.", 'te': "మంచి డ్రైనేజ్ మరియు స్వల్ప ఆమ్లితనం కావాలి."},
            'black': {'en': "Improve drainage and raise beds if needed.", 'hi': "ड्रेन बढ़ाएं और चकाती बेड बनाएं।", 'kn': "ನೆರೆ ನೀರನ್ನು ತಡೆಯಿರಿ.", 'te': "డ్రెయిన్ మెరుగుపరచండి."},
            'alluvial': {'en': "Maintain organic matter and mulch to conserve moisture.", 'hi': "सेंद्रिय पदार्थ और मल्च बनाये रखें।", 'kn': "ಆರ್ಗ್ಯಾನಿಕ್ ಮೆಟರ್ ಬಳಸಿ.", 'te': "ఆర్గానిక్ మెటర్ వాడండి."},
            'general': {'en': "Prune old canes and manage fruiting canes; monitor for fungal/cane diseases.", 'hi': "पुरानी डंठलों को छांटे।", 'kn': "ಹಳೆಯ ಕೇನ್ಗಳನ್ನು ಕತ್ತರಿಸಿ.", 'te': "పాత డింకలను తొలగించండి."}
        },
        'seasons': {
            'monsoon': {'en': "Protect from waterlogging; fungal issues possible during wet spells.", 'hi': "जलभराव से बचें; फफूंदी हो सकती है।", 'kn': "ತೇವವಿರುವ ಸಮಯದಲ್ಲಿ ರೋಗಗಳು ಬರುತ್ತವೆ.", 'te': "తడి కాలంలో ఫంగల్ సమస్యలు ఉంటాయి."},
            'summer': {'en': "Manage heat stress and irrigation.", 'hi': "गर्मी और सिंचाई प्रबंधित करें।", 'kn': "ಬಿಸಿಲಿನಿಂದ ರಕ್ಷಿಸಿ.", 'te': "వేడితో రక్షించండి."},
            'winter': {'en': "Prune and burn old canes where permitted.", 'hi': "पुरानी डंठल हटाएँ।", 'kn': "ಹಳೆಯ ಕೇನ್ಗಳು ತೆಗೆದುಹಾಕಿ.", 'te': "పాత డింకలను తొలగించండి."},
            'general': {'en': "Maintain soil pH and organic matter; fertilize per local recommendations.", 'hi': "मिट्टी pH और जैविक पदार्थ बनाए रखें; स्थानीय सिफारिशों के अनुसार उर्वरक दें।", 'kn': "ಮಣ್ಣು pH ಮತ್ತು ಕಾರ್ಬೋನಿಕ್ ವಿಷಯ ನೀರಾವರಿ ಮಾಡಿ.", 'te': "మట్టి pH మరియు ఆర్గానిక్ matter నిర్వహించండి."}
        },
        'action_plan': {
            'cultural': {'en': "Mulch, maintain acidic pH, avoid waterlogging, good drainage, provide trellising and pruning.", 'hi': "मल्च, अम्लता बनाए रखें, जलभराव से बचें, ट्रेलिसिंग और प्रूनिंग।", 'kn': "ಮಲ್ಚ್ ಮಾಡಿ, pH ಕಾಪಾಡಿ, ನೀರು ನಿಲ್ಲಿಸಬೇಡಿ, ಟ್ರೆಲ್ಲಿಸಿಂಗ್ ಮತ್ತು ಪ್ರೂನಿಂಗ್.", 'te': "మల్చ్ చేయండి, pH నిర్వహించండి, నీరు నిల్వకుండా చూడండి, ట్రెల్లిసింగ్ మరియు ప్రూనింగ్."},
            'organic': {'en': "Use composted organic matter; mycorrhizae inoculants may help root health.", 'hi': "कम्पोस्टेड जैविक पदार्थ उपयोग करें; मायकोराइजा जड़ स्वास्थ्य में मदद कर सकता है।", 'kn': "ಕಂಪೋಸ್ಟ್ ಮತ್ತು ಮೈಕೊರಿಜಾ ಬಳಸಿ.", 'te': "కంపోస్ట్ వాడండి; మైకోరైజా ఉపయోగించండి."},
            'chemical': {'en': "Only if disease occurs; monitor for root rots and botrytis.", 'hi': "रोग होने पर ही; रूट रॉट और बोट्राइटिस की जाँच करें।", 'kn': "ರೋಗ ಬಂದರೆ ಮಾತ್ರ; ರೂಟ್ ರಾಟ್ ಮತ್ತು ಬೊಟ್ರೈಟಿಸ್ ಗಮನಿಸಿ.", 'te': "వ్యాధి వస్తేనే; రూట్ రాట్ మరియు బోట్రైటిస్ పర్యవేక్షించండి."}
        }
    },

    # -------------------------
    # SOYBEAN
    # -------------------------
    'Soybean___healthy': {
        'soils': {
            'red': {'en': "Manage fertility, ensure good drainage.", 'hi': "उर्वरता और जल निकासी प्रबंधित करें।", 'kn': "ಫಲವತ್ತತೆ ಮತ್ತು ಒಳಚರಂಡಿ ನಿರ್ವಹಿಸಿ.", 'te': "సారవంతం మరియు డ్రైనేజీని నిర్వహించండి."},
            'black': {'en': "Good soil for soybean, but ensure drainage during heavy monsoon.", 'hi': "सोयाबीन के लिए अच्छी मिट्टी, भारी मानसून में जल निकासी सुनिश्चित करें।", 'kn': "ಸೋಯಾಬೀನ್‌ಗೆ ಉತ್ತಮ ಮಣ್ಣು, ಭಾರೀ ಮಳೆಯಲ್ಲಿ ಒಳಚರಂಡಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.", 'te': "సోయాబీన్‌కు మంచి నేల, భారీ వర్షాకాలంలో డ్రైనేజీ ఉండేలా చూసుకోండి."},
            'alluvial': {'en': "Very good soil for soybean, maintain balanced nutrition.", 'hi': "सोयाबीन के लिए बहुत अच्छी मिट्टी, संतुलित पोषण बनाए रखें।", 'kn': "ಸೋಯಾಬೀನ್‌ಗೆ ಅತ್ಯುತ್ತಮ ಮಣ್ಣು, ಸಮತೋಲಿತ ಪೋಷಣೆ ಕಾಪಾಡಿ.", 'te': "సోయాబీన్‌కు చాలా మంచి నేల, సమతుల్య పోషణను నిర్వహించండి."},
            'general': {'en': "Rotate with non-legume crops, manage residue, select resistant varieties.", 'hi': "गैर-फलीदार फसलों के साथ रोटेट करें, अवशेषों का प्रबंधन करें, प्रतिरोधी किस्में चुनें।", 'kn': "ದ್ವಿದಳವಲ್ಲದ ಬೆಳೆಗಳೊಂದಿಗೆ ತಿರುಗಿಸಿ, ಅವಶೇಷಗಳನ್ನು ನಿರ್ವಹಿಸಿ, ನಿರೋಧಕ ಪ್ರಭೇದಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ.", 'te': "లెగ్యూమ్ కాని పంటలతో రొటేట్ చేయండి, అవశేషాలను నిర్వహించండి, నిరోధక రకాలను ఎంచుకోండి."}
        },
        'seasons': {
            'monsoon': {'en': "Primary growing season (Kharif). Watch for foliar diseases and waterlogging.", 'hi': "मुख्य बढ़ता मौसम (खरीफ)। पर्ण रोगों और जलभराव पर ध्यान दें।", 'kn': "ಮುಖ್ಯ ಬೆಳೆಯುವ ಋತು (ಖಾರಿಫ್). ಎಲೆ ರೋಗಗಳು ಮತ್ತು ನೀರು ನಿಲ್ಲುವ ಬಗ್ಗೆ ಗಮನ ಕೊಡಿ.", 'te': "ప్రధాన పెరుగుతున్న కాలం (ఖరీఫ్). ఆకు వ్యాధులు మరియు నీటి నిల్వపై నిఘా ఉంచండి."},
            'summer': {'en': "Not typically grown, requires heavy irrigation.", 'hi': "आमतौर पर नहीं उगाया जाता, भारी सिंचाई की आवश्यकता होती है।", 'kn': "ಸಾಮಾನ್ಯವಾಗಿ ಬೆಳೆಯುವುದಿಲ್ಲ, ಭಾರಿ ನೀರಾವರಿ ಅಗತ್ಯವಿದೆ.", 'te': "సాధారణంగా పండించరు, భారీ నీటిపారుదల అవసరం."},
            'winter': {'en': "Can be grown in some regions as a Rabi crop.", 'hi': "कुछ क्षेत्रों में रबी फसल के रूप में उगाया जा सकता है।", 'kn': "ಕೆಲವು ಪ್ರದೇಶಗಳಲ್ಲಿ ಹಿಂಗಾರು ಬೆಳೆಯಾಗಿ ಬೆಳೆಯಬಹುದು.", 'te': "కొన్ని ప్రాంతాల్లో రబీ పంటగా పండించవచ్చు."},
            'general': {'en': "Warm-season crop, needs moisture but is sensitive to waterlogging.", 'hi': "गर्म मौसम की फसल, नमी की जरूरत है लेकिन जलभराव के प्रति संवेदनशील है।", 'kn': "ಬೆಚ್ಚಗಿನ ಋತುವಿನ ಬೆಳೆ, ತೇವಾಂಶ ಬೇಕು ಆದರೆ ನೀರು ನಿಲ್ಲುವುದಕ್ಕೆ ಸೂಕ್ಷ್ಮವಾಗಿರುತ್ತದೆ.", 'te': "వెచ్చని-కాలపు పంట, తేమ అవసరం కానీ నీటి నిల్వకు సున్నితంగా ఉంటుంది."}
        },
        'action_plan': {
            'cultural': {'en': "Crop rotation, residue management, select resistant varieties, balanced nutrition.", 'hi': "फसल चक्र, अवशेष प्रबंधन, प्रतिरोधी किस्में चुनें, संतुलित पोषण।", 'kn': "ಬೆಳೆ ಸರದಿ, ಅವಶೇಷ ನಿರ್ವಹಣೆ, ನಿರೋಧಕ ಪ್ರಭೇದಗಳನ್ನು ಆರಿಸಿ, ಸಮತೋಲಿತ ಪೋಷಣೆ.", 'te': "పంట మార్పిడి, అవశేషాల నిర్వహణ, నిరోధక రకాలను ఎంచుకోండి, సమతుల్య పోషణ."},
            'organic': {'en': "Use compost, biofertilizers (Rhizobium inoculum is crucial for nitrogen fixation).", 'hi': "कम्पोस्ट, जैव उर्वरक (नाइट्रोजन स्थिरीकरण के लिए राइजोबियम टीका महत्वपूर्ण है) का प्रयोग करें।", 'kn': "ಕಾಂಪೋಸ್ಟ್, ಜೈವಿಕ ಗೊಬ್ಬರಗಳನ್ನು ಬಳಸಿ (ಸಾರಜನಕ ಸ್ಥಿರೀಕರಣಕ್ಕೆ ರೈಜೋಬಿಯಂ ಇನಾಕ್ಯುಲಮ್ ಅತ್ಯಗತ್ಯ).", 'te': "కంపోస్ట్, జీవ ఎరువులు వాడండి (నత్రజని స్థిరీకరణకు రైజోబియం ఇనాక్యులమ్ చాలా ముఖ్యం)."},
            'chemical': {'en': "No chemical action if healthy; monitor for foliar diseases in monsoon.", 'hi': "स्वस्थ होने पर कोई रासायनिक कार्रवाई नहीं; मानसून में पर्ण रोगों की निगरानी करें।", 'kn': "ಆರೋಗ್ಯಕರವಾಗಿದ್ದರೆ ರಾಸಾಯನಿಕ ಕ್ರಮವಿಲ್ಲ; ಮಳೆಗಾಲದಲ್ಲಿ ಎಲೆ ರೋಗಗಳಿಗಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ.", 'te': "ఆరోగ్యంగా ఉంటే రసాయన చర్య లేదు; వర్షాకాలంలో ఆకు వ్యాధుల కోసం పర్యవేక్షించండి."}
        }
    },

    # -------------------------
    # SQUASH
    # -------------------------
    'Squash___Powdery_mildew': {
        'soils': {
            'red': {'en': "Drought-stressed plants in red soil are more susceptible. Ensure consistent moisture.", 'hi': "लाल मिट्टी में सूखे से तनावग्रस्त पौधे अधिक संवेदनशील होते हैं। लगातार नमी सुनिश्चित करें।", 'kn': "ಕೆಂಪು ಮಣ್ಣಿನಲ್ಲಿ ಬರದಿಂದ ಬಳಲುತ್ತಿರುವ ಸಸ್ಯಗಳು ಹೆಚ್ಚು ಒಳಗಾಗುತ್ತವೆ. ಸ್ಥಿರವಾದ ತೇವಾಂಶವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.", 'te': "ఎర్ర నేలలో కరువు-ఒత్తిడికి గురైన మొక్కలు ఎక్కువగా వ్యాధి బారిన పడతాయి. స్థిరమైన తేమను నిర్ధారించుకోండి."},
            'black': {'en': "Good fertility, but ensure drainage. Stressed plants are more susceptible.", 'hi': "अच्छी उर्वरता, लेकिन जल निकासी सुनिश्चित करें। तनावग्रस्त पौधे अधिक संवेदनशील होते हैं।", 'kn': "ಉತ್ತಮ ಫಲವತ್ತತೆ, ಆದರೆ ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಒತ್ತಡಕ್ಕೊಳಗಾದ ಸಸ್ಯಗಳು ಹೆಚ್ಚು ಒಳಗಾಗುತ್ತವೆ.", 'te': "మంచి సంతానోత్పత్తి, కానీ డ్రైనేజీని నిర్ధారించుకోండి. ఒత్తిడికి గురైన మొక్కలు ఎక్కువగా వ్యాధి బారిన పడతాయి."},
            'alluvial': {'en': "Good soil, but ensure consistent moisture as drought-stressed plants are susceptible.", 'hi': "अच्छी मिट्टी, लेकिन लगातार नमी सुनिश्चित करें क्योंकि सूखे से तनावग्रस्त पौधे संवेदनशील होते हैं।", 'kn': "ಉತ್ತಮ ಮಣ್ಣು, ಆದರೆ ಬರದಿಂದ ಬಳಲುತ್ತಿರುವ ಸಸ್ಯಗಳು ಸೂಕ್ಷ್ಮವಾಗಿರುವುದರಿಂದ ಸ್ಥಿರವಾದ ತೇವಾಂಶವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.", 'te': "మంచి నేల, కానీ కరువు-ఒత్తిడికి గురైన మొక్కలు సున్నితంగా ఉంటాయి కాబట్టి స్థిరమైన తేమను నిర్ధారించుకోండి."},
            'general': {'en': "Plant vigor is key. Drought-stressed plants in any soil type are more susceptible.", 'hi': "पौधे की शक्ति महत्वपूर्ण है। किसी भी प्रकार की मिट्टी में सूखे से तनावग्रस्त पौधे अधिक संवेदनशील होते हैं।", 'kn': "ಸಸ್ಯದ ಹುರುಪು ಮುಖ್ಯ. ಯಾವುದೇ ರೀತಿಯ ಮಣ್ಣಿನಲ್ಲಿ ಬರದಿಂದ ಬಳಲುತ್ತಿರುವ ಸಸ್ಯಗಳು ಹೆಚ್ಚು ಒಳಗಾಗುತ್ತವೆ.", 'te': "మొక్కల శక్తి ముఖ్యం. ఏ రకమైన నేలలోనైనా కరువు-ఒత్తిడికి గురైన మొక్కలు ఎక్కువగా వ్యాధి బారిన పడతాయి."}
        },
        'seasons': {
            'monsoon': {'en': "Can thrive in high humidity, even if rain is not heavy. Often appears late in the monsoon.", 'hi': "तेज बारिश न होने पर भी उच्च आर्द्रता में पनप सकता है। अक्सर मानसून के अंत में दिखाई देता है।", 'kn': "ಭಾರೀ ಮಳೆಯಾಗದಿದ್ದರೂ, ಹೆಚ್ಚಿನ ತೇವಾಂಶದಲ್ಲಿ ಬೆಳೆಯಬಹುದು. ಹೆಚ್ಚಾಗಿ ಮಾನ್ಸೂನ್ ಕೊನೆಯಲ್ಲಿ ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತದೆ.", 'te': "భారీ వర్షాలు లేకపోయినా, అధిక తేమలో వృద్ధి చెందుతుంది. తరచుగా వర్షాకాలం చివరలో కనిపిస్తుంది."},
            'summer': {'en': "Powdery mildew often appears late summer, especially when days are warm/dry and nights are cool/humid.", 'hi': "पाउडरी मिल्ड्यू अक्सर गर्मियों के अंत में दिखाई देता है, खासकर जब दिन गर्म/शुष्क और रातें ठंडी/आर्द्र होती हैं।", 'kn': "ಬೇಸಿಗೆಯ ಕೊನೆಯಲ್ಲಿ, ವಿಶೇಷವಾಗಿ ಹಗಲು ಬೆಚ್ಚಗಾಗಿದ್ದಾಗ/ಶುಷ್ಕವಾಗಿದ್ದಾಗ ಮತ್ತು ರಾತ್ರಿಗಳು ತಂಪಾಗಿ/ತೇವವಾಗಿದ್ದಾಗ ಬೂజు ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತದೆ.", 'te': "పొడి మిల్డ్యూ తరచుగా వేసవి చివరలో కనిపిస్తుంది, ప్రత్యేకించి పగటిపూట వెచ్చగా/పొడిగా మరియు రాత్రులు చల్లగా/తేమగా ఉన్నప్పుడు."},
            'winter': {'en': "Low risk in most areas.", 'hi': "अधिकांश क्षेत्रों में कम जोखिम।", 'kn': "ಹೆಚ್ಚಿನ ಪ್ರದೇಶಗಳಲ್ಲಿ ಕಡಿಮೆ ಅಪಾಯ.", 'te': "చాలా ప్రాంతాల్లో తక్కువ ప్రమాదం."},
            'general': {'en': "Widespread in domestic gardens and fields in humid areas.", 'hi': "घरेलू बगीचों और आर्द्र क्षेत्रों के खेतों में व्यापक रूप से फैला हुआ है।", 'kn': "ದೇಶೀಯ ಉದ್ಯಾನವನಗಳಲ್ಲಿ ಮತ್ತು ತೇವಾಂಶವುಳ್ಳ ಪ್ರದೇಶಗಳಲ್ಲಿ ವ್ಯಾಪಕವಾಗಿ ಹರಡಿದೆ.", 'te': "దేశీయ తోటలలో మరియు తేమతో కూడిన ప్రాంతాలలో విస్తృతంగా వ్యాపించింది."}
        },
        'action_plan': {
            'cultural': {'en': "Space plants for airflow, avoid excess nitrogen, remove infected leaves.", 'hi': "वायु प्रवाह के लिए पौधों को जगह दें, अतिरिक्त नाइट्रोजन से बचें, संक्रमित पत्तियों को हटा दें।", 'kn': "ಗಾಳಿಯ ಹರಿವಿಗೆ ಸಸ್ಯಗಳಿಗೆ ಜಾಗ ನೀಡಿ, ಹೆಚ್ಚುವರಿ ಸಾರಜನಕವನ್ನು ತಪ್ಪಿಸಿ, ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.", 'te': "గాలి ప్రవాహం కోసం మొక్కలకు స్థలం ఇవ్వండి, అదనపు నత్రజనిని నివారించండి, సోకిన ఆకులను తొలగించండి."},
            'organic': {'en': "Potassium bicarbonate sprays, neem oil, wettable sulfur.", 'hi': "पोटेशियम बाइकार्बोनेट स्प्रे, नीम का तेल, वेटेबल सल्फर।", 'kn': "ಪೊಟ್ಯಾಸಿಯಮ್ ಬೈಕಾರ್ಬನೇಟ್ ಸ್ಪ್ರೇಗಳು, ಬೇವಿನ ಎಣ್ಣೆ, ವೆಟ್ಟಬಲ್ ಸಲ್ಫರ್.", 'te': "పొటాషియం బైకార్బోనేట్ స్ప్రేలు, వేప నూనె, వెట్టబుల్ సల్ఫర్."},
            'chemical': {'en': "Wettable sulfur 0.2–0.3% (200–300 g / 100 L) or specific fungicides (myclobutanil, triforine) as label suggests. Interval: At first sign and repeat 7–14 days.", 'hi': "वेटेबल सल्फर 0.2–0.3% (200–300 ग्राम / 100 लीटर) या विशिष्ट कवकनाशी (माइक्लोबुटानिल, ट्राइफोरिन) जैसा कि लेबल सुझाता है। अंतराल: पहले संकेत पर और 7-14 दिनों में दोहराएं।", 'kn': "ಲೇಬಲ್ ಸೂಚಿಸಿದಂತೆ ವೆಟ್ಟಬಲ್ ಸಲ್ಫರ್ 0.2–0.3% (200–300 g / 100 L) ಅಥವಾ ನಿರ್ದಿಷ್ಟ ಶಿಲೀಂಧ್ರನಾಶಕಗಳು (ಮೈಕ್ಲೋಬುಟಾನಿಲ್, ಟ್ರೈಫೊರಿನ್). ಮಧ್ಯಂತರ: ಮೊದಲ ಚಿಹ್ನೆಯಲ್ಲಿ ಮತ್ತು 7-14 ದಿನಗಳನ್ನು ಪುನರಾವರ್ತಿಸಿ.", 'te': "వెట్టబుల్ సల్ఫర్ 0.2–0.3% (200–300 g / 100 L) లేదా లేబుల్ సూచించిన విధంగా నిర్దిష్ట శిలీంద్రనాశకాలు (మైక్లోబుటానిల్, ట్రైఫోరిన్). విరామం: మొదటి సంకేతం వద్ద మరియు 7-14 రోజులు పునరావృతం చేయండి."}
        }
    },

    # -------------------------
    # STRAWBERRY
    # -------------------------
    'Strawberry___Leaf_scorch': {
        'soils': {
            'red': {'en': "Poorly drained red soil increases root stress. Ensure good drainage.", 'hi': "खराब जल निकासी वाली लाल मिट्टी जड़ तनाव बढ़ाती है। अच्छी जल निकासी सुनिश्चित करें।", 'kn': "ಕಳಪೆ ಒಳಚರಂಡಿ ಕೆಂಪು ಮಣ್ಣು ಬೇರಿನ ಒತ್ತಡವನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ. ಉತ್ತಮ ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.", 'te': "సరిగా осуDrainage లేని ఎర్ర నేల రూట్ ఒత్తిడిని పెంచుతుంది. మంచి డ్రైనేజీని నిర్ధారించుకోండి."},
            'black': {'en': "Heavy, poorly drained black soil is high risk for root stress. Use raised beds.", 'hi': "भारी, खराब जल निकासी वाली काली मिट्टी जड़ तनाव के लिए उच्च जोखिम है। ऊँची क्यारियों का उपयोग करें।", 'kn': "ಭಾರೀ, ಕಳಪೆ ಒಳಚರಂಡಿ ಕಪ್ಪು ಮಣ್ಣು ಬೇರಿನ ಒತ್ತಡಕ್ಕೆ ಹೆಚ್ಚಿನ ಅಪಾಯವನ್ನುಂಟುಮಾಡುತ್ತದೆ. ಎತ್ತರದ ಹಾಸಿಗೆಗಳನ್ನು ಬಳಸಿ.", 'te': "భారీ, సరిగా осуDrainage లేని నల్ల నేల రూట్ ఒత్తిడికి అధిక ప్రమాదం. ఎత్తైన పడకలను వాడండి."},
            'alluvial': {'en': "Ensure good drainage and avoid waterlogging.", 'hi': "अच्छी जल निकासी सुनिश्चित करें और जलभराव से बचें।", 'kn': "ಉತ್ತಮ ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ ಮತ್ತು ನೀರು ನಿಲ್ಲುವುದನ್ನು ತಪ್ಪಿಸಿ.", 'te': "మంచి డ్రైనేజీని నిర్ధారించుకోండి మరియు నీటి నిల్వను నివారించండి."},
            'general': {'en': "Poorly drained soils increase root stress, which makes plants more susceptible to scorch and secondary infections.", 'hi': "खराब जल निकासी वाली मिट्टी जड़ तनाव बढ़ाती है, जिससे पौधे झुलसने और द्वितीयक संक्रमणों के प्रति अधिक संवेदनशील हो जाते हैं।", 'kn': "ಕಳಪೆ ಒಳಚರಂಡಿ ಮಣ್ಣು ಬೇರಿನ ಒತ್ತಡವನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ, ಇದು ಸಸ್ಯಗಳನ್ನು ಸುಡುವಿಕೆ ಮತ್ತು ದ್ವಿತೀಯ ಸೋಂಕುಗಳಿಗೆ ಹೆಚ್ಚು ಒಳಗಾಗುವಂತೆ ಮಾಡುತ್ತದೆ.", 'te': "సరిగా осуDrainage లేని నేలలు రూట్ ఒత్తిడిని పెంచుతాయి, ఇది మొక్కలను వేడికి మరియు ద్వితీయ సంక్రమణలకు ఎక్కువగా గురి చేస్తుంది."}
        },
        'seasons': {
            'monsoon': {'en': "High humidity and rain can worsen fungal leaf spots.", 'hi': "उच्च आर्द्रता और बारिश फंगल पत्ती धब्बों को खराब कर सकती है।", 'kn': "ಹೆಚ್ಚಿನ ತೇವಾಂಶ ಮತ್ತು ಮಳೆಯು ಶಿಲೀಂಧ್ರಗಳ ಎಲೆಗಳ ಕಲೆಗಳನ್ನು ಇನ್ನಷ್ಟು ಹದಗೆಡಿಸುತ್ತದೆ.", 'te': "అధిక తేమ మరియు వర్షం ఫంగల్ ఆకు మచ్చలను మరింత తీవ్రతరం చేస్తాయి."},
            'summer': {'en': "High temperatures and high humidity can cause scorch symptoms or exacerbate fungal issues. Provide shade in extreme heat.", 'hi': "उच्च तापमान और उच्च आर्द्रता झुलसने के लक्षण पैदा कर सकती है या फंगल समस्याओं को बढ़ा सकती है। अत्यधिक गर्मी में छाया प्रदान करें।", 'kn': "ಹೆಚ್ಚಿನ ತಾಪಮಾನ ಮತ್ತು ಹೆಚ್ಚಿನ ತೇವಾಂಶವು ಸುಡುವ ಲಕ್ಷಣಗಳನ್ನು ಉಂಟುಮಾಡಬಹುದು ಅಥವಾ ಶಿಲೀಂಧ್ರಗಳ ಸಮಸ್ಯೆಗಳನ್ನು ಉಲ್ಬಣಗೊಳಿಸಬಹುದು. ತೀವ್ರ ಶಾಖದಲ್ಲಿ ನೆರಳು ನೀಡಿ.", 'te': "అధిక ఉష్ణోగ్రతలు మరియు అధిక తేమ వేడి లక్షణాలను కలిగించవచ్చు లేదా ఫంగల్ సమస్యలను తీవ్రతరం చేస్తాయి. తీవ్రమైన వేడిలో నీడను అందించండి."},
            'winter': {'en': "Clean up dead leaves to reduce inoculum.", 'hi': "संक्रमण कम करने के लिए मृत पत्तियों को साफ करें।", 'kn': "ರೋಗಾಣು ಕಡಿಮೆ ಮಾಡಲು ಸತ್ತ ಎಲೆಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", 'te': "ఇనాక్యులమ్‌ను తగ్గించడానికి చనిపోయిన ఆకులను శుభ్రం చేయండి."},
            'general': {'en': "This is often a stress-related disease, worse in hot, humid, and wet conditions.", 'hi': "यह अक्सर तनाव से संबंधित बीमारी है, जो गर्म, आर्द्र और गीली स्थितियों में बदतर होती है।", 'kn': "ಇದು ಸಾಮಾನ್ಯವಾಗಿ ಒತ್ತಡ-ಸಂಬಂಧಿತ ಕಾಯಿಲೆಯಾಗಿದ್ದು, ಬಿಸಿ, ತೇವಾಂಶ ಮತ್ತು ಆರ್ದ್ರ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಕೆಟ್ಟದಾಗಿದೆ.", 'te': "ఇది తరచుగా ఒత్తిడికి సంబంధించిన వ్యాధి, వేడి, తేమ మరియు తడి పరిస్థితులలో అధ్వాన్నంగా ఉంటుంది."}
        },
        'action_plan': {
            'cultural': {'en': "Use well-draining raised beds, provide shade in extreme heat, remove infected leaves.", 'hi': "अच्छी जल निकासी वाली ऊँची क्यारियों का उपयोग करें, अत्यधिक गर्मी में छाया प्रदान करें, संक्रमित पत्तियों को हटा दें।", 'kn': "ಉತ್ತಮ ಒಳಚರಂಡಿ ಎತ್ತರದ ಹಾಸಿಗೆಗಳನ್ನು ಬಳಸಿ, ತೀವ್ರ ಶಾಖದಲ್ಲಿ ನೆರಳು ನೀಡಿ, ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.", 'te': "మంచి డ్రైనేజీ ఉన్న ఎత్తైన పడకలను వాడండి, తీవ్రమైన వేడిలో నీడను అందించండి, సోకిన ఆకులను తొలగించండి."},
            'organic': {'en': "Copper sprays if bacterial component suspected; biofungicides for fungal causes.", 'hi': "यदि जीवाणु घटक का संदेह हो तो कॉपर स्प्रे; फंगल कारणों के लिए जैव कवकनाशी।", 'kn': "ಬ್ಯಾಕ್ಟೀರಿಯಾದ ಅಂಶವನ್ನು ಶಂಕಿಸಿದರೆ ತಾಮ್ರದ ಸ್ಪ್ರೇಗಳು; ಶಿಲೀಂಧ್ರ ಕಾರಣಗಳಿಗಾಗಿ ಜೈವಿಕ ಶಿಲೀಂಧ್ರನಾಶಕಗಳು.", 'te': "బాక్టీరియా భాగం అనుమానించబడితే కాపర్ స్ప్రేలు; ఫంగల్ కారణాల కోసం బయోఫంగిసైడ్లు."},
            'chemical': {'en': "Copper oxychloride 0.2–0.3% for bacterial symptoms. For fungal leaf scorch, fungicides like Mancozeb or systemic azoles may be used, depending on the exact diagnosis. Interval: At symptom appearance and follow up every 7–10 days if disease pressure high.", 'hi': "जीवाणु लक्षणों के लिए कॉपर ऑक्सीक्लोराइड 0.2–0.3%। फंगल पत्ती झुलसने के लिए, सटीक निदान के आधार पर मैनकोजेब या सिस्टमिक एजोल जैसे कवकनाशी का उपयोग किया जा सकता है। अंतराल: लक्षण दिखने पर और यदि रोग का दबाव अधिक हो तो हर 7-10 दिनों में फॉलो अप करें।", 'kn': "ಬ್ಯಾಕ್ಟೀರಿಯಾದ ರೋಗಲಕ್ಷಣಗಳಿಗೆ ತಾಮ್ರದ ಆಕ್ಸಿಕ್ಲೋರೈಡ್ 0.2–0.3%. ಶಿಲೀಂಧ್ರಗಳ ಎಲೆಗಳ ಸುಡುವಿಕೆಗೆ, ನಿಖರವಾದ ರೋಗನಿರ್ಣಯವನ್ನು ಅವಲಂಬಿಸಿ, ಮ್ಯಾಂಕೋಜೆಬ್ ಅಥವಾ ವ್ಯವಸ್ಥಿತ ಅಜೋಲ್‌ಗಳಂತಹ ಶಿಲೀಂಧ್ರನಾಶಕಗಳನ್ನು ಬಳಸಬಹುದು. ಮಧ್ಯಂತರ: ರೋಗಲಕ್ಷಣ ಕಾಣಿಸಿಕೊಂಡಾಗ ಮತ್ತು ರೋಗದ ಒತ್ತಡ ಹೆಚ್ಚಿದ್ದರೆ ಪ್ರತಿ 7-10 ದಿನಗಳಿಗೊಮ್ಮೆ ಅನುಸರಿಸಿ.", 'te': "బాక్టీరియా లక్షణాల కోసం కాపర్ ఆక్సీక్లోరైడ్ 0.2–0.3%. ఫంగల్ ఆకు మచ్చల కోసం, ఖచ్చితమైన రోగనిర్ధారణను బట్టి, మాంకోజెబ్ లేదా సిస్టమిక్ అజోల్స్ వంటి శిలీంద్రనాశకాలను ఉపయోగించవచ్చు. విరామం: లక్షణం కనిపించినప్పుడు మరియు వ్యాధి ఒత్తిడి ఎక్కువగా ఉంటే ప్రతి 7-10 రోజులకు ఫాలో అప్ చేయండి."}
        }
    },
    'Strawberry___healthy': {
        'soils': {
            'red': {'en': "Good, if well-drained and heavily amended with organic matter.", 'hi': "अच्छा है, यदि अच्छी जल निकासी हो और जैविक पदार्थ के साथ भारी मात्रा में संशोधित किया गया हो।", 'kn': "ಉತ್ತಮ, ಒಳಚರಂಡಿ ಮತ್ತು ಸಾವಯವ ಪದಾರ್ಥಗಳೊಂದಿಗೆ ಹೆಚ್ಚು ತಿದ್ದುಪಡಿ ಮಾಡಿದರೆ.", 'te': "మంచిది, మంచి డ్రైనేజీ మరియు సేంద్రియ పదార్థంతో ఎక్కువగా సవరించబడితే."},
            'black': {'en': "Not ideal. Must use raised beds to ensure drainage and prevent fruit rot.", 'hi': "आदर्श नहीं। जल निकासी सुनिश्चित करने और फल सड़न को रोकने के लिए ऊँची क्यारियों का उपयोग करना चाहिए।", 'kn': "ಸೂಕ್ತವಲ್ಲ. ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಲು ಮತ್ತು ಹಣ್ಣು ಕೊಳೆಯುವುದನ್ನು ತಡೆಯಲು ಎತ್ತರದ ಹಾಸಿಗೆಗಳನ್ನು ಬಳಸಬೇಕು.", 'te': "ఆదర్శంగా లేదు. డ్రైనేజీని నిర్ధారించడానికి మరియు పండు కుళ్ళిపోకుండా నిరోధించడానికి ఎత్తైన పడకలను ఉపయోగించాలి."},
            'alluvial': {'en': "Good, if sandy loam and well-drained. Amend with compost.", 'hi': "अच्छा है, यदि रेतीली दोमट और अच्छी जल निकासी हो। खाद के साथ संशोधित करें।", 'kn': "ಉತ್ತಮ, ಮರಳಿನ ಲೋಮ್ ಮತ್ತು ಚೆನ್ನಾಗಿ ಬರಿದಾಗಿದ್ದರೆ. ಮಿಶ್ರಗೊಬ್ಬರದೊಂದಿಗೆ ತಿದ್ದುಪಡಿ ಮಾಡಿ.", 'te': "మంచిది, ఇసుక లోమ్ మరియు మంచి డ్రైనేజీ ఉంటే. కంపోస్ట్‌తో సవరించండి."},
            'general': {'en': "Strawberries require well-drained, sandy loam soil rich in organic matter. Use raised beds. Mulch (plastic or straw) is essential.", 'hi': "स्ट्रॉबेरी को अच्छी जल निकासी वाली, जैविक पदार्थ से भरपूर रेतीली दोमट मिट्टी की आवश्यकता होती है। ऊँची क्यारियों का उपयोग करें। मल्च (प्लास्टिक या पुआल) आवश्यक है।", 'kn': "ಸ್ಟ್ರಾಬೆರಿಗಳಿಗೆ ಚೆನ್ನಾಗಿ ಬರಿದಾಗುವ, ಸಾವಯವ ಪದಾರ್ಥಗಳಿಂದ ಸಮೃದ್ಧವಾಗಿರುವ ಮರಳಿನ ಲೋಮ್ ಮಣ್ಣು ಬೇಕಾಗುತ್ತದೆ. ಎತ್ತರದ ಹಾಸಿಗೆಗಳನ್ನು ಬಳಸಿ. ಮಲ್ಚ್ (ಪ್ಲಾಸ್ಟಿಕ್ ಅಥವಾ ಒಣಹುಲ್ಲಿನ) ಅವಶ್ಯಕವಾಗಿದೆ.", 'te': "స్ట్రాబెర్రీలకు మంచి డ్రైనేజీ, సేంద్రియ పదార్థంతో కూడిన ఇసుక లోమ్ నేల అవసరం. ఎత్తైన పడకలను వాడండి. మల్చ్ (ప్లాస్టిక్ లేదా గడ్డి) అవసరం."}
        },
        'seasons': {
            'monsoon': {'en': "High risk for fruit rot (Botrytis) and other fungal diseases. Ensure good drainage.", 'hi': "फल सड़न (बोट्राइटिस) और अन्य फंगल रोगों का उच्च जोखिम। अच्छी जल निकासी सुनिश्चित करें।", 'kn': "ಹಣ್ಣು ಕೊಳೆತ (ಬೊಟ್ರಿಟಿಸ್) ಮತ್ತು ಇತರ ಶಿಲೀಂಧ್ರ ರೋಗಗಳ ಹೆಚ್ಚಿನ ಅಪಾಯ. ಉತ್ತಮ ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.", 'te': "పండు కుళ్ళు (బోట్రిటిస్) మరియు ఇతర ఫంగల్ వ్యాధుల అధిక ప్రమాదం. మంచి డ్రైనేజీని నిర్ధారించుకోండి."},
            'summer': {'en': "Plants can suffer from heat stress. Provide consistent water.", 'hi': "पौधे गर्मी के तनाव से पीड़ित हो सकते हैं। लगातार पानी प्रदान करें।", 'kn': "ಸಸ್ಯಗಳು ಶಾಖದ ಒತ್ತಡದಿಂದ ಬಳಲುತ್ತವೆ. ಸ್ಥಿರವಾದ ನೀರನ್ನು ಒದಗಿಸಿ.", 'te': "మొక్కలు వేడి ఒత్తిడికి గురవుతాయి. స్థిరమైన నీటిని అందించండి."},
            'winter': {'en': "This is the primary growing and fruiting season in the Indian plains.", 'hi': "यह भारतीय मैदानों में प्राथमिक बढ़ता और फलने वाला मौसम है।", 'kn': "ಇದು ಭಾರತೀಯ ಬಯಲು ಪ್ರದೇಶಗಳಲ್ಲಿ ಪ್ರಾಥಮಿಕವಾಗಿ ಬೆಳೆಯುವ ಮತ್ತು ಫ್ರುಟಿಂಗ್ ಋತುವಾಗಿದೆ.", 'te': "ఇది భారతీయ మైదానాలలో ప్రాథమిక పెరుగుతున్న మరియు ఫలవంతమైన కాలం."},
            'general': {'en': "Grown as a winter crop in plains or year-round in temperate hill stations. Sensitive to frost and extreme heat.", 'hi': "मैदानों में सर्दियों की फसल के रूप में या समशीतोष्ण पहाड़ी स्टेशनों में साल भर उगाया जाता है। पाले और अत्यधिक गर्मी के प्रति संवेदनशील।", 'kn': "ಬಯಲು ಪ್ರದೇಶಗಳಲ್ಲಿ ಚಳಿಗಾಲದ ಬೆಳೆಯಾಗಿ ಅಥವಾ ಸಮಶೀತೋಷ್ಣ ಗಿರಿಧಾಮಗಳಲ್ಲಿ ವರ್ಷಪೂರ್ತಿ ಬೆಳೆಯಲಾಗುತ್ತದೆ. ಹಿಮ ಮತ್ತು ತೀವ್ರ ಶಾಖಕ್ಕೆ ಸೂಕ್ಷ್ಮ.", 'te': "మైదానాలలో శీతాకాలపు పంటగా లేదా సమశీతోష్ణ కొండ ప్రాంతాలలో ఏడాది పొడవునా పండిస్తారు. మంచు మరియు తీవ్రమైన వేడికి సున్నితంగా ఉంటుంది."}
        },
        'action_plan': {
            'cultural': {'en': "Use mulch (plastic or straw) to keep fruit off the soil, conserve moisture, and suppress weeds. Use drip irrigation. Plant certified disease-free runners. Renovate beds as needed.", 'hi': "मिट्टी से फल को दूर रखने, नमी बनाए रखने और खरपतवारों को दबाने के लिए मल्च (प्लास्टिक या पुआल) का उपयोग करें। ड्रिप सिंचाई का उपयोग करें। प्रमाणित रोग मुक्त रनर लगाएं। आवश्यकतानुसार बेड का नवीनीकरण करें।", 'kn': "ಹಣ್ಣನ್ನು ಮಣ್ಣಿನಿಂದ ದೂರವಿಡಲು, ತೇವಾಂಶವನ್ನು ಸಂರಕ್ಷಿಸಲು ಮತ್ತು ಕಳೆಗಳನ್ನು ನಿಗ್ರಹಿಸಲು ಮಲ್ಚ್ (ಪ್ಲಾಸ್ಟಿಕ್ ಅಥವಾ ಒಣಹುಲ್ಲಿನ) ಬಳಸಿ. ಹನಿ ನೀರಾವರಿ ಬಳಸಿ. ಪ್ರಮಾಣೀಕೃತ ರೋಗ-ಮುಕ್ತ ರನ್ನರ್‌ಗಳನ್ನು ನೆಡಿರಿ. ಅಗತ್ಯವಿರುವಂತೆ ಹಾಸಿಗೆಗಳನ್ನು ನವೀಕರಿಸಿ.", 'te': "పండును నేల నుండి దూరంగా ఉంచడానికి, తేమను సంరక్షించడానికి మరియు కలుపు మొక్కలను అణిచివేసేందుకు మల్చ్ (ప్లాస్టిక్ లేదా గడ్డి) ఉపయోగించండి. డ్రిప్ ఇరిగేషన్ ఉపయోగించండి. ధృవీకరించబడిన వ్యాధి రహిత రన్నర్లను నాటండి. అవసరమైన విధంగా పడకలను పునరుద్ధరించండి."},
            'organic': {'en': "Amend soil heavily with compost.", 'hi': "मिट्टी को खाद के साथ भारी मात्रा में संशोधित करें।", 'kn': "ಮಿಶ್ರಗೊಬ್ಬರದೊಂದಿಗೆ ಮಣ್ಣನ್ನು ಹೆಚ್ಚು ತಿದ್ದುಪಡಿ ಮಾಡಿ.", 'te': "కంపోస్ట్‌తో నేలను భారీగా సవరించండి."},
            'chemical': {'en': "No chemical action needed. Monitor for mites, aphids, and fruit rot (Botrytis).", 'hi': "किसी रासायनिक कार्रवाई की आवश्यकता नहीं है। माइट्स, एफिड्स और फल सड़न (बोट्राइटिस) के लिए मॉनिटर करें।", 'kn': "ಯಾವುದೇ ರಾಸಾಯನಿಕ ಕ್ರಮ ಅಗತ್ಯವಿಲ್ಲ. ಮಿಟೆಗಳು, ಅಫಿಡ್ಗಳು ಮತ್ತು ಹಣ್ಣು ಕೊಳೆತ (ಬೊಟ್ರಿಟಿಸ್) ಗಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ.", 'te': "రసాయన చర్య అవసరం లేదు. మైట్స్, అఫిడ్స్ మరియు పండు కుళ్ళు (బోట్రిటిస్) కోసం పర్యవేక్షించండి."}
        }
    },

    # -------------------------
    # TOMATO
    # -------------------------
    'Tomato___Bacterial_spot': {
        'soils': {
            'red': {'en': "Soil splash spreads bacteria. Use mulch.", 'hi': "मिट्टी के छींटे बैक्टीरिया फैलाते हैं। मल्च का प्रयोग करें।", 'kn': "ಮಣ್ಣಿನ ಸ್ಪ್ಲಾಶ್ ಬ್ಯಾಕ್ಟೀರಿಯಾವನ್ನು ಹರಡುತ್ತದೆ. ಮಲ್ಚ್ ಬಳಸಿ.", 'te': "మట్టి స్ప్లాష్ బ్యాక్టీరియాను వ్యాపింపజేస్తుంది. మల్చ్ ఉపయోగించండి."},
            'black': {'en': "Soil splash spreads bacteria. Use mulch and raised beds for drainage.", 'hi': "मिट्टी के छींटे बैक्टीरिया फैलाते हैं। मल्च और जल निकासी के लिए ऊँची क्यारियों का उपयोग करें।", 'kn': "ಮಣ್ಣಿನ ಸ್ಪ್ಲಾಶ್ ಬ್ಯಾಕ್ಟೀರಿಯಾವನ್ನು ಹರಡುತ್ತದೆ. ಒಳಚರಂಡಿಗಾಗಿ ಮಲ್ಚ್ ಮತ್ತು ಎತ್ತರದ ಹಾಸಿಗೆಗಳನ್ನು ಬಳಸಿ.", 'te': "మట్టి స్ప్లాష్ బ్యాక్టీరియాను వ్యాపింపజేస్తుంది. డ్రైనేజీ కోసం మల్చ్ మరియు ఎత్తైన పడకలను వాడండి."},
            'alluvial': {'en': "Soil splash spreads bacteria. Use mulch.", 'hi': "मिट्टी के छींटे बैक्टीरिया फैलाते हैं। मल्च का प्रयोग करें।", 'kn': "ಮಣ್ಣಿನ ಸ್ಪ್ಲಾಶ್ ಬ್ಯಾಕ್ಟೀರಿಯಾವನ್ನು ಹರಡುತ್ತದೆ. ಮಲ್ಚ್ ಬಳಸಿ.", 'te': "మట్టి స్ప్లాష్ బ్యాక్టీరియాను వ్యాపింపజేస్తుంది. మల్చ్ ఉపయోగించండి."},
            'general': {'en': "Use mulch (straw or plastic) and drip irrigation to reduce water splashing from the soil onto the leaves.", 'hi': "मिट्टी से पत्तियों पर पानी के छींटे कम करने के लिए मल्च (पुआल या प्लास्टिक) और ड्रिप सिंचाई का उपयोग करें।", 'kn': "ಮಣ್ಣಿನಿಂದ ಎಲೆಗಳ ಮೇಲೆ ನೀರು ಸ್ಪ್ಲಾಶ್ ಆಗುವುದನ್ನು ಕಡಿಮೆ ಮಾಡಲು ಮಲ್ಚ್ (ಒಣಹುಲ್ಲಿನ ಅಥವಾ ಪ್ಲಾಸ್ಟಿಕ್) ಮತ್ತು ಹನಿ ನೀರಾವರಿ ಬಳಸಿ.", 'te': "మట్టి నుండి ఆకులపై నీరు స్ప్లాష్ కాకుండా తగ్గించడానికి మల్చ్ (గడ్డి లేదా ప్లాస్టిక్) మరియు డ్రిప్ ఇరిగేషన్ ఉపయోగించండి."}
        },
        'seasons': {
            'monsoon': {'en': "Severe risk. Protect seedlings and early fruit. Splashing rain is the main way it spreads.", 'hi': "गंभीर जोखिम। अंकुरों और शुरुआती फलों की रक्षा करें। छींटे वाली बारिश इसके फैलने का मुख्य तरीका है।", 'kn': "ತೀವ್ರ ಅಪಾಯ. ಸಸಿಗಳನ್ನು ಮತ್ತು ಆರಂಭಿಕ ಹಣ್ಣುಗಳನ್ನು ರಕ್ಷಿಸಿ. ಸ್ಪ್ಲಾಶಿಂಗ್ ಮಳೆ ಅದರ ಹರಡುವಿಕೆಯ ಮುಖ್ಯ ಮಾರ್ಗವಾಗಿದೆ.", 'te': "తీవ్రమైన ప్రమాదం. మొలకలను మరియు ప్రారంభ పండ్లను రక్షించండి. స్ప్లాషింగ్ వర్షం వ్యాప్తి చెందడానికి ప్రధాన మార్గం."},
            'summer': {'en': "Can be spread by overhead irrigation.", 'hi': "ओवरहेड सिंचाई से फैल सकता है।", 'kn': "ಓವರ್ಹೆಡ್ ನೀರಾವರಿಯಿಂದ ಹರಡಬಹುದು.", 'te': "ఓవర్హెడ్ ఇరిగేషన్ ద్వారా వ్యాపించవచ్చు."},
            'winter': {'en': "Low risk. Clean up plant debris after harvest.", 'hi': "कम जोखिम। फसल के बाद पौधे के मलबे को साफ करें।", 'kn': "ಕಡಿಮೆ ಅಪಾಯ. ಸುಗ್ಗಿಯ ನಂತರ ಸಸ್ಯದ ಅವಶೇಷಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", 'te': "తక్కువ ప్రమాదం. పంట తర్వాత మొక్కల వ్యర్థాలను శుభ్రం చేయండి."},
            'general': {'en': "Warm, wet, humid conditions are high risk. Humid regions higher risk.", 'hi': "गर्म, गीली, आर्द्र स्थितियाँ उच्च जोखिम वाली होती हैं। आर्द्र क्षेत्रों में अधिक जोखिम।", 'kn': "ಬೆಚ್ಚಗಿನ, ಆರ್ದ್ರ, ತೇವಾಂಶವುಳ್ಳ ಪರಿಸ್ಥಿತಿಗಳು ಹೆಚ್ಚಿನ ಅಪಾಯವನ್ನುಂಟುಮಾಡುತ್ತವೆ. ತೇವಾಂಶವುಳ್ಳ ಪ್ರದೇಶಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ಅಪಾಯವಿದೆ.", 'te': "వెచ్చని, తడి, తేమతో కూడిన పరిస్థితులు అధిక ప్రమాదం. తేమతో కూడిన ప్రాంతాల్లో ఎక్కువ ప్రమాదం."}
        },
        'action_plan': {
            'cultural': {'en': "Use certified disease-free seed/transplants. Sanitize stakes and tools. Remove and destroy infected plants. Avoid overhead irrigation.", 'hi': "प्रमाणित रोग मुक्त बीज/प्रत्यारोपण का उपयोग करें। स्टेक्स और उपकरणों को सैनिटाइज करें। संक्रमित पौधों को हटा दें और नष्ट कर दें। ओवरहेड सिंचाई से बचें।", 'kn': "ಪ್ರಮಾಣೀಕೃತ ರೋಗ-ಮುಕ್ತ ಬೀಜ/ಸಸಿಗಳನ್ನು ಬಳಸಿ. ಸ್ಟೇಕ್‌ಗಳು ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ. ಸೋಂಕಿತ ಸಸ್ಯಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ನಾಶಮಾಡಿ. ಓವರ್ಹೆಡ್ ನೀರಾವರಿಯನ್ನು ತಪ್ಪಿಸಿ.", 'te': "ధృవీకరించబడిన వ్యాధి రహిత విత్తనం/మొక్కలను వాడండి. స్టేక్స్ మరియు సాధనాలను శుభ్రపరచండి. సోకిన మొక్కలను తొలగించి నాశనం చేయండి. ఓవర్హెడ్ ఇరిగేషన్‌ను నివారించండి."},
            'organic': {'en': "Copper sprays (0.2–0.3%) as a protective measure.", 'hi': "सुरक्षात्मक उपाय के रूप में कॉपर स्प्रे (0.2–0.3%)।", 'kn': "ರಕ್ಷಣಾತ್ಮಕ ಕ್ರಮವಾಗಿ ತಾಮ್ರದ ಸ್ಪ್ರೇಗಳು (0.2–0.3%).", 'te': "రక్షిత చర్యగా కాపర్ స్ప్రేలు (0.2–0.3%)."},
            'chemical': {'en': "Copper formulations (0.2–0.3%) as protective sprays. Interval: At first sign and repeat every 7–14 days.", 'hi': "सुरक्षात्मक स्प्रे के रूप में कॉपर फॉर्मूलेशन (0.2–0.3%)। अंतराल: पहले संकेत पर और हर 7-14 दिनों में दोहराएं।", 'kn': "ರಕ್ಷಣಾತ್ಮಕ ಸ್ಪ್ರೇಗಳಾಗಿ ತಾಮ್ರದ ಸೂತ್ರೀಕರಣಗಳು (0.2–0.3%). ಮಧ್ಯಂತರ: ಮೊದಲ ಚಿಹ್ನೆಯಲ್ಲಿ ಮತ್ತು ಪ್ರತಿ 7-14 ದಿನಗಳಿಗೊಮ್ಮೆ ಪುನರಾವರ್ತಿಸಿ.", 'te': "రక్షిత స్ప్రేలుగా కాపర్ ఫార్ములేషన్లు (0.2–0.3%). విరామం: మొదటి సంకేతం వద్ద మరియు ప్రతి 7-14 రోజులకు పునరావృతం చేయండి."}
        }
    },
    'Tomato___Early_blight': {
        'soils': {
            'general': {'en': "Fungus survives in crop residue in the soil (all types). High Nitrogen fertilizer can make plants more susceptible. Stressed plants are more vulnerable.", 'hi': "कवक मिट्टी में फसल अवशेषों में जीवित रहता है (सभी प्रकार)। उच्च नाइट्रोजन उर्वरक पौधों को अधिक संवेदनशील बना सकता है। तनावग्रस्त पौधे अधिक कमजोर होते हैं।", 'kn': "ಶಿಲೀಂಧ್ರವು ಮಣ್ಣಿನಲ್ಲಿ (ಎಲ್ಲಾ ವಿಧಗಳು) ಬೆಳೆ ಉಳಿಕೆಗಳಲ್ಲಿ ಬದುಕುಳಿಯುತ್ತದೆ. ಹೆಚ್ಚಿನ ಸಾರಜನಕ ಗೊಬ್ಬರವು ಸಸ್ಯಗಳನ್ನು ಹೆಚ್ಚು ಒಳಗಾಗುವಂತೆ ಮಾಡುತ್ತದೆ. ಒತ್ತಡಕ್ಕೊಳಗಾದ ಸಸ್ಯಗಳು ಹೆಚ್ಚು ದುರ್ಬಲವಾಗಿರುತ್ತವೆ.", 'te': "శిలీంధ్రం నేలలో (అన్ని రకాలు) పంట అవశేషాలలో జీవిస్తుంది. అధిక నత్రజని ఎరువు మొక్కలను మరింత సున్నితంగా చేస్తుంది. ఒత్తిడికి గురైన మొక్కలు మరింత బలహీనంగా ఉంటాయి."}
        },
        'seasons': {
            'monsoon': {'en': "Greatest risk during rainy, humid seasons. Often starts on lower, older leaves.", 'hi': "बरसात, आर्द्र मौसमों के दौरान सबसे बड़ा जोखिम। अक्सर निचली, पुरानी पत्तियों पर शुरू होता है।", 'kn': "ಮಳೆ, ತೇವಾಂಶವುಳ್ಳ ಋತುಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ಅಪಾಯ. ಹೆಚ್ಚಾಗಿ ಕೆಳಗಿನ, ಹಳೆಯ ಎಲೆಗಳ ಮೇಲೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.", 'te': "వర్షపు, తేమతో కూడిన సీజన్లలో గొప్ప ప్రమాదం. తరచుగా దిగువ, పాత ఆకులపై ప్రారంభమవుతుంది."},
            'summer': {'en': "Can occur in warm, humid conditions, especially with overhead irrigation.", 'hi': "गर्म, आर्द्र स्थितियों में हो सकता है, खासकर ओवरहेड सिंचाई के साथ।", 'kn': "ಬೆಚ್ಚಗಿನ, ತೇವಾಂಶವುಳ್ಳ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ, ವಿಶೇಷವಾಗಿ ಓವರ್ಹೆಡ್ ನೀರಾವರಿಯೊಂದಿಗೆ ಸಂಭವಿಸಬಹುದು.", 'te': "వెచ్చని, తేమతో కూడిన పరిస్థితులలో, ముఖ్యంగా ఓవర్హెడ్ ఇరిగేషన్‌తో సంభవించవచ్చు."},
            'winter': {'en': "Low risk. Clean up debris.", 'hi': "कम जोखिम। मलबे को साफ करें।", 'kn': "ಕಡಿಮೆ ಅಪಾಯ. ಅವಶೇಷಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", 'te': "తక్కువ ప్రమాదం. వ్యర్థాలను శుభ్రం చేయండి."},
            'general': {'en': "High humidity and wet foliage favor the disease.", 'hi': "उच्च आर्द्रता और गीली पत्तियां रोग को बढ़ावा देती हैं।", 'kn': "ಹೆಚ್ಚಿನ ತೇವಾಂಶ ಮತ್ತು ಒದ್ದೆಯಾದ ಎಲೆಗಳು ರೋಗಕ್ಕೆ ಅನುಕೂಲಕರವಾಗಿವೆ.", 'te': "అధిక తేమ మరియు తడి ఆకులు వ్యాధికి అనుకూలంగా ఉంటాయి."}
        },
        'action_plan': {
            'cultural': {'en': "Remove lower leaves as the plant grows (pruning). Rotate crops (do not plant potatoes/tomatoes for 3 years). Stake or trellis plants to keep foliage off the ground and improve airflow.", 'hi': "पौधे के बढ़ने (छंटाई) के साथ निचली पत्तियों को हटा दें। फसलें घुमाएँ (3 साल तक आलू/टमाटर न लगाएँ)। पौधों को जमीन से दूर रखने और वायु प्रवाह में सुधार करने के लिए स्टेक या ट्रेलिस करें।", 'kn': "ಸಸ್ಯವು ಬೆಳೆದಂತೆ (ಸವರುವಿಕೆ) ಕೆಳಗಿನ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ. ಬೆಳೆಗಳನ್ನು ತಿರುಗಿಸಿ (3 ವರ್ಷಗಳವರೆಗೆ ಆಲೂಗಡ್ಡೆ/ಟೊಮ್ಯಾಟೊ ನೆಡಬೇಡಿ). ಎಲೆಗಳನ್ನು ನೆಲದಿಂದ ದೂರವಿಡಲು ಮತ್ತು ಗಾಳಿಯ ಹರಿವನ್ನು ಸುಧಾರಿಸಲು ಸಸ್ಯಗಳನ್ನು ಸ್ಟೇಕ್ ಮಾಡಿ ಅಥವಾ ಟ್ರೆಲ್ಲಿಸ್ ಮಾಡಿ.", 'te': "మొక్క పెరిగే కొద్దీ (కత్తిరింపు) దిగువ ఆకులను తొలగించండి. పంటలను మార్చండి (3 సంవత్సరాలు బంగాళాదుంపలు/టమోటాలు నాటవద్దు). ఆకులను నేల నుండి దూరంగా ఉంచడానికి మరియు గాలి ప్రవాహాన్ని మెరుగుపరచడానికి మొక్కలను స్టేక్ చేయండి లేదా ట్రేల్లిస్ చేయండి."},
            'organic': {'en': "Copper-based sprays. Bacillus subtilis sprays.", 'hi': "तांबे पर आधारित स्प्रे। बैसिलस सबटिलिस स्प्रे।", 'kn': "ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳು. ಬ್ಯಾಸಿಲಸ್ ಸಬ್ಟಿಲಿಸ್ ಸ್ಪ್ರೇಗಳು.", 'te': "రాగి ఆధారిత స్ప్రేలు. బాసిల్లస్ సబ్టిలిస్ స్ప్రేలు."},
            'chemical': {'en': "Mancozeb 0.2–0.25% as a protectant. Propiconazole/Tebuconazole as a systemic option, used in rotation. Interval: Start sprays at the first sign of infection on fruiting foliage and repeat per label.", 'hi': "मैनकोजेब 0.2–0.25% एक रक्षक के रूप में। प्रोपिकोनाज़ोल/टेबुकोनाज़ोल एक प्रणालीगत विकल्प के रूप में, रोटेशन में उपयोग किया जाता है। अंतराल: फलने वाली पत्तियों पर संक्रमण के पहले संकेत पर स्प्रे शुरू करें और प्रति लेबल दोहराएं।", 'kn': "ಮ್ಯಾಂಕೋಜೆಬ್ 0.2–0.25% ರಕ್ಷಕನಾಗಿ. ಪ್ರೊಪಿಕೊನಜೋಲ್/ಟೆಬುಕೊನಜೋಲ್ ವ್ಯವಸ್ಥಿತ ಆಯ್ಕೆಯಾಗಿ, ತಿರುಗುವಿಕೆಯಲ್ಲಿ ಬಳಸಲಾಗುತ್ತದೆ. ಮಧ್ಯಂತರ: ಫ್ರುಟಿಂಗ್ ಎಲೆಗಳ ಮೇಲೆ ಸೋಂಕಿನ ಮೊದಲ ಚಿಹ್ನೆಯಲ್ಲಿ ಸ್ಪ್ರೇಗಳನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಪ್ರತಿ ಲೇಬಲ್‌ಗೆ ಪುನರಾವರ್ತಿಸಿ.", 'te': "మాంకోజెబ్ 0.2–0.25% రక్షితంగా. ప్రోపికోనజోల్/టెబుకోనజోల్ దైహిక ఎంపికగా, భ్రమణంలో వాడబడుతుంది. విరామం: ఫలాలు కాసే ఆకులపై సంక్రమణ మొదటి సంకేతం వద్ద స్ప్రేలను ప్రారంభించండి మరియు ప్రతి లేబుల్‌కు పునరావృతం చేయండి."}
        }
    },
    'Tomato___Late_blight': {
        'soils': {
            'general': {'en': "Poor drainage in any soil type (especially heavy black soil) combined with cool, wet weather increases risk.", 'hi': "किसी भी प्रकार की मिट्टी में खराब जल निकासी (विशेषकर भारी काली मिट्टी) ठंडे, गीले मौसम के साथ मिलकर जोखिम बढ़ाती है।", 'kn': "ಯಾವುದೇ ರೀತಿಯ ಮಣ್ಣಿನಲ್ಲಿ (ವಿಶೇಷವಾಗಿ ಭಾರೀ ಕಪ್ಪು ಮಣ್ಣು) ಕಳಪೆ ಒಳಚರಂಡಿ ತಂಪಾದ, ಆರ್ದ್ರ ವಾತಾವರಣದೊಂದಿಗೆ ಸೇರಿ ಅಪಾಯವನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.", 'te': "ఏ రకమైన నేలలోనైనా (ముఖ్యంగా భారీ నల్ల నేల) పేలవమైన డ్రైనేజీ చల్లని, తడి వాతావరణంతో కలిసి ప్రమాదాన్ని పెంచుతుంది."}
        },
        'seasons': {
            'monsoon': {'en': "HIGH RISK, especially in cool, wet monsoon or temperate nights. This disease is explosive.", 'hi': "उच्च जोखिम, विशेष रूप से ठंडे, गीले मानसून या समशीतोष्ण रातों में। यह बीमारी विस्फोटक है।", 'kn': "ಹೆಚ್ಚಿನ ಅಪಾಯ, ವಿಶೇಷವಾಗಿ ತಂಪಾದ, ಆರ್ದ್ರ ಮಾನ್ಸೂನ್ ಅಥವಾ ಸಮಶೀತೋಷ್ಣ ರಾತ್ರಿಗಳಲ್ಲಿ. ಈ ರೋಗವು ಸ್ಫೋಟಕವಾಗಿದೆ.", 'te': "అధిక ప్రమాదం, ముఖ్యంగా చల్లని, తడి రుతుపవనాలు లేదా సమశీతోష్ణ రాత్రులలో. ఈ వ్యాధి పేలుడుగా ఉంటుంది."},
            'summer': {'en': "Generally too hot and dry for late blight.", 'hi': "आमतौर पर लेट ब्लाइट के लिए बहुत गर्म और शुष्क।", 'kn': "ಸಾಮಾನ್ಯವಾಗಿ ಲೇಟ್ ಬ್ಲೈಟ್‌ಗೆ ತುಂಬಾ ಬಿಸಿ ಮತ್ತು ಒಣಗಿರುತ್ತದೆ.", 'te': "సాధారణంగా లేట్ బ్లైట్ కోసం చాలా వేడిగా మరియు పొడిగా ఉంటుంది."},
            'winter': {'en': "Can occur in winter crops if conditions are unusually cool and wet.", 'hi': "यदि स्थितियाँ असामान्य रूप से ठंडी और गीली हों तो सर्दियों की फसलों में हो सकता है।", 'kn': "ಪರಿಸ್ಥಿತಿಗಳು ಅಸಾಮಾನ್ಯವಾಗಿ ತಂಪಾಗಿದ್ದರೆ ಮತ್ತು ತೇವವಾಗಿದ್ದರೆ ಚಳಿಗಾಲದ ಬೆಳೆಗಳಲ್ಲಿ ಸಂಭವಿಸಬಹುದು.", 'te': "పరిస్థితులు అసాధారణంగా చల్లగా మరియు తడిగా ఉంటే శీతాకాలపు పంటలలో సంభవించవచ్చు."},
            'general': {'en': "High risk during cool (15-21°C), wet, and humid conditions.", 'hi': "ठंडी (15-21°C), गीली और आर्द्र स्थितियों के दौरान उच्च जोखिम।", 'kn': "ತಂಪಾದ (15-21 ° C), ಆರ್ದ್ರ ಮತ್ತು ತೇವಾಂಶವುಳ್ಳ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ಅಪಾಯ.", 'te': "చల్లని (15-21°C), తడి మరియు తేమతో కూడిన పరిస్థితులలో అధిక ప్రమాదం."}
        },
        'action_plan': {
            'cultural': {'en': "Use certified disease-free seed/transplants. Remove volunteer potato/tomato plants. Ensure good drainage and spacing for airflow.", 'hi': "प्रमाणित रोग मुक्त बीज/प्रत्यारोपण का उपयोग करें। स्वयंसेवी आलू/टमाटर के पौधों को हटा दें। वायु प्रवाह के लिए अच्छी जल निकासी और अंतर सुनिश्चित करें।", 'kn': "ಪ್ರಮಾಣೀಕೃತ ರೋಗ-ಮುಕ್ತ ಬೀಜ/ಸಸಿಗಳನ್ನು ಬಳಸಿ. ಸ್ವಯಂಸೇವಕ ಆಲೂಗಡ್ಡೆ/ಟೊಮ್ಯಾಟೊ ಸಸ್ಯಗಳನ್ನು ತೆಗೆದುಹಾಕಿ. ಗಾಳಿಯ ಹರಿವಿಗೆ ಉತ್ತಮ ಒಳಚರಂಡಿ ಮತ್ತು ಅಂತರವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.", 'te': "ధృవీకరించబడిన వ్యాధి రహిత విత్తనం/మొక్కలను వాడండి. స్వచ్ఛంద బంగాళాదుంప/టమోటా మొక్కలను తొలగించండి. గాలి ప్రవాహం కోసం మంచి డ్రైనేజీ మరియు అంతరం ఉండేలా చూసుకోండి."},
            'organic': {'en': "Copper formulations as a protectant (may have limited control in severe outbreaks).", 'hi': "एक रक्षक के रूप में कॉपर फॉर्मूलेशन (गंभीर प्रकोपों में सीमित नियंत्रण हो सकता है)।", 'kn': "ರಕ್ಷಕನಾಗಿ ತಾಮ್ರದ ಸೂತ್ರೀಕರಣಗಳು (ತೀವ್ರ ಏಕಾಏಕಿ ಸೀಮಿತ ನಿಯಂತ್ರಣವನ್ನು ಹೊಂದಿರಬಹುದು).", 'te': "రక్షితంగా కాపర్ ఫార్ములేషన్లు (తీవ్రమైన వ్యాప్తిలో పరిమిత నియంత్రణ ఉండవచ్చు)."},
            'chemical': {'en': "Mancozeb 0.2–0.25% as a protectant. MUST use oomycete-specific systemic fungicides like Metalaxyl/Mefenoxam in rotation (use strictly per label to avoid resistance). Interval: Treat IMMEDIATELY at first sign. Repeat every 7 days during conducive weather.", 'hi': "मैनकोजेब 0.2–0.25% एक रक्षक के रूप में। मेटलॉक्सिल/मेफेनोक्सम जैसे ओमीसीट-विशिष्ट प्रणालीगत कवकनाशी का रोटेशन में उपयोग करें (प्रतिरोध से बचने के लिए प्रति लेबल सख्ती से उपयोग करें)। अंतराल: पहले संकेत पर तुरंत उपचार करें। अनुकूल मौसम के दौरान हर 7 दिनों में दोहराएं।", 'kn': "ಮ್ಯಾಂಕೋಜೆಬ್ 0.2–0.25% ರಕ್ಷಕನಾಗಿ. ಮೆಟಾಲಾಕ್ಸಿಲ್/ಮೆಫೆನೊಕ್ಸಾಮ್‌ನಂತಹ ಊಮೈಸೆಟ್-ನಿರ್ದಿಷ್ಟ ವ್ಯವಸ್ಥಿತ ಶಿಲೀಂಧ್ರನಾಶಕಗಳನ್ನು ರೊಟೇಶನ್‌ನಲ್ಲಿ ಬಳಸಬೇಕು (ಪ್ರತಿರೋಧವನ್ನು ತಪ್ಪಿಸಲು ಪ್ರತಿ ಲೇಬಲ್‌ಗೆ ಕಟ್ಟುನಿಟ್ಟಾಗಿ ಬಳಸಿ). ಮಧ್ಯಂತರ: ಮೊದಲ ಚಿಹ್ನೆಯಲ್ಲಿ ತಕ್ಷಣ ಚಿಕಿತ್ಸೆ ನೀಡಿ. ಅನುಕೂಲಕರ ವಾತಾವರಣದಲ್ಲಿ ಪ್ರತಿ 7 ದಿನಗಳಿಗೊಮ್ಮೆ ಪುನರಾವರ್ತಿಸಿ.", 'te': "మాంకోజెబ్ 0.2–0.25% రక్షితంగా. మెటాలాక్సిల్/మెఫెనోక్సామ్ వంటి ఊమైసెట్-నిర్దిష్ట దైహిక శిలీంద్రనాశకాలను తప్పనిసరిగా భ్రమణంలో వాడాలి (నిరోధకతను నివారించడానికి ప్రతి లేబుల్‌కు కఠినంగా వాడండి). విరామం: మొదటి సంకేతం వద్ద తక్షణమే చికిత్స చేయండి. అనుకూలమైన వాతావరణంలో ప్రతి 7 రోజులకు పునరావృతం చేయండి."}
        }
    },
    'Tomato___Leaf_mold': {
        'soils': {
            'general': {'en': "Soil is not a primary factor. This disease is all about high humidity and poor air circulation.", 'hi': "मिट्टी प्राथमिक कारक नहीं है। यह बीमारी उच्च आर्द्रता और खराब वायु परिसंचरण के बारे में है।", 'kn': "ಮಣ್ಣು ಪ್ರಾಥಮಿಕ ಅಂಶವಲ್ಲ. ಈ ರೋಗವು ಹೆಚ್ಚಿನ ಆರ್ದ್ರತೆ ಮತ್ತು ಕಳಪೆ ಗಾಳಿಯ ಪ್ರಸರಣಕ್ಕೆ ಸಂಬಂಧಿಸಿದೆ.", 'te': "నేల ప్రాథమిక అంశం కాదు. ఈ వ్యాధి అధిక తేమ మరియు గాలి ప్రసరణ సరిగా లేకపోవడం గురించి."}
        },
        'seasons': {
            'monsoon': {'en': "High risk due to high humidity, especially in densely planted fields or greenhouses.", 'hi': "उच्च आर्द्रता के कारण उच्च जोखिम, विशेष रूप से घनी आबादी वाले खेतों या ग्रीनहाउस में।", 'kn': "ಹೆಚ್ಚಿನ ತೇವಾಂಶದಿಂದಾಗಿ ಹೆಚ್ಚಿನ ಅಪಾಯ, ವಿಶೇಷವಾಗಿ ದಟ್ಟವಾಗಿ ನೆಟ್ಟ ಹೊಲಗಳಲ್ಲಿ ಅಥವಾ ಹಸಿರುಮನೆಗಳಲ್ಲಿ.", 'te': "అధిక తేమ కారణంగా అధిక ప్రమాదం, ముఖ్యంగా దట్టంగా నాటిన పొలాలలో లేదా గ్రీన్‌హౌస్‌లలో."},
            'summer': {'en': "Occurs in humid summer conditions, especially with evening humidity.", 'hi': "आर्द्र गर्मियों की स्थितियों में होता है, खासकर शाम की आर्द्रता के साथ।", 'kn': "ಆರ್ದ್ರ ಬೇಸಿಗೆಯ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ, ವಿಶೇಷವಾಗಿ ಸಂಜೆಯ ತೇವಾಂಶದೊಂದಿಗೆ ಸಂಭವಿಸುತ್ತದೆ.", 'te': "తేమతో కూడిన వేసవి పరిస్థితులలో, ముఖ్యంగా సాయంత్రం తేమతో సంభవిస్తుంది."},
            'winter': {'en': "Low risk unless in a heated, humid greenhouse.", 'hi': "कम जोखिम जब तक कि गर्म, आर्द्र ग्रीनहाउस में न हो।", 'kn': "ಬಿಸಿಯಾದ, ತೇವಾಂಶವುಳ್ಳ ಹಸಿರುಮನೆಯಲ್ಲಿ ಹೊರತುಪಡಿಸಿ ಕಡಿಮೆ ಅಪಾಯ.", 'te': "వేడిచేసిన, తేమతో కూడిన గ్రీన్‌హౌస్‌లో తప్ప తక్కువ ప్రమాదం."},
            'general': {'en': "High humidity (>85%) and poor airflow are the main drivers. Very common in greenhouses.", 'hi': "उच्च आर्द्रता (>85%) और खराब वायु प्रवाह मुख्य चालक हैं। ग्रीनहाउस में बहुत आम है।", 'kn': "ಹೆಚ್ಚಿನ ಆರ್ದ್ರತೆ (>85%) ಮತ್ತು ಕಳಪೆ ಗಾಳಿಯ ಹರಿವು ಮುಖ್ಯ ಚಾಲಕಗಳಾಗಿವೆ. ಹಸಿರುಮನೆಗಳಲ್ಲಿ ತುಂಬಾ ಸಾಮಾನ್ಯವಾಗಿದೆ.", 'te': "అధిక తేమ (>85%) మరియు గాలి ప్రసరణ సరిగా లేకపోవడం ప్రధాన చోదకాలు. గ్రీన్‌హౌస్‌లలో చాలా సాధారణం."}
        },
        'action_plan': {
            'cultural': {'en': "CRITICAL: Increase plant spacing and prune lower leaves for airflow. If in a greenhouse, ventilate heavily. Avoid overhead irrigation, especially in the evening.", 'hi': "महत्वपूर्ण: वायु प्रवाह के लिए पौधों के बीच की दूरी बढ़ाएँ और निचली पत्तियों की छंटाई करें। यदि ग्रीनहाउस में है, तो भारी वेंटीलेशन करें। ओवरहेड सिंचाई से बचें, खासकर शाम को।", 'kn': "ನಿರ್ಣಾಯಕ: ಗಾಳಿಯ ಹರಿವಿಗಾಗಿ ಸಸ್ಯಗಳ ಅಂತರವನ್ನು ಹೆಚ್ಚಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ. ಹಸಿರುಮನೆಯಲ್ಲಿದ್ದರೆ, ಹೆಚ್ಚು ಗಾಳಿ ನೀಡಿ. ಓವರ್ಹೆಡ್ ನೀರಾವರಿಯನ್ನು ತಪ್ಪಿಸಿ, ವಿಶೇಷವಾಗಿ ಸಂಜೆ.", 'te': "కీలకం: గాలి ప్రవాహం కోసం మొక్కల అంతరాన్ని పెంచండి మరియు దిగువ ఆకులను కత్తిరించండి. గ్రీన్‌హౌస్‌లో ఉంటే, భారీగా వెంటిలేట్ చేయండి. ఓవర్హెడ్ ఇరిగేషన్‌ను నివారించండి, ముఖ్యంగా సాయంత్రం."},
            'organic': {'en': "Copper-based sprays.", 'hi': "तांबे पर आधारित स्प्रे।", 'kn': "ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳು.", 'te': "రాగి ఆధారిత స్ప్రేలు."},
            'chemical': {'en': "Mancozeb or Chlorothalonil as protectants. Systemic DMI fungicides (e.g., Tebuconazole) if needed, used in rotation. Interval: Protect young foliage and repeat as required.", 'hi': "मैनकोजेब या क्लोरोथालोनिल रक्षक के रूप में। यदि आवश्यक हो तो प्रणालीगत DMI कवकनाशी (जैसे, टेबुकोनाज़ोल), रोटेशन में उपयोग किया जाता है। अंतराल: युवा पत्तियों की रक्षा करें और आवश्यकतानुसार दोहराएं।", 'kn': "ಮ್ಯಾಂಕೋಜೆಬ್ ಅಥವಾ ಕ್ಲೋರೊಥಾಲೋನಿಲ್ ರಕ್ಷಕಗಳಾಗಿ. ಅಗತ್ಯವಿದ್ದರೆ ವ್ಯವಸ್ಥಿತ DMI ಶಿಲೀಂಧ್ರನಾಶಕಗಳು (ಉದಾ., ಟೆಬುಕೊನಜೋಲ್), ತಿರುಗುವಿಕೆಯಲ್ಲಿ ಬಳಸಲಾಗುತ್ತದೆ. ಮಧ್ಯಂತರ: ಯುವ ಎಲೆಗಳನ್ನು ರಕ್ಷಿಸಿ ಮತ್ತು ಅಗತ್ಯವಿರುವಂತೆ ಪುನರಾವರ್ತಿಸಿ.", 'te': "మాంకోజెబ్ లేదా క్లోరోథలోనిల్ రక్షితంగా. అవసరమైతే దైహిక DMI శిలీంద్రనాశకాలు (ఉదా., టెబుకోనజోల్), భ్రమణంలో వాడబడతాయి. విరామం: యువ ఆకులను రక్షించండి మరియు అవసరమైన విధంగా పునరావృతం చేయండి."}
        }
    },
    'Tomato___Septoria_leaf_spot': {
        'soils': {
            'red': {'en': "Splashing from soil spreads spores. Mulch helps.", 'hi': "मिट्टी से छींटे बीजाणुओं को फैलाते हैं। मल्च मदद करता है।", 'kn': "ಮಣ್ಣಿನಿಂದ ಸ್ಪ್ಲಾಶಿಂಗ್ ಬೀಜಕಗಳನ್ನು ಹರಡುತ್ತದೆ. ಮಲ್ಚ್ ಸಹಾಯ ಮಾಡುತ್ತದೆ.", 'te': "మట్టి నుండి స్ప్లాషింగ్ బీజాంశాలను వ్యాపింపజేస్తుంది. మల్చ్ సహాయపడుతుంది."},
            'black': {'en': "Splashing from soil spreads spores. Mulch helps.", 'hi': "मिट्टी से छींटे बीजाणुओं को फैलाते हैं। मल्च मदद करता है।", 'kn': "ಮಣ್ಣಿನಿಂದ ಸ್ಪ್ಲಾಶಿಂಗ್ ಬೀಜಕಗಳನ್ನು ಹರಡುತ್ತದೆ. ಮಲ್ಚ್ ಸಹಾಯ ಮಾಡುತ್ತದೆ.", 'te': "మట్టి నుండి స్ప్లాషింగ్ బీజాంశాలను వ్యాపింపజేస్తుంది. మల్చ్ సహాయపడుతుంది."},
            'alluvial': {'en': "Splashing from soil spreads spores. Mulch helps.", 'hi': "मिट्टी से छींटे बीजाणुओं को फैलाते हैं। मल्च मदद करता है।", 'kn': "ಮಣ್ಣಿನಿಂದ ಸ್ಪ್ಲಾಶಿಂಗ್ ಬೀಜಕಗಳನ್ನು ಹರಡುತ್ತದೆ. ಮಲ್ಚ್ ಸಹಾಯ ಮಾಡುತ್ತದೆ.", 'te': "మట్టి నుండి స్ప్లాషింగ్ బీజాంశాలను వ్యాపింపజేస్తుంది. మల్చ్ సహాయపడుతుంది."},
            'general': {'en': "Fungus survives in crop debris in the soil. Splashing rain from the soil is a primary way it spreads. Mulch is very helpful.", 'hi': "कवक मिट्टी में फसल के मलबे में जीवित रहता है। मिट्टी से बारिश के छींटे इसके फैलने का एक प्राथमिक तरीका है। मल्च बहुत मददगार है।", 'kn': "ಶಿಲೀಂಧ್ರವು ಮಣ್ಣಿನಲ್ಲಿ ಬೆಳೆ ಅವಶೇಷಗಳಲ್ಲಿ ಬದುಕುಳಿಯುತ್ತದೆ. ಮಣ್ಣಿನಿಂದ ಮಳೆ ಸ್ಪ್ಲಾಶಿಂಗ್ ಇದು ಹರಡುವ ಪ್ರಾಥಮಿಕ ಮಾರ್ಗವಾಗಿದೆ. ಮಲ್ಚ್ ತುಂಬಾ ಸಹಾಯಕವಾಗಿದೆ.", 'te': "శిలీంధ్రం నేలలో పంట వ్యర్థాలలో జీవిస్తుంది. మట్టి నుండి వర్షం స్ప్లాషింగ్ ఇది వ్యాప్తి చెందడానికి ప్రాథమిక మార్గం. మల్చ్ చాలా సహాయకారిగా ఉంటుంది."}
        },
        'seasons': {
            'monsoon': {'en': "High risk during monsoon / early rainy season due to rain splash.", 'hi': "बारिश के छींटों के कारण मानसून / शुरुआती बरसात के मौसम में उच्च जोखिम।", 'kn': "ಮಳೆಗಾಲ / ಆರಂಭಿಕ ಮಳೆಗಾಲದಲ್ಲಿ ಮಳೆ ಸ್ಪ್ಲಾಶ್‌ನಿಂದಾಗಿ ಹೆಚ್ಚಿನ ಅಪಾಯ.", 'te': "వర్షాకాలం / ప్రారంభ వర్షాకాలంలో వర్షం స్ప్లాష్ కారణంగా అధిక ప్రమాదం."},
            'summer': {'en': "Can be spread by overhead irrigation.", 'hi': "ओवरहेड सिंचाई से फैल सकता है।", 'kn': "ಓವರ್ಹೆಡ್ ನೀರಾವರಿಯಿಂದ ಹರಡಬಹುದು.", 'te': "ఓవర్హెడ్ ఇరిగేషన్ ద్వారా వ్యాపించవచ్చు."},
            'winter': {'en': "Low risk. Clean up debris.", 'hi': "कम जोखिम। मलबे को साफ करें।", 'kn': "ಕಡಿಮೆ ಅಪಾಯ. ಅವಶೇಷಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", 'te': "తక్కువ ప్రమాదం. వ్యర్థాలను శుభ్రం చేయండి."},
            'general': {'en': "Warm, wet, and humid weather favors the disease.", 'hi': "गर्म, गीला और आर्द्र मौसम रोग को बढ़ावा देता है।", 'kn': "ಬೆಚ್ಚಗಿನ, ಆರ್ದ್ರ ಮತ್ತು ತೇವಾಂಶವುಳ್ಳ ವಾತಾವರಣವು ರೋಗಕ್ಕೆ ಅನುಕೂಲಕರವಾಗಿದೆ.", 'te': "వెచ్చని, తడి మరియు తేమతో కూడిన వాతావరణం వ్యాధికి అనుకూలంగా ఉంటుంది."}
        },
        'action_plan': {
            'cultural': {'en': "Remove and destroy infected debris. Space plants for airflow. Use mulch (straw or plastic) to prevent soil splash. Prune lower leaves.", 'hi': "संक्रमित मलबे को हटा दें और नष्ट कर दें। वायु प्रवाह के लिए पौधों को जगह दें। मिट्टी के छींटों को रोकने के लिए मल्च (पुआल या प्लास्टिक) का उपयोग करें। निचली पत्तियों की छंटाई करें।", 'kn': "ಸೋಂಕಿತ ಅವಶೇಷಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ನಾಶಮಾಡಿ. ಗಾಳಿಯ ಹರಿವಿಗಾಗಿ ಸಸ್ಯಗಳಿಗೆ ಜಾಗ ನೀಡಿ. ಮಣ್ಣಿನ ಸ್ಪ್ಲಾಶ್ ಅನ್ನು ತಡೆಗಟ್ಟಲು ಮಲ್ಚ್ (ಒಣಹುಲ್ಲಿನ ಅಥವಾ ಪ್ಲಾಸ್ಟಿಕ್) ಬಳಸಿ. ಕೆಳಗಿನ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ.", 'te': "సోకిన వ్యర్థాలను తొలగించి నాశనం చేయండి. గాలి ప్రవాహం కోసం మొక్కలకు స్థలం ఇవ్వండి. మట్టి స్ప్లాష్‌ను నివారించడానికి మల్చ్ (గడ్డి లేదా ప్లాస్టిక్) ఉపయోగించండి. దిగువ ఆకులను కత్తిరించండి."},
            'organic': {'en': "Copper-based sprays.", 'hi': "तांबे पर आधारित स्प्रे।", 'kn': "ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳು.", 'te': "రాగి ఆధారిత స్ప్రేలు."},
            'chemical': {'en': "Mancozeb 0.2–0.25% or Chlorothalonil. Interval: Repeat every 7–10 days in rainy weather.", 'hi': "मैनकोजेब 0.2–0.25% या क्लोरोथालोनिल। अंतराल: बरसात के मौसम में हर 7-10 दिनों में दोहराएं।", 'kn': "ಮ್ಯಾಂಕೋಜೆಬ್ 0.2–0.25% ಅಥವಾ ಕ್ಲೋರೊಥಾಲೋನಿಲ್. ಮಧ್ಯಂತರ: ಮಳೆಯ ವಾತಾವರಣದಲ್ಲಿ ಪ್ರತಿ 7-10 ದಿನಗಳಿಗೊಮ್ಮೆ ಪುನರಾವರ್ತಿಸಿ.", 'te': "మాంకోజెబ్ 0.2–0.25% లేదా క్లోరోథలోనిల్. విరామం: వర్షపు వాతావరణంలో ప్రతి 7-10 రోజులకు పునరావృతం చేయండి."}
        }
    },
    'Tomato___Spider_mites_Two-spotted_spider_mite': {
        'soils': {
            'red': {'en': "Dry, dusty conditions from red soil can favor mites.", 'hi': "लाल मिट्टी से सूखी, धूल भरी स्थितियां माइट्स के लिए अनुकूल हो सकती हैं।", 'kn': "ಕೆಂಪು ಮಣ್ಣಿನಿಂದ ಒಣ, ಧೂಳಿನ ಪರಿಸ್ಥಿತಿಗಳು ಮಿಟೆಗಳಿಗೆ ಅನುಕೂಲಕರವಾಗಿರುತ್ತದೆ.", 'te': "ఎర్ర నేల నుండి పొడి, ధూళి పరిస్థితులు మైట్లకు అనుకూలంగా ఉంటాయి."},
            'black': {'en': "Dry, dusty conditions can favor mites.", 'hi': "शुष्क, धूल भरी स्थितियां माइट्स के लिए अनुकूल हो सकती हैं।", 'kn': "ಒಣ, ಧೂಳಿನ ಪರಿಸ್ಥಿತಿಗಳು ಮಿಟೆಗಳಿಗೆ ಅನುಕೂಲಕರವಾಗಿರುತ್ತದೆ.", 'te': "పొడి, ధూళి పరిస్థితులు మైట్లకు అనుకూలంగా ఉంటాయి."},
            'alluvial': {'en': "Dry, dusty conditions can favor mites.", 'hi': "शुष्क, धूल भरी स्थितियां माइट्स के लिए अनुकूल हो सकती हैं।", 'kn': "ಒಣ, ಧೂಳಿನ ಪರಿಸ್Dತಿಗಳು ಮಿಟೆಗಳಿಗೆ ಅನುಕೂಲಕರವಾಗಿರುತ್ತದೆ.", 'te': "పొడి, ధూళి పరిస్థితులు మైట్లకు అనుకూలంగా ఉంటాయి."},
            'general': {'en': "Dry, dusty conditions in any soil type favor mites. Drought-stressed plants are more susceptible.", 'hi': "किसी भी प्रकार की मिट्टी में शुष्क, धूल भरी स्थितियां माइट्स के लिए अनुकूल होती हैं। सूखे से तनावग्रस्त पौधे अधिक संवेदनशील होते हैं।", 'kn': "ಯಾವುದೇ ರೀತಿಯ ಮಣ್ಣಿನಲ್ಲಿ ಒಣ, ಧೂಳಿನ ಪರಿಸ್ಥಿತಿಗಳು ಮಿಟೆಗಳಿಗೆ ಅನುಕೂಲಕರವಾಗಿವೆ. ಬರ-ಒತ್ತಡದ ಸಸ್ಯಗಳು ಹೆಚ್ಚು ಒಳಗಾಗುತ್ತವೆ.", 'te': "ఏ రకమైన నేలలోనైనా పొడి, ధూళి పరిస్థితులు మైట్లకు అనుకూలంగా ఉంటాయి. కరువు-ఒత్తిడికి గురైన మొక్కలు ఎక్కువగా వ్యాధి బారిన పడతాయి."}
        },
        'seasons': {
            'monsoon': {'en': "Low risk. Rain and high humidity naturally suppress mite populations.", 'hi': "कम जोखिम। बारिश और उच्च आर्द्रता स्वाभाविक रूप से माइट आबादी को दबा देती है।", 'kn': "ಕಡಿಮೆ ಅಪಾಯ. ಮಳೆ ಮತ್ತು ಹೆಚ್ಚಿನ ಆರ್ದ್ರತೆಯು ಮಿಟೆ ಜನಸಂಖ್ಯೆಯನ್ನು ನೈಸರ್ಗಿಕವಾಗಿ ನಿಗ್ರಹಿಸುತ್ತದೆ.", 'te': "తక్కువ ప్రమాదం. వర్షం మరియు అధిక తేమ సహజంగా మైట్ జనాభాను అణిచివేస్తాయి."},
            'summer': {'en': "HIGH RISK. Mites thrive in hot, dry summer conditions.", 'hi': "उच्च जोखिम। माइट्स गर्म, शुष्क गर्मियों की स्थितियों में पनपते हैं।", 'kn': "ಹೆಚ್ಚಿನ ಅಪಾಯ. ಬಿಸಿ, ಒಣ ಬೇಸಿಗೆಯ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಮಿಟೆಗಳು ಬೆಳೆಯುತ್ತವೆ.", 'te': "అధిక ప్రమాదం. మైట్స్ వేడి, పొడి వేసవి పరిస్థితులలో వృద్ధి చెందుతాయి."},
            'winter': {'en': "Can be a problem in protected cultivation (greenhouses) or dry winters.", 'hi': "संरक्षित खेती (ग्रीनहाउस) या शुष्क सर्दियों में समस्या हो सकती है।", 'kn': "ಸಂರಕ್ಷಿತ ಕೃಷಿ (ಹಸಿರುಮನೆಗಳು) ಅಥವಾ ಒಣ ಚಳಿಗಾಲದಲ್ಲಿ ಸಮಸ್ಯೆಯಾಗಬಹುದು.", 'te': "రక్షిత సాగు (గ్రీన్‌హౌస్‌లు) లేదా పొడి శీతాకాలంలో సమస్య కావచ్చు."},
            'general': {'en': "Hot, dry, and dusty conditions are ideal for spider mites.", 'hi': "गर्म, शुष्क और धूल भरी स्थितियां स्पाइडर माइट्स के लिए आदर्श होती हैं।", 'kn': "ಬಿಸಿ, ಒಣ ಮತ್ತು ಧೂಳಿನ ಪರಿಸ್ಥಿತಿಗಳು ಜೇಡ ಮಿಟೆಗಳಿಗೆ ಸೂಕ್ತವಾಗಿವೆ.", 'te': "వేడి, పొడి మరియు ధూళి పరిస్థితులు స్పైడర్ మైట్లకు అనువైనవి."}
        },
        'action_plan': {
            'cultural': {'en': "Increase humidity by spraying foliage with water (this can increase fungal risk, so be careful). Avoid dust buildup. Scout for mites (look for fine webbing on undersides of leaves).", 'hi': "पत्तियों पर पानी का छिड़काव करके आर्द्रता बढ़ाएँ (इससे फंगल जोखिम बढ़ सकता है, इसलिए सावधान रहें)। धूल जमने से बचें। माइट्स के लिए स्काउट (पत्तियों के नीचे की तरफ महीन बद्धी की तलाश करें)।", 'kn': "ಎಲೆಗಳ ಮೇಲೆ ನೀರನ್ನು ಸಿಂಪಡಿಸುವ ಮೂಲಕ ತೇವಾಂಶವನ್ನು ಹೆಚ್ಚಿಸಿ (ಇದು ಶಿಲೀಂಧ್ರಗಳ ಅಪಾಯವನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ, ಆದ್ದರಿಂದ ಜಾಗರೂಕರಾಗಿರಿ). ಧೂಳು ಸಂಗ್ರಹವಾಗುವುದನ್ನು ತಪ್ಪಿಸಿ. ಮಿಟೆಗಳಿಗಾಗಿ ಸ್ಕೌಟ್ (ಎಲೆಗಳ ಕೆಳಭಾಗದಲ್ಲಿ ಸೂಕ್ಷ್ಮವಾದ ಜಾಲವನ್ನು ನೋಡಿ).", 'te': "ఆకులపై నీటిని చల్లడం ద్వారా తేమను పెంచండి (ఇది ఫంగల్ ప్రమాదాన్ని పెంచుతుంది, కాబట్టి జాగ్రత్తగా ఉండండి). దుమ్ము పేరుకుపోకుండా ఉండండి. మైట్స్ కోసం స్కౌట్ (ఆకుల అడుగు భాగంలో చక్కటి వెబ్బింగ్ కోసం చూడండి)."},
            'organic': {'en': "Neem oil or horticultural oil sprays (ensure good coverage, especially under leaves). Release predatory mites (Phytoseiulus persimilis) if available.", 'hi': "नीम का तेल या बागवानी तेल स्प्रे (अच्छा कवरेज सुनिश्चित करें, खासकर पत्तियों के नीचे)। यदि उपलब्ध हो तो शिकारी माइट्स (फाइटोसेलस पर्सिमिलिस) छोड़ें।", 'kn': "ಬೇವಿನ ಎಣ್ಣೆ ಅಥವಾ ತೋಟಗಾರಿಕಾ ತೈಲ ಸ್ಪ್ರೇಗಳು (ವಿಶೇಷವಾಗಿ ಎಲೆಗಳ ಕೆಳಗೆ ಉತ್ತಮ ವ್ಯಾಪ್ತಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ). ಲಭ್ಯವಿದ್ದರೆ ಪರಭಕ್ಷಕ ಮಿಟೆಗಳನ್ನು (ಫೈಟೊಸೆಯುಲಸ್ ಪರ್ಸಿಮಿಲಿಸ್) ಬಿಡುಗಡೆ ಮಾಡಿ.", 'te': "వేప నూనె లేదా హార్టికల్చరల్ ఆయిల్ స్ప్రేలు (ముఖ్యంగా ఆకుల కింద మంచి కవరేజీని నిర్ధారించుకోండి). అందుబాటులో ఉంటే ప్రిడేటరీ మైట్స్ (ఫైటోసియులస్ పెర్సిమిలిస్) ను విడుదల చేయండి."},
            'chemical': {'en': "Use a specific ACARICIDE (miticide), not a general insecticide. Active ingredients include Abamectin, Fenpyroximate, or Spiromesifen. Follow label for rates. Interval: Apply when mites are first detected. Repeat per label and ALWAYS rotate modes of action as mites develop resistance very quickly.", 'hi': "एक सामान्य कीटनाशक नहीं, बल्कि एक विशिष्ट ACARICIDE (माइटिसाइड) का उपयोग करें। सक्रिय अवयवों में एबामेक्टिन, फेनपायरोक्सिमेट, या स्पिरोमेसिफेन शामिल हैं। दरों के लिए लेबल का पालन करें। अंतराल: जब माइट्स का पहली बार पता चले तब लागू करें। प्रति लेबल दोहराएं और हमेशा कार्रवाई के तरीकों को घुमाएं क्योंकि माइट्स बहुत जल्दी प्रतिरोध विकसित करते हैं।", 'kn': "ಸಾಮಾನ್ಯ ಕೀಟನಾಶಕವಲ್ಲ, ನಿರ್ದಿಷ್ಟ ACARICIDE (ಮೈಟಿಸೈಡ್) ಬಳಸಿ. ಸಕ್ರಿಯ ಪದಾರ್ಥಗಳು ಅಬಾಮೆಕ್ಟಿನ್, ಫೆನ್ಪೈರಾಕ್ಸಿಮೇಟ್, ಅಥವಾ ಸ್ಪಿರೋಮೆಸಿಫೆನ್ ಅನ್ನು ಒಳಗೊಂಡಿವೆ. ದರಗಳಿಗಾಗಿ ಲೇಬಲ್ ಅನ್ನು ಅನುಸರಿಸಿ. ಮಧ್ಯಂತರ: ಮಿಟೆಗಳು ಮೊದಲು ಪತ್ತೆಯಾದಾಗ ಅನ್ವಯಿಸಿ. ಪ್ರತಿ ಲೇಬಲ್‌ಗೆ ಪುನರಾವರ್ತಿಸಿ ಮತ್ತು ಮಿಟೆಗಳು ಬೇಗನೆ ಪ್ರತಿರೋಧವನ್ನು ಬೆಳೆಸಿಕೊಳ್ಳುವುದರಿಂದ ಕ್ರಿಯೆಯ ವಿಧಾನಗಳನ್ನು ಯಾವಾಗಲೂ ತಿರುಗಿಸಿ.", 'te': "సాధారణ పురుగుమందు కాదు, నిర్దిష్ట ACARICIDE (మైటిసైడ్) ఉపయోగించండి. క్రియాశీల పదార్ధాలలో అబామెక్టిన్, ఫెన్‌పైరాక్సిమేట్ లేదా స్పిరోమెసిఫెన్ ఉన్నాయి. రేట్ల కోసం లేబుల్‌ను అనుసరించండి. విరామం: మైట్స్ మొదట కనుగొనబడినప్పుడు వర్తించండి. ప్రతి లేబుల్‌కు పునరావృతం చేయండి మరియు మైట్స్ చాలా త్వరగా నిరోధకతను పెంచుతాయి కాబట్టి ఎల్లప్పుడూ చర్య యొక్క మోడ్‌లను తిప్పండి."}
        }
    },
    'Tomato___Target_spot': {
        'soils': {
            'general': {'en': "Fungus survives in crop residue. Moist environments and soils rich in undecomposed organic matter promote the disease.", 'hi': "कवक फसल अवशेषों में जीवित रहता है। नम वातावरण और विघटित न हुए जैविक पदार्थ से भरपूर मिट्टी रोग को बढ़ावा देती है।", 'kn': "ಶಿಲೀಂಧ್ರವು ಬೆಳೆ ಉಳಿಕೆಗಳಲ್ಲಿ ಬದುಕುಳಿಯುತ್ತದೆ. ತೇವಾಂಶವುಳ್ಳ ಪರಿಸರಗಳು ಮತ್ತು ವಿಘಟಿತಗೊಳ್ಳದ ಸಾವಯವ ಪದಾರ್ಥಗಳಿಂದ ಸಮೃದ್ಧವಾಗಿರುವ ಮಣ್ಣು ರೋಗವನ್ನು ಉತ್ತೇಜಿಸುತ್ತದೆ.", 'te': "శిలీంధ్రం పంట అవశేషాలలో జీవిస్తుంది. తేమతో కూడిన వాతావరణం మరియు కుళ్ళిపోని సేంద్రియ పదార్థంతో కూడిన నేలలు వ్యాధిని ప్రోత్సహిస్తాయి."}
        },
        'seasons': {
            'monsoon': {'en': "High risk during late rainy season and high-humidity periods.", 'hi': "देर से बरसात के मौसम और उच्च आर्द्रता वाले समय के दौरान उच्च जोखिम।", 'kn': "ಮಳೆಗಾಲದ ಕೊನೆಯಲ್ಲಿ ಮತ್ತು ಹೆಚ್ಚಿನ ತೇವಾಂಶದ ಅವಧಿಗಳಲ್ಲಿ ಹೆಚ್ಚಿನ ಅಪಾಯ.", 'te': "ఆలస్యంగా వర్షాకాలం మరియు అధిక తేమ ఉన్న కాలంలో అధిక ప్రమాదం."},
            'summer': {'en': "Can occur in warm, humid, irrigated fields.", 'hi': "गर्म, आर्द्र, सिंचित खेतों में हो सकता है।", 'kn': "ಬೆಚ್ಚಗಿನ, ತೇವಾಂಶವುಳ್ಳ, ನೀರಾವರಿ ಹೊಲಗಳಲ್ಲಿ ಸಂಭವಿಸಬಹುದು.", 'te': "వెచ్చని, తేమతో కూడిన, నీటిపారుదల పొలాలలో సంభవించవచ్చు."},
            'winter': {'en': "Low risk. Clean up debris.", 'hi': "कम जोखिम। मलबे को साफ करें।", 'kn': "ಕಡಿಮೆ ಅಪಾಯ. ಅವಶೇಷಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ.", 'te': "తక్కువ ప్రమాదం. వ్యర్థాలను శుభ్రం చేయండి."},
            'general': {'en': "Warm, moist, and humid conditions favor the disease.", 'hi': "गर्म, नम और आर्द्र स्थितियां रोग को बढ़ावा देती हैं।", 'kn': "ಬೆಚ್ಚಗಿನ, ತೇವಾಂಶ ಮತ್ತು ತೇವಾಂಶವುಳ್ಳ ಪರಿಸ್ಥಿತಿಗಳು ರೋಗಕ್ಕೆ ಅನುಕೂಲಕರವಾಗಿವೆ.", 'te': "వెచ్చని, తడి మరియు తేమతో కూడిన పరిస్థితులు వ్యాధికి అనుకూలంగా ఉంటాయి."}
        },
        'action_plan': {
            'cultural': {'en': "Remove and destroy plant debris. Avoid overhead irrigation. Prune for airflow.", 'hi': "पौधे के मलबे को हटा दें और नष्ट कर दें। ओवरहेड सिंचाई से बचें। वायु प्रवाह के लिए छंटाई करें।", 'kn': "ಸಸ್ಯದ ಅವಶೇಷಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ನಾಶಮಾಡಿ. ಓವರ್ಹೆಡ್ ನೀರಾವರಿಯನ್ನು ತಪ್ಪಿಸಿ. ಗಾಳಿಯ ಹರಿವಿಗಾಗಿ ಕತ್ತರಿಸಿ.", 'te': "మొక్కల వ్యర్థాలను తొలగించి నాశనం చేయండి. ఓవర్హెడ్ ఇరిగేషన్‌ను నివారించండి. గాలి ప్రవాహం కోసం కత్తిరించండి."},
            'organic': {'en': "Copper-based sprays.", 'hi': "तांबे पर आधारित स्प्रे।", 'kn': "ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳು.", 'te': "రాగి ఆధారిత స్ప్రేలు."},
            'chemical': {'en': "Mancozeb or Chlorothalonil. Systemic fungicides (azoles or strobilurins) can be used in rotation if the disease is severe.", 'hi': "मैनकोजेब या क्लोरोथालोनिल। यदि रोग गंभीर हो तो प्रणालीगत कवकनाशी (एजोल या स्ट्रोबिलुरिन) का रोटेशन में उपयोग किया जा सकता है।", 'kn': "ಮ್ಯಾಂಕೋಜೆಬ್ ಅಥವಾ ಕ್ಲೋರೊಥಾಲೋನಿಲ್. ರೋಗವು ತೀವ್ರವಾಗಿದ್ದರೆ ವ್ಯವಸ್ಥಿತ ಶಿಲೀಂಧ್ರನಾಶಕಗಳನ್ನು (ಅಜೋಲ್‌ಗಳು ಅಥವಾ ಸ್ಟ್ರೋಬಿಲುರಿನ್‌ಗಳು) ತಿರುಗುವಿಕೆಯಲ್ಲಿ ಬಳಸಬಹುದು.", 'te': "మాంకోజెబ్ లేదా క్లోరోథలోనిల్. వ్యాధి తీవ్రంగా ఉంటే దైహిక శిలీంద్రనాశకాలను (అజోల్స్ లేదా స్ట్రోబిలురిన్స్) భ్రమణంలో ఉపయోగించవచ్చు."}
        }
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'soils': {
            'general': {'en': "Soil type is not a determinant. This is a virus spread by an insect vector (whitefly).", 'hi': "मिट्टी का प्रकार निर्धारक नहीं है। यह एक कीट वेक्टर (व्हाइटफ्लाई) द्वारा फैलने वाला वायरस है।", 'kn': "ಮಣ್ಣಿನ ಪ್ರಕಾರವು ನಿರ್ಣಾಯಕವಲ್ಲ. ಇದು ಕೀಟ ವಾಹಕದಿಂದ (ಬಿಳಿನೊಣ) ಹರಡುವ ವೈರಸ್ ಆಗಿದೆ.", 'te': "నేల రకం నిర్ణయాత్మకమైనది కాదు. ఇది ఒక కీటక వాహకం (తెల్లదోమ) ద్వారా వ్యాపించే వైరస్."}
        },
        'seasons': {
            'summer': {'en': "High risk. The vector (whitefly) thrives in warm, dry seasons.", 'hi': "उच्च जोखिम। वेक्टर (व्हाइटफ्लाई) गर्म, शुष्क मौसमों में पनपता है।", 'kn': "ಹೆಚ್ಚಿನ ಅಪಾಯ. ವಾಹಕ (ಬಿಳಿನೊಣ) ಬೆಚ್ಚಗಿನ, ಒಣ ಋತುಗಳಲ್ಲಿ ಬೆಳೆಯುತ್ತದೆ.", 'te': "అధిక ప్రమాదం. వెక్టర్ (తెల్లదోమ) వెచ్చని, పొడి సీజన్లలో వృద్ధి చెందుతుంది."},
            'monsoon': {'en': "Risk can persist, but whitefly populations may be lower than in dry summer.", 'hi': "जोखिम बना रह सकता है, लेकिन व्हाइटफ्लाई की आबादी शुष्क गर्मियों की तुलना में कम हो सकती है।", 'kn': "ಅಪಾಯವು ಮುಂದುವರಿಯಬಹುದು, ಆದರೆ ಒಣ ಬೇಸಿಗೆಗಿಂತ ಬಿಳಿನೊಣಗಳ ಸಂಖ್ಯೆ ಕಡಿಮೆಯಿರಬಹುದು.", 'te': "ప్రమాదం కొనసాగవచ్చు, కానీ పొడి వేసవి కంటే తెల్లదోమ జనాభా తక్కువగా ఉండవచ్చు."},
            'winter': {'en': "Risk is high in warm winter regions where whiteflies persist.", 'hi': "गर्म सर्दियों वाले क्षेत्रों में जोखिम अधिक होता है जहां व्हाइटफ्लाई बनी रहती है।", 'kn': "ಬಿಳಿನೊಣಗಳು ಮುಂದುವರಿಯುವ ಬೆಚ್ಚಗಿನ ಚಳಿಗಾಲದ ಪ್ರದೇಶಗಳಲ್ಲಿ ಅಪಾಯ ಹೆಚ್ಚು.", 'te': "తెల్లదోమలు నిలిచి ఉండే వెచ్చని శీతాకాల ప్రాంతాల్లో ప్రమాదం ఎక్కువగా ఉంటుంది."},
            'general': {'en': "Risk is highest during warm seasons when whitefly populations are high. Widespread in warm climates.", 'hi': "गर्म मौसमों के दौरान जोखिम सबसे अधिक होता है जब व्हाइटफ्लाई की आबादी अधिक होती है। गर्म जलवायु में व्यापक।", 'kn': "ಬಿಳಿನೊಣಗಳ ಸಂಖ್ಯೆ ಹೆಚ್ಚಿರುವಾಗ ಬೆಚ್ಚಗಿನ ಋತುಗಳಲ್ಲಿ ಅಪಾಯ ಹೆಚ್ಚಾಗಿರುತ್ತದೆ. ಬೆಚ್ಚಗಿನ ವಾತಾವರಣದಲ್ಲಿ ವ್ಯಾಪಕವಾಗಿದೆ.", 'te': "తెల్లదోమల జనాభా ఎక్కువగా ఉన్నప్పుడు వెచ్చని సీజన్లలో ప్రమాదం ఎక్కువగా ఉంటుంది. వెచ్చని వాతావరణంలో విస్తృతంగా వ్యాపించింది."}
        },
        'action_plan': {
            'cultural': {'en': "THIS IS A VIRUS - NO CURE. Focus on prevention. 1) Use resistant/tolerant varieties (crucial!). 2) Use reflective mulches (e.g., silver plastic) to deter whiteflies. 3) Remove and destroy infected plants immediately to reduce spread.", 'hi': "यह एक वायरस है - कोई इलाज नहीं। रोकथाम पर ध्यान दें। 1) प्रतिरोधी/सहिष्णु किस्मों (महत्वपूर्ण!) का उपयोग करें। 2) व्हाइटफ्लाई को रोकने के लिए परावर्तक मल्च (जैसे, चांदी का प्लास्टिक) का उपयोग करें। 3) प्रसार को कम करने के लिए संक्रमित पौधों को तुरंत हटा दें और नष्ट कर दें।", 'kn': "ಇದು ವೈರಸ್ - ಚಿಕಿತ್ಸೆ ಇಲ್ಲ. ತಡೆಗಟ್ಟುವಿಕೆಯ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಿ. 1) ನಿರೋಧಕ/ಸಹಿಷ್ಣು ಪ್ರಭೇದಗಳನ್ನು (ನಿರ್ಣಾಯಕ!) ಬಳಸಿ. 2) ಬಿಳಿನೊಣಗಳನ್ನು ತಡೆಯಲು ಪ್ರತಿಫಲಿತ ಮಲ್ಚ್‌ಗಳನ್ನು (ಉದಾ., ಬೆಳ್ಳಿ ಪ್ಲಾಸ್ಟಿಕ್) ಬಳಸಿ. 3) ಹರಡುವುದನ್ನು ಕಡಿಮೆ ಮಾಡಲು ಸೋಂಕಿತ ಸಸ್ಯಗಳನ್ನು ತಕ್ಷಣವೇ ತೆಗೆದುಹಾಕಿ ಮತ್ತು ನಾಶಮಾಡಿ.", 'te': "ఇది వైరస్ - నివారణ లేదు. నివారణపై దృష్టి పెట్టండి. 1) నిరోధక/సహన రకాలను (కీలకం!) వాడండి. 2) తెల్లదోమలను నిరోధించడానికి ప్రతిబింబ మల్చ్‌లను (ఉదా., వెండి ప్లాస్టిక్) వాడండి. 3) వ్యాప్తిని తగ్గించడానికి సోకిన మొక్కలను వెంటనే తొలగించి నాశనం చేయండి."},
            'organic': {'en': "Vector control: Use yellow sticky traps to monitor and catch whiteflies. Neem oil can deter whiteflies. Release biologicals (Encarsia formosa) where applicable.", 'hi': "वेक्टर नियंत्रण: व्हाइटफ्लाई की निगरानी और पकड़ने के लिए पीले चिपचिपे जाल का उपयोग करें। नीम का तेल व्हाइटफ्लाई को रोक सकता है। जहां लागू हो वहां जैविक (एनकार्सिया फॉर्मोसा) छोड़ें।", 'kn': "ವೆಕ್ಟರ್ ನಿಯಂತ್ರಣ: ಬಿಳಿನೊಣಗಳನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಲು ಮತ್ತು ಹಿಡಿಯಲು ಹಳದಿ ಜಿಗುಟಾದ ಬಲೆಗಳನ್ನು ಬಳಸಿ. ಬೇವಿನ ಎಣ್ಣೆಯು ಬಿಳಿನೊಣಗಳನ್ನು ತಡೆಯುತ್ತದೆ. ಅನ್ವಯವಾಗುವಲ್ಲಿ ಜೈವಿಕಗಳನ್ನು (ಎಂಕಾರ್ಸಿಯಾ ಫಾರ್ಮೋಸಾ) ಬಿಡುಗಡೆ ಮಾಡಿ.", 'te': "వెక్టర్ నియంత్రణ: తెల్లదోమలను పర్యవేక్షించడానికి మరియు పట్టుకోవడానికి పసుపు జిగట ఉచ్చులను వాడండి. వేప నూనె తెల్లదోమలను నిరోధిస్తుంది. వర్తించే చోట జీవసంబంధమైన (ఎంకార్సియా ఫార్మోసా) విడుదల చేయండి."},
            'chemical': {'en': "VECTOR CONTROL. Control the whitefly population. Use appropriate insecticides like Lambda-cyhalothrin or Spirotetramat, following the label. Follow IPM principles and rotate modes of action to prevent insecticide resistance.", 'hi': "वेक्टर नियंत्रण। व्हाइटफ्लाई आबादी को नियंत्रित करें। लैम्ब्डा-साइहेलोथ्रिन या स्पिरोटेट्रामैट जैसे उपयुक्त कीटनाशकों का उपयोग करें, लेबल का पालन करें। IPM सिद्धांतों का पालन करें और कीटनाशक प्रतिरोध को रोकने के लिए कार्रवाई के तरीकों को घुमाएं।", 'kn': "ವೆಕ್ಟರ್ ನಿಯಂತ್ರಣ. ಬಿಳಿನೊಣಗಳ ಸಂಖ್ಯೆಯನ್ನು ನಿಯಂತ್ರಿಸಿ. ಲ್ಯಾಂಬ್ಡಾ-ಸೈಹಲೋಥ್ರಿನ್ ಅಥವಾ ಸ್ಪಿರೋಟೆಟ್ರಾಮಾಟ್‌ನಂತಹ ಸೂಕ್ತವಾದ ಕೀಟನಾಶಕಗಳನ್ನು ಬಳಸಿ, ಲೇಬಲ್ ಅನ್ನು ಅನುಸರಿಸಿ. IPM ತತ್ವಗಳನ್ನು ಅನುಸರಿಸಿ ಮತ್ತು ಕೀಟನಾಶಕ ನಿರೋಧಕತೆಯನ್ನು ತಡೆಗಟ್ಟಲು ಕ್ರಿಯೆಯ ವಿಧಾನಗಳನ್ನು ತಿರುಗಿಸಿ.", 'te': "వెక్టర్ నియంత్రణ. తెల్లదోమ జనాభాను నియంత్రించండి. లాంబ్డా-సైహలోథ్రిన్ లేదా స్పిరోటెట్రామాట్ వంటి తగిన పురుగుమందులను వాడండి, లేబుల్‌ను అనుసరించండి. IPM సూత్రాలను అనుసరించండి మరియు పురుగుమందుల నిరోధకతను నివారించడానికి చర్య యొక్క మోడ్‌లను తిప్పండి."}
        }
    },
    'Tomato___Tomato_mosaic_virus': {
        'soils': {
            'general': {'en': "Soil is not a primary source. This virus is spread mechanically (on hands, tools) and can be seed-borne.", 'hi': "मिट्टी प्राथमिक स्रोत नहीं है। यह वायरस यांत्रिक रूप से (हाथों, औजारों पर) फैलता है और बीज जनित हो सकता है।", 'kn': "ಮಣ್ಣು ಪ್ರಾಥಮಿಕ ಮೂಲವಲ್ಲ. ಈ ವೈರಸ್ ಯಾಂತ್ರಿಕವಾಗಿ (ಕೈಗಳು, ಉಪಕರಣಗಳ ಮೇಲೆ) ಹರಡುತ್ತದೆ ಮತ್ತು ಬೀಜ-ಹರಡಬಹುದು.", 'te': "నేల ప్రాథమిక మూలం కాదు. ఈ వైరస్ యాంత్రికంగా (చేతులు, ఉపకరణాలపై) వ్యాపిస్తుంది మరియు విత్తనం ద్వారా సంక్రమించవచ్చు."}
        },
        'seasons': {
            'general': {'en': "Can be present year-round. Outbreaks are related to handling plants (transplanting, pruning, tying), not season.", 'hi': "साल भर मौजूद रह सकता है। प्रकोप मौसम से नहीं, बल्कि पौधों को संभालने (प्रत्यारोपण, छंटाई, बांधने) से संबंधित हैं।", 'kn': "ವರ್ಷಪೂರ್ತಿ ಇರಬಹುದು. ಏಕಾಏಕಿ ಋತುವಿಗೆ ಸಂಬಂಧಿಸಿಲ್ಲ, ಆದರೆ ಸಸ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವುದಕ್ಕೆ (ಕಸಿ, ಸಮರುವಿಕೆ, ಕಟ್ಟುವುದು) ಸಂಬಂಧಿಸಿದೆ.", 'te': "ఏడాది పొడవునా ఉండవచ్చు. వ్యాప్తి సీజన్‌కు సంబంధించినది కాదు, కానీ మొక్కలను నిర్వహించడం (నాటడం, కత్తిరింపు, కట్టడం)కు సంబంధించినది."}
        },
        'action_plan': {
            'cultural': {'en': "THIS IS A VIRUS - NO CURE. 1) Use certified, disease-free seed. 2) Sanitize tools (with bleach or milk) and hands between working on different plants. 3) Rogue out and destroy infected plants. 4) CRITICAL: Avoid tobacco use (smoking, chewing) when handling plants, as tobacco mosaic virus (a related virus) can easily transmit to tomatoes.", 'hi': "यह एक वायरस है - कोई इलाज नहीं। 1) प्रमाणित, रोग मुक्त बीज का उपयोग करें। 2) विभिन्न पौधों पर काम करने के बीच औजारों (ब्लीच या दूध के साथ) और हाथों को सैनिटाइज करें। 3) संक्रमित पौधों को बाहर निकालें और नष्ट कर दें। 4) महत्वपूर्ण: पौधों को संभालते समय तंबाकू (धूम्रपान, चबाना) के उपयोग से बचें, क्योंकि तंबाकू मोज़ेक वायरस (एक संबंधित वायरस) आसानी से टमाटर में फैल सकता है।", 'kn': "ಇದು ವೈರಸ್ - ಚಿಕಿತ್ಸೆ ಇಲ್ಲ. 1) ಪ್ರಮಾಣೀಕೃತ, ರೋಗ-ಮುಕ್ತ ಬೀಜವನ್ನು ಬಳಸಿ. 2) ವಿವಿಧ ಸಸ್ಯಗಳ ಮೇಲೆ ಕೆಲಸ ಮಾಡುವ ನಡುವೆ ಉಪಕರಣಗಳನ್ನು (ಬ್ಲೀಚ್ ಅಥವಾ ಹಾಲಿನೊಂದಿಗೆ) ಮತ್ತು ಕೈಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ. 3) ಸೋಂಕಿತ ಸಸ್ಯಗಳನ್ನು ಹೊರಹಾಕಿ ಮತ್ತು ನಾಶಮಾಡಿ. 4) ನಿರ್ಣಾಯಕ: ಸಸ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವಾಗ ತಂಬಾಕು (ಧೂಮಪಾನ, ಅಗಿಯುವುದು) ಬಳಕೆಯನ್ನು ತಪ್ಪಿಸಿ, ಏಕೆಂದರೆ ತಂಬಾಕು ಮೊಸಾಯಿಕ್ ವೈರಸ್ (ಸಂಬಂಧಿತ ವೈರಸ್) ಟೊಮೆಟೊಗಳಿಗೆ ಸುಲಭವಾಗಿ ಹರಡುತ್ತದೆ.", 'te': "ఇది వైరస్ - నివారణ లేదు. 1) ధృవీకరించబడిన, వ్యాధి రహిత విత్తనాన్ని వాడండి. 2) వివిధ మొక్కలపై పనిచేసేటప్పుడు సాధనాలను (బ్లీచ్ లేదా పాలతో) మరియు చేతులను శుభ్రపరచండి. 3) సోకిన మొక్కలను బయటకు తీసి నాశనం చేయండి. 4) కీలకం: మొక్కలను నిర్వహించేటప్పుడు పొగాకు (ధూమపానం, నమలడం) వాడకాన్ని నివారించండి, ఎందుకంటే పొగాకు మొజాయిక్ వైరస్ (సంబంధిత వైరస్) టమోటాలకు సులభంగా వ్యాపిస్తుంది."},
            'organic': {'en': "Focus entirely on sanitation and resistant varieties.", 'hi': "पूरी तरह से स्वच्छता और प्रतिरोधी किस्मों पर ध्यान दें।", 'kn': "ನೈರ್ಮಲ್ಯ ಮತ್ತು ನಿರೋಧಕ ಪ್ರಭೇದಗಳ ಮೇಲೆ ಸಂಪೂರ್ಣವಾಗಿ ಕೇಂದ್ರೀಕರಿಸಿ.", 'te': "పారిశుధ్యం మరియు నిరోధక రకాలపై పూర్తిగా దృష్టి పెట్టండి."},
            'chemical': {'en': "No chemical cure. Control insect vectors (like aphids) if they are involved in spreading other viruses, but ToMV is mainly mechanical.", 'hi': "कोई रासायनिक इलाज नहीं। यदि वे अन्य वायरस फैलाने में शामिल हों तो कीट वैक्टर (जैसे एफिड्स) को नियंत्रित करें, लेकिन ToMV मुख्य रूप से यांत्रिक है।", 'kn': "ಯಾವುದೇ ರಾಸಾಯನಿಕ ಚಿಕಿತ್ಸೆ ಇಲ್ಲ. ಇತರ ವೈರಸ್‌ಗಳನ್ನು ಹರಡುವುದರಲ್ಲಿ ಕೀಟ ವಾಹಕಗಳು (ಅಫಿಡ್‌ಗಳಂತಹ) ಭಾಗಿಯಾಗಿದ್ದರೆ ಅವುಗಳನ್ನು ನಿಯಂತ್ರಿಸಿ, ಆದರೆ ToMV ಮುಖ್ಯವಾಗಿ ಯಾಂತ್ರಿಕವಾಗಿರುತ್ತದೆ.", 'te': "రసాయన నివారణ లేదు. ఇతర వైరస్‌లను వ్యాప్తి చేయడంలో కీటక వాహకాలు (అఫిడ్స్ వంటివి) పాల్గొంటే వాటిని నియంత్రించండి, కానీ ToMV ప్రధానంగా యాంత్రికమైనది."}
        }
    },
    'Tomato___healthy': {
        'soils': {
            'red': {'en': "Red soils are excellent for tomatoes if well-drained and amended with organic matter.", 'hi': "यदि अच्छी जल निकासी हो और जैविक पदार्थ के साथ संशोधित किया गया हो तो लाल मिट्टी टमाटर के लिए उत्कृष्ट है।", 'kn': "ಕೆಂಪು ಮಣ್ಣು ಟೊಮೆಟೊಗಳಿಗೆ ಅತ್ಯುತ್ತಮವಾಗಿದೆ, თუ ಚೆನ್ನಾಗಿ ಬರಿದು ಮತ್ತು ಸಾವಯವ ಪದಾರ್ಥಗಳೊಂದಿಗೆ ತಿದ್ದುಪಡಿ ಮಾಡಲಾಗುತ್ತದೆ.", 'te': "ఎర్ర నేలలు టమోటాలకు అద్భుతమైనవి, మంచి డ్రైనేజీ మరియు సేంద్రియ పదార్థంతో సవరించబడితే."},
            'black': {'en': "Heavy black soil requires raised beds and careful water management to prevent root rot.", 'hi': "भारी काली मिट्टी में जड़ सड़न को रोकने के लिए ऊँची क्यारियों और सावधानीपूर्वक जल प्रबंधन की आवश्यकता होती है।", 'kn': "ಭಾರೀ ಕಪ್ಪು ಮಣ್ಣಿಗೆ ಎತ್ತರದ ಹಾಸಿಗೆಗಳು ಮತ್ತು ಬೇರು ಕೊಳೆಯುವುದನ್ನು ತಡೆಯಲು ಎಚ್ಚರಿಕೆಯ ನೀರಿನ ನಿರ್ವಹಣೆ ಅಗತ್ಯವಿರುತ್ತದೆ.", 'te': "భారీ నల్ల నేలకు రూట్ రాట్‌ను నివారించడానికి ఎత్తైన పడకలు మరియు జాగ్రత్తగా నీటి నిర్వహణ అవసరం."},
            'alluvial': {'en': "Alluvial soils are often ideal, being deep, fertile, and well-drained.", 'hi': "जलोढ़ मिट्टी अक्सर गहरी, उपजाऊ और अच्छी जल निकासी वाली होने के कारण आदर्श होती है।", 'kn': "ಮೆಕ್ಕಲು ಮಣ್ಣು ಆಳವಾದ, ಫಲವತ್ತಾದ ಮತ್ತು ಚೆನ್ನಾಗಿ ಬರಿದಾಗುವುದರಿಂದ ಆದರ್ಶಪ್ರಾಯವಾಗಿದೆ.", 'te': "ఒండ్రు నేలలు తరచుగా లోతైనవి, సారవంతమైనవి మరియు మంచి డ్రైనేజీ కలిగి ఉండటం వలన ఆదర్శంగా ఉంటాయి."},
            'general': {'en': "Tomatoes need deep, well-drained soil rich in organic matter. Use mulch to prevent soil splash and maintain moisture.", 'hi': "टमाटर को जैविक पदार्थ से भरपूर गहरी, अच्छी जल निकासी वाली मिट्टी की आवश्यकता होती है। मिट्टी के छींटों को रोकने और नमी बनाए रखने के लिए मल्च का उपयोग करें।", 'kn': "ಟೊಮೆಟೊಗಳಿಗೆ ಸಾವಯವ ಪದಾರ್ಥಗಳಿಂದ ಸಮೃದ್ಧವಾಗಿರುವ ಆಳವಾದ, ಚೆನ್ನಾಗಿ ಬರಿದಾಗುವ ಮಣ್ಣು ಬೇಕಾಗುತ್ತದೆ. ಮಣ್ಣಿನ ಸ್ಪ್ಲಾಶ್ ಅನ್ನು ತಡೆಗಟ್ಟಲು ಮತ್ತು ತೇವಾಂಶವನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಲು ಮಲ್ಚ್ ಬಳಸಿ.", 'te': "టమోటాలకు సేంద్రియ పదార్థంతో కూడిన లోతైన, మంచి డ్రైనేజీ ఉన్న నేల అవసరం. మట్టి స్ప్లాష్‌ను నివారించడానికి మరియు తేమను నిర్వహించడానికి మల్చ్ ఉపయోగించండి."}
        },
        'seasons': {
            'monsoon': {'en': "High disease pressure. Ensure good airflow and drainage.", 'hi': "उच्च रोग दबाव। अच्छा वायु प्रवाह और जल निकासी सुनिश्चित करें।", 'kn': "ಹೆಚ್ಚಿನ ರೋಗದ ಒತ್ತಡ. ಉತ್ತಮ ಗಾಳಿಯ ಹರಿವು ಮತ್ತು ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.", 'te': "అధిక వ్యాధి ఒత్తిడి. మంచి గాలి ప్రవాహం మరియు డ్రైనేజీని నిర్ధారించుకోండి."},
            'summer': {'en': "A primary growing season, but extreme heat (>35°C) can cause flower drop and poor fruit set.", 'hi': "एक प्राथमिक बढ़ता मौसम, लेकिन अत्यधिक गर्मी (>35°C) फूलों के गिरने और खराब फल लगने का कारण बन सकती है।", 'kn': "ಪ್ರಾಥಮಿಕ ಬೆಳೆಯುವ ಋತು, ಆದರೆ ತೀವ್ರ ಶಾಖ (>35 ° C) ಹೂವು ಬೀಳಲು ಮತ್ತು ಕಳಪೆ ಹಣ್ಣು ಸೆಟ್ಗೆ ಕಾರಣವಾಗಬಹುದು.", 'te': "ప్రాధమిక పెరుగుతున్న కాలం, కానీ తీవ్రమైన వేడి (>35°C) పువ్వులు రాలడానికి మరియు పేలవమైన పండు సెట్‌కు కారణమవుతుంది."},
            'winter': {'en': "A primary growing season in South and Central India. Low disease pressure but sensitive to frost.", 'hi': "दक्षिण और मध्य भारत में एक प्राथमिक बढ़ता मौसम। कम रोग दबाव लेकिन पाले के प्रति संवेदनशील।", 'kn': "ದಕ್ಷಿಣ ಮತ್ತು ಮಧ್ಯ ಭಾರತದಲ್ಲಿ ಪ್ರಾಥಮಿಕ ಬೆಳೆಯುವ ಋತು. ಕಡಿಮೆ ರೋಗದ ಒತ್ತಡ ಆದರೆ ಹಿಮಕ್ಕೆ ಸೂಕ್ಷ್ಮ.", 'te': "దక్షిణ మరియు మధ్య భారతదేశంలో ప్రాథమిక పెరుగుతున్న కాలం. తక్కువ వ్యాధి ఒత్తిడి కానీ మంచుకు సున్నితంగా ఉంటుంది."},
            'general': {'en': "Tomatoes are a warm-season crop, sensitive to frost.", 'hi': "टमाटर गर्म मौसम की फसल है, जो पाले के प्रति संवेदनशील है।", 'kn': "ಟೊಮ್ಯಾಟೊ ಬೆಚ್ಚಗಿನ ಋತುವಿನ ಬೆಳೆಯಾಗಿದ್ದು, ಹಿಮಕ್ಕೆ ಸೂಕ್ಷ್ಮವಾಗಿರುತ್ತದೆ.", 'te': "టమోటాలు వెచ్చని-కాలపు పంట, మంచుకు సున్నితంగా ఉంటాయి."}
        },
        'action_plan': {
            'cultural': {'en': "Use certified seedlings. Rotate crops. Stake or trellis plants. Use drip irrigation and mulch. Prune lower leaves for airflow. Scout regularly.", 'hi': "प्रमाणित अंकुरों का उपयोग करें। फसलें घुमाएँ। पौधों को स्टेक या ट्रेलिस करें। ड्रिप सिंचाई और मल्च का उपयोग करें। वायु प्रवाह के लिए निचली पत्तियों की छंटाई करें। नियमित रूप से स्काउट करें।", 'kn': "ಪ್ರಮಾಣೀಕೃತ ಸಸಿಗಳನ್ನು ಬಳಸಿ. ಬೆಳೆಗಳನ್ನು ತಿರುಗಿಸಿ. ಸಸ್ಯಗಳನ್ನು ಸ್ಟೇಕ್ ಮಾಡಿ ಅಥವಾ ಟ್ರೆಲ್ಲಿಸ್ ಮಾಡಿ. ಹನಿ ನೀರಾವರಿ ಮತ್ತು ಮಲ್ಚ್ ಬಳಸಿ. ಗಾಳಿಯ ಹರಿವಿಗಾಗಿ ಕೆಳಗಿನ ಎಲೆಗಳನ್ನು ಕತ್ತರಿಸಿ. ನಿಯಮಿತವಾಗಿ ಸ್ಕೌಟ್ ಮಾಡಿ.", 'te': "ధృవీకరించబడిన మొలకలను వాడండి. పంటలను మార్చండి. మొక్కలను స్టేక్ చేయండి లేదా ట్రేల్లిస్ చేయండి. డ్రిప్ ఇరిగేషన్ మరియు మల్చ్ ఉపయోగించండి. గాలి ప్రవాహం కోసం దిగువ ఆకులను కత్తిరించండి. క్రమం తప్పకుండా స్కౌట్ చేయండి."},
            'organic': {'en': "Amend soil with rich compost. Use balanced organic fertilizers.", 'hi': "समृद्ध खाद के साथ मिट्टी में संशोधन करें। संतुलित जैविक उर्वरकों का उपयोग करें।", 'kn': "ಸಮೃದ್ಧ ಮಿಶ್ರಗೊಬ್ಬರದೊಂದಿಗೆ ಮಣ್ಣನ್ನು ತಿದ್ದುಪಡಿ ಮಾಡಿ. ಸಮತೋಲಿತ ಸಾವಯವ ಗೊಬ್ಬರಗಳನ್ನು ಬಳಸಿ.", 'te': "సమృద్ధిగా కంపోస్ట్‌తో నేలను సవరించండి. సమతుల్య సేంద్రియ ఎరువులను వాడండి."},
            'chemical': {'en': "No chemical action needed. Focus on preventive monitoring for pests (fruit borer, whitefly) and diseases (blight, leaf curl).", 'hi': "किसी रासायनिक कार्रवाई की आवश्यकता नहीं है। कीटों (फल छेदक, व्हाइटफ्लाई) और रोगों (ब्लाइट, पत्ती कर्ल) के लिए निवारक निगरानी पर ध्यान दें।", 'kn': "ಯಾವುದೇ ರಾಸಾಯನಿಕ ಕ್ರಮ ಅಗತ್ಯವಿಲ್ಲ. ಕೀಟಗಳು (ಹಣ್ಣು ಕೊರೆಯುವ, ಬಿಳಿನೊಣ) ಮತ್ತು ರೋಗಗಳು (ಬ್ಲೈಟ್, ಎಲೆ ಸುರುಳಿ) ಗಾಗಿ ತಡೆಗಟ್ಟುವ ಮೇಲ್ವಿಚಾರಣೆಯ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಿ.", 'te': "రసాయన చర్య అవసరం లేదు. తెగుళ్లు (పండు తొలుచు, తెల్లదోమ) మరియు వ్యాధులు (బ్లైట్, ఆకు ముడత) కోసం నివారణ పర్యవేక్షణపై దృష్టి పెట్టండి."}
        }
    },
# -------------------------
    # RICE (Nutrient Deficiency)
    # -------------------------
    
    # --- CHECK THIS KEY NAME ---
    'Rice___healthy': {
        'soils': {
            'red': {
                'en': "Red soils can be low in organic matter. Ensure balanced NPK and add compost to maintain fertility for healthy rice.",
                'kn': "ಕೆಂಪು ಮಣ್ಣಿನಲ್ಲಿ ಸಾವಯವ ಅಂಶ ಕಡಿಮೆ ಇರಬಹುದು. ಆರೋಗ್ಯಕರ ಅಕ್ಕಿಗಾಗಿ ಸಮತೋಲಿತ NPK ಮತ್ತು ಕಾಂಪೋಸ್ಟ್ ಸೇರಿಸಿ.",
                'te': "ఎర్ర నేలల్లో సేంద్రియ పదార్థం తక్కువగా ఉండవచ్చు. ఆరోగ్యకరమైన బియ్యం కోసం సమతుల్య NPK మరియు కంపోస్ట్ జోడించండి.",
                'hi': "लाल मिट्टी में जैविक पदार्थ कम हो सकते हैं। स्वस्थ चावल के लिए संतुलित एनपीके सुनिश्चित करें और खाद डालें।"
            },
            'black': {
                'en': "Black soils are fertile but can have drainage issues. Ensure good water management to prevent root rot.",
                'kn': "ಕಪ್ಪು ಮಣ್ಣು ಫಲವತ್ತಾಗಿದೆ ಆದರೆ ಒಳಚರಂಡಿ ಸಮಸ್ಯೆಗಳನ್ನು ಹೊಂದಿರಬಹುದು. ಬೇರು ಕೊಳೆತವನ್ನು ತಡೆಯಲು ಉತ್ತಮ ನೀರಿನ ನಿರ್ವಹಣೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
                'te': "నల్ల నేలలు సారవంతమైనవి కానీ డ్రైనేజీ సమస్యలు ఉండవచ్చు. వేరుకుళ్లును నివారించడానికి మంచి నీటి యాజమాన్యాన్ని నిర్ధారించుకోండి.",
                'hi': "काली मिट्टी उपजाऊ होती है लेकिन इसमें जल निकासी की समस्या हो सकती है। जड़ सड़न को रोकने के लिए उचित जल प्रबंधन सुनिश्चित करें।"
            },
            'alluvial': {
                'en': "Alluvial soils are ideal for rice. Maintain fertility with balanced fertilizer application based on soil testing.",
                'kn': "ಮೆಕ್ಕಲು ಮಣ್ಣು ಅಕ್ಕಿಗೆ ಸೂಕ್ತವಾಗಿದೆ. ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ ಆಧಾರದ ಮೇಲೆ ಸಮತೋಲಿತ ಗೊಬ್ಬರ ಬಳಸಿ ಫಲವತ್ತತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ.",
                'te': "ఒండ్రు నేలలు వరికి చాలా అనుకూలం. నేల పరీక్ష ఆధారంగా సమతుల్య ఎరువుల వాడకంతో సారాన్ని కాపాడుకోండి.",
                'hi': "जलोढ़ मिट्टी चावल के लिए आदर्श होती है। मिट्टी परीक्षण के आधार पर संतुलित उर्वरक प्रयोग से उर्वरता बनाए रखें।"
            },
            'general': {
                'en': "Healthy rice requires proper water management (flooded or SRI), balanced NPK nutrition, and good weed control.",
                'kn': "ಆರೋಗ್ಯಕರ ಅಕ್ಕಿಗೆ ಸರಿಯಾದ ನೀರಿನ ನಿರ್ವಹಣೆ, ಸಮತೋಲಿತ NPK ಪೋಷಣೆ ಮತ್ತು ಉತ್ತಮ ಕಳೆ ನಿಯಂತ್ರಣ ಬೇಕಾಗುತ್ತದೆ.",
                'te': "ఆరోగ్యకరమైన వరికి సరైన నీటి యాజమాన్యం, సమతుల్య NPK పోషణ మరియు మంచి కలుపు నియంత్రణ అవసరం.",
                'hi': "स्वस्थ चावल के लिए उचित जल प्रबंधन (बाढ़ या एसआरआई), संतुलित एनपीके पोषण और अच्छा खरपतवार नियंत्रण आवश्यक है।"
            }
        },
        'seasons': {
            'monsoon': {
                'en': "Main growing season (Kharif). Monitor for pests and fungal diseases favored by high humidity.",
                'kn': "ಮುಖ್ಯ ಬೆಳೆಯುವ ಋತು (ಖಾರಿಫ್). ಹೆಚ್ಚಿನ ತೇವಾಂಶದಿಂದಾಗಿ ಕೀಟಗಳು ಮತ್ತು ಶಿಲೀಂಧ್ರ ರೋಗಗಳಿಗಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ.",
                'te': "ప్రధాన పంట కాలం (ఖరీఫ్). అధిక తేమ కారణంగా తెగుళ్లు మరియు ఫంగల్ వ్యాధుల కోసం పర్యవేక్షించండి.",
                'hi': "मुख्य बढ़ता मौसम (खरीफ)। उच्च आर्द्रता के कारण होने वाले कीटों और फंगल रोगों की निगरानी करें।"
            },
            'summer': {
                'en': "Summer (Rabi/Boro) rice requires heavy and consistent irrigation. Monitor for heat stress.",
                'kn': "ಬೇಸಿಗೆ (ರಬಿ/ಬೋರೋ) ಅಕ್ಕಿಗೆ ಭಾರಿ ಮತ್ತು ಸ್ಥಿರ ನೀರಾವರಿ ಬೇಕಾಗುತ್ತದೆ. ಶಾಖದ ಒತ್ತಡಕ್ಕಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ.",
                'te': "వేసవి (రబీ/బోరో) వరికి భారీ మరియు స్థిరమైన నీటిపారుదల అవసరం. వేడి ఒత్తిడి కోసం పర్యవేక్షించండి.",
                'hi': "ग्रीष्मकालीन (रबी/बोरो) चावल को भारी और निरंतर सिंचाई की आवश्यकता होती है। गर्मी के तनाव की निगरानी करें।"
            },
            'winter': {
                'en': "Not a primary season unless in specific tropical zones. Protect from any cool snaps.",
                'kn': "ನಿರ್ದಿಷ್ಟ ಉಷ್ಣವಲಯದ ವಲಯಗಳನ್ನು ಹೊರತುಪಡಿಸಿ, ಇದು ಮುಖ್ಯ ಋತುವಲ್ಲ. ಯಾವುದೇ ತಂಪಾದ ವಾತಾವರಣದಿಂದ ರಕ್ಷಿಸಿ.",
                'te': "నిర్దిష్ట ఉష్ణమండల ప్రాంతాలలో తప్ప, ఇది ప్రాథమిక సీజన్ కాదు. ఏదైనా చల్లని వాతావరణం నుండి రక్షించండి.",
                'hi': "विशिष्ट उष्णकटिबंधीय क्षेत्रों को छोड़कर, यह एक प्राथमिक मौसम नहीं है। किसी भी ठंडी लहर से बचाएं।"
            },
            'general': {
                'en': "Ensure nutrient availability matches the plant's growth stage (e.g., more N at tillering).",
                'kn': "ಸಸ್ಯದ ಬೆಳವಣಿಗೆಯ ಹಂತಕ್ಕೆ (ಉದಾಹರಣೆಗೆ, ಟಿಲ್ಲರಿಂಗ್ ಸಮಯದಲ್ಲಿ ಹೆಚ್ಚು N) ಪೋಷಕಾಂಶಗಳ ಲಭ್ಯತೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
                'te': "మొక్కల పెరుగుదల దశకు (ఉదా., దుబ్బు చేసే సమయంలో ఎక్కువ N) పోషకాల లభ్యత సరిపోయేలా చూసుకోండి.",
                'hi': "सुनिश्चित करें कि पोषक तत्वों की उपलब्धता पौधे के विकास चरण से मेल खाती है (जैसे, टिलरिंग के समय अधिक एन)।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "Maintain correct water level. Ensure proper plant spacing for airflow. Control weeds early.",
                'kn': "ಸರಿಯಾದ ನೀರಿನ ಮಟ್ಟವನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ. ಗಾಳಿಯ ಹರಿವಿಗಾಗಿ ಸರಿಯಾದ ಸಸ್ಯ ಅಂತರವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಕಳೆಗಳನ್ನು ಮೊದಲೇ ನಿಯಂತ್ರಿಸಿ.",
                'te': "సరైన నీటి మట్టాన్ని నిర్వహించండి. గాలి ప్రసరణ కోసం మొక్కల మధ్య సరైన దూరం ఉండేలా చూసుకోండి. కలుపు మొక్కలను ముందుగానే నియంత్రించండి.",
                'hi': "सही जल स्तर बनाए रखें। वायु प्रवाह के लिए पौधों के बीच उचित दूरी सुनिश्चित करें। खरपतवारों को जल्दी नियंत्रित करें।"
            },
            'organic': {
                'en': "Use compost, green manure (like Azolla), or vermicompost to build soil fertility.",
                'kn': "ಮಣ್ಣಿನ ಫಲವತ್ತತೆಯನ್ನು ಹೆಚ್ಚಿಸಲು ಕಾಂಪೋಸ್ಟ್, ಹಸಿರು ಗೊಬ್ಬರ (ಅಜೊಲ್ಲಾದಂತಹ) ಅಥವಾ ಎರೆಹುಳು ಗೊಬ್ಬರವನ್ನು ಬಳಸಿ.",
                'te': "నేల సారాన్ని పెంచడానికి కంపోస్ట్, పచ్చిరొట్ట ఎరువు (అజొల్లా వంటివి) లేదా వర్మీకంపోస్ట్‌ను వాడండి.",
                'hi': "मिट्टी की उर्वरता बढ़ाने के लिए कम्पोस्ट, हरी खाद (जैसे अजोला), या वर्मीकम्पोस्ट का उपयोग करें।"
            },
            'chemical': {
                'en': "No chemical action needed. Focus on a balanced NPK fertilizer schedule based on soil test results.",
                'kn': "ಯಾವುದೇ ರಾಸಾಯನಿಕ ಕ್ರಿಯೆ ಅಗತ್ಯವಿಲ್ಲ. ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ ಫಲಿತಾಂಶಗಳ ಆಧಾರದ ಮೇಲೆ ಸಮತೋಲಿತ NPK ಗೊಬ್ಬರದ ವೇಳಾಪಟ್ಟಿಯ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಿ.",
                'te': "రసాయన చర్య అవసరం లేదు. నేల పరీక్ష ఫలితాల ఆధారంగా సమతుల్య NPK ఎరువుల షెడ్యూల్‌పై దృష్టి పెట్టండి.",
                'hi': "किसी रासायनिक कार्रवाई की आवश्यकता नहीं है। मिट्टी परीक्षण के परिणामों के आधार पर संतुलित एनपीके उर्वरक अनुसूची पर ध्यान दें।"
            }
        }
    },
    
    # --- CHECK THIS KEY NAME ---
    'Rice___Nitrogen(N)': { 
        'soils': {
            'general': {
                'en': "Nitrogen leaches easily from sandy red soils. Black and alluvial soils hold it better. Deficiency is common in all soil types if not properly fertilized.",
                'kn': "ಸಾರಜನಕವು ಮರಳು ಮಿಶ್ರಿತ ಕೆಂಪು ಮಣ್ಣಿನಿಂದ ಸುಲಭವಾಗಿ ಸೋರಿಕೆಯಾಗುತ್ತದೆ. ಕಪ್ಪು ಮತ್ತು ಮೆಕ್ಕಲು ಮಣ್ಣು ಅದನ್ನು ಉತ್ತಮವಾಗಿ ಹಿಡಿದಿಟ್ಟುಕೊಳ್ಳುತ್ತದೆ. ಸರಿಯಾಗಿ ಫಲವತ್ತಾಗಿಸದಿದ್ದರೆ ಎಲ್ಲಾ ಮಣ್ಣಿನ ಪ್ರಕಾರಗಳಲ್ಲಿ ಕೊರತೆ ಸಾಮಾನ್ಯವಾಗಿದೆ.",
                'te': "ఇసుకతో కూడిన ఎర్ర నేలల నుండి నత్రజని సులభంగా బయటకు వెళుతుంది. నల్ల మరియు ఒండ్రు నేలలు దానిని బాగా పట్టి ఉంచుతాయి. సరిగ్గా ఎరువులు వేయకపోతే అన్ని నేల రకాల్లో లోపం సాధారణం.",
                'hi': "नाइट्रोजन रेतीली लाल मिट्टी से आसानी से निकल जाता है। काली और जलोढ़ मिट्टी इसे बेहतर बनाए रखती है। यदि ठीक से निषेचित न किया जाए तो सभी प्रकार की मिट्टी में कमी आम है।"
            }
        },
        'seasons': {
            'general': {
                'en': "Apply Nitrogen in splits: during transplanting, at the tillering stage, and at the panicle initiation stage. Avoid heavy application during monsoon rains to prevent runoff.",
                'kn': "ಸಾರಜನಕವನ್ನು ವಿಭಜಿಸಿ ಅನ್ವಯಿಸಿ: ನಾಟಿ ಮಾಡುವಾಗ, ಟಿಲ್ಲರಿಂಗ್ ಹಂತದಲ್ಲಿ, ಮತ್ತು ಪ್ಯಾನಿಕಲ್ ಪ್ರಾರಂಭದ ಹಂತದಲ್ಲಿ. ಮಳೆಗಾಲದಲ್ಲಿ ಹರಿಯುವುದನ್ನು ತಡೆಯಲು ಭಾರಿ ಬಳಕೆಯನ್ನು ತಪ್ಪಿಸಿ.",
                'te': "నత్రజనిని విభజించి వాడండి: నాట్లు వేసేటప్పుడు, దుబ్బు చేసే దశలో మరియు కంకి ప్రారంభ దశలో. వర్షాకాలంలో నీటితో కొట్టుకుపోకుండా అధిక వాడకాన్ని నివారించండి.",
                'hi': "नाइट्रोजन को हिस्सों में डालें: रोपाई के दौरान, टिलरिंग चरण में, और पुष्पगुच्छ बनने के चरण में। मानसून की बारिश के दौरान भारी प्रयोग से बचें ताकि यह बह न जाए।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "Ensure proper water management, as it heavily affects nitrogen uptake. Incorporate legume green manures in crop rotation.",
                'kn': "ಸರಿಯಾದ ನೀರಿನ ನಿರ್ವಹಣೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ, ಏಕೆಂದರೆ ಇದು ಸಾರಜನಕ ಹೀರಿಕೊಳ್ಳುವಿಕೆಯ ಮೇಲೆ ಹೆಚ್ಚು ಪರಿಣಾಮ ಬೀರುತ್ತದೆ. ಬೆಳೆ ಸರದಿಯಲ್ಲಿ ದ್ವಿದಳ ಧಾನ್ಯದ ಹಸಿರು ಗೊಬ್ಬರಗಳನ್ನು ಸೇರಿಸಿ.",
                'te': "సరైన నీటి యాజమాన్యాన్ని నిర్ధారించుకోండి, ఎందుకంటే ఇది నత్రజని గ్రహణను బాగా ప్రభావితం చేస్తుంది. పంట మార్పిడిలో పప్పుధాన్యాల పచ్చిరొట్ట ఎరువులను చేర్చండి.",
                'hi': "उचित जल प्रबंधन सुनिश्चित करें, क्योंकि यह नाइट्रोजन अवशोषण को बहुत प्रभावित करता है। फसल चक्र में फलीदार हरी खाद शामिल करें।"
            },
            'organic': {
                'en': "Top-dress with nitrogen-rich organic sources like poultry manure, vermicompost, or oil cakes (e.g., neem cake).",
                'kn': "ಸಾರಜನಕ-ಭರಿತ ಸಾವಯವ ಮೂಲಗಳಾದ ಕೋಳಿ ಗೊಬ್ಬರ, ಎರೆಹುಳು ಗೊಬ್ಬರ, ಅಥವಾ ಹಿಂಡಿ (ಉದಾ., ಬೇವಿನ ಹಿಂಡಿ) ಯೊಂದಿಗೆ ಟಾಪ್-ಡ್ರೆಸ್ ಮಾಡಿ.",
                'te': "నత్రజని అధికంగా ఉండే సేంద్రియ వనరులైన కోళ్ల ఎరువు, వర్మీకంపోస్ట్, లేదా నూనె కేకులు (ఉదా., వేప పిండి) తో టాప్-డ్రెస్ చేయండి.",
                'hi': "नाइट्रोजन युक्त जैविक स्रोतों जैसे मुर्गी की खाद, वर्मीकम्पोस्ट, या खली (जैसे, नीम की खली) के साथ टॉप-ड्रेसिंग करें।"
            },
            'chemical': {
                'en': "Apply a top-dressing of Urea (46% N) as per your local agricultural university's recommendations (e.g., 25-30 kg/acre, split). A Leaf Color Chart (LCC) can help guide precise application.",
                'kn': "ನಿಮ್ಮ ಸ್ಥಳೀಯ ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯದ ಶಿಫಾರಸುಗಳ ಪ್ರಕಾರ ಯೂರಿಯಾ (46% N) ದ ಟಾಪ್-ಡ್ರೆಸ್ಸಿಂಗ್ ಅನ್ವಯಿಸಿ (ಉದಾ., 25-30 ಕೆಜಿ/ಎಕರೆ, ವಿಭಜಿತ). ಎಲೆ ಬಣ್ಣದ ಚಾರ್ಟ್ (LCC) ನಿಖರವಾದ ಬಳಕೆಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡಬಹುದು.",
                'te': "మీ స్థానిక వ్యవసాయ విశ్వవిద్యాలయం సిఫార్సుల ప్రకారం యూరియా (46% N) తో టాప్-డ్రెస్సింగ్ చేయండి (ఉదా., 25-30 కిలోలు/ఎకరం, విభజించి). లీఫ్ కలర్ చార్ట్ (LCC) కచ్చితమైన వాడకానికి మార్గనిర్దేశం చేస్తుంది.",
                'hi': "अपने स्थानीय कृषि विश्वविद्यालय की सिफारिशों के अनुसार यूरिया (46% N) की टॉप-ड्रेसिंग करें (जैसे, 25-30 किग्रा/एकड़, हिस्सों में)। एक लीफ कलर चार्ट (LCC) सटीक प्रयोग का मार्गदर्शन करने में मदद कर सकता है।"
            }
        }
    },

    # --- CHECK THIS KEY NAME ---
    'Rice___Phosphorus(P)': { # This is an EXAMPLE name, check your .npy file
        'soils': {
            'general': {
                'en': "Phosphorus deficiency is common in acidic red soils and in some black soils where it gets 'fixed' and becomes unavailable. Soil testing is key.",
                'kn': "ರಂಜಕದ ಕೊರತೆಯು ಆಮ್ಲೀಯ ಕೆಂಪು ಮಣ್ಣುಗಳಲ್ಲಿ ಮತ್ತು ಕೆಲವು ಕಪ್ಪು ಮಣ್ಣುಗಳಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿದೆ, ಅಲ್ಲಿ ಅದು 'ಸ್ಥಿರ'ಗೊಂಡು ಲಭ್ಯವಾಗುವುದಿಲ್ಲ. ಮಣ್ಣು ಪರೀಕ್ಷೆ ಮುಖ್ಯ.",
                'te': "ఆమ్ల ఎర్ర నేలల్లో మరియు కొన్ని నల్ల నేలల్లో ఫాస్పరస్ లోపం సాధారణం, ఇక్కడ అది 'స్థిరపడి' అందుబాటులో ఉండదు. నేల పరీక్ష ముఖ్యం.",
                'hi': "फास्फोरस की कमी अम्लीय लाल मिट्टी और कुछ काली मिट्टी में आम है, जहाँ यह 'फिक्स' हो जाता है और अनुपलब्ध हो जाता है। मिट्टी की जाँच प्रमुख है।"
            }
        },
        'seasons': {
            'general': {
                'en': "Phosphorus is crucial at the very beginning of the plant's life. Apply as a basal dose (at the time of planting).",
                'kn': "ಸಸ್ಯದ ಜೀವನದ ಆರಂಭದಲ್ಲಿ ರಂಜಕವು ನಿರ್ಣಾಯಕವಾಗಿದೆ. ಇದನ್ನು ಮೂಲ ಡೋಸ್ ಆಗಿ (ನೆಡುವ ಸಮಯದಲ್ಲಿ) ಅನ್ವಯಿಸಿ.",
                'te': "మొక్క జీవితం ప్రారంభంలో ఫాస్పరస్ చాలా ముఖ్యం. దీనిని బేసల్ డోస్‌గా (నాటే సమయంలో) వేయండి.",
                'hi': "फास्फोरस पौधे के जीवन की शुरुआत में बहुत महत्वपूर्ण है। इसे बेसल डोज़ के रूप में (रोपण के समय) डालें।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "Maintain proper water levels. Use organic matter (compost) which helps in releasing soil-bound phosphorus.",
                'kn': "ಸರಿಯಾದ ನೀರಿನ ಮಟ್ಟವನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ. ಸಾವಯವ ಪದಾರ್ಥಗಳನ್ನು (ಕಾಂಪೋಸ್ಟ್) ಬಳಸಿ, ಇದು ಮಣ್ಣಿನಲ್ಲಿ ಬಂಧಿತವಾಗಿರುವ ರಂಜಕವನ್ನು ಬಿಡುಗಡೆ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
                'te': "సరైన నీటి మట్టాలను నిర్వహించండి. సేంద్రియ పదార్థాన్ని (కంపోస్ట్) వాడండి, ఇది నేలలో బంధించబడిన ఫాస్పరస్‌ను విడుదల చేయడానికి సహాయపడుతుంది.",
                'hi': "उचित जल स्तर बनाए रखें। जैविक पदार्थ (कम्पोस्ट) का उपयोग करें जो मिट्टी में बंधे फास्फोरस को छोड़ने में मदद करता है।"
            },
            'organic': {
                'en': "Apply rock phosphate or bone meal as a basal application. Use Phosphorus Solubilizing Bacteria (PSB) to make existing soil phosphorus available.",
                'kn': "ರಾಕ್ ಫಾಸ್ಫೇಟ್ ಅಥವಾ ಮೂಳೆ ಪುಡಿಯನ್ನು ಮೂಲ ಅನ್ವಯವಾಗಿ ಬಳಸಿ. ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಮಣ್ಣಿನ ರಂಜಕವನ್ನು ಲಭ್ಯವಾಗುವಂತೆ ಮಾಡಲು ಫಾಸ್ಫರಸ್ ಕರಗಿಸುವ ಬ್ಯಾಕ್ಟೀರಿಯಾ (PSB) ಬಳಸಿ.",
                'te': "రాక్ ఫాస్ఫేట్ లేదా ఎముకల పొడిని బేసల్ అప్లికేషన్‌గా వాడండి. ఇప్పటికే ఉన్న నేల ఫాస్పరస్‌ను అందుబాటులోకి తెవడానికి ఫాస్పరస్ సోల్యుబిలైజింగ్ బ్యాక్టీరియా (PSB) ను వాడండి.",
                'hi': "रॉक फॉस्फेट या बोन मील को बेसल अनुप्रयोग के रूप में लागू करें। मौजूदा मिट्टी के फास्फोरस को उपलब्ध कराने के लिए फास्फोरस सोल्यूबिलाइजिंग बैक्टीरिया (PSB) का उपयोग करें।"
            },
            'chemical': {
                'en': "Apply DAP (Diammonium Phosphate) or SSP (Single Super Phosphate) as a basal dose based on soil test results.",
                'kn': "ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ ಫಲಿತಾಂಶಗಳ ಆಧಾರದ ಮೇಲೆ ಡಿಎಪಿ (ಡೈಅಮೋನಿಯಂ ಫಾಸ್ಫೇಟ್) ಅಥವಾ ಎಸ್‌ಎಸ್‌ಪಿ (ಸಿಂಗಲ್ ಸೂಪರ್ ಫಾಸ್ಫೇಟ್) ಅನ್ನು ಮೂಲ ಡೋಸ್ ಆಗಿ ಅನ್ವಯಿಸಿ.",
                'te': "నేల పరీక్ష ఫలితాల ఆధారంగా DAP (డైఅమోనియం ఫాస్ఫేట్) లేదా SSP (సింగిల్ సూపర్ ఫాస్ఫేట్) ను బేసల్ డోస్‌గా వేయండి.",
                'hi': "मिट्टी परीक्षण के परिणामों के आधार पर डीएपी (डायमोनियम फॉस्फेट) या एसएसपी (सिंगल सुपर फॉस्फेट) को बेसल डोज़ के रूप में लागू करें।"
            }
        }
    },

    # --- CHECK THIS KEY NAME ---
    'Rice___Potassium(K)': { # This is an EXAMPLE name, check your .npy file
        'soils': {
            'general': {
                'en': "Potassium deficiency is common in sandy, acidic red soils (due to leaching) and also in some alluvial soils. Black soils are often rich in Potassium.",
                'kn': "ಪೊಟ್ಯಾಸಿಯಮ್ ಕೊರತೆಯು ಮರಳು, ಆಮ್ಲೀಯ ಕೆಂಪು ಮಣ್ಣುಗಳಲ್ಲಿ (ಲೀಚಿಂಗ್‌ನಿಂದಾಗಿ) ಮತ್ತು ಕೆಲವು ಮೆಕ್ಕಲು ಮಣ್ಣುಗಳಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿದೆ. ಕಪ್ಪು ಮಣ್ಣು ಸಾಮಾನ್ಯವಾಗಿ ಪೊಟ್ಯಾಸಿಯಮ್‌ನಿಂದ ಸಮೃದ್ಧವಾಗಿರುತ್ತದೆ.",
                'te': "పొటాషియం లోపం ఇసుక, ఆమ్ల ఎర్ర నేలల్లో (లీచింగ్ కారణంగా) మరియు కొన్ని ఒండ్రు నేలల్లో సాధారణం. నల్ల నేలలు తరచుగా పొటాషియంతో సమృద్ధిగా ఉంటాయి.",
                'hi': "पोटेशियम की कमी रेतीली, अम्लीय लाल मिट्टी (लीचिंग के कारण) और कुछ जलोढ़ मिट्टी में आम है। काली मिट्टी अक्सर पोटेशियम से भरपूर होती है।"
            }
        },
        'seasons': {
            'general': {
                'en': "Potassium is needed throughout the plant's life. Apply as a basal dose and also as a top-dressing at the panicle initiation stage.",
                'kn': "ಸಸ್ಯದ ಜೀವನದುದ್ದಕ್ಕೂ ಪೊಟ್ಯಾಸಿಯಮ್ ಬೇಕಾಗುತ್ತದೆ. ಇದನ್ನು ಮೂಲ ಡೋಸ್ ಆಗಿ ಮತ್ತು ಪ್ಯಾನಿಕಲ್ ಪ್ರಾರಂಭದ ಹಂತದಲ್ಲಿ ಟಾಪ್-ಡ್ರೆಸ್ಸಿಂಗ್ ಆಗಿ ಅನ್ವಯಿಸಿ.",
                'te': "మొక్క జీవితాంతం పొటాషియం అవసరం. దీనిని బేసల్ డోస్‌గా మరియు కంకి ప్రారంభ దశలో టాప్-డ్రెస్సింగ్‌గా వేయండి.",
                'hi': "पौधे के पूरे जीवनकाल में पोटेशियम की आवश्यकता होती है। इसे बेसल डोज़ के रूप में और पुष्पगुच्छ बनने के चरण में टॉप-ड्रेसिंग के रूप में लागू करें।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "Ensure rice straw and husk are not completely removed from the field, as they contain potassium. Avoid excessive Nitrogen, which can create an imbalance.",
                'kn': "ಅಕ್ಕಿ ಹುಲ್ಲು ಮತ್ತು ಹೊಟ್ಟು ಸಂಪೂರ್ಣವಾಗಿ ಹೊಲದಿಂದ ತೆಗೆದುಹಾಕದಂತೆ ನೋಡಿಕೊಳ್ಳಿ, ಏಕೆಂದರೆ ಅವುಗಳಲ್ಲಿ ಪೊಟ್ಯಾಸಿಯಮ್ ಇರುತ್ತದೆ. ಅತಿಯಾದ ಸಾರಜನಕವನ್ನು ತಪ್ಪಿಸಿ, ಇದು ಅಸಮತೋಲನವನ್ನು ಉಂಟುಮಾಡಬಹುದು.",
                'te': "వరి గడ్డి మరియు పొట్టు పొలం నుండి పూర్తిగా తొలగించబడలేదని నిర్ధారించుకోండి, ఎందుకంటే వాటిలో పొటాషియం ఉంటుంది. అధిక నత్రజనిని నివారించండి, ఇది అసమతుల్యతను సృష్టిస్తుంది.",
                'hi': "सुनिश्चित करें कि चावल का पुआल और भूसी खेत से पूरी तरह से न हटाई जाए, क्योंकि उनमें पोटेशियम होता है। अत्यधिक नाइट्रोजन से बचें, जो असंतुलन पैदा कर सकता है।"
            },
            'organic': {
                'en': "Apply wood ash (if not alkaline soil), rice straw compost, or composted manure.",
                'kn': "ಮರದ ಬೂದಿ (ಕ್ಷಾರೀಯ ಮಣ್ಣಲ್ಲದಿದ್ದರೆ), ಅಕ್ಕಿ ಹುಲ್ಲಿನ ಕಾಂಪೋಸ್ಟ್, ಅಥವಾ ಕಾಂಪೋಸ್ಟ್ ಮಾಡಿದ ಗೊಬ್ಬರವನ್ನು ಅನ್ವಯಿಸಿ.",
                'te': "కలప బూడిద (క్షార నేల కాకపోతే), వరి గడ్డి కంపోస్ట్, లేదా కంపోస్ట్ ఎరువును వాడండి.",
                'hi': "लकड़ी की राख (यदि क्षारीय मिट्टी न हो), चावल के पुआल की खाद, या कम्पोस्ट की गई खाद का प्रयोग करें।"
            },
            'chemical': {
                'en': "Apply MOP (Muriate of Potash / KCl) as a basal dose and/or top-dressing based on soil test results.",
                'kn': "ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ ಫಲಿತಾಂಶಗಳ ಆಧಾರದ ಮೇಲೆ MOP (ಮ್ಯೂರಿಯೇಟ್ ಆಫ್ ಪೊಟ್ಯಾಶ್ / KCl) ಅನ್ನು ಮೂಲ ಡೋಸ್ ಆಗಿ ಮತ್ತು/ಅಥವಾ ಟಾಪ್-ಡ್ರೆಸ್ಸಿಂಗ್ ಆಗಿ ಅನ್ವಯಿಸಿ.",
                'te': "నేల పరీక్ష ఫలితాల ఆధారంగా MOP (మ్యూరియేట్ ఆఫ్ పొటాష్ / KCl) ను బేసల్ డోస్‌గా మరియు/లేదా టాప్-డ్రెస్సింగ్‌గా వేయండి.",
                'hi': "मिट्टी परीक्षण के परिणामों के आधार पर MOP (म्यूरेट ऑफ पोटाश / KCl) को बेसल डोज़ और/या टॉप-ड्रेसिंग के रूप में लागू करें।"
            }
        }
    },

    # -------------------------
    # BANANA (Nutrient Deficiency)
    # -------------------------
    
    # --- CHECK THIS KEY NAME ---
    'Banana___healthy': { 
        'soils': {
            'red': {
                'en': "Red soils are good for bananas if well-drained and rich in organic matter. They are heavy feeders, so add a lot of compost.",
                'kn': "ಕೆಂಪು ಮಣ್ಣು ಚೆನ್ನಾಗಿ ಒಳಚರಂಡಿಯಾಗಿದ್ದರೆ ಮತ್ತು ಸಾವಯವ ಪದಾರ್ಥಗಳಿಂದ ಸಮೃದ್ಧವಾಗಿದ್ದರೆ ಬಾಳೆಹಣ್ಣುಗಳಿಗೆ ಒಳ್ಳೆಯದು. ಅವು ಭಾರೀ ಪೋಷಕಾಂಶಗಳನ್ನು ಬಳಸುವುದರಿಂದ, ಸಾಕಷ್ಟು ಕಾಂಪೋಸ್ಟ್ ಸೇರಿಸಿ.",
                'te': "ఎర్ర నేలలు బాగా నీరు పోయేవిగా మరియు సేంద్రియ పదార్థంతో సమృద్ధిగా ఉంటే అరటిపండ్లకు మంచివి. అవి భారీగా పోషకాలను తీసుకుంటాయి, కాబట్టి చాలా కంపోస్ట్ జోడించండి.",
                'hi': "लाल मिट्टी केले के लिए अच्छी होती है यदि वह अच्छी तरह से सूखी हो और जैविक पदार्थों से भरपूर हो। वे भारी फीडर होते हैं, इसलिए ढेर सारी खाद डालें।"
            },
            'black': {
                'en': "Heavy black soils can lead to root rot. Ensure excellent drainage or plant on raised beds.",
                'kn': "ಭಾರೀ ಕಪ್ಪು ಮಣ್ಣು ಬೇರು ಕೊಳೆತಕ್ಕೆ ಕಾರಣವಾಗಬಹುದು. ಅತ್ಯುತ್ತಮ ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ ಅಥವಾ ಎತ್ತರದ ಹಾಸಿಗೆಗಳ ಮೇಲೆ ನೆಡಿರಿ.",
                'te': "భారీ నల్ల నేలలు వేరుకుళ్లుకు దారితీయవచ్చు. అద్భుతమైన డ్రైనేజీని నిర్ధారించుకోండి లేదా ఎత్తైన гряdulaపై నాటండి.",
                'hi': "भारी काली मिट्टी से जड़ सड़न हो सकती है। उत्कृष्ट जल निकासी सुनिश्चित करें या ऊँची क्यारियों पर पौधे लगाएँ।"
            },
            'alluvial': {
                'en': "Alluvial soils are often very fertile and ideal for bananas, but still require large amounts of organic matter.",
                'kn': "ಮೆಕ್ಕಲು ಮಣ್ಣು ಸಾಮಾನ್ಯವಾಗಿ ಬಹಳ ಫಲವತ್ತಾಗಿರುತ್ತದೆ ಮತ್ತು ಬಾಳೆಹಣ್ಣುಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ, ಆದರೆ ಇನ್ನೂ ಹೆಚ್ಚಿನ ಪ್ರಮಾಣದ ಸಾವಯವ ಪದಾರ್ಥಗಳ ಅಗತ್ಯವಿರುತ್ತದೆ.",
                'te': "ఒండ్రు నేలలు తరచుగా చాలా సారవంతమైనవి మరియు అరటిపండ్లకు అనువైనవి, కానీ ఇప్పటికీ పెద్ద మొత్తంలో సేంద్రియ పదార్థం అవసరం.",
                'hi': "जलोढ़ मिट्टी अक्सर बहुत उपजाऊ और केले के लिए आदर्श होती है, लेकिन फिर भी इसे बड़ी मात्रा में जैविक पदार्थ की आवश्यकता होती है।"
            },
            'general': {
                'en': "Bananas are heavy feeders. They need deep, fertile, well-drained soil with a lot of organic matter and consistent moisture.",
                'kn': "ಬಾಳೆಹಣ್ಣುಗಳು ಭಾರೀ ಪೋಷಕಾಂಶಗಳನ್ನು ಬಳಸುತ್ತವೆ. ಅವುಗಳಿಗೆ ಆಳವಾದ, ಫಲವತ್ತಾದ, ಚೆನ್ನಾಗಿ ಒಳಚರಂಡಿ ಇರುವ ಮಣ್ಣು ಮತ್ತು ಸಾಕಷ್ಟು ಸಾವಯವ ಪದಾರ್ಥಗಳು ಮತ್ತು ಸ್ಥಿರವಾದ ತೇವಾಂಶ ಬೇಕಾಗುತ್ತದೆ.",
                'te': "అరటిపండ్లు భారీగా పోషకాలను తీసుకుంటాయి. వాటికి లోతైన, సారవంతమైన, బాగా నీరు పోయే నేల, చాలా సేంద్రియ పదార్థం మరియు స్థిరమైన తేమ అవసరం.",
                'hi': "केले भारी फीडर होते हैं। उन्हें गहरी, उपजाऊ, अच्छी जल निकासी वाली मिट्टी की आवश्यकता होती है जिसमें बहुत अधिक जैविक पदार्थ और लगातार नमी हो।"
            }
        },
        'seasons': {
            'monsoon': {
                'en': "Ensure drainage to prevent rhizome rot. High winds during monsoon can topple plants; provide support.",
                'kn': "ಗೆಡ್ಡೆ ಕೊಳೆತವನ್ನು ತಡೆಯಲು ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಮಾನ್ಸೂನ್ ಸಮಯದಲ್ಲಿ ಬೀಸುವ ಬಲವಾದ ಗಾಳಿಯು ಸಸ್ಯಗಳನ್ನು ಉರುಳಿಸಬಹುದು; ಬೆಂಬಲ ನೀಡಿ.",
                'te': "దుంప కుళ్ళిపోకుండా నివారించడానికి డ్రైనేజీని నిర్ధారించుకోండి. వర్షాకాలంలో బలమైన గాలులు మొక్కలను పడగొట్టగలవు; మద్దతు అందించండి.",
                'hi': "प्रकंद सड़न को रोकने के लिए जल निकासी सुनिश्चित करें। मानसून के दौरान तेज हवाएं पौधों को गिरा सकती हैं; सहारा प्रदान करें।"
            },
            'summer': {
                'en': "Crucial irrigation period. Bananas need a lot of water. Use heavy mulch to conserve moisture.",
                'kn': "ನಿರ್ಣಾಯಕ ನೀರಾವರಿ ಅವಧಿ. ಬಾಳೆಹಣ್ಣುಗಳಿಗೆ ಬಹಳಷ್ಟು ನೀರು ಬೇಕು. ತೇವಾಂಶವನ್ನು ಸಂರಕ್ಷಿಸಲು ದಪ್ಪವಾದ ಮಲ್ಚ್ ಬಳಸಿ.",
                'te': "కీలకమైన నీటిపారుదల కాలం. అరటిపండ్లకు చాలా నీరు అవసరం. తేమను సంరక్షించడానికి భారీ మల్చ్ ఉపయోగించండి.",
                'hi': "महत्वपूर्ण सिंचाई अवधि। केले को बहुत अधिक पानी की आवश्यकता होती है। नमी बनाए रखने के लिए भारी मल्च का उपयोग करें।"
            },
            'winter': {
                'en': "Growth slows in cool weather. Protect from frost in temperate regions.",
                'kn': "ತಂಪಾದ ವಾತಾವರಣದಲ್ಲಿ ಬೆಳವಣಿಗೆ ನಿಧಾನವಾಗುತ್ತದೆ. ಸಮಶೀತೋಷ್ಣ ಪ್ರದೇಶಗಳಲ್ಲಿ ಹಿಮದಿಂದ ರಕ್ಷಿಸಿ.",
                'te': "చల్లని వాతావరణంలో పెరుగుదల మందగిస్తుంది. సమశీతోష్ణ ప్రాంతాలలో మంచు నుండి రక్షించండి.",
                'hi': "ठंडे मौसम में वृद्धि धीमी हो जाती है। समशीतोष्ण क्षेत्रों में पाले से बचाएं।"
            },
            'general': {
                'en': "Bananas are heavy feeders. They need a continuous supply of nutrients (especially N and K) and water throughout the year.",
                'kn': "ಬಾಳೆಹಣ್ಣುಗಳು ಭಾರೀ ಪೋಷಕಾಂಶಗಳನ್ನು ಬಳಸುತ್ತವೆ. ಅವುಗಳಿಗೆ ವರ್ಷವಿಡೀ ಪೋಷಕಾಂಶಗಳ (ವಿಶೇಷವಾಗಿ N ಮತ್ತು K) ಮತ್ತು ನೀರಿನ ನಿರಂತರ ಪೂರೈಕೆ ಬೇಕಾಗುತ್ತದೆ.",
                'te': "అరటిపండ్లు భారీగా పోషకాలను తీసుకుంటాయి. వాటికి ఏడాది పొడవునా పోషకాలు (ముఖ్యంగా N మరియు K) మరియు నీరు నిరంతరం సరఫరా చేయాలి.",
                'hi': "केले भारी फीडर होते हैं। उन्हें साल भर पोषक तत्वों (विशेषकर एन और के) और पानी की निरंतर आपूर्ति की आवश्यकता होती है।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "De-sucker regularly (leave only one follower). Provide propping/support for the bunch. Maintain a thick layer of organic mulch. Remove old, dry leaves.",
                'kn': "ನಿಯಮಿತವಾಗಿ ಕಂದುಗಳನ್ನು ತೆಗೆಯಿರಿ (ಒಬ್ಬ ಹಿಂಬಾಲಕನನ್ನು ಮಾತ್ರ ಬಿಡಿ). ಗೊಂಚಲಿಗೆ ಆಧಾರ/ಬೆಂಬಲ ನೀಡಿ. ಸಾವಯವ ಮಲ್ಚ್‌ನ ದಪ್ಪ ಪದರವನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ. ಹಳೆಯ, ಒಣ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
                'te': "పిలకలను క్రమం తప్పకుండా తీసివేయండి (ఒక అనుచరుడిని మాత్రమే వదిలివేయండి). గెలకి ఊతం/మద్దతు అందించండి. సేంద్రియ మల్చ్ యొక్క మందపాటి పొరను నిర్వహించండి. పాత, ఎండిన ఆకులను తొలగించండి.",
                'hi': "नियमित रूप से सकर हटाएँ (केवल एक फॉलोअर छोड़ें)। गुच्छे के लिए सहारा/समर्थन प्रदान करें। जैविक मल्च की एक मोटी परत बनाए रखें। पुरानी, सूखी पत्तियाँ हटा दें।"
            },
            'organic': {
                'en': "Apply very large quantities of compost or well-rotted farmyard manure several times a year.",
                'kn': "ವರ್ಷಕ್ಕೆ ಹಲವಾರು ಬಾರಿ ದೊಡ್ಡ ಪ್ರಮಾಣದಲ್ಲಿ ಕಾಂಪೋಸ್ಟ್ ಅಥವಾ ಚೆನ್ನಾಗಿ ಕೊಳೆತ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರವನ್ನು ಅನ್ವಯಿಸಿ.",
                'te': "సంవత్సరానికి చాలాసార్లు పెద్ద మొత్తంలో కంపోస్ట్ లేదా బాగా చివికిన పశువుల ఎరువును వేయండి.",
                'hi': "साल में कई बार बड़ी मात्रा में कम्पोस्ट या अच्छी तरह से सड़ी हुई गोबर की खाद डालें।"
            },
            'chemical': {
                'en': "No chemical action needed. Focus on a robust, balanced fertilizer schedule rich in Nitrogen (N) and Potassium (K) based on soil analysis.",
                'kn': "ಯಾವುದೇ ರಾಸಾಯನಿಕ ಕ್ರಿಯೆ ಅಗತ್ಯವಿಲ್ಲ. ಮಣ್ಣಿನ ವಿಶ್ಲೇಷಣೆಯ ಆಧಾರದ ಮೇಲೆ ಸಾರಜನಕ (N) ಮತ್ತು ಪೊಟ್ಯಾಸಿಯಮ್ (K) ಸಮೃದ್ಧವಾಗಿರುವ ದೃಢವಾದ, ಸಮತೋಲಿತ ಗೊಬ್ಬರದ ವೇಳಾಪಟ್ಟಿಯ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಿ.",
                'te': "రసాయన చర్య అవసరం లేదు. నేల విశ్లేషణ ఆధారంగా నత్రజని (N) మరియు పొటాషియం (K) అధికంగా ఉండే దృఢమైన, సమతుల్య ఎరువుల షెడ్యూల్‌పై దృష్టి పెట్టండి.",
                'hi': "किसी रासायनिक कार्रवाई की आवश्यकता नहीं है। मिट्टी के विश्लेषण के आधार पर नाइट्रोजन (एन) और पोटेशियम (के) से भरपूर एक मजबूत, संतुलित उर्वरक अनुसूची पर ध्यान दें।"
            }
        }
    },
    
    # --- CHECK THIS KEY NAME ---
    'Banana___Nitrogen_Deficiency': { # This is an EXAMPLE name, check your .npy file
        'soils': {
            'general': {
                'en': "Deficiency is common in sandy soils (like some red or alluvial soils) where nitrogen leaches easily. Bananas are heavy feeders and quickly deplete N.",
                'kn': "ಸಾರಜನಕವು ಸುಲಭವಾಗಿ ಹರಿದುಹೋಗುವ ಮರಳು ಮಣ್ಣುಗಳಲ್ಲಿ (ಕೆಲವು ಕೆಂಪು ಅಥವಾ ಮೆಕ್ಕಲು ಮಣ್ಣುಗಳಂತಹ) ಕೊರತೆ ಸಾಮಾನ್ಯವಾಗಿದೆ. ಬಾಳೆಹಣ್ಣುಗಳು ಭಾರೀ ಪೋಷಕಾಂಶಗಳನ್ನು ಬಳಸುತ್ತವೆ ಮತ್ತು N ಅನ್ನು ತ್ವರಿತವಾಗಿ ಖಾಲಿಮಾಡುತ್ತವೆ.",
                'te': "నత్రజని సులభంగా బయటకు వెళ్ళే ఇసుక నేలల్లో (కొన్ని ఎర్ర లేదా ఒండ్రు నేలల వంటివి) లోపం సాధారణం. అరటిపండ్లు భారీగా పోషకాలను తీసుకుంటాయి మరియు N ను త్వరగా క్షీణింపజేస్తాయి.",
                'hi': "नाइट्रोजन की कमी रेतीली मिट्टी (जैसे कुछ लाल या जलोढ़ मिट्टी) में आम है जहाँ से नाइट्रोजन आसानी से निकल जाता है। केले भारी फीडर होते हैं और जल्दी से एन को समाप्त कर देते हैं।"
            }
        },
        'seasons': {
            'general': {
                'en': "Nitrogen is needed constantly during active growth. Apply in split doses, especially during the monsoon (to avoid leaching) and summer (to support rapid growth).",
                'kn': "ಸಕ್ರಿಯ ಬೆಳವಣಿಗೆಯ ಸಮಯದಲ್ಲಿ ಸಾರಜನಕವು ನಿರಂತರವಾಗಿ ಬೇಕಾಗುತ್ತದೆ. ವಿಭಜಿತ ಡೋಸ್‌ಗಳಲ್ಲಿ ಅನ್ವಯಿಸಿ, ವಿಶೇಷವಾಗಿ ಮಾನ್ಸೂನ್ ಸಮಯದಲ್ಲಿ (ಹರಿದು ಹೋಗುವುದನ್ನು ತಪ್ಪಿಸಲು) ಮತ್ತು ಬೇಸಿಗೆಯಲ್ಲಿ (ವೇಗದ ಬೆಳವಣಿಗೆಯನ್ನು ಬೆಂಬಲಿಸಲು).",
                'te': "చురుకైన పెరుగుదల సమయంలో నత్రజని నిరంతరం అవసరం. ముఖ్యంగా వర్షాకాలంలో (లీచింగ్‌ను నివారించడానికి) మరియు వేసవిలో (వేగవంతమైన పెరుగుదలకు మద్దతు ఇవ్వడానికి) విభజిత మోతాదులలో వాడండి.",
                'hi': "सक्रिय वृद्धि के दौरान नाइट्रोजन की लगातार आवश्यकता होती है। विभाजित खुराकों में लागू करें, विशेष रूप से मानसून के दौरान (लीचिंग से बचने के लिए) और गर्मियों में (तेजी से विकास का समर्थन करने के लिए)।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "Apply heavy mulch of organic matter, which will slowly release nitrogen as it decomposes.",
                'kn': "ಸಾವಯವ ಪದಾರ್ಥಗಳ ದಪ್ಪವಾದ ಮಲ್ಚ್ ಅನ್ನು ಅನ್ವಯಿಸಿ, ಅದು ಕೊಳೆಯುತ್ತಿದ್ದಂತೆ ನಿಧಾನವಾಗಿ ಸಾರಜನಕವನ್ನು ಬಿಡುಗಡೆ ಮಾಡುತ್ತದೆ.",
                'te': "సేంద్రియ పదార్థం యొక్క మందపాటి మల్చ్‌ను వేయండి, అది కుళ్ళిపోయేటప్పుడు నెమ్మదిగా నత్రజనిని విడుదల చేస్తుంది.",
                'hi': "जैविक पदार्थ का भारी मल्च लागू करें, जो विघटित होने पर धीरे-धीरे नाइट्रोजन छोड़ेगा।"
            },
            'organic': {
                'en': "Apply nitrogen-rich compost, poultry manure, or oil cakes (like neem or castor cake) around the base of the plant.",
                'kn': "ಸಸ್ಯದ ಬುಡದ ಸುತ್ತಲೂ ಸಾರಜನಕ-ಸಮೃದ್ಧ ಕಾಂಪೋಸ್ಟ್, ಕೋಳಿ ಗೊಬ್ಬರ, ಅಥವಾ ಹಿಂಡಿ (ಬೇವಿನ ಅಥವಾ ಹರಳು ಹಿಂಡಿ) ಅನ್ವಯಿಸಿ.",
                'te': "మొక్కల మొదళ్ల చుట్టూ నత్రజని అధికంగా ఉండే కంపోస్ట్, కోళ్ల ఎరువు, లేదా నూనె కేకులు (వేప లేదా ఆముదం కేక్ వంటివి) వేయండి.",
                'hi': "पौधे के आधार के आसपास नाइट्रोजन युक्त कम्पोस्ट, मुर्गी की खाद, या खली (जैसे नीम या अरंडी की खली) डालें।"
            },
            'chemical': {
                'en': "Apply Urea as part of a balanced fertilizer schedule, often in split doses every 2-3 months. Consult local recommendations for exact rates.",
                'kn': "ಸಮತೋಲಿತ ಗೊಬ್ಬರದ ವೇಳಾಪಟ್ಟಿಯ ಭಾಗವಾಗಿ ಯೂರಿಯಾವನ್ನು ಅನ್ವಯಿಸಿ, ಸಾಮಾನ್ಯವಾಗಿ ಪ್ರತಿ 2-3 ತಿಂಗಳಿಗೊಮ್ಮೆ ವಿಭಜಿತ ಡೋಸ್‌ಗಳಲ್ಲಿ. ನಿಖರವಾದ ದರಗಳಿಗಾಗಿ ಸ್ಥಳೀಯ ಶಿಫಾರಸುಗಳನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                'te': "సమతుల్య ఎరువుల షెడ్యూల్‌లో భాగంగా యూరియాను వాడండి, తరచుగా ప్రతి 2-3 నెలలకు విభజిత మోతాదులలో. కచ్చితమైన రేట్ల కోసం స్థానిక సిఫార్సులను సంప్రదించండి.",
                'hi': "संतुलित उर्वरक अनुसूची के हिस्से के रूप में यूरिया लागू करें, अक्सर हर 2-3 महीने में विभाजित खुराकों में। सटीक दरों के लिए स्थानीय सिफारिशों से परामर्श करें।"
            }
        }
    },
    
    # --- CHECK THIS KEY NAME ---
    'Banana___Potassium_Deficiency': { # This is an EXAMPLE name, check your .npy file
        'soils': {
            'general': {
                'en': "Potassium (K) is CRITICAL for bananas. Deficiency is common in sandy, light soils (red, alluvial) due to leaching. Bananas are 'luxury consumers' of K and need a lot.",
                'kn': "ಬಾಳೆಹಣ್ಣುಗಳಿಗೆ ಪೊಟ್ಯಾಸಿಯಮ್ (K) ನಿರ್ಣಾಯಕವಾಗಿದೆ. ಮರಳು, ಹಗುರವಾದ ಮಣ್ಣುಗಳಲ್ಲಿ (ಕೆಂಪು, ಮೆಕ್ಕಲು) ಸೋರಿಕೆಯಿಂದಾಗಿ ಕೊರತೆ ಸಾಮಾನ್ಯವಾಗಿದೆ. ಬಾಳೆಹಣ್ಣುಗಳು K ಯ 'ಐಷಾರಾಮಿ ಗ್ರಾಹಕರು' ಮತ್ತು ಬಹಳಷ್ಟು ಬೇಕಾಗುತ್ತದೆ.",
                'te': "అరటిపండ్లకు పొటాషియం (K) చాలా ముఖ్యం. ఇసుక, తేలికపాటి నేలల్లో (ఎరుపు, ఒండ్రు) లీచింగ్ కారణంగా లోపం సాధారణం. అరటిపండ్లు Kను 'విలాసవంతంగా' వినియోగిస్తాయి మరియు వాటికి చాలా అవసరం.",
                'hi': "केले के लिए पोटेशियम (K) बहुत महत्वपूर्ण है। रेतीली, हल्की मिट्टी (लाल, जलोढ़) में लीचिंग के कारण कमी आम है। केले K के 'विलासिता उपभोक्ता' होते हैं और उन्हें बहुत अधिक K की आवश्यकता होती है।"
            }
        },
        'seasons': {
            'general': {
                'en': "Potassium is required in large amounts, especially during bunch formation and fruit filling. Apply in split doses throughout the year.",
                'kn': "විශೇಷವಾಗಿ ಗೊಂಚಲು ರಚನೆ ಮತ್ತು ಹಣ್ಣು ತುಂಬುವ ಸಮಯದಲ್ಲಿ ಪೊಟ್ಯಾಸಿಯಮ್ ದೊಡ್ಡ ಪ್ರಮಾಣದಲ್ಲಿ ಬೇಕಾಗುತ್ತದೆ. ವರ್ಷವಿಡೀ ವಿಭಜಿತ ಡೋಸ್‌ಗಳಲ್ಲಿ ಅನ್ವಯಿಸಿ.",
                'te': "ముఖ్యంగా గెల ఏర్పడేటప్పుడు మరియు పండ్లు నిండే సమయంలో పొటాషియం పెద్ద మొత్తంలో అవసరం. ఏడాది పొడవునా విభజిత మోతాదులలో వాడండి.",
                'hi': "पोटेशियम की बड़ी मात्रा में आवश्यकता होती है, खासकर गुच्छा बनने और फल भरने के दौरान। साल भर विभाजित खुराकों में लागू करें।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "Mulching with the banana plant's own leaves (trash) after harvest returns a significant amount of potassium to the soil.",
                'kn': "ಕೊಯ್ಲಿನ ನಂತರ ಬಾಳೆ ಗಿಡದ ಸ್ವಂತ ಎಲೆಗಳಿಂದ (ಕಸ) ಮಲ್ಚಿಂಗ್ ಮಾಡುವುದರಿಂದ ಮಣ್ಣಿಗೆ ಗಮನಾರ್ಹ ಪ್ರಮಾಣದ ಪೊಟ್ಯಾಸಿಯಮ್ ಮರಳುತ್ತದೆ.",
                'te': "పంట కోసిన తర్వాత అరటి మొక్కల ఆకులతో (చెత్త) మల్చింగ్ చేయడం వల్ల నేలకు గణనీయమైన మొత్తంలో పొటాషియం తిరిగి వస్తుంది.",
                'hi': "कटाई के बाद केले के पौधे की अपनी पत्तियों (कचरे) से मल्चिंग करने से मिट्टी में पोटेशियम की महत्वपूर्ण मात्रा वापस आ जाती है।"
            },
            'organic': {
                'en': "Apply wood ash (if soil is not alkaline). Sulfate of Potash (SOP) is often available in organic-approved forms.",
                'kn': "ಮರದ ಬೂದಿಯನ್ನು ಅನ್ವಯಿಸಿ (ಮಣ್ಣು ಕ್ಷಾರೀಯವಾಗಿಲ್ಲದಿದ್ದರೆ). ಸಲ್ಫೇಟ್ ಆಫ್ ಪೊಟ್ಯಾಶ್ (SOP) ಸಾವಯವ-ಅನುಮೋದಿತ ರೂಪಗಳಲ್ಲಿ ಲಭ್ಯವಿದೆ.",
                'te': "కలప బూడిదను వాడండి (నేల క్షారంగా లేకపోతే). సల్ఫేట్ ఆఫ్ పొటాష్ (SOP) తరచుగా సేంద్రియ-ఆమోదిత రూపాల్లో లభిస్తుంది.",
                'hi': "लकड़ी की राख (यदि मिट्टी क्षारीय नहीं है) लागू करें। सल्फेट ऑफ पोटाश (SOP) अक्सर जैविक-अनुमोदित रूपों में उपलब्ध होता है।"
            },
            'chemical': {
                'en': "Apply Muriate of Potash (MOP / KCl) in split doses throughout the year, based on soil testing. Bananas require a high N:K ratio, often 1:3.",
                'kn': "ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ ಆಧಾರದ ಮೇಲೆ ಮ್ಯೂರಿಯೇಟ್ ಆಫ್ ಪೊಟ್ಯಾಶ್ (MOP / KCl) ಅನ್ನು ವರ್ಷವಿಡೀ ವಿಭಜಿತ ಡೋಸ್‌ಗಳಲ್ಲಿ ಅನ್ವಯಿಸಿ. ಬಾಳೆಹಣ್ಣುಗಳಿಗೆ ಹೆಚ್ಚಿನ N:K ಅನುಪಾತ, ಸಾಮಾನ್ಯವಾಗಿ 1:3 ಬೇಕಾಗುತ್ತದೆ.",
                'te': "నేల పరీక్ష ఆధారంగా మ్యూరియేట్ ఆఫ్ పొటాష్ (MOP / KCl) ను ఏడాది పొడవునా విభజిత మోతాదులలో వాడండి. అరటిపండ్లకు అధిక N:K నిష్పత్తి, తరచుగా 1:3 అవసరం.",
                'hi': "मिट्टी परीक्षण के आधार पर म्यूरेट ऑफ पोटाश (MOP / KCl) को साल भर विभाजित खुराकों में लागू करें। केले को उच्च N:K अनुपात, अक्सर 1:3 की आवश्यकता होती है।"
            }
        }
    },
    
    # --- CHECK THIS KEY NAME ---
    'Banana___Sulphur_Deficiency': { # This is an EXAMPLE name, check your .npy file
        'soils': {
            'general': {
                'en': "Sulphur deficiency often appears in sandy soils (like some red or alluvial soils) and soils with low organic matter, as it is held by organic matter.",
                'kn': "ಸಲ್ಫರ್ ಕೊರತೆಯು ಮರಳು ಮಣ್ಣುಗಳಲ್ಲಿ (ಕೆಲವು ಕೆಂಪು ಅಥವಾ ಮೆಕ್ಕಲು ಮಣ್ಣುಗಳಂತಹ) ಮತ್ತು ಕಡಿಮೆ ಸಾವಯವ ಪದಾರ್ಥಗಳಿರುವ ಮಣ್ಣುಗಳಲ್ಲಿ ಹೆಚ್ಚಾಗಿ ಕಂಡುಬರುತ್ತದೆ, ಏಕೆಂದರೆ ಇದನ್ನು ಸಾವಯವ ಪದಾರ್ಥಗಳು ಹಿಡಿದಿಟ್ಟುಕೊಳ್ಳುತ್ತವೆ.",
                'te': "సల్ఫర్ లోపం ఇసుక నేలల్లో (కొన్ని ఎర్ర లేదా ఒండ్రు నేలల వంటివి) మరియు తక్కువ సేంద్రియ పదార్థం ఉన్న నేలల్లో తరచుగా కనిపిస్తుంది, ఎందుకంటే ఇది సేంద్రియ పదార్థం ద్వారా పట్టుకోబడుతుంది.",
                'hi': "सल्फर की कमी अक्सर रेतीली मिट्टी (जैसे कुछ लाल या जलोढ़ मिट्टी) और कम जैविक पदार्थ वाली मिट्टी में दिखाई देती है, क्योंकि यह जैविक पदार्थ द्वारा धारण किया जाता है।"
            }
        },
        'seasons': {
            'general': {
                'en': "Sulphur is needed for new growth, so symptoms (yellowing of *new* leaves) can appear at any time during active growth.",
                'kn': "ಹೊಸ ಬೆಳವಣಿಗೆಗೆ ಸಲ್ಫರ್ ಬೇಕಾಗುತ್ತದೆ, ಆದ್ದರಿಂದ ರೋಗಲಕ್ಷಣಗಳು (ಹೊಸ ಎಲೆಗಳ ಹಳದಿ ಬಣ್ಣ) ಸಕ್ರಿಯ ಬೆಳವಣಿಗೆಯ ಸಮಯದಲ್ಲಿ ಯಾವುದೇ ಸಮಯದಲ್ಲಿ ಕಾಣಿಸಿಕೊಳ್ಳಬಹುದು.",
                'te': "కొత్త పెరుగుదలకు సల్ఫర్ అవసరం, కాబట్టి లక్షణాలు (కొత్త ఆకులు పసుపు రంగులోకి మారడం) చురుకైన పెరుగుదల సమయంలో ఎప్పుడైనా కనిపించవచ్చు.",
                'hi': "नई वृद्धि के लिए सल्फर की आवश्यकता होती है, इसलिए लक्षण (नई पत्तियों का पीला पड़ना) सक्रिय वृद्धि के दौरान किसी भी समय दिखाई दे सकते हैं।"
            }
        },
        'action_plan': {
            'cultural': {
                'en': "Improve soil organic matter with heavy applications of compost or manure.",
                'kn': "ಕಾಂಪೋಸ್ಟ್ ಅಥವಾ ಗೊಬ್ಬರದ ಭಾರಿ ಅನ್ವಯಗಳೊಂದಿಗೆ ಮಣ್ಣಿನ ಸಾವಯವ ಪದಾರ್ಥವನ್ನು ಸುಧಾರಿಸಿ.",
                'te': "కంపోస్ట్ లేదా ఎరువును అధికంగా వాడటం ద్వారా నేల సేంద్రియ పదార్థాన్ని మెరుగుపరచండి.",
                'hi': "कम्पोस्ट या खाद के भारी अनुप्रयोगों के साथ मिट्टी के जैविक पदार्थ में सुधार करें।"
            },
            'organic': {
                'en': "Apply gypsum (Calcium Sulfate) or organic-approved forms of elemental sulfur.",
                'kn': "ಜಿಪ್ಸಮ್ (ಕ್ಯಾಲ್ಸಿಯಂ ಸಲ್ಫೇಟ್) ಅಥವಾ ಸಾವಯವ-ಅನುಮೋದಿತ ಧಾತುರೂಪದ ಗಂಧಕದ ರೂಪಗಳನ್ನು ಅನ್ವಯಿಸಿ.",
                'te': "జిప్సం (కాల్షియం సల్ఫేట్) లేదా సేంద్రియ-ఆమోదిత మూలక గంధకం రూపాలను వాడండి.",
                'hi': "जिप्सम (कैल्शियम सल्फेट) या तात्विक सल्फर के जैविक-अनुमोदित रूपों को लागू करें।"
            },
            'chemical': {
                'en': "Use fertilizers containing sulphate, such as Ammonium Sulphate (if N is also needed) or Sulphate of Potash (if K is also needed).",
                'kn': "ಸಲ್ಫೇಟ್ ಹೊಂದಿರುವ ಗೊಬ್ಬರಗಳನ್ನು ಬಳಸಿ, ಉದಾಹರಣೆಗೆ ಅಮೋನಿಯಂ ಸಲ್ಫೇಟ್ (N ಕೂಡ ಅಗತ್ಯವಿದ್ದರೆ) ಅಥವಾ ಸಲ್ಫೇಟ್ ಆಫ್ ಪೊಟ್ಯಾಶ್ (K ಕೂಡ ಅಗತ್ಯವಿದ್ದರೆ).",
                'te': "సల్ఫేట్ ఉన్న ఎరువులను వాడండి, ఉదాహరణకు అమ్మోనియం సల్ఫేట్ (N కూడా అవసరమైతే) లేదా సల్ఫేట్ ఆఫ్ పొటాష్ (K కూడా అవసరమైతే).",
                'hi': "सल्फेट युक्त उर्वरकों का उपयोग करें, जैसे अमोनियम सल्फेट (यदि एन की भी आवश्यकता हो) या सल्फेट ऑफ पोटाश (यदि के की भी आवश्यकता हो)।"
            }
        }
    },
    

    # -------------------------
    # DEFAULT
    # -------------------------
    'default': {
        'soils': {
            'red': {
                'en': "Ensure good drainage as red soils can compact.",
                'hi': "अच्छी जल निकासी सुनिश्चित करें क्योंकि लाल मिट्टी संघनित हो सकती है।",
                'kn': "ಕೆಂಪು ಮಣ್ಣು ಸಾಂದ್ರವಾಗುವುದರಿಂದ ಉತ್ತಮ ಒಳಚರಂಡಿಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
                'te': "ఎర్ర నేలలు కుదించగలవు కాబట్టి మంచి డ్రైనేజీని నిర్ధారించుకోండి."
            },
            'black': {
                'en': "Be careful of waterlogging in heavy black soils.",
                'hi': "भारी काली मिट्टी में जलभराव से सावधान रहें।",
                'kn': "ಭಾರೀ ಕಪ್ಪು ಮಣ್ಣಿನಲ್ಲಿ ನೀರು ನಿಲ್ಲದಂತೆ ಎಚ್ಚರವಹಿಸಿ.",
                'te': "భారీ నల్ల నేలలలో నీటి నిల్వ పట్ల జాగ్రత్తగా ఉండండి."
            },
            'alluvial': {
                'en': "Generally good soil, maintain balanced fertility.",
                'hi': "आम तौर पर अच्छी मिट्टी, संतुलित उर्वरता बनाए रखें।",
                'kn': "ಸಾಮಾನ್ಯವಾಗಿ ಉತ್ತಮ ಮಣ್ಣು, ಸಮತೋಲಿತ ಫಲವತ್ತತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ.",
                'te': "సాధారణంగా మంచి నేల, సమతుల్య సంతానోత్పత్తిని నిర్వహించండి."
            },
            'general': {
                'en': "No specific soil information available for this condition.",
                'kn': "ಈ ಸ್ಥಿತಿಗೆ ನಿರ್ದಿಷ್ಟ ಮಣ್ಣಿನ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ.",
                'te': "ఈ పరిస్థితికి నిర్దిష్ట నేల సమాచారం అందుబాటులో లేదు.",
                'hi': "इस स्थिति के लिए कोई विशिष्ट मिट्टी की जानकारी उपलब्ध नहीं है।"
            }
        },

        'seasons': {
            'monsoon': {
                'en': "Monitor for high humidity diseases.",
                'hi': "उच्च आर्द्रता वाले रोगों की निगरानी करें।",
                'kn': "ಹೆಚ್ಚಿನ ತೇವಾಂಶದ ರೋಗಗಳಿಗಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ.",
                'te': "அதிक తేమ వ్యాధుల కోసం పర్యవేక్షించండి."
            },
            'summer': {
                'en': "Watch for heat stress and manage irrigation.",
                'hi': "गर्मी के तनाव पर ध्यान दें और सिंचाई का प्रबंधन करें।",
                'kn': "ಶಾಖದ ಒತ್ತಡವನ್ನು ಗಮನಿಸಿ ಮತ್ತು ನೀರಾವರಿ ನಿರ್ವಹಿಸಿ.",
                'te': "వేడి ఒత్తిడి కోసం చూడండి మరియు నీటిపారుదలని నిర్వహించండి."
            },
            'winter': {
                'en': "Protect from frost if in a susceptible area.",
                'hi': "यदि संवेदनशील क्षेत्र में हो तो पाले से बचाएं।",
                'kn': "ಸೂಕ್ಷ್ಮ ಪ್ರದೇಶದಲ್ಲಿದ್ದರೆ ಹಿಮದಿಂದ ರಕ್ಷಿಸಿ.",
                'te': "సున్నితమైన ప్రాంతంలో ఉంటే మంచు నుండి రక్షించండి."
            },
            'general': {
                'en': "No specific seasonal information available for this condition.",
                'kn': "ಈ ಸ್ಥಿತಿಗೆ ನಿರ್ದಿಷ್ಟ ಋತುಮಾನದ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ.",
                'te': "ఈ పరిస్థితికి నిర್ದిష్ట కాలానుగుణ సమాచారం అందుబాటులో లేదు.",
                'hi': "इस स्थिति के लिए कोई विशिष्ट मौसमी जानकारी उपलब्ध नहीं है।"
            }
        },

        'action_plan': {
            'cultural': {
                'en': "Ensure good farm sanitation, remove infected debris, and ensure proper plant spacing.",
                'kn': "ಉತ್ತಮ ಕೃಷಿ ನೈರ್ಮಲ್ಯವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ, ಸೋಂಕಿತ ಅವಶೇಷಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಸರಿಯಾದ ಸಸ್ಯ ಅಂತರವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
                'te': "మంచి వ్యవసాయ పారిశుధ్యాన్ని నిర్ధారించండి, సోకిన శిధిలాలను తొలగించండి మరియు మొక్కల మధ్య సరైన దూరాన్ని నిర్ధారించండి.",
                'hi': "अच्छी कृषि स्वच्छता सुनिश्चित करें, संक्रमित मलबे को हटा दें, और पौधों के बीच उचित दूरी सुनिश्चित करें।"
            },
            'organic': {
                'en': "Consider neem oil or copper-based sprays where appropriate.",
                'kn': "ಸೂಕ್ತವಾದಲ್ಲಿ ಬೇವಿನ ಎಣ್ಣೆ ಅಥವಾ ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳನ್ನು ಪರಿಗಣಿಸಿ.",
                'te': "తగిన చోట వేప నూనె లేదా రాగి ఆధಾರిత స్ప్రేలను పరిగణించండి.",
                'hi': "जहाँ उपयुक्त हो वहाँ नीम के तेल या तांबे पर आधारित स्प्रे पर विचार करें।"
            },
            'chemical': {
                'en': "Consult your local agricultural extension for chemical recommendations.",
                'kn': "ರಾಸಾಯನಿಕ ಶಿಫಾರಸುಗಳಿಗಾಗಿ ನಿಮ್ಮ ಸ್ಥಳೀಯ ಕೃಷಿ ವಿಸ್ತರಣೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
                'te': "రసాయన సిఫార్సుల కోసం మీ స్థానిక వ్యవసాయ విస్తరణను సంప్రదించండి.",
                'hi': "रासायनिक सिफारिशों के लिए अपने स्थानीय कृषि विस्तार से परामर्श करें।"
            }
        }
    }
}
