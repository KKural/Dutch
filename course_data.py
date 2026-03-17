# -*- coding: utf-8 -*-
"""All course data for Dutch B1 Part 2 Interactive Course.

Enhanced version with:
- Detailed grammar (theory + Let op! + extra examples + quick reference)
- 12-15 exercises per session (fill, choice, tf, translate, reorder)
- Hints on questions
- Modelled on Net-box / NT2 Threshold 2 style
"""

import random as _rnd
CHAPTERS = [
    {"id": 1, "name": "Vrije Tijd", "icon": "🎉",
        "desc": "Free Time & Hobbies", "pages": "p. 3–8", "sessions": [1, 2, 3]},
    {"id": 2, "name": "Een Verhaal Vertellen", "icon": "📖",
        "desc": "Telling a Story", "pages": "p. 9–14", "sessions": [4, 5]},
    {"id": 3, "name": "Gezond Eten & Bewegen", "icon": "🥗",
        "desc": "Healthy Eating & Exercise", "pages": "p. 15–19", "sessions": [6, 7]},
    {"id": 4, "name": "Bij de Dokter", "icon": "🏥",
        "desc": "At the Doctor", "pages": "p. 20–26", "sessions": [8]},
    {"id": 5, "name": "Gent", "icon": "🏰", "desc": "Ghent — Your City!",
        "pages": "p. 27–31", "sessions": [9]},
    {"id": 6, "name": "Inpakken & Wegwezen", "icon": "✈️",
        "desc": "Travel", "pages": "p. 32–40", "sessions": [10]},
    {"id": 7, "name": "Grammatica", "icon": "📝", "desc": "Grammar Deep-Dive",
        "pages": "p. 42–79", "sessions": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]},
    {"id": 8, "name": "Examenvoorbereiding", "icon": "🎯",
        "desc": "Exam Preparation", "pages": "—", "sessions": [21, 22, 23, 24, 25]},
]

SESSIONS = [
    # =====================================================================
    # SESSION 1 — Weekend Vocabulary & Al eens / Nog nooit
    # =====================================================================
    {
        "id": 1,
        "title": "Weekend Vocabulary & Al eens / Nog nooit",
        "chapter": "Vrije Tijd",
        "book_page": "p. 3",
        "review": [],
        "vocabulary": [
            {"nl": "zich vervelen", "en": "to be bored",
                "ex": "Ik verveel me nooit in Gent."},
            {"nl": "het pretpark", "en": "amusement park",
                "ex": "Walibi is een groot pretpark."},
            {"nl": "de loopband", "en": "treadmill",
                "ex": "Op zondag ga ik naar de loopband."},
            {"nl": "bijkletsen",
                "en": "to catch up (chat)", "ex": "Ik wil met collega's bijkletsen."},
            {"nl": "voederen",
                "en": "to feed (animals)", "ex": "Eendjes voederen aan de Leie."},
            {"nl": "de draaimolen", "en": "merry-go-round",
                "ex": "Kinderen zitten op de draaimolen."},
            {"nl": "de botsauto", "en": "bumper car",
                "ex": "We reden botsauto op de kermis."},
            {"nl": "mottig",
                "en": "annoyed / fed up (Flemish)", "ex": "Daar word ik mottig van."},
            {"nl": "in de wolken zijn", "en": "to be over the moon",
                "ex": "Ze was in de wolken!"},
            {"nl": "al eens",
                "en": "already (once)", "ex": "Heb je al eens sushi gegeten?"},
            {"nl": "nog nooit",
                "en": "never (yet)", "ex": "Ik heb nog nooit sushi gegeten."},
            {"nl": "de kermis", "en": "funfair", "ex": "De kermis is in oktober."},
            {"nl": "uitslapen", "en": "to sleep in",
                "ex": "Op zaterdag slaap ik uit."},
        ],

        # ── GRAMMAR ──
        "grammar_title": "Al eens / Nog nooit (+ Perfectum)",
        "grammar_html": """
<h4>What is this about?</h4>
<p>In Dutch, to talk about experiences (things you have or haven't done), you use the <strong>perfectum</strong>
(present perfect) with the expressions <em>al eens</em> and <em>nog nooit</em>.</p>

<h4>How to form the Perfectum</h4>
<p>The perfectum = <strong>hebben / zijn</strong> (conjugated) + <strong>past participle</strong> (voltooid deelwoord)</p>

<table>
<tr><th>Step</th><th>How</th><th>Example</th></tr>
<tr><td>1. Find the stem</td><td>Remove -en from infinitive</td><td>werk<strong>en</strong> → werk</td></tr>
<tr><td>2. Regular: add ge-…-t or ge-…-d</td><td>Last letter of stem in 't kofschip → -t, otherwise → -d</td><td>ge<strong>werk</strong>t / ge<strong>speel</strong>d</td></tr>
<tr><td>3. Irregular: memorise!</td><td>See list below</td><td>gaan → gegaan, eten → gegeten</td></tr>
</table>

<h4>Hebben or Zijn?</h4>
<p>Most verbs use <strong>hebben</strong>. Use <strong>zijn</strong> for:</p>
<ul>
<li>Verbs of <strong>movement from A to B</strong>: gaan, komen, rijden, vliegen, lopen, fietsen, vertrekken, verhuizen</li>
<li>Verbs of <strong>change of state</strong>: worden, groeien, sterven, beginnen, stoppen</li>
<li><strong>zijn</strong> and <strong>blijven</strong> themselves</li>
</ul>

<h4>Al eens / Nog nooit Pattern</h4>
<table>
<tr><th>Question</th><th>Yes answer</th><th>No answer</th></tr>
<tr><td>Heb je <em>al eens</em> sushi gegeten?</td><td>Ja, ik heb <em>al eens</em> sushi gegeten.</td><td>Nee, ik heb <em>nog nooit</em> sushi gegeten.</td></tr>
<tr><td>Ben je <em>al eens</em> naar Parijs geweest?</td><td>Ja, ik ben <em>al eens</em> naar Parijs geweest.</td><td>Nee, ik ben er <em>nog nooit</em> geweest.</td></tr>
</table>
<p><strong>🇬🇧 English comparison:</strong> "Have you ever…?" = <em>Heb je al eens…?</em> · "I have never…" = <em>Ik heb nog nooit…</em></p>
""",

        "grammar_letop": """
<ul>
<li><span class="wrong">Heb je al eens naar Parijs gegaan?</span> → <span class="right">Ben je al eens naar Parijs geweest?</span><br>
   <em>gaan</em> uses <strong>zijn</strong>, not hebben! And for "been to a place" use <em>geweest</em>.</li>
<li><span class="wrong">Ik heb nog nooit gegaan naar Brussel.</span> → <span class="right">Ik ben nog nooit naar Brussel geweest.</span><br>
   The past participle goes to the <strong>end</strong> of the sentence!</li>
<li><span class="wrong">Ik heb al nooit dat gedaan.</span> → <span class="right">Ik heb dat nog nooit gedaan.</span><br>
   <em>nog nooit</em> is the pair (never use <em>al nooit</em>).</li>
</ul>
""",

        "grammar_extra": """
<p><strong>Common irregular past participles you need:</strong></p>
<table>
<tr><th>Infinitief</th><th>Perfectum</th><th>Hebben/Zijn</th></tr>
<tr><td>gaan</td><td>ben gegaan</td><td>zijn</td></tr>
<tr><td>komen</td><td>ben gekomen</td><td>zijn</td></tr>
<tr><td>eten</td><td>heb gegeten</td><td>hebben</td></tr>
<tr><td>drinken</td><td>heb gedronken</td><td>hebben</td></tr>
<tr><td>zien</td><td>heb gezien</td><td>hebben</td></tr>
<tr><td>doen</td><td>heb gedaan</td><td>hebben</td></tr>
<tr><td>zijn</td><td>ben geweest</td><td>zijn</td></tr>
<tr><td>schrijven</td><td>heb geschreven</td><td>hebben</td></tr>
<tr><td>lezen</td><td>heb gelezen</td><td>hebben</td></tr>
<tr><td>rijden</td><td>heb/ben gereden</td><td>both (depends on context)</td></tr>
</table>

<p><strong>More example sentences:</strong></p>
<ul>
<li><em>Heb je al eens frieten met stoofvlees gegeten?</em> — Have you ever eaten fries with stew?</li>
<li><em>Ik heb nog nooit een huis gekocht.</em> — I have never bought a house.</li>
<li><em>Ben je al eens naar de Gentse Feesten geweest?</em> — Have you ever been to the Ghent Festivities?</li>
<li><em>We hebben al eens in een restaurant in de Veldstraat gegeten.</em></li>
<li><em>Zij is nog nooit met de trein naar Brussel gereden.</em></li>
</ul>
""",

        "grammar_quick": """
<ul>
<li><strong>al eens</strong> = positive experience ("already/ever")</li>
<li><strong>nog nooit</strong> = negative experience ("never yet")</li>
<li>Always use <strong>perfectum</strong> (hebben/zijn + voltooid deelwoord)</li>
<li>Past participle goes to the <strong>END</strong></li>
<li>zijn for movement (A→B) and change of state</li>
</ul>
""",

        # ── EXERCISES (15) ──
        "exercises": [
            {"type": "fill", "q": "Je collega vraagt over je weekend: 'Heb je ___ stoofvlees gegeten?' (positive = already once)", "a": "al eens",
             "tip": "The positive version of 'ever' in Dutch is two words: al + eens."},
            {"type": "fill", "q": "Op een feestje in Gent: 'Nee, ik heb ___ stoofvlees gegeten!' (negative = never yet)", "a": "nog nooit",
             "tip": "The negative pair of 'al eens' is 'nog nooit'. Two words!"},
            {"type": "fill", "q": "Ik heb het hele weekend op UGent ___. (werken → past participle)", "a": "gewerkt",
             "tip": "Stem = werk. Last letter k is in 't kofschip → ge-…-t: gewerkt."},
            {"type": "fill", "q": "Vorige zomer ben ik naar Brugge ___. (gaan → past participle)", "a": "gegaan",
             "tip": "Irregular! gaan → gegaan. Movement verb → use zijn."},
            {"type": "fill", "q": "We hebben gisteren op de Korenmarkt Belgische frieten ___. (eten)", "a": "gegeten",
             "tip": "Irregular: eten → gegeten. Eating is not movement → hebben."},
            {"type": "fill", "q": "Ben je al eens naar het Gravensteen ___? (gaan — careful: which auxiliary?)", "a": "gegaan",
             "tip": "Gaan = movement → ben gegaan (not heb!). Gravensteen is Ghent's famous castle."},
            {"type": "fill", "q": "Mijn vriend is vorig jaar uit India ___. (komen → past participle)", "a": "gekomen",
             "tip": "Irregular: komen → gekomen. Coming = movement → use zijn."},
            {"type": "choice", "q": "Je vertelt over je weekend. Which is correct?", "options": ["Ik heb naar Brussel gegaan.", "Ik ben naar Brussel gegaan.", "Ik heb naar Brussel geweest."], "a": "Ik ben naar Brussel gegaan.",
             "tip": "Gaan = movement verb → always use ZIJN. Ik BEN gegaan."},
            {"type": "choice", "q": "Aan tafel in een Belgisch restaurant. Which is correct?", "options": ["Ik heb al eens mosselen gegeten.", "Ik ben al eens mosselen gegeten.", "Ik heb al eens mosselen eten."], "a": "Ik heb al eens mosselen gegeten.",
             "tip": "Eten = not a movement verb → hebben. Past participle gegeten at the end."},
            {"type": "tf", "q": "'Ik heb al eens naar Gent gegaan' is correct Dutch.", "a": False,
             "correction": "Gaan uses ZIJN: Ik BEN al eens naar Gent gegaan.",
             "tip": "Gaan = movement → zijn, not hebben!"},
            {"type": "tf", "q": "'Heb je nog nooit Belgische chocolade gegeten?' is correct.", "a": True,
             "correction": "Correct! Hebben + nog nooit + past participle at end ✓",
             "tip": "Eten → hebben. Word order: auxiliary + nog nooit + … + participle at end."},
            {"type": "tf", "q": "'Ik ben al eens op de Korenmarkt een pintje gedronken' is correct.", "a": False,
             "correction": "Drinken uses HEBBEN: Ik HEB al eens op de Korenmarkt een pintje gedronken.",
             "tip": "Drinken = not a movement verb → auxiliary is hebben, not zijn!"},
            {"type": "translate", "q": "Have you ever been to the Gentse Feesten?", "a": "Ben je al eens naar de Gentse Feesten geweest?",
             "tip": "been to = geweest (zijn). 'De Gentse Feesten' = Ghent's famous festival."},
            {"type": "translate", "q": "I have never cycled in Belgium.", "a": "Ik heb nog nooit in België gefietst.",
             "tip": "fietsen → gefietst (ge-…-t, s is in kofschip). Fietsen = not movement A→B → hebben."},
            {"type": "reorder", "q": "nooit / nog / heb / ik / gegeten / wafels",
             "a": "Ik heb nog nooit wafels gegeten.",
             "tip": "Subject + auxiliary + nog nooit + object + past participle at END."},
        ],

        "jouw_beurt": "Write 5 sentences about things you have or haven't done since moving to Ghent.\nUse: Ik heb al eens … / Ik heb nog nooit … / Ben je al eens …?\n\nIdeas: Gentse Feesten, frieten, fietsen in België, Gravensteen, stoofvlees",
    },

    # =====================================================================
    # SESSION 2 — Social Media & Giving Opinions
    # =====================================================================
    {
        "id": 2,
        "title": "Social Media & Giving Opinions",
        "chapter": "Vrije Tijd",
        "book_page": "p. 4–7",
        "review": [
            {"q": "How do you say 'I have never eaten sushi'?",
                "a": "Ik heb nog nooit sushi gegeten."},
            {"q": "Perfectum of 'gaan' (ik)?", "a": "ik ben gegaan"},
            {"q": "What does 'mottig' mean?",
                "a": "annoyed / fed up (Flemish)"},
            {"q": "'schrijven' → perfectum?", "a": "ik heb geschreven"},
        ],
        "vocabulary": [
            {"nl": "Ik denk dat…", "en": "I think that…",
                "ex": "Ik denk dat sociale media gevaarlijk zijn."},
            {"nl": "Ik vind dat…", "en": "I find/think that…",
                "ex": "Ik vind dat het nuttig is."},
            {"nl": "Volgens mij…", "en": "In my opinion…",
                "ex": "Volgens mij is dat waar."},
            {"nl": "Ik ga akkoord.", "en": "I agree.",
                "ex": "Ik ga akkoord met jou."},
            {"nl": "Ik ben het (niet) eens.", "en": "I (dis)agree.",
             "ex": "Ik ben het niet met je eens."},
            {"nl": "Ja, da's waar.",
                "en": "Yes, that's true. (Flemish)", "ex": "Ja, da's waar!"},
            {"nl": "Ik vind van wel.", "en": "I think so.", "ex": "—"},
            {"nl": "Ik vind van niet.", "en": "I don't think so.", "ex": "—"},
            {"nl": "Je zou … kunnen", "en": "You could …",
                "ex": "Je zou je telefoon vaker kunnen uitzetten."},
            {"nl": "Misschien kan je …", "en": "Maybe you can …",
                "ex": "Misschien kan je meer lezen."},
            {"nl": "gevaarlijk", "en": "dangerous",
                "ex": "Sociale media zijn gevaarlijk."},
            {"nl": "nuttig / nutteloos", "en": "useful / useless",
                "ex": "Instagram is nutteloos."},
            {"nl": "verslaafd aan", "en": "addicted to",
                "ex": "Jongeren zijn verslaafd aan TikTok."},
        ],

        # ── GRAMMAR ──
        "grammar_title": "Ik denk dat… + Bijzin (verb to end!)",
        "grammar_html": """
<h4>What is a bijzin?</h4>
<p>A <strong>bijzin</strong> (subordinate clause) is a part of a sentence that starts with a <em>voegwoord</em>
(conjunction) like <strong>dat, omdat, als, toen, voordat, nadat, terwijl</strong>.
In a bijzin, the <strong>conjugated verb moves to the END</strong> of the clause.</p>

<h4>The pattern: Ik denk dat… / Ik vind dat…</h4>
<table>
<tr><th>Main clause</th><th>Bijzin</th></tr>
<tr><td>Ik denk</td><td><strong>dat</strong> sociale media gevaarlijk <strong>zijn</strong>.</td></tr>
<tr><td>Ik vind</td><td><strong>dat</strong> het internet nuttig <strong>is</strong>.</td></tr>
<tr><td>Ik geloof</td><td><strong>dat</strong> je gelijk <strong>hebt</strong>.</td></tr>
</table>

<h4>Normal sentence → dat-sentence comparison</h4>
<table>
<tr><th>Normal (main clause)</th><th>With "dat" (bijzin)</th></tr>
<tr><td>Sociale media <strong>zijn</strong> gevaarlijk.</td><td>Ik denk dat sociale media gevaarlijk <strong>zijn</strong>.</td></tr>
<tr><td>Het internet <strong>is</strong> nuttig.</td><td>Ik vind dat het internet nuttig <strong>is</strong>.</td></tr>
<tr><td>Je <strong>hebt</strong> gelijk.</td><td>Ik geloof dat je gelijk <strong>hebt</strong>.</td></tr>
</table>

<p><strong>🇬🇧 English comparison:</strong> "I think <em>that</em> it <em>is</em> dangerous." — the verb stays in place.
In Dutch, the verb JUMPS to the END after <em>dat</em>!</p>

<h4>Volgens mij + Inversie</h4>
<p>When you start with <em>Volgens mij</em> (or any non-subject), the verb comes SECOND (V2 rule) and the subject follows:</p>
<p><em><strong>Volgens mij</strong> <strong>is</strong> dat waar.</em> (not: ~~Volgens mij dat is waar.~~)</p>
""",

        "grammar_letop": """
<ul>
<li><span class="wrong">Ik denk dat sociale media zijn gevaarlijk.</span> →
    <span class="right">Ik denk dat sociale media gevaarlijk <strong>zijn</strong>.</span><br>
    After <em>dat</em>, the verb goes to the END, not in position 2!</li>
<li><span class="wrong">Volgens mij dat is goed.</span> →
    <span class="right">Volgens mij <strong>is</strong> dat goed.</span><br>
    <em>Volgens mij</em> triggers inversie (V2): verb before subject.</li>
<li><span class="wrong">Ik denk dat het is nuttig.</span> →
    <span class="right">Ik denk dat het nuttig <strong>is</strong>.</span><br>
    The verb must be at the very END of the bijzin.</li>
<li><span class="wrong">Ik vind het goed dat je komt hier.</span> →
    <span class="right">Ik vind het goed dat je hier <strong>komt</strong>.</span><br>
    Everything before the verb — including place words!</li>
</ul>
""",

        "grammar_extra": """
<p><strong>More opinion starters you can use:</strong></p>
<ul>
<li><em>Ik geloof dat …</em> — I believe that…</li>
<li><em>Ik weet dat …</em> — I know that…</li>
<li><em>Ik hoop dat …</em> — I hope that…</li>
<li><em>Het is duidelijk dat …</em> — It is clear that…</li>
<li><em>Het is belangrijk dat …</em> — It is important that…</li>
</ul>

<p><strong>Full example sentences:</strong></p>
<ul>
<li><em>Ik denk dat de universiteit een goede plek <strong>is</strong>.</em></li>
<li><em>Volgens mij <strong>moeten</strong> kinderen minder op hun telefoon zitten.</em></li>
<li><em>Ik vind dat Gent de mooiste stad van België <strong>is</strong>.</em></li>
<li><em>Het is belangrijk dat je elke dag Nederlands <strong>oefent</strong>.</em></li>
<li><em>Ik hoop dat ik snel beter Nederlands <strong>spreek</strong>.</em></li>
</ul>

<p><strong>Agreeing and disagreeing — full dialogues:</strong></p>
<p>A: <em>Ik vind dat sociale media gevaarlijk zijn.</em><br>
B: <em>Ja, da's waar. Ik ga akkoord.</em> / <em>Nee, ik ben het er niet mee eens. Ik denk dat ze nuttig zijn.</em></p>
""",

        "grammar_quick": """
<ul>
<li>After <strong>dat, omdat, als, toen, terwijl</strong> → verb to <strong>END</strong></li>
<li>After <strong>Volgens mij, Misschien, etc.</strong> → <strong>inversie</strong> (V2: verb before subject)</li>
<li><em>Ik denk dat…</em> / <em>Ik vind dat…</em> = most common opinion patterns</li>
<li>To agree: <em>Ik ga akkoord / Ja, da's waar / Ik vind van wel</em></li>
<li>To disagree: <em>Ik ben het er niet mee eens / Ik vind van niet</em></li>
</ul>
""",

        # ── EXERCISES (15) ──
        "exercises": [
            {"type": "fill", "q": "In de les over sociale media: 'Sociale media zijn gevaarlijk.' → Ik denk dat sociale media gevaarlijk ___.", "a": "zijn",
             "tip": "In a dat-bijzin, the verb moves to the END. What was the verb? → zijn."},
            {"type": "fill", "q": "Een debat aan UGent: 'Het internet is nuttig.' → Ik vind dat het internet nuttig ___.", "a": "is",
             "tip": "After 'dat', the verb goes to the very end: nuttig IS."},
            {"type": "fill", "q": "Je medestudent klaagt over de cursus: 'Nederlands is niet makkelijk.' → Volgens mij ___ Nederlands niet makkelijk.", "a": "is",
             "tip": "'Volgens mij' triggers inversie: verb comes right after it, before subject."},
            {"type": "fill", "q": "In een e-mail aan een vriend: Ik geloof dat je gelijk ___.", "a": "hebt",
             "tip": "'hebt' is the verb — it moves to the end after 'dat'."},
            {"type": "fill", "q": "Over het nieuws: Ik vind dat kinderen meer ___ moeten. (should play more)", "a": "spelen",
             "tip": "With 2 verbs in a bijzin, both go to the end. Conjugated verb (moeten) goes LAST."},
            {"type": "fill", "q": "In een gesprek met je buurvrouw: Ik denk dat het weer morgen beter ___.", "a": "is",
             "tip": "Dat-bijzin: het weer morgen beter IS. The verb 'is' goes to the end."},
            {"type": "choice", "q": "In de klas: je leerkracht vraagt je mening over TikTok. Which is correct?", "options": [
                "Ik denk dat TikTok is gevaarlijk voor kinderen.",
                "Ik denk dat TikTok gevaarlijk voor kinderen is.",
                "Ik denk dat is TikTok gevaarlijk voor kinderen."
            ], "a": "Ik denk dat TikTok gevaarlijk voor kinderen is.",
                "tip": "Dat-bijzin → verb at the END: gevaarlijk voor kinderen IS."},
            {"type": "choice", "q": "Je schrijft een mening op een forum. Which is correct?", "options": [
                "Volgens mij WhatsApp is beter dan Instagram.",
                "Volgens mij is WhatsApp beter dan Instagram.",
                "Volgens mij beter is WhatsApp dan Instagram."
            ], "a": "Volgens mij is WhatsApp beter dan Instagram.",
                "tip": "'Volgens mij' triggers inversie: IS WhatsApp (verb before subject)."},
            {"type": "tf", "q": "'Ik denk dat sociale media zijn gevaarlijk' is correct word order.", "a": False,
             "correction": "Verb to END: Ik denk dat sociale media gevaarlijk ZIJN.",
             "tip": "In a dat-bijzin, the verb ALWAYS goes to the end."},
            {"type": "tf", "q": "'Ik vind dat Gent de mooiste stad is' has correct word order.", "a": True,
             "correction": "Correct! 'is' is at the end of the dat-clause ✓",
             "tip": "Check: is the verb at the end of the bijzin? Yes → correct!"},
            {"type": "tf", "q": "'Volgens mij het weer is slecht vandaag' is correct.", "a": False,
             "correction": "Volgens mij IS het weer slecht vandaag. (inversie!)",
             "tip": "After 'Volgens mij', the verb must come BEFORE the subject."},
            {"type": "translate", "q": "I think that Ghent is a beautiful city.", "a": "Ik denk dat Gent een mooie stad is.",
             "tip": "Use 'Ik denk dat…'. Verb 'is' to the end. beautiful city = mooie stad (de stad → +e)."},
            {"type": "translate", "q": "In my opinion, cycling in Belgium is dangerous.", "a": "Volgens mij is fietsen in België gevaarlijk.",
             "tip": "Volgens mij + inversie: IS fietsen (verb before subject)."},
            {"type": "reorder", "q": "dat / ik / vind / nuttig / het internet / is / Ik", "a": "Ik vind dat het internet nuttig is.",
             "tip": "Main clause first (Ik vind), then dat + subject + rest + verb at end."},
            {"type": "reorder", "q": "is / mij / Volgens / beter / WhatsApp / dan / Instagram", "a": "Volgens mij is WhatsApp beter dan Instagram.",
             "tip": "Volgens mij + inversie: verb in position 2. Comparative + dan."},
        ],

        "jouw_beurt": "Write your real opinion on social media (6–8 sentences).\n\nUse these starters:\n• Ik denk dat…\n• Volgens mij…\n• Ik vind dat… omdat…\n• Ik ben het (niet) eens met mensen die zeggen dat…\n\nIdeas: TikTok, Instagram, WhatsApp, nieuws, fake news, cyberpesten",
    },

    # =====================================================================
    # SESSION 3 — Sequencing & Inversie (V2 Rule)
    # =====================================================================
    {
        "id": 3,
        "title": "Sequencing & Inversie (V2 Rule)",
        "chapter": "Vrije Tijd",
        "book_page": "p. 6–8",
        "review": [
            {"q": "'Ik denk dat het mooi is.' — which word sends the verb to the end?", "a": "dat"},
            {"q": "Translate: 'Maybe you should rest more.'",
                "a": "Misschien moet je meer rusten."},
            {"q": "Dutch for 'I agree with you'?",
                "a": "Ik ga akkoord met jou. / Ik ben het met je eens."},
            {"q": "Rewrite: 'Het is goed.' → Ik vind dat…",
                "a": "Ik vind dat het goed is."},
        ],
        "vocabulary": [
            {"nl": "eerst", "en": "first", "ex": "Eerst eet ik ontbijt."},
            {"nl": "dan / daarna", "en": "then / after that",
                "ex": "Dan ga ik naar mijn werk."},
            {"nl": "vervolgens", "en": "subsequently / next",
                "ex": "Vervolgens eet ik mijn lunch."},
            {"nl": "meestal", "en": "usually", "ex": "Meestal fiets ik naar UGent."},
            {"nl": "'s ochtends", "en": "in the morning",
                "ex": "'s Ochtends drink ik koffie."},
            {"nl": "'s middags", "en": "in the afternoon",
                "ex": "'s Middags eet ik in de resto."},
            {"nl": "'s avonds", "en": "in the evening",
                "ex": "'s Avonds kijk ik Netflix."},
            {"nl": "om een uur of twaalf",
                "en": "around noon", "ex": "Om 12u eet ik."},
            {"nl": "ten slotte", "en": "finally",
                "ex": "Ten slotte ga ik slapen."},
            {"nl": "uiteindelijk", "en": "eventually",
                "ex": "Uiteindelijk vond ik het leuk."},
            {"nl": "ondertussen", "en": "meanwhile",
                "ex": "Ondertussen kookt mijn vrouw."},
            {"nl": "om … uur", "en": "at … o'clock", "ex": "Om 8 uur sta ik op."},
        ],

        # ── GRAMMAR ──
        "grammar_title": "Inversie — The Dutch V2 Rule",
        "grammar_html": """
<h4>What is the V2 Rule?</h4>
<p>In Dutch main clauses, the <strong>conjugated verb is ALWAYS in position 2</strong>.
Position 1 can be the subject, but it can also be a time word, a place, or any other element.
When something OTHER than the subject is in position 1, the subject and verb <strong>swap</strong> — this is called <strong>inversie</strong>.</p>

<h4>How it works step by step</h4>
<table>
<tr><th>Position 1</th><th>Position 2 (VERB)</th><th>Position 3</th><th>Rest</th></tr>
<tr><td><strong>Ik</strong> (subject)</td><td>loop</td><td>—</td><td>op de loopband.</td></tr>
<tr><td><strong>Eerst</strong> (time)</td><td><strong>loop</strong></td><td><strong>ik</strong></td><td>op de loopband.</td></tr>
<tr><td><strong>'s Avonds</strong> (time)</td><td><strong>kijk</strong></td><td><strong>ik</strong></td><td>Netflix.</td></tr>
<tr><td><strong>Gisteren</strong> (time)</td><td><strong>liep</strong></td><td><strong>ik</strong></td><td>in het park.</td></tr>
<tr><td><strong>In Gent</strong> (place)</td><td><strong>woon</strong></td><td><strong>ik</strong></td><td>al 3 jaar.</td></tr>
<tr><td><strong>Volgens mij</strong> (opinion)</td><td><strong>is</strong></td><td><strong>het</strong></td><td>waar.</td></tr>
</table>

<p><strong>🇬🇧 English comparison:</strong> "First <em>I run</em>…" — no swap needed in English.
Dutch: "Eerst <em>loop ik</em>…" — SWAP! The verb must stay in position 2.</p>

<h4>Time words that trigger inversie (when used at start)</h4>
<p><em>Eerst, dan, daarna, vervolgens, ten slotte, 's ochtends, 's middags, 's avonds,
gisteren, vandaag, morgen, meestal, soms, om 8 uur, daarom, misschien, volgens mij</em></p>
""",

        "grammar_letop": """
<ul>
<li><span class="wrong">Eerst ik ga naar het werk.</span> →
    <span class="right">Eerst <strong>ga ik</strong> naar het werk.</span><br>
    Time word first → verb MUST come second, then subject!</li>
<li><span class="wrong">'s Avonds ik kijk Netflix.</span> →
    <span class="right">'s Avonds <strong>kijk ik</strong> Netflix.</span><br>
    Same rule: anything in position 1 that isn't the subject → inversie.</li>
<li><span class="wrong">Gisteren ik heb gewerkt.</span> →
    <span class="right">Gisteren <strong>heb ik</strong> gewerkt.</span><br>
    With perfectum, the AUXILIARY (heb/ben) goes in position 2, not the past participle.</li>
<li><span class="wrong">Dan ik eet mijn lunch.</span> →
    <span class="right">Dan <strong>eet ik</strong> mijn lunch.</span><br>
    Every time word at the start needs inversie!</li>
</ul>
""",

        "grammar_extra": """
<p><strong>Describing your daily routine (a common exam topic!):</strong></p>
<ul>
<li><em>'s Ochtends <strong>sta</strong> ik om 7 uur op.</em> — In the morning I get up at 7.</li>
<li><em>Daarna <strong>douche</strong> ik en <strong>kleed</strong> ik me aan.</em> — Then I shower and get dressed.</li>
<li><em>Om 8 uur <strong>vertrek</strong> ik naar UGent.</em> — At 8 I leave for UGent.</li>
<li><em>Meestal <strong>fiets</strong> ik.</em> — Usually I cycle.</li>
<li><em>'s Middags <strong>eet</strong> ik in de resto.</em> — At noon I eat in the cafeteria.</li>
<li><em>'s Avonds <strong>kook</strong> ik en daarna <strong>kijk</strong> ik een film.</em></li>
<li><em>Ten slotte <strong>ga</strong> ik om 11 uur naar bed.</em></li>
</ul>

<p><strong>Two clauses connected with 'en':</strong></p>
<p>After <em>en</em>, the normal word order returns (no inversie):
<em>Eerst eet ik ontbijt <strong>en</strong> dan ga ik naar het werk.</em>
But if 'dan' starts the second clause: <em>Eerst eet ik ontbijt. Dan ga ik naar het werk.</em> → inversie in the second sentence.</p>
""",

        "grammar_quick": """
<ul>
<li>The verb is <strong>ALWAYS in position 2</strong> in a main clause</li>
<li>If position 1 ≠ subject → <strong>swap subject and verb</strong> (inversie)</li>
<li>Common triggers: time words, place phrases, opinion starters</li>
<li>With perfectum: the <strong>auxiliary</strong> (heb/ben) goes in position 2</li>
<li>This does NOT apply inside a bijzin (after dat, omdat, etc. → verb to end)</li>
</ul>
""",

        # ── EXERCISES (15) ──
        "exercises": [
            {"type": "fill", "q": "Je vertelt over je dag aan een vriend: ''s Ochtends ___ ik altijd koffie op het terras.' (drinken)", "a": "drink",
             "tip": "Time word first → inversie: verb in position 2, then subject. Drinken → ik drink."},
            {"type": "fill", "q": "Je routine in Gent: 'Eerst ___ ik ontbijt, daarna ga ik naar UGent.' (eten)", "a": "eet",
             "tip": "Eerst + verb + ik. Eten → ik eet."},
            {"type": "fill", "q": "Over gisteren: 'Gisteren ___ ik de hele dag op het labo.' (werken, imperfectum)", "a": "werkte",
             "tip": "Time word → inversie. Imperfectum of werken: stam 'werk' + te (k is in 't kofschip)."},
            {"type": "fill", "q": "Je dagelijks leven: 'Meestal ___ ik langs de Coupure naar UGent.' (fietsen)", "a": "fiets",
             "tip": "Meestal + verb + ik. Fietsen for ik = fiets. De Coupure is a canal in Ghent."},
            {"type": "fill", "q": "Je avondprogramma: ''s Avonds ___ ik een serie op Netflix.' (kijken)", "a": "kijk",
             "tip": "'s Avonds (time) starts the sentence → inversie: kijk ik."},
            {"type": "fill", "q": "Over het weekend: 'Op zaterdag ___ ik naar de markt op de Groentenmarkt.' (gaan)", "a": "ga",
             "tip": "Op zaterdag (time first) → inversie: ga ik. De Groentenmarkt is a square in Ghent."},
            {"type": "choice", "q": "Je beschrijft je ochtend aan een collega. Which is correct?", "options": [
                "Eerst ik ga naar het werk.",
                "Eerst ga ik naar het werk.",
                "Eerst ik naar het werk ga."
            ], "a": 1, "tip": "Time word (Eerst) in position 1 → verb (ga) must be in position 2 → subject (ik) in 3."},
            {"type": "choice", "q": "In een e-mail over gisteren. Which is correct?", "options": [
                "Gisteren heb ik de hele dag op UGent gewerkt.",
                "Gisteren ik heb de hele dag gewerkt.",
                "Gisteren gewerkt ik heb op UGent."
            ], "a": "Gisteren heb ik de hele dag op UGent gewerkt.",
                "tip": "Time first + perfectum → auxiliary (heb) in position 2, participle at end."},
            {"type": "tf", "q": "'Daarna ik eet mijn lunch' is correct word order.", "a": False,
             "correction": "Daarna EET IK mijn lunch. (inversie: verb before subject!)",
             "tip": "'Daarna' in position 1 → verb MUST be in position 2."},
            {"type": "tf", "q": "'Om 12 uur eet ik lunch in de mensa van UGent' is correct.", "a": True,
             "correction": "Correct! Om 12 uur (time) → eet (verb pos 2) → ik (subject pos 3) ✓",
             "tip": "Time expression first → inversie. This sentence is perfect!"},
            {"type": "tf", "q": "'Ik ga 's avonds naar de sporthal' is correct.", "a": True,
             "correction": "Correct! Ik (subject) is in position 1 → normal order, no inversie needed ✓",
             "tip": "When the subject starts the sentence, the word order stays normal."},
            {"type": "translate", "q": "In the morning I cycle to the university.", "a": "'s Ochtends fiets ik naar de universiteit.",
             "tip": "In the morning = 's Ochtends. Cycle = fietsen → ik fiets. Time first → inversie!"},
            {"type": "translate", "q": "After that we eat lunch at the Korenmarkt.", "a": "Daarna eten we lunch op de Korenmarkt.",
             "tip": "After that = Daarna. Inversie: eten we (verb before subject)."},
            {"type": "reorder", "q": "ik / Eerst / ontbijt / eet / daarna / fiets / ik / naar / UGent", "a": "Eerst eet ik ontbijt, daarna fiets ik naar UGent.",
             "tip": "Two inversie clauses: Eerst eet ik … , daarna fiets ik …"},
            {"type": "reorder", "q": "ik / 's Avonds / kook / en / serie / kijk / een / ik", "a": "'s Avonds kook ik en kijk ik een serie.",
             "tip": "Time first → inversie in both clauses: kook ik … en kijk ik …"},
        ],

        "jouw_beurt": "Describe your typical Saturday in Ghent using at least 5 time words with correct inversie.\n\nUse: 's Ochtends … / Daarna … / Om … uur … / Meestal … / 's Avonds … / Ten slotte …\n\nExample start: 's Ochtends slaap ik uit tot 9 uur. Daarna …",
    },

    # =====================================================================
    # SESSION 4 — Life Events & Imperfectum Introduction
    # =====================================================================
    {
        "id": 4,
        "title": "Life Events & Imperfectum Introduction",
        "chapter": "Een Verhaal Vertellen",
        "book_page": "p. 9–14",
        "review": [
            {"q": "How do you make inversie with 'Dan'? (example with 'gaan')",
             "a": "Dan ga ik … (verb + subject swap)"},
            {"q": "Dutch for 'subsequently'?", "a": "vervolgens"},
            {"q": "'s Avonds ___ ik Netflix. — verb or subject next?",
                "a": "verb! (kijk ik — inversie)"},
            {"q": "Put in order: eerst / ik / eet / ontbijt",
                "a": "Eerst eet ik ontbijt."},
        ],
        "vocabulary": [
            {"nl": "het hoogtepunt", "en": "highlight / high point",
                "ex": "Het hoogtepunt van mijn carrière."},
            {"nl": "het dieptepunt", "en": "low point",
                "ex": "Een dieptepunt in mijn leven."},
            {"nl": "gebuisd zijn",
                "en": "to have failed (exam) (Flemish)", "ex": "Ik ben gebuisd voor het examen."},
            {"nl": "opgebrand zijn", "en": "to be burned out",
                "ex": "Zij is opgebrand."},
            {"nl": "doodgraag",
                "en": "desperately (want sth)", "ex": "Ik wil dit doodgraag doen."},
            {"nl": "vieren", "en": "to celebrate",
                "ex": "We vierden mijn verjaardag."},
            {"nl": "overleven", "en": "to survive",
                "ex": "Ze heeft het overleefd."},
            {"nl": "het sprookje", "en": "fairy tale",
                "ex": "Er was eens een prinses…"},
            {"nl": "er was eens …", "en": "once upon a time…",
                "ex": "Er was eens een grote wolf."},
            {"nl": "ze leefden nog lang en gelukkig",
                "en": "they lived happily ever after", "ex": "—"},
            {"nl": "de levenslijn",
                "en": "timeline (of life)", "ex": "Teken je levenslijn."},
            {"nl": "geboren worden", "en": "to be born",
                "ex": "Ik ben geboren in India."},
            {"nl": "opgroeien", "en": "to grow up",
                "ex": "Ik groeide op in Chennai."},
        ],

        # ── GRAMMAR ──
        "grammar_title": "Imperfectum — Regular Verbs ('t kofschip)",
        "grammar_html": """
<h4>What is the Imperfectum?</h4>
<p>The imperfectum (simple past / onvoltooid verleden tijd) is used for past actions, especially
for <strong>habitual actions, descriptions, and stories</strong>. It's the tense you use to tell a story:
<em>Er was eens een prinses. Ze woonde in een kasteel…</em></p>

<h4>How to form it — Step by step</h4>
<ol>
<li><strong>Find the stem:</strong> Remove <em>-en</em> from the infinitive → <em>werken → werk</em></li>
<li><strong>Check 't kofschip:</strong> Is the LAST letter of the stem in <strong>'t k o f s ch p</strong>?</li>
<li><strong>Yes → add -te (singular) / -ten (plural)</strong><br>
    <em>werken → werk → werk<strong>te</strong></em> (k is in 't kofschip)</li>
<li><strong>No → add -de (singular) / -den (plural)</strong><br>
    <em>spelen → speel → speel<strong>de</strong></em> (l is NOT in 't kofschip)</li>
</ol>

<h4>'t kofschip — memorise this!</h4>
<p>The letters are: <strong>t, k, f, s, ch, p</strong>. A mnemonic: think of a ship called "'t kofschip".</p>
<table>
<tr><th>Infinitief</th><th>Stem</th><th>Last letter</th><th>In 't kofschip?</th><th>Imperfectum (ik)</th></tr>
<tr><td>werken</td><td>werk</td><td>k</td><td>YES ✓</td><td>werk<strong>te</strong></td></tr>
<tr><td>fietsen</td><td>fiets</td><td>s</td><td>YES ✓</td><td>fiet<strong>ste</strong></td></tr>
<tr><td>dansen</td><td>dans</td><td>s</td><td>YES ✓</td><td>dan<strong>ste</strong></td></tr>
<tr><td>praten</td><td>praat</td><td>t</td><td>YES ✓</td><td>praat<strong>te</strong></td></tr>
<tr><td>spelen</td><td>speel</td><td>l</td><td>NO ✗</td><td>speel<strong>de</strong></td></tr>
<tr><td>studeren</td><td>studeer</td><td>r</td><td>NO ✗</td><td>studeer<strong>de</strong></td></tr>
<tr><td>wonen</td><td>woon</td><td>n</td><td>NO ✗</td><td>woon<strong>de</strong></td></tr>
<tr><td>reizen</td><td>reis</td><td>s</td><td>YES ✓</td><td>rei<strong>sde</strong>*</td></tr>
<tr><td>leven</td><td>leef</td><td>f</td><td>YES ✓</td><td>leef<strong>de</strong>*</td></tr>
</table>

<p><strong>* Spelling traps (v→f, z→s in stem):</strong><br>
<em>leven</em> → stem = <strong>leef</strong> (v→f). Even though f IS in kofschip, historically this verb uses <strong>-de</strong>: <em>leefde</em>.<br>
<em>reizen</em> → stem = <strong>reis</strong> (z→s). Same pattern: <em>reisde</em>.<br>
The rule: when v→f or z→s happens in the stem, use <strong>-de</strong> (not -te).</p>

<h4>Conjugation table</h4>
<table>
<tr><th></th><th>-te verbs (kofschip)</th><th>-de verbs (other)</th></tr>
<tr><td>ik / jij / hij / ze</td><td>werkte</td><td>speelde</td></tr>
<tr><td>wij / jullie / zij (pl.)</td><td>werkten</td><td>speelden</td></tr>
</table>

<p><strong>🇬🇧 English comparison:</strong> Very similar! "I worked / I studied" = <em>Ik werkte / Ik studeerde</em>.
But Dutch spelling is more systematic with the -te/-de distinction.</p>
""",

        "grammar_letop": """
<ul>
<li><span class="wrong">Ik werkde gisteren.</span> →
    <span class="right">Ik werk<strong>te</strong> gisteren.</span><br>
    Stem = werk, k is in 't kofschip → use -te (not -de)!</li>
<li><span class="wrong">Ik fietsde naar UGent.</span> →
    <span class="right">Ik fiet<strong>ste</strong> naar UGent.</span><br>
    Stem = fiets, s is in 't kofschip → -te</li>
<li><span class="wrong">Ik praate met mijn collega.</span> →
    <span class="right">Ik praat<strong>te</strong> met mijn collega.</span><br>
    Stem = praat (already ends in t), add -te → praatte (double t!).</li>
<li><span class="wrong">Ik levede in India.</span> →
    <span class="right">Ik leef<strong>de</strong> in India.</span><br>
    leven → stem leef (v→f). Despite f in kofschip, v→f stems use -de.</li>
<li><span class="wrong">Wij speelde cricket.</span> →
    <span class="right">Wij speel<strong>den</strong> cricket.</span><br>
    Plural (wij) → add -den (not -de)!</li>
</ul>
""",

        "grammar_extra": """
<h4>Onregelmatige imperfectumvormen (Irregular — MUST memorise!)</h4>
<p>De 't kofschip-regel geldt alleen voor <b>regelmatige werkwoorden</b>. Veel veelgebruikte werkwoorden zijn <b>onregelmatig</b>:</p>
<table>
<tr><th>Infinitief</th><th>Ik (imperf.)</th><th>Wij (imperf.)</th><th>English</th></tr>
<tr><td><b>zijn</b></td><td><b>was</b></td><td><b>waren</b></td><td>to be</td></tr>
<tr><td><b>hebben</b></td><td><b>had</b></td><td><b>hadden</b></td><td>to have</td></tr>
<tr><td>gaan</td><td>ging</td><td>gingen</td><td>to go</td></tr>
<tr><td>komen</td><td>kwam</td><td>kwamen</td><td>to come</td></tr>
<tr><td>doen</td><td>deed</td><td>deden</td><td>to do</td></tr>
<tr><td>zien</td><td>zag</td><td>zagen</td><td>to see</td></tr>
<tr><td>eten</td><td>at</td><td>aten</td><td>to eat</td></tr>
<tr><td>drinken</td><td>dronk</td><td>dronken</td><td>to drink</td></tr>
<tr><td>lezen</td><td>las</td><td>lazen</td><td>to read</td></tr>
<tr><td>schrijven</td><td>schreef</td><td>schreven</td><td>to write</td></tr>
<tr><td>nemen</td><td>nam</td><td>namen</td><td>to take</td></tr>
<tr><td>lopen</td><td>liep</td><td>liepen</td><td>to walk</td></tr>
<tr><td>slapen</td><td>sliep</td><td>sliepen</td><td>to sleep</td></tr>
<tr><td>rijden</td><td>reed</td><td>reden</td><td>to drive</td></tr>
<tr><td>vinden</td><td>vond</td><td>vonden</td><td>to find</td></tr>
<tr><td>staan</td><td>stond</td><td>stonden</td><td>to stand</td></tr>
<tr><td>zitten</td><td>zat</td><td>zaten</td><td>to sit</td></tr>
</table>

<h4>Vervoeging van zijn (imperfectum)</h4>
<table>
<tr><td>ik</td><td><b>was</b></td><td>wij</td><td><b>waren</b></td></tr>
<tr><td>jij</td><td><b>was</b></td><td>jullie</td><td><b>waren</b></td></tr>
<tr><td>hij/zij/het</td><td><b>was</b></td><td>zij (pl.)</td><td><b>waren</b></td></tr>
</table>

<h4>Vervoeging van hebben (imperfectum)</h4>
<table>
<tr><td>ik</td><td><b>had</b></td><td>wij</td><td><b>hadden</b></td></tr>
<tr><td>jij</td><td><b>had</b></td><td>jullie</td><td><b>hadden</b></td></tr>
<tr><td>hij/zij/het</td><td><b>had</b></td><td>zij (pl.)</td><td><b>hadden</b></td></tr>
</table>

<h4>Was vs Had — wanneer welke?</h4>
<table>
<tr><th>Gebruik <b>was/waren</b> (= to be)</th><th>Gebruik <b>had/hadden</b> (= to have)</th></tr>
<tr><td>Ik <b>was</b> moe.</td><td>Ik <b>had</b> honger.</td></tr>
<tr><td>Het <b>was</b> koud.</td><td>Ik <b>had</b> geen tijd.</td></tr>
<tr><td>Zij <b>was</b> ziek.</td><td>Wij <b>hadden</b> een hond.</td></tr>
<tr><td>We <b>waren</b> op vakantie.</td><td>Hij <b>had</b> veel werk.</td></tr>
<tr><td>Het <b>was</b> 10 uur.</td><td>Ze <b>hadden</b> drie kinderen.</td></tr>
</table>
<p><b>Regel:</b> Denk aan het presens → <em>Ik <b>ben</b> moe → Ik <b>was</b> moe. Ik <b>heb</b> honger → Ik <b>had</b> honger.</em></p>

<hr>
<p><strong>Regelmatige imperfectum — oefentabel:</strong></p>
<table>
<tr><th>Infinitief</th><th>Stem</th><th>Kofschip?</th><th>Ik (imperfectum)</th><th>Wij (imperfectum)</th></tr>
<tr><td>koken</td><td>kook</td><td>k = YES</td><td>kookte</td><td>kookten</td></tr>
<tr><td>leren</td><td>leer</td><td>r = NO</td><td>leerde</td><td>leerden</td></tr>
<tr><td>wandelen</td><td>wandel</td><td>l = NO</td><td>wandelde</td><td>wandelden</td></tr>
<tr><td>stoppen</td><td>stop</td><td>p = YES</td><td>stopte</td><td>stopten</td></tr>
<tr><td>hopen</td><td>hoop</td><td>p = YES</td><td>hoopte</td><td>hoopten</td></tr>
<tr><td>verhuizen</td><td>verhuis</td><td>s = YES*</td><td>verhuisde*</td><td>verhuisden</td></tr>
</table>
<p>* verhuizen: z→s in stem, so use -de despite s being in kofschip.</p>

<p><strong>Life events — example sentences:</strong></p>
<ul>
<li><em>Ik <strong>groeide</strong> op in Chennai.</em> — I grew up in Chennai.</li>
<li><em>Ik <strong>studeerde</strong> informatica aan de universiteit.</em> — I studied computer science.</li>
<li><em>We <strong>vierden</strong> elk jaar Diwali.</em> — We celebrated Diwali every year.</li>
<li><em>Mijn ouders <strong>werkten</strong> op een school.</em> — My parents worked at a school.</li>
<li><em>Ik <strong>verhuisde</strong> naar Gent in 2020.</em> — I moved to Ghent in 2020.</li>
</ul>
""",

        "grammar_quick": """
<ul>
<li><strong>'t kofschip</strong> letters: t, k, f, s, ch, p</li>
<li>Stem ends in kofschip letter → <strong>-te / -ten</strong></li>
<li>Stem ends in other letter → <strong>-de / -den</strong></li>
<li>Exception: v→f and z→s stems always use <strong>-de / -den</strong></li>
<li>Singular: -te/-de · Plural: -ten/-den</li>
<li><strong>zijn → was/waren</strong> · <strong>hebben → had/hadden</strong> (onregelmatig!)</li>
<li>Used for stories, habitual past, descriptions</li>
</ul>
""",

        # ── EXERCISES (15) ──
        "exercises": [
            {"type": "fill", "q": "Vroeger ___ ik elke dag naar school in Chennai. (fietsen, imperfectum)", "a": "fietste",
             "tip": "Stem = fiets. s is in 't kofschip → -te: fietste. Vroeger = past habit → imperfectum."},
            {"type": "fill", "q": "Mijn moeder ___ vroeger altijd Indiase curry. (koken, imperfectum)", "a": "kookte",
             "tip": "Stem = kook. k is in 't kofschip → -te: kookte. Past habit → imperfectum."},
            {"type": "fill", "q": "In India ___ ik in een groot huis met mijn familie. (wonen, imperfectum)", "a": "woonde",
             "tip": "Stem = woon. n is NOT in 't kofschip → -de: woonde."},
            {"type": "fill", "q": "Op zaterdag ___ wij altijd in het park. (spelen, imperfectum, plural)", "a": "speelden",
             "tip": "Stem = speel. l NOT kofschip → -de. Plural → -den: speelden."},
            {"type": "fill", "q": "Mijn vader ___ heel hard op kantoor. (werken, imperfectum)", "a": "werkte",
             "tip": "Stem = werk. k in 't kofschip → -te: werkte."},
            {"type": "fill", "q": "In het begin ___ ik veel in het Engels met collega's. (praten, imperfectum)", "a": "praatte",
             "tip": "Stem = praat. t in 't kofschip → -te: praat+te = praatte (double t!)."},
            {"type": "fill", "q": "Mijn zus ___ in Brussel als verpleegster. (leven, imperfectum)", "a": "leefde",
             "tip": "Special: v→f in stem (leef). Despite f in kofschip, v→f stems always use -de: leefde."},
            {"type": "fill", "q": "Vroeger ___ wij veel door India. (reizen, imperfectum, plural)", "a": "reisden",
             "tip": "Special: z→s in stem (reis). Despite s in kofschip, z→s stems use -de. Plural → -den: reisden."},
            {"type": "choice", "q": "Een verhaal over je kindertijd: 'Vroeger ___ ik elke dag naar school.' (lopen)", "options": ["loopte", "liep", "lopte"], "a": "liep",
             "tip": "Lopen is IRREGULAR — it doesn't follow 't kofschip. lopen → liep."},
            {"type": "choice", "q": "Over je eerste maanden in Gent: 'Ik ___ veel nieuwe woorden.' (leren)", "options": ["leerde", "leerte", "leren"], "a": "leerde",
             "tip": "Stem = leer. r is NOT in 't kofschip → -de: leerde."},
            {"type": "tf", "q": "'Ik werkde gisteren op de universiteit' is correct.", "a": False,
             "correction": "Ik WERKTE gisteren. k is in 't kofschip → -te, not -de!",
             "tip": "Check the last letter of the stem 'werk': is k in 't kofschip → yes → -te."},
            {"type": "tf", "q": "'Vroeger studeerde ik in India' is correct.", "a": True,
             "correction": "Correct! Stem = studeer. r is NOT in kofschip → -de: studeerde ✓",
             "tip": "Check: is r in 't kofschip? No → -de is correct."},
            {"type": "tf", "q": "'Ik danste op het feest' is correct.", "a": True,
             "correction": "Correct! Stem = dans. s IS in 't kofschip → -te: danste ✓",
             "tip": "s is in 't kofschip → -te is correct."},
            {"type": "translate", "q": "I grew up in India and moved to Belgium.", "a": "Ik groeide op in India en verhuisde naar België.",
             "tip": "opgroeien (separable: groeide op). verhuizen: stem = verhuis, s kofschip → -de (z→s exception!)."},
            {"type": "translate", "q": "We celebrated my birthday and danced all evening.", "a": "We vierden mijn verjaardag en dansten de hele avond.",
             "tip": "vieren → vierden (r not kofschip, plural -den). dansen → dansten (s kofschip, plural -ten)."},
        ],

        "jouw_beurt": "Write your personal levenslijn (life timeline) with 5–6 key moments.\n\nUse imperfectum throughout:\nIk ben geboren in … / Ik groeide op in … / Ik studeerde … / Ik werkte … / Ik verhuisde naar Gent in …\n\nWhat was your hoogtepunt? What was your dieptepunt?",
    },

    # =====================================================================
    # SESSION 5 — Om … te … Construction
    # =====================================================================
    {
        "id": 5,
        "title": "Om … te … Construction",
        "chapter": "Een Verhaal Vertellen",
        "book_page": "p. 13, 18",
        "review": [
            {"q": "fietsen → imperfectum (ik)?",
             "a": "fietste (s is in 't kofschip → -te)"},
            {"q": "Why does 'leven' become 'leefde' not 'leevde'?",
                "a": "v → f in stem (leef), and v→f stems use -de"},
            {"q": "What are hoogtepunt and dieptepunt?",
                "a": "highlight / high point and low point"},
            {"q": "wonen → wij ___ (imperfectum plural)", "a": "woonden"},
        ],
        "vocabulary": [
            {"nl": "het avontuur", "en": "adventure",
                "ex": "Een groot avontuur in India."},
            {"nl": "verborgen", "en": "hidden", "ex": "Een verborgen schat."},
            {"nl": "de bestemming", "en": "destination",
                "ex": "Wat is je bestemming?"},
            {"nl": "verbaasd zijn", "en": "to be astonished",
                "ex": "Ik was verbaasd!"},
            {"nl": "de held", "en": "hero", "ex": "Hij is de held van het verhaal."},
            {"nl": "de slechterik", "en": "villain",
                "ex": "De slechterik verloor."},
            {"nl": "proberen", "en": "to try",
                "ex": "Ik probeer om gezond te eten."},
            {"nl": "slagen",
                "en": "to pass (exam)", "ex": "Ik wil slagen voor het examen."},
            {"nl": "beslissen", "en": "to decide",
                "ex": "Ik besliste om te verhuizen."},
            {"nl": "beloven", "en": "to promise",
                "ex": "Ik beloof om hard te werken."},
            {"nl": "het doel", "en": "goal / purpose",
                "ex": "Wat is het doel van je reis?"},
        ],

        # ── GRAMMAR ──
        "grammar_title": "Om … te … (in order to / to)",
        "grammar_html": """
<h4>What does this structure do?</h4>
<p>The <strong>om … te …</strong> construction expresses <strong>purpose</strong> (why you do something)
or connects a verb to another verb with "to". It's equivalent to English "in order to" or "(verb) to (verb)".</p>

<h4>The pattern</h4>
<p>[main clause] + <strong>om</strong> + [other words] + <strong>te</strong> + [infinitive]</p>

<table>
<tr><th>Dutch</th><th>English</th></tr>
<tr><td>Ik ga naar de markt <strong>om</strong> groenten <strong>te</strong> kopen.</td><td>I go to the market <strong>to</strong> buy vegetables.</td></tr>
<tr><td>Ik leer Nederlands <strong>om</strong> met Belgen <strong>te</strong> communiceren.</td><td>I learn Dutch <strong>to</strong> communicate with Belgians.</td></tr>
<tr><td>Ze werkt hard <strong>om</strong> <strong>te</strong> slagen.</td><td>She works hard <strong>to</strong> pass.</td></tr>
</table>

<h4>With adjective: Ik vind het [adj] om … te …</h4>
<table>
<tr><th>Dutch</th><th>English</th></tr>
<tr><td>Ik vind het <strong>belangrijk om</strong> Nederlands <strong>te</strong> leren.</td><td>I find it important to learn Dutch.</td></tr>
<tr><td>Ik vind het <strong>moeilijk om</strong> vroeg op <strong>te</strong> staan.</td><td>I find it difficult to get up early.</td></tr>
<tr><td>Het is <strong>leuk om</strong> in Gent <strong>te</strong> wonen.</td><td>It's nice to live in Ghent.</td></tr>
</table>

<h4>Separable verbs with om…te…</h4>
<p>With separable verbs, <strong>te</strong> goes BETWEEN the prefix and the verb:</p>
<p><em>Ik vind het moeilijk om vroeg <strong>op te staan</strong>.</em> (op·staan → op <strong>te</strong> staan)<br>
<em>Ik probeer om gezond <strong>te</strong> eten.</em> (not separable → normal)</p>

<h4>Common verb starters</h4>
<ul>
<li><em>Ik probeer om … te …</em> — I try to …</li>
<li><em>Ik hoop om … te …</em> — I hope to …</li>
<li><em>Ik beloof om … te …</em> — I promise to …</li>
<li><em>Ik besluit om … te …</em> — I decide to …</li>
<li><em>Ik vind het [adj] om … te …</em> — I find it [adj] to …</li>
</ul>

<p><strong>🇬🇧 English comparison:</strong> Almost identical to "to + verb" or "in order to"!
The main difference is that <em>om</em> and <em>te</em> are split around other words.</p>
""",

        "grammar_letop": """
<ul>
<li><span class="wrong">Ik ga naar de markt om te groenten kopen.</span> →
    <span class="right">Ik ga naar de markt om groenten <strong>te kopen</strong>.</span><br>
    <em>te</em> goes directly before the infinitive, not before the object!</li>
<li><span class="wrong">Ik vind het moeilijk om op te vroeg staan.</span> →
    <span class="right">Ik vind het moeilijk om vroeg <strong>op te staan</strong>.</span><br>
    For separable verbs: te goes BETWEEN prefix and verb. Other words (like vroeg) come before.</li>
<li><span class="wrong">Ik leer Nederlands voor communiceren met Belgen.</span> →
    <span class="right">Ik leer Nederlands <strong>om</strong> met Belgen <strong>te</strong> communiceren.</span><br>
    Don't translate "for" literally — use om…te…!</li>
<li><span class="wrong">Om ik wil slagen, werk ik hard.</span> →
    <span class="right"><strong>Om te slagen</strong>, werk ik hard.</span><br>
    om…te… has NO subject — it refers to the subject of the main clause.</li>
</ul>
""",

        "grammar_extra": """
<p><strong>Full example sentences for your life at UGent:</strong></p>
<ul>
<li><em>Ik ben naar Gent gekomen <strong>om</strong> een doctoraat <strong>te</strong> doen.</em></li>
<li><em>Ik leer Nederlands <strong>om</strong> met mijn collega's <strong>te</strong> communiceren.</em></li>
<li><em>Ik fiets elke dag <strong>om</strong> gezond <strong>te</strong> blijven.</em></li>
<li><em>Ik ga naar het Citadelpark <strong>om te</strong> ontspannen.</em></li>
<li><em>Ik vind het belangrijk <strong>om</strong> de Belgische cultuur <strong>te</strong> begrijpen.</em></li>
<li><em>Het is leuk <strong>om</strong> in het centrum van Gent <strong>te</strong> wandelen.</em></li>
<li><em>Ik probeer <strong>om</strong> elke dag een beetje Nederlands <strong>te</strong> oefenen.</em></li>
</ul>

<p><strong>With separable verbs:</strong></p>
<ul>
<li><em>Ik probeer om elke dag om 7 uur <strong>op te staan</strong>.</em> (op·staan)</li>
<li><em>Ik vind het leuk om in Gent <strong>uit te gaan</strong>.</em> (uit·gaan)</li>
<li><em>Ze probeerde om het licht <strong>aan te doen</strong>.</em> (aan·doen)</li>
</ul>
""",

        "grammar_quick": """
<ul>
<li><strong>om … te + infinitief</strong> = in order to / to</li>
<li><em>te</em> goes directly before the infinitive</li>
<li>Separable verbs: <em>te</em> goes BETWEEN prefix and verb (op <strong>te</strong> staan)</li>
<li>No subject in the om…te… part</li>
<li>Common: <em>Ik vind het [adj] om … te …</em></li>
<li>Common: <em>Ik probeer / hoop / beloof om … te …</em></li>
</ul>
""",

        # ── EXERCISES (15) ──
        "exercises": [
            # --- fill (7) ---
            {"type": "fill", "q": "Bij de inschrijving aan UGent: Ik ga naar de universiteit ___ Nederlands te studeren.", "a": "om",
             "tip": "'Om' starts the purpose clause: om … te + infinitief."},
            {"type": "fill", "q": "In de les: Mijn docent spreekt langzaam om ons te ___. (help = helpen)", "a": "helpen",
             "tip": "te + infinitive at the end. helpen = to help."},
            {"type": "fill", "q": "Op het werk: Ik vind het moeilijk ___ e-mails in het Nederlands te schrijven.", "a": "om",
             "tip": "Pattern: Ik vind het [adj] OM … te …"},
            {"type": "fill", "q": "In het weekend: Ik ga naar de Korenmarkt om met vrienden iets te ___. (drink = drinken)", "a": "drinken",
             "tip": "te + infinitive. drinken = to drink."},
            {"type": "fill", "q": "Bij de sportclub: Ze traint elke dag om fit te ___. (stay = blijven)", "a": "blijven",
             "tip": "te + infinitive. blijven = to stay."},
            {"type": "fill", "q": "'s Ochtends: Ik probeer om elke dag om 7 uur op te ___. (get up = staan)", "a": "staan",
             "tip": "Separable verb: op·staan → op te staan. The base verb goes last."},
            {"type": "fill", "q": "Aan een collega: Het is fijn om in Gent te ___. (live = wonen)", "a": "wonen",
             "tip": "Het is [adj] om … te + infinitief. wonen = to live."},
            # --- choice (3) ---
            {"type": "choice", "q": "Je vertelt aan je buurman waarom je Nederlands leert. Welke zin is correct?", "options": [
                "Ik leer Nederlands om te met Belgen communiceren.",
                "Ik leer Nederlands om met Belgen te communiceren.",
                "Ik leer Nederlands om Belgen met te communiceren."
            ], "a": 1, "tip": "'te' staat direct vóór het infinitief, de rest komt ervoor."},
            {"type": "choice", "q": "Je wekker gaat om 6 uur. Hoe zeg je 'to get up early' met om…te?", "options": [
                "om vroeg op te staan",
                "om op vroeg te staan",
                "om te vroeg opstaan"
            ], "a": 0, "tip": "Scheidbaar werkwoord: 'te' komt tussen prefix en stam → op te staan."},
            {"type": "choice", "q": "Je maakt een oefening voor het examen. Welke zin gebruikt om…te… correct?", "options": [
                "Om ik wil slagen, werk ik hard.",
                "Ik werk hard om te slagen.",
                "Ik werk hard om ik slaag."
            ], "a": 1, "tip": "om…te… heeft geen apart onderwerp — het verwijst naar het subject van de hoofdzin."},
            # --- tf (3) ---
            {"type": "tf", "q": "'Ik ga naar de Groentenmarkt om te groenten kopen' is correct.", "a": False,
             "correction": "Fout! Correct: Ik ga naar de Groentenmarkt om groenten TE KOPEN. ('te' staat vóór het infinitief, niet vóór het object!)",
             "tip": "Waar staat 'te'? Vóór het object of vóór het infinitief?"},
            {"type": "tf", "q": "'Ik vind het belangrijk om Nederlands te leren' is correct.", "a": True,
             "correction": "Correct! Patroon: Ik vind het [adj] om … te [infinitief] ✓",
             "tip": "Controleer: staat 'te' direct vóór het infinitief 'leren'?"},
            {"type": "tf", "q": "'Hij fietst naar UGent om te niet laat komen' is correct.", "a": False,
             "correction": "Fout! Correct: Hij fietst naar UGent om niet te laat te komen. ('te' staat vóór het infinitief, niet na 'om'!)",
             "tip": "'niet te laat' is het bijwoord; 'te komen' is het infinitief met 'te'."},
            # --- translate (1) ---
            {"type": "translate", "q": "I find it difficult to get up early.", "a": "Ik vind het moeilijk om vroeg op te staan.",
             "tip": "Pattern: Ik vind het [adj] om … te … Separable: op·staan → op te staan."},
            # --- reorder (1) ---
            {"type": "reorder", "q": "om / Ik / te / fiets / gezond / blijven", "a": "Ik fiets om gezond te blijven.",
             "tip": "Hoofdzin eerst (Ik fiets), dan om + rest + te + infinitief."},
        ],

        "jouw_beurt": "Write 5 sentences using om…te… about why you do things at UGent and in Ghent.\n\nUse these starters:\n• Ik leer Nederlands om …\n• Ik ga naar het Citadelpark om …\n• Ik vind het belangrijk om …\n• Ik probeer om …\n• Het is leuk om … in Gent …",
    },

    # ──────────────────────────────────────────────
    #  SESSION 6 — Omdat vs Want vs Daarom + Gezond Eten
    # ──────────────────────────────────────────────
    {
        "id": 6,
        "title": "Omdat, Want & Daarom – Redenen geven",
        "chapter": "Hoofdstuk 3 – Gezond Leven",
        "book_page": "NT2 Drempel 2, H3 p. 40–48",

        "review": "In Sessions 2–3 you practised bijzin (verb→end) and inversie (verb–subject). "
                  "Now you combine both: <b>omdat</b> = bijzin (verb→end), <b>want</b> = normal order, "
                  "<b>daarom</b> = inversie (verb–subject). All three express reason/cause but follow different rules.",

        "vocabulary": [
            ("gezond", "healthy", "Groenten zijn gezond."),
            ("ongezond", "unhealthy", "Chips zijn ongezond."),
            ("bewegen", "to exercise / move", "Je moet elke dag bewegen."),
            ("voeding", "nutrition / diet", "Goede voeding is belangrijk."),
            ("groente (de)", "vegetable", "Ik eet veel groente."),
            ("fruit (het)", "fruit", "Fruit is lekker en gezond."),
            ("suiker (de)", "sugar", "Te veel suiker is slecht."),
            ("vet (het)", "fat", "Vet maakt eten lekker."),
            ("maaltijd (de)", "meal", "We eten drie maaltijden per dag."),
            ("ontbijt (het)", "breakfast", "Het ontbijt is de eerste maaltijd."),
            ("tussendoortje (het)", "snack",
             "Een appel is een gezond tussendoortje."),
            ("recept (het)", "recipe", "Dit recept is makkelijk."),
        ],

        "grammar_title": "Omdat vs Want vs Daarom — Three Ways to Give a Reason",

        "grammar_html": """
<h4>1. Three words, three structures</h4>
<table>
  <tr><th>Word</th><th>Meaning</th><th>Type</th><th>Word order after it</th></tr>
  <tr><td><b>omdat</b></td><td>because</td><td>subordinating conjunction (bijzin)</td><td>subject … <u>verb at END</u></td></tr>
  <tr><td><b>want</b></td><td>because</td><td>coordinating conjunction</td><td>subject + verb (normal)</td></tr>
  <tr><td><b>daarom</b></td><td>therefore / that's why</td><td>linking adverb</td><td><u>verb–subject</u> (inversie)</td></tr>
</table>

<h4>2. Examples (same meaning, different structure)</h4>
<table>
  <tr><th>Connector</th><th>Example</th></tr>
  <tr><td>omdat</td><td>Ik eet groente <b>omdat</b> het gezond <u>is</u>.</td></tr>
  <tr><td>want</td><td>Ik eet groente, <b>want</b> het <u>is</u> gezond.</td></tr>
  <tr><td>daarom</td><td>Groente is gezond. <b>Daarom</b> <u>eet</u> ik groente.</td></tr>
</table>

<h4>3. Tamil comparison</h4>
<p>In Tamil, "ஏனென்றால் (ēṉeṉṟāl)" = because. Dutch has TWO "because" words: <b>omdat</b> and <b>want</b>. 
They mean the same but change the word order! Think of <b>omdat</b> as the strict one (pushes verb to end) and <b>want</b> as the relaxed one (keeps normal order).</p>

<h4>4. Formula card</h4>
<pre>
  OMDAT:  main clause + omdat + subject + … + VERB (end)
  WANT:   main clause + , want + subject + VERB + …
  DAAROM: statement. Daarom + VERB + subject + …
</pre>
""",

        "grammar_letop": """
<ul>
  <li>❌ Ik eet groente omdat het <b>is</b> gezond. → ✅ … omdat het gezond <b>is</b>. <br><em>Omdat = bijzin → verb goes to the END.</em></li>
  <li>❌ Ik eet groente, want het gezond <b>is</b>. → ✅ … want het <b>is</b> gezond. <br><em>Want = normal order → verb stays in position 2.</em></li>
  <li>❌ Daarom ik eet groente. → ✅ Daarom <b>eet ik</b> groente. <br><em>Daarom causes inversie → verb before subject.</em></li>
  <li>❌ Omdat groente gezond is, eet ik het. → Actually ✅! This is correct. <br><em>When omdat-clause comes FIRST, the main clause starts with the verb (inversie). This is advanced but correct.</em></li>
  <li>❌ Want groente is gezond, eet ik het. → ✅ That's wrong! <br><em>Want can NEVER start a sentence. Want always comes after a comma mid-sentence.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Practice: Fill the correct connector</h4>
<table>
  <tr><th>#</th><th>Sentence</th><th>Answer</th></tr>
  <tr><td>1</td><td>Ik drink water ___ ik dorst heb.</td><td>omdat (verb 'heb' → end)</td></tr>
  <tr><td>2</td><td>Ik drink water, ___ ik heb dorst.</td><td>want (normal order)</td></tr>
  <tr><td>3</td><td>Ik heb dorst. ___ drink ik water.</td><td>Daarom (inversie)</td></tr>
  <tr><td>4</td><td>Ze kookt thuis ___ het goedkoper is.</td><td>omdat</td></tr>
  <tr><td>5</td><td>Het is goedkoper. ___ kookt ze thuis.</td><td>Daarom</td></tr>
</table>

<h4>More examples with food & health</h4>
<ul>
  <li>Ik eet geen chips <b>omdat</b> ze ongezond <b>zijn</b>.</li>
  <li>Ik eet geen chips, <b>want</b> ze <b>zijn</b> ongezond.</li>
  <li>Chips zijn ongezond. <b>Daarom</b> <b>eet</b> ik ze niet.</li>
  <li>Hij sport elke dag <b>omdat</b> hij fit <b>wil blijven</b>.</li>
  <li>Zij drinkt geen cola, <b>want</b> er <b>zit</b> veel suiker in.</li>
</ul>
""",

        "grammar_quick": """
<ul>
  <li><b>Omdat</b> = because → bijzin (verb to END)</li>
  <li><b>Want</b> = because → normal word order (never starts a sentence)</li>
  <li><b>Daarom</b> = therefore → inversie (verb–subject)</li>
  <li>Omdat & want mean the same; only word order differs</li>
  <li>Omdat-clause CAN start a sentence → then main clause = inversie</li>
  <li>Want NEVER starts a sentence</li>
</ul>
""",

        "exercises": [
            {"type": "choice", "q": "In de mensa van UGent: Ik eet fruit ___ het gezond is.", "options": ["omdat", "want", "daarom"],
             "a": "omdat", "tip": "Het werkwoord 'is' staat op het einde → bijzin → omdat."},
            {"type": "choice", "q": "Gesprek met een collega: Ik eet fruit, ___ het is gezond.", "options": ["omdat", "want", "daarom"],
             "a": "want", "tip": "Normale woordvolgorde (het IS gezond) → want."},
            {"type": "choice", "q": "Bij de huisarts: Fruit is gezond. ___ eet ik het elke dag.", "options": ["Omdat", "Want", "Daarom"],
             "a": "Daarom", "tip": "Nieuwe zin + inversie (eet ik) → daarom."},
            {"type": "fill", "q": "Op de sportclub: Ik sport elke dag ___ ik gezond wil blijven.", "a": "omdat",
             "tip": "Werkwoordgroep 'wil blijven' op het einde → omdat."},
            {"type": "fill", "q": "In de Delhaize: Groente is belangrijk, ___ het veel vitamines heeft.", "a": "want",
             "tip": "Normale volgorde na de komma (het heeft) → want."},
            {"type": "fill", "q": "Na de les: Ik heb honger. ___ maak ik een boterham.", "a": "Daarom",
             "tip": "Nieuwe zin + inversie (maak ik) → Daarom."},
            {"type": "tf", "q": "'Want' kan aan het begin van een zin staan.", "a": False,
             "correction": "Fout! 'Want' kan NOOIT een zin beginnen. Gebruik omdat of daarom.",
             "tip": "Want staat altijd na een komma, midden in een zin."},
            {"type": "tf", "q": "'Omdat' stuurt het werkwoord naar het einde van de bijzin.", "a": True,
             "correction": "Correct! Omdat = onderschikkend voegwoord → bijzin → werkwoord op het einde.",
             "tip": "Omdat = bijzin = werkwoord → einde."},
            {"type": "tf", "q": "'Ik eet gezond. Daarom ik voel me goed.' is correct.", "a": False,
             "correction": "Fout! Na 'daarom' komt inversie: Daarom VOEL ik me goed. (werkwoord vóór subject)",
             "tip": "Daarom veroorzaakt inversie: werkwoord vóór het onderwerp."},
            {"type": "choice", "q": "In een e-mail: Ze drinkt geen cola ___ er veel suiker in zit.",
             "options": ["omdat", "want", "daarom"], "a": "omdat",
             "tip": "'zit' staat op het einde → bijzin → omdat."},
            {"type": "translate", "q": "I eat vegetables because they are healthy. (use omdat)",
             "a": "Ik eet groente omdat ze gezond zijn.",
             "tip": "omdat + subject (ze) + … + werkwoord op einde (zijn)."},
            {"type": "translate", "q": "I eat vegetables because they are healthy. (use want)",
             "a": "Ik eet groente, want ze zijn gezond.",
             "tip": "want + normale volgorde: ze zijn gezond. Vergeet de komma niet vóór want."},
            {"type": "translate", "q": "Vegetables are healthy. Therefore I eat them every day.",
             "a": "Groente is gezond. Daarom eet ik ze elke dag.",
             "tip": "Daarom + inversie: eet ik (werkwoord vóór subject)."},
            {"type": "reorder", "q": "omdat / sport / hij / wil / fit / blijven / hij",
             "a": "Hij sport omdat hij fit wil blijven.",
             "tip": "Hoofdzin (Hij sport) + omdat + subject + … + werkwoordgroep op einde."},
            {"type": "choice", "q": "Op het examen: Omdat het regent, ___ ik thuis.", "options": ["blijf", "omdat", "want"],
             "a": "blijf", "tip": "Omdat-bijzin eerst → hoofdzin begint met werkwoord (inversie): blijf ik."},
        ],

        "jouw_beurt": "Write 6 sentences about your eating habits — 2 with omdat, 2 with want, 2 with daarom.\n\n"
                      "Use these starters:\n"
                      "• Ik eet graag … omdat …\n"
                      "• Ik kook vaak thuis, want …\n"
                      "• … is ongezond. Daarom …\n"
                      "• Ik drink geen … omdat …\n"
                      "• Ik hou van …, want …\n"
                      "• Ik wil gezond leven. Daarom …",
    },

    # ──────────────────────────────────────────────
    #  SESSION 7 — Als (if/when) + Advies geven + Gezond Bewegen
    # ──────────────────────────────────────────────
    {
        "id": 7,
        "title": "Als (if/when) – Condities & Advies geven",
        "chapter": "Hoofdstuk 3 – Gezond Leven",
        "book_page": "NT2 Drempel 2, H3 p. 48–55",

        "review": "In Session 6 you learned omdat/want/daarom (reasons). Now you learn <b>als</b> (if/when) "
                  "for conditions and giving advice. Als is also a bijzin-connector (verb→end), just like omdat. "
                  "The advice patterns use <b>moeten</b> (must) and <b>kunnen</b> (can) with als-clauses.",

        "vocabulary": [
            ("bewegen", "to exercise / move", "Je moet meer bewegen."),
            ("sporten", "to do sports", "Ik sport drie keer per week."),
            ("wandelen", "to walk", "Wandelen is goed voor je gezondheid."),
            ("fietsen", "to cycle", "In Gent fietsen veel mensen."),
            ("zwemmen", "to swim", "Zwemmen is een goede sport."),
            ("moe", "tired", "Ik ben moe na het sporten."),
            ("energie (de)", "energy", "Sport geeft je energie."),
            ("advies (het)", "advice", "De dokter geeft advies."),
            ("gezondheid (de)", "health", "Gezondheid is het belangrijkst."),
            ("stress (de)", "stress", "Te veel stress is ongezond."),
            ("ontspannen", "to relax", "Yoga helpt om te ontspannen."),
            ("gewoonte (de)", "habit", "Elke dag sporten is een goede gewoonte."),
        ],

        "grammar_title": "Als (if / when) — Conditions & Giving Advice",

        "grammar_html": """
<h4>1. Als = if / when (subordinating conjunction)</h4>
<p><b>Als</b> creates a bijzin (subordinate clause): the verb moves to the END, just like <b>omdat</b>.</p>
<table>
  <tr><th>Structure</th><th>Example</th></tr>
  <tr><td>main + als + bijzin</td><td>Ik ga wandelen <b>als</b> het mooi weer <u>is</u>.</td></tr>
  <tr><td>als + bijzin, + main (inversie)</td><td><b>Als</b> het mooi weer <u>is</u>, <b>ga</b> ik wandelen.</td></tr>
</table>

<h4>2. Als-clause FIRST → main clause has inversie</h4>
<p>When the als-clause comes first, the main clause starts with the <b>verb</b> (just like after daarom, then, etc.):</p>
<pre>
  Als + subject + … + VERB(end), VERB + subject + rest.
  Als je moe bent, moet je rusten.
</pre>

<h4>3. Tamil comparison</h4>
<p>In Tamil, "என்றால் (eṉṟāl)" or "-ஆல் (-āl)" = if. Dutch <b>als</b> works similarly but remember: 
verb goes to the END of the als-clause. In Tamil, verb position doesn't change for conditions.</p>

<h4>4. Giving advice with als + moeten/kunnen</h4>
<table>
  <tr><th>Pattern</th><th>Example</th></tr>
  <tr><td>Als je … wilt, moet je …</td><td>Als je gezond <u>wilt</u> leven, <b>moet</b> je meer bewegen.</td></tr>
  <tr><td>Als je … hebt, kun je …</td><td>Als je stress <u>hebt</u>, <b>kun</b> je gaan wandelen.</td></tr>
  <tr><td>Je moet … als je … wilt</td><td>Je <b>moet</b> meer slapen als je moe <u>bent</u>.</td></tr>
</table>

<h4>5. Als vs Wanneer vs Of</h4>
<table>
  <tr><th>Word</th><th>Use</th><th>Example</th></tr>
  <tr><td><b>als</b></td><td>if / when (condition, future)</td><td>Als het regent, blijf ik thuis.</td></tr>
  <tr><td><b>wanneer</b></td><td>when (more formal, same as als)</td><td>Wanneer kom je? (= When are you coming?)</td></tr>
  <tr><td><b>of</b></td><td>if (= whether, in indirect questions)</td><td>Ik weet niet <b>of</b> hij komt.</td></tr>
</table>
""",

        "grammar_letop": """
<ul>
  <li>❌ Als het regent, ik blijf thuis. → ✅ Als het regent, <b>blijf ik</b> thuis. <br><em>After an als-clause, the main clause needs inversie (verb before subject).</em></li>
  <li>❌ Als je wilt gezond leven → ✅ Als je gezond wilt <b>leven</b>. <br><em>In the bijzin, modals + infinitive cluster at the end.</em></li>
  <li>❌ Ik weet niet als hij komt. → ✅ Ik weet niet <b>of</b> hij komt. <br><em>For indirect yes/no questions, use 'of' (whether), NOT 'als'.</em></li>
  <li>❌ Als ik ben ziek, ga ik naar de dokter. → ✅ Als ik ziek <b>ben</b>, ga ik naar de dokter. <br><em>In the als-clause, verb 'ben' goes to the end.</em></li>
  <li>❌ Als je hebt stress → ✅ Als je stress <b>hebt</b>. <br><em>Verb to the end in the als-clause!</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Practice: als-clause word order</h4>
<table>
  <tr><th>#</th><th>Scrambled als-clause</th><th>Correct</th></tr>
  <tr><td>1</td><td>als / moe / je / bent</td><td>als je moe bent</td></tr>
  <tr><td>2</td><td>als / regent / het</td><td>als het regent</td></tr>
  <tr><td>3</td><td>als / wilt / je / afvallen</td><td>als je wilt afvallen</td></tr>
  <tr><td>4</td><td>als / geen / je / hebt / tijd</td><td>als je geen tijd hebt</td></tr>
  <tr><td>5</td><td>als / kan / hij / niet / slapen</td><td>als hij niet kan slapen</td></tr>
</table>

<h4>Giving advice — example sentences</h4>
<ul>
  <li><b>Als</b> je moe <b>bent</b>, moet je vroeger naar bed gaan.</li>
  <li><b>Als</b> je wilt afvallen, moet je minder suiker eten.</li>
  <li><b>Als</b> je stress <b>hebt</b>, kun je gaan wandelen in het Citadelpark.</li>
  <li>Je moet meer water drinken <b>als</b> je hoofdpijn <b>hebt</b>.</li>
  <li><b>Als</b> je in Gent <b>woont</b>, kun je overal fietsen.</li>
  <li>Je kunt beter slapen <b>als</b> je 's avonds geen koffie <b>drinkt</b>.</li>
</ul>
""",

        "grammar_quick": """
<ul>
  <li><b>Als</b> = if / when → bijzin (verb to END)</li>
  <li>Als-clause first → main clause starts with verb (inversie)</li>
  <li>Advice pattern: Als je … wilt, moet je …</li>
  <li>Use <b>of</b> (not als) for indirect yes/no questions (= whether)</li>
  <li>Als & wanneer are interchangeable for "when" (als is more common)</li>
  <li>Modal verbs in als-clause: als je … wilt/kunt/moet + infinitive (end)</li>
</ul>
""",

        "exercises": [
            {"type": "fill", "q": "Advies van de dokter: ___ je moe bent, moet je rusten.", "a": "Als",
             "tip": "Conditie (als je moe bent) → als."},
            {"type": "fill", "q": "Gesprek met een vriend: Je moet meer bewegen ___ je gezond wilt blijven.", "a": "als",
             "tip": "als je gezond wilt blijven → bijzin volgt."},
            {"type": "choice", "q": "Weer in Gent: Als het regent, ___ ik thuis.", "options": ["blijf", "ik blijf", "blijf ik"],
             "a": "blijf", "tip": "Als-bijzin eerst → inversie in de hoofdzin: blijf ik. Alleen 'blijf' past vóór 'ik'."},
            {"type": "choice", "q": "Aan een collega: Ik weet niet ___ hij morgen komt.",
             "options": ["als", "of", "wanneer"], "a": "of",
             "tip": "Indirecte ja/nee-vraag (= whether) → of, niet als."},
            {"type": "tf", "q": "'Als' stuurt het werkwoord naar het einde van de bijzin.", "a": True,
             "correction": "Correct! Als = onderschikkend voegwoord → bijzin → werkwoord op het einde.",
             "tip": "Als = bijzin = werkwoord → einde."},
            {"type": "tf", "q": "'Na een als-bijzin heeft de hoofdzin een normale woordvolgorde (subject–werkwoord).'", "a": False,
             "correction": "Fout! Na een als-bijzin komt INVERSIE in de hoofdzin: werkwoord–subject.",
             "tip": "Na de als-bijzin → inversie: werkwoord vóór het subject."},
            {"type": "fill", "q": "In het Citadelpark: Als je stress ___ (hebben), kun je gaan wandelen.", "a": "hebt",
             "tip": "In de als-bijzin: je + … + werkwoord(einde). hebben → je hebt."},
            {"type": "fill", "q": "Over wonen in België: Als je in Gent ___ (wonen), kun je overal fietsen.", "a": "woont",
             "tip": "wonen met je → woont. Staat op het einde van de als-bijzin."},
            {"type": "choice", "q": "Bij de diëtist: Als je wilt afvallen, ___ je minder suiker eten.",
             "options": ["moet", "moeten", "wilt"], "a": "moet",
             "tip": "Hoofdzin na als-bijzin: werkwoord eerst (inversie) → moet je."},
            {"type": "tf", "q": "'Als ik ben ziek, ga ik naar de dokter.' is correct.", "a": False,
             "correction": "Fout! Correct: Als ik ziek BEN, ga ik naar de dokter. (werkwoord op het einde van de bijzin!)",
             "tip": "In de als-bijzin gaat het werkwoord naar het einde."},
            {"type": "translate", "q": "If you are tired, you should sleep more.",
             "a": "Als je moe bent, moet je meer slapen.",
             "tip": "als + je moe bent (werkwoord einde), moet je (inversie) + meer slapen."},
            {"type": "translate", "q": "You can go cycling if the weather is nice.",
             "a": "Je kunt gaan fietsen als het weer mooi is.",
             "tip": "Hoofdzin eerst: Je kunt gaan fietsen + als + het weer mooi is (werkwoord einde)."},
            {"type": "translate", "q": "If you want to relax, you can walk in the Citadelpark.",
             "a": "Als je wilt ontspannen, kun je in het Citadelpark wandelen.",
             "tip": "als + je wilt ontspannen (werkwoordcluster einde), kun je (inversie) + rest."},
            {"type": "reorder", "q": "als / moe / je / bent / , / moet / rusten / je",
             "a": "Als je moe bent, moet je rusten.",
             "tip": "Als-bijzin (werkwoord einde) + komma + hoofdzin (inversie)."},
            {"type": "choice", "q": "Op het examen: Welke zin is correct?",
             "options": [
                 "Als je bent ziek, moet je naar de dokter.",
                 "Als je ziek bent, moet je naar de dokter.",
                 "Als je ziek bent, je moet naar de dokter."
             ], "a": "Als je ziek bent, moet je naar de dokter.",
             "tip": "Als-bijzin: werkwoord (bent) op het EINDE. Hoofdzin: inversie (moet je)."},
        ],

        "jouw_beurt": "Write 6 advice sentences using als for a friend who wants to live healthier in Ghent.\n\n"
                      "Use these patterns:\n"
                      "• Als je … wilt, moet je …\n"
                      "• Als je … hebt, kun je …\n"
                      "• Je moet … als je …\n\n"
                      "Ideas: fietsen naar UGent, wandelen in Citadelpark, koken met verse groente, "
                      "minder suiker, meer water drinken, yoga doen, vroeg slapen.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 8 — Bij de Dokter: Lichaamsdelen & Klachten
    # ──────────────────────────────────────────────
    {
        "id": 8,
        "title": "Bij de Dokter – Lichaamsdelen & Klachten beschrijven",
        "chapter": "Hoofdstuk 3 – Gezond Leven",
        "book_page": "NT2 Drempel 2, H3 p. 55–65",

        "review": "In Sessions 6–7 you practised omdat/want/daarom (reasons) and als (conditions/advice). "
                  "Now you combine everything: you visit the doctor, describe symptoms using body-part vocabulary, "
                  "give reasons with omdat/want, and receive advice with als + moeten/kunnen. "
                  "You'll also learn reflexive verbs (zich voelen, zich wassen) and separable verbs in medical context.",

        "vocabulary": [
            ("het hoofd", "head", "Ik heb pijn in mijn hoofd."),
            ("de keel", "throat", "Mijn keel doet pijn."),
            ("de buik", "stomach / belly", "Ik heb buikpijn."),
            ("de rug", "back", "Mijn rug doet pijn."),
            ("het been", "leg", "Ik heb pijn in mijn been."),
            ("de arm", "arm", "Mijn arm is gebroken."),
            ("koorts (de)", "fever", "Ik heb koorts."),
            ("hoesten", "to cough", "Ik hoest al drie dagen."),
            ("niezen", "to sneeze", "Ik moet steeds niezen."),
            ("verkouden", "having a cold", "Ik ben verkouden."),
            ("griep (de)", "flu", "Ik heb de griep."),
            ("medicijn (het)", "medicine", "De dokter geeft een medicijn."),
            ("recept (het)", "prescription", "Ik heb een recept van de dokter."),
            ("zich voelen", "to feel (reflexive)", "Ik voel me niet lekker."),
        ],

        "grammar_title": "Bij de Dokter — Reflexive Verbs, Klachten & Lichaam",

        "grammar_html": """
<h4>1. Describing complaints (klachten)</h4>
<table>
  <tr><th>Pattern</th><th>Example</th><th>Translation</th></tr>
  <tr><td>Ik heb pijn in mijn + body part</td><td>Ik heb pijn in mijn <b>hoofd</b>.</td><td>I have pain in my head.</td></tr>
  <tr><td>Mijn + body part + doet pijn</td><td>Mijn <b>keel</b> doet pijn.</td><td>My throat hurts.</td></tr>
  <tr><td>Ik heb + symptom</td><td>Ik heb <b>koorts</b>.</td><td>I have a fever.</td></tr>
  <tr><td>Ik ben + adjective</td><td>Ik ben <b>verkouden</b>.</td><td>I have a cold.</td></tr>
  <tr><td>Ik heb last van + noun</td><td>Ik heb last van <b>hoofdpijn</b>.</td><td>I suffer from headache.</td></tr>
</table>

<h4>2. Reflexive verbs (reflexieve werkwoorden)</h4>
<p>Some verbs need a reflexive pronoun (me, je, zich, ons, je, zich):</p>
<table>
  <tr><th>Subject</th><th>Pronoun</th><th>Example</th></tr>
  <tr><td>ik</td><td><b>me</b></td><td>Ik voel <b>me</b> ziek.</td></tr>
  <tr><td>jij/je</td><td><b>je</b></td><td>Voel jij <b>je</b> goed?</td></tr>
  <tr><td>hij/zij/het</td><td><b>zich</b></td><td>Hij voelt <b>zich</b> moe.</td></tr>
  <tr><td>wij</td><td><b>ons</b></td><td>Wij voelen <b>ons</b> beter.</td></tr>
  <tr><td>jullie</td><td><b>je</b></td><td>Voelen jullie <b>je</b> goed?</td></tr>
  <tr><td>zij (pl.)</td><td><b>zich</b></td><td>Zij voelen <b>zich</b> niet lekker.</td></tr>
</table>

<h4>3. Tamil comparison</h4>
<p>Tamil uses "எனக்கு வலிக்கிறது (eṉakku valikkiṟatu)" = it hurts me. Dutch uses two patterns:
<b>Ik heb pijn in…</b> (I have pain in…) or <b>Mijn … doet pijn</b> (My … hurts).
Reflexive: Tamil has "-ஐ தான்" for self-reference. Dutch uses separate pronouns: me, je, zich.</p>

<h4>4. At the doctor — useful dialogue phrases</h4>
<table>
  <tr><th>Dokter vraagt</th><th>Patiënt antwoordt</th></tr>
  <tr><td>Wat kan ik voor u doen?</td><td>Ik voel me niet lekker.</td></tr>
  <tr><td>Wat zijn uw klachten?</td><td>Ik heb hoofdpijn en koorts.</td></tr>
  <tr><td>Hoe lang hebt u dit al?</td><td>Sinds drie dagen.</td></tr>
  <tr><td>Hebt u nog andere klachten?</td><td>Ja, ik hoest ook veel.</td></tr>
  <tr><td>Ik schrijf een medicijn voor.</td><td>Dank u wel, dokter.</td></tr>
</table>

<h4>5. Compound body-part words</h4>
<p>Dutch loves compounds: <b>hoofd + pijn = hoofdpijn</b>, <b>buik + pijn = buikpijn</b>, <b>keel + pijn = keelpijn</b>, <b>rug + pijn = rugpijn</b>.</p>
""",

        "grammar_letop": """
<ul>
  <li>❌ Ik voel <b>mij</b> niet lekker. → Actually both OK, but <b>me</b> is more common in speech. ✅ Ik voel <b>me</b> niet lekker. <br><em>'Mij' is formal/written; 'me' is standard spoken Dutch.</em></li>
  <li>❌ Mijn hoofd doet <b>zeer</b>. → ✅ Mijn hoofd doet <b>pijn</b>. <br><em>In Belgium, 'zeer' is common, but standard Dutch uses 'pijn'. Both are understood in Ghent!</em></li>
  <li>❌ Ik heb pijn in mijn <b>keel</b>. → ✅ Also correct! But you can also say: Ik heb <b>keelpijn</b>. <br><em>Both patterns work. Compound nouns (keelpijn, hoofdpijn) are very common.</em></li>
  <li>❌ Hij voelt <b>hem</b> ziek. → ✅ Hij voelt <b>zich</b> ziek. <br><em>Reflexive 3rd person = zich, NOT hem/haar.</em></li>
  <li>❌ Ik ben ziek <b>sinds</b> drie dagen. → ✅ Ik ben ziek sinds drie dagen. OR: Ik heb dit <b>al</b> drie dagen. <br><em>Both work! 'Sinds' = since, 'al drie dagen' = for three days already.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Practice: match the complaint</h4>
<table>
  <tr><th>#</th><th>Symptom (EN)</th><th>Dutch</th></tr>
  <tr><td>1</td><td>I have a headache</td><td>Ik heb hoofdpijn.</td></tr>
  <tr><td>2</td><td>My throat hurts</td><td>Mijn keel doet pijn. / Ik heb keelpijn.</td></tr>
  <tr><td>3</td><td>I have a fever</td><td>Ik heb koorts.</td></tr>
  <tr><td>4</td><td>I have a cold</td><td>Ik ben verkouden.</td></tr>
  <tr><td>5</td><td>I feel nauseous</td><td>Ik voel me misselijk.</td></tr>
  <tr><td>6</td><td>My back hurts</td><td>Ik heb rugpijn. / Mijn rug doet pijn.</td></tr>
</table>

<h4>Reflexive verbs — more examples</h4>
<ul>
  <li>Ik <b>voel me</b> vandaag veel beter.</li>
  <li>Hij <b>voelt zich</b> niet lekker sinds gisteren.</li>
  <li>Wij <b>voelen ons</b> moe na het werk.</li>
  <li>Zij <b>wast zich</b> elke ochtend. (to wash oneself)</li>
  <li>Ik <b>vergis me</b> soms. (to make a mistake — reflexive)</li>
  <li>Je moet <b>je</b> goed <b>aankleden</b> als het koud is. (to dress oneself)</li>
</ul>

<h4>Doctor dialogue — complete example</h4>
<p>🩺 Dokter: Goedemorgen. Wat kan ik voor u doen?<br>
🤒 Patiënt: Ik voel me niet lekker. Ik heb hoofdpijn en koorts.<br>
🩺 Dokter: Hoe lang hebt u dit al?<br>
🤒 Patiënt: Sinds twee dagen. Ik hoest ook veel.<br>
🩺 Dokter: Hebt u ook keelpijn?<br>
🤒 Patiënt: Ja, mijn keel doet pijn.<br>
🩺 Dokter: U bent waarschijnlijk verkouden. Ik schrijf een medicijn voor. U moet veel rusten.<br>
🤒 Patiënt: Dank u wel, dokter.</p>
""",

        "grammar_quick": """
<ul>
  <li><b>Ik heb pijn in mijn…</b> / <b>Mijn … doet pijn</b> — two ways to say something hurts</li>
  <li>Compound words: hoofd+pijn = hoofdpijn, buik+pijn = buikpijn, keel+pijn = keelpijn</li>
  <li><b>Ik heb koorts / de griep</b> — use 'hebben' for symptoms</li>
  <li><b>Ik ben verkouden / ziek / moe</b> — use 'zijn' for states</li>
  <li>Reflexive pronouns: ik→me, jij→je, hij/zij→zich, wij→ons, jullie→je, zij(pl.)→zich</li>
  <li>Duration: <b>sinds + time</b> or <b>al + time</b> (Ik heb dit al drie dagen.)</li>
</ul>
""",

        "exercises": [
            {"type": "fill", "q": "Bij de huisarts: Ik heb pijn in mijn ___. (head)", "a": "hoofd",
             "tip": "head = hoofd. Of: Ik heb hoofdpijn."},
            {"type": "fill", "q": "Aan de telefoon met de dokter: Mijn ___ doet pijn. (throat)", "a": "keel",
             "tip": "throat = keel. Samenstelling: keelpijn."},
            {"type": "choice", "q": "Je bent ziek. Hoe zeg je 'I feel sick'?",
             "options": ["Ik voel me ziek.", "Ik voel mij ziek.", "Beide zijn correct."],
             "a": "Beide zijn correct.", "tip": "'Me' (gewoon) en 'mij' (formeel) zijn allebei goed. 'Me' is natuurlijker."},
            {"type": "fill", "q": "In de wachtkamer: Hij voelt ___ niet lekker. (reflexief voornaamwoord)", "a": "zich",
             "tip": "3e persoon reflexief = zich (niet hem)."},
            {"type": "fill", "q": "Na een lange dag aan UGent: Wij voelen ___ moe na het werk.", "a": "ons",
             "tip": "wij → ons (reflexief voornaamwoord voor 'we')."},
            {"type": "choice", "q": "In de winter in Gent: Ik ___ verkouden.", "options": ["heb", "ben", "heeft"],
             "a": "ben", "tip": "Verkouden is een toestand → zijn: Ik BEN verkouden."},
            {"type": "choice", "q": "Bij de dokter: Ik ___ koorts.", "options": ["heb", "ben", "heeft"],
             "a": "heb", "tip": "Koorts is een symptoom → hebben: Ik HEB koorts."},
            {"type": "tf", "q": "'Hoofdpijn' betekent 'headache' en is een samenstelling (hoofd + pijn).", "a": True,
             "correction": "Correct! Nederlands houdt van samenstellingen: hoofd (head) + pijn (pain) = hoofdpijn.",
             "tip": "Samenstellingen zijn heel gewoon in het Nederlands."},
            {"type": "tf", "q": "Het reflexief voornaamwoord voor 'hij' is 'hem'.", "a": False,
             "correction": "Fout! Het reflexief voor hij/zij/het is 'zich', niet hem/haar.",
             "tip": "Reflexief 3e persoon = zich."},
            {"type": "tf", "q": "'Ik ben koorts' is correct.", "a": False,
             "correction": "Fout! Correct: Ik HEB koorts. Koorts is een symptoom → hebben.",
             "tip": "Symptomen gebruiken 'hebben': koorts, hoofdpijn, buikpijn."},
            {"type": "fill", "q": "In het ziekenhuis: Ik hoest al drie ___. (days)", "a": "dagen",
             "tip": "days = dagen (meervoud van dag). 'Al drie dagen' = for three days already."},
            {"type": "translate", "q": "I don't feel well. I have a headache and a fever.",
             "a": "Ik voel me niet lekker. Ik heb hoofdpijn en koorts.",
             "tip": "voel me (reflexief) + niet lekker. hoofdpijn = headache, koorts = fever."},
            {"type": "translate", "q": "If you are sick, you must go to the doctor.",
             "a": "Als je ziek bent, moet je naar de dokter gaan.",
             "tip": "Als-bijzin (werkwoord einde: bent) + hoofdzin (inversie: moet je) + gaan op einde."},
            {"type": "reorder", "q": "me / niet / ik / lekker / voel",
             "a": "Ik voel me niet lekker.",
             "tip": "Subject (Ik) + werkwoord (voel) + reflexief (me) + niet lekker."},
            {"type": "reorder", "q": "dokter / de / een / schrijft / voor / medicijn",
             "a": "De dokter schrijft een medicijn voor.",
             "tip": "Scheidbaar werkwoord: voor·schrijven → schrijft … voor."},
        ],

        "jouw_beurt": "Write a short doctor dialogue (6–8 lines) in Dutch. You are the patient.\n\n"
                      "Include:\n"
                      "• Dokter: Wat kan ik voor u doen?\n"
                      "• Describe 2-3 symptoms (use heb/ben + body parts)\n"
                      "• Say how long you've had the symptoms (sinds / al)\n"
                      "• Dokter gives advice (Als je … moet je …)\n\n"
                      "Use: verkouden, koorts, hoofdpijn, keelpijn, zich voelen, medicijn.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 9 — Gent: Je stad beschrijven
    # ──────────────────────────────────────────────
    {
        "id": 9,
        "title": "Gent – Je stad beschrijven & Vergelijkingen",
        "chapter": "Hoofdstuk 4 – Gent, mijn stad",
        "book_page": "NT2 Drempel 2, H4 p. 66–78",

        "review": "You've covered daily life, stories, health and the doctor. Now we focus on your city — <b>Gent</b>! "
                  "You'll learn to describe places, give directions, compare things using <b>comparatives</b> "
                  "(groter, mooier) and <b>superlatives</b> (grootst, mooist). Since you live in Ghent, "
                  "all examples use real Ghent locations!",

        "vocabulary": [
            ("de stad", "city", "Gent is een mooie stad."),
            ("het centrum", "centre", "Het centrum van Gent is gezellig."),
            ("de brug", "bridge", "De Sint-Michielsbrug is beroemd."),
            ("de kerk", "church", "De Sint-Baafskathedraal is een grote kerk."),
            ("het plein", "square", "De Korenmarkt is een bekend plein."),
            ("de gracht", "canal", "Gent heeft mooie grachten."),
            ("het station", "train station",
             "Gent-Sint-Pieters is het grote station."),
            ("de universiteit", "university", "UGent is een grote universiteit."),
            ("gezellig", "cozy / pleasant", "De Graslei is heel gezellig."),
            ("druk", "busy / crowded", "De Veldstraat is druk op zaterdag."),
            ("rustig", "quiet / calm", "Het Citadelpark is rustig."),
            ("beroemd", "famous", "Het Lam Gods is beroemd."),
            ("de wijk", "neighbourhood", "Ik woon in een leuke wijk."),
            ("de richting", "direction", "Ga in de richting van het station."),
        ],

        "grammar_title": "Comparatives & Superlatives — Vergelijkingen",

        "grammar_html": """
<h4>1. Comparatives (vergrotende trap) — "more / -er"</h4>
<p>Add <b>-er</b> to the adjective. Use <b>dan</b> (= than).</p>
<table>
  <tr><th>Adjective</th><th>Comparative</th><th>Example</th></tr>
  <tr><td>groot (big)</td><td>grot<b>er</b></td><td>Gent is <b>groter</b> dan Brugge.</td></tr>
  <tr><td>mooi (beautiful)</td><td>mooi<b>er</b></td><td>De Graslei is <b>mooier</b> dan de Korenlei.</td></tr>
  <tr><td>druk (busy)</td><td>druk<b>ker</b></td><td>De Veldstraat is <b>drukker</b> dan het Citadelpark.</td></tr>
  <tr><td>gezellig (cozy)</td><td>gezellig<b>er</b></td><td>Een café is <b>gezelliger</b> dan een restaurant.</td></tr>
  <tr><td>duur (expensive)</td><td>duur<b>der</b></td><td>Het centrum is <b>duurder</b> dan de rand.</td></tr>
</table>

<h4>2. Superlatives (overtreffende trap) — "most / -est"</h4>
<p>Add <b>-st</b> to the adjective. Usually with <b>het</b> or <b>de + -ste</b>.</p>
<table>
  <tr><th>Adjective</th><th>Superlative</th><th>Example</th></tr>
  <tr><td>groot</td><td>het groot<b>st</b> / de groot<b>ste</b></td><td>Brussel is <b>de grootste</b> stad van België.</td></tr>
  <tr><td>mooi</td><td>het mooi<b>st</b> / de mooi<b>ste</b></td><td>Gent is <b>de mooiste</b> stad!</td></tr>
  <tr><td>oud</td><td>het oud<b>st</b> / de oud<b>ste</b></td><td>Sint-Baafs is <b>de oudste</b> kerk.</td></tr>
  <tr><td>druk</td><td>het druk<b>st</b> / de druk<b>ste</b></td><td>Zaterdag is <b>de drukste</b> dag.</td></tr>
</table>

<h4>3. Irregular comparisons</h4>
<table>
  <tr><th>Base</th><th>Comparative</th><th>Superlative</th></tr>
  <tr><td>goed (good)</td><td><b>beter</b></td><td><b>best</b></td></tr>
  <tr><td>veel (much/many)</td><td><b>meer</b></td><td><b>meest</b></td></tr>
  <tr><td>weinig (little/few)</td><td><b>minder</b></td><td><b>minst</b></td></tr>
  <tr><td>graag (gladly)</td><td><b>liever</b></td><td><b>het liefst</b></td></tr>
</table>

<h4>4. Tamil comparison</h4>
<p>Tamil uses "விட (viṭa)" for "than" — e.g., "சென்னை டெல்லியை விட பெரியது". 
Dutch uses <b>dan</b>: "Gent is groter <b>dan</b> Brugge." The pattern is similar: 
A is [adj]-er dan B.</p>

<h4>5. Equality: net zo … als</h4>
<p>To say "as … as": <b>net zo + adjective + als</b></p>
<p>Gent is <b>net zo mooi als</b> Brugge. (Ghent is as beautiful as Bruges.)</p>
""",

        "grammar_letop": """
<ul>
  <li>❌ Gent is groter <b>als</b> Brugge. → ✅ Gent is groter <b>dan</b> Brugge. <br><em>Comparison = dan (NOT als). 'Als' is only used in 'net zo … als' (equality).</em></li>
  <li>❌ De <b>groot</b> stad → ✅ De <b>grote</b> stad. <br><em>Before a noun, adjective gets -e (except het + een + adj). This isn't comparative, just adjective inflection.</em></li>
  <li>❌ Gent is de <b>mooierste</b> stad. → ✅ Gent is de <b>mooiste</b> stad. <br><em>Superlative = base + st(e), NOT comparative + ste.</em></li>
  <li>❌ Dit is <b>goeder</b> dan dat. → ✅ Dit is <b>beter</b> dan dat. <br><em>Goed → beter (irregular, like English good → better).</em></li>
  <li>❌ Ik ga <b>meer graag</b> naar Gent. → ✅ Ik ga <b>liever</b> naar Gent. <br><em>Graag → liever (irregular). "I prefer to go to Ghent."</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Practice: comparative & superlative forms</h4>
<table>
  <tr><th>Base</th><th>Comparative</th><th>Superlative</th></tr>
  <tr><td>klein (small)</td><td>kleiner</td><td>kleinst(e)</td></tr>
  <tr><td>lang (long/tall)</td><td>langer</td><td>langst(e)</td></tr>
  <tr><td>kort (short)</td><td>korter</td><td>kortst(e)</td></tr>
  <tr><td>goedkoop (cheap)</td><td>goedkoper</td><td>goedkoopst(e)</td></tr>
  <tr><td>lekker (tasty)</td><td>lekkerder</td><td>lekkerst(e)</td></tr>
  <tr><td>interessant</td><td>interessanter</td><td>interessantst(e)</td></tr>
</table>

<h4>Describing Ghent — example sentences</h4>
<ul>
  <li>De Graslei is <b>mooier</b> dan de Korenlei, vind ik.</li>
  <li>De Sint-Baafskathedraal is <b>de oudste</b> kerk van Gent.</li>
  <li>Het Citadelpark is <b>rustiger</b> dan de Korenmarkt.</li>
  <li>UGent is <b>een van de grootste</b> universiteiten van België.</li>
  <li>De Veldstraat is <b>de drukste</b> winkelstraat van Gent.</li>
  <li>Ik vind Gent <b>gezelliger</b> dan Brussel.</li>
  <li>Het <b>beste</b> restaurant is in de Patershol.</li>
</ul>

<h4>Spelling rules for comparatives</h4>
<ul>
  <li>Adjective ending in <b>-r</b> → add <b>-der</b>: duur → duur<b>der</b>, lekker → lekker<b>der</b></li>
  <li>Adjective ending in <b>-s</b> → just add <b>-er</b>: fris → fris<b>er</b></li>
  <li>One-syllable with short vowel → double consonant: druk → druk<b>ker</b>, dik → dik<b>ker</b></li>
</ul>
""",

        "grammar_quick": """
<ul>
  <li>Comparative: adjective + <b>-er</b> + <b>dan</b> (A is groter dan B)</li>
  <li>Superlative: <b>de/het</b> + adjective + <b>-st(e)</b> (de grootste stad)</li>
  <li>Equality: <b>net zo</b> + adj + <b>als</b> (net zo mooi als)</li>
  <li>Irregular: goed→beter→best, veel→meer→meest, graag→liever→liefst</li>
  <li>Comparison uses <b>dan</b> (NOT als!)</li>
  <li>Spelling: -r ending → +der; short vowel → double consonant + er</li>
</ul>
""",

        "exercises": [
            {"type": "fill", "q": "Aan een toerist: Gent is ___ (groot + vergrotende trap) dan Brugge.", "a": "groter",
             "tip": "groot + er = groter. Vergelijking → dan."},
            {"type": "fill", "q": "In een reisgids: De Sint-Baafskathedraal is ___ (oud + overtreffende trap) kerk van Gent.", "a": "de oudste",
             "tip": "oud → oudst + e (vóór zelfstandig naamwoord met de). de oudste kerk."},
            {"type": "choice", "q": "Je vergelijkt twee steden: Gent is mooier ___ Brussel.", "options": ["dan", "als", "van"],
             "a": "dan", "tip": "Vergelijking = dan. 'Als' is alleen voor gelijkheid (net zo … als)."},
            {"type": "choice", "q": "In de mensa: Ik vind koffie ___ dan thee.",
             "options": ["lekker", "lekkerder", "lekkerst"], "a": "lekkerder",
             "tip": "Twee dingen vergelijken → vergrotende trap: lekkerder."},
            {"type": "fill", "q": "Over restaurants: Dit restaurant is ___ (goed + vergrotende trap) dan dat restaurant.", "a": "beter",
             "tip": "Goed → beter (onregelmatig, zoals Engels good → better)."},
            {"type": "fill", "q": "In een gesprek: Ik ga ___ (graag + vergrotende trap) naar Gent dan naar Brussel.", "a": "liever",
             "tip": "Graag → liever (onregelmatig). 'Ik ga liever naar Gent.'"},
            {"type": "tf", "q": "De vergrotende trap van 'veel' is 'veeler'.", "a": False,
             "correction": "Fout! Veel → meer (onregelmatig). Zoals Engels much → more.",
             "tip": "Veel → meer → meest (onregelmatig)."},
            {"type": "tf", "q": "'Net zo groot als' betekent 'as big as'.", "a": True,
             "correction": "Correct! Net zo + bijvoeglijk naamwoord + als = as … as.",
             "tip": "Net zo + adj + als = as … as."},
            {"type": "tf", "q": "'Gent is groter als Brugge' is correct.", "a": False,
             "correction": "Fout! Correct: Gent is groter DAN Brugge. Vergelijking = dan (niet als!).",
             "tip": "Vergelijking gebruikt altijd 'dan', niet 'als'."},
            {"type": "choice", "q": "Over parken: Het Citadelpark is ___ dan de Korenmarkt.",
             "options": ["rustig", "rustiger", "rustigste"], "a": "rustiger",
             "tip": "Twee plaatsen vergelijken → vergrotende trap: rustiger + dan."},
            {"type": "fill", "q": "In de Veldstraat: Dit is ___ (druk + overtreffende trap) winkelstraat van Gent.", "a": "de drukste",
             "tip": "druk → drukst + e (vóór zelfstandig naamwoord). 'de drukste' (the busiest)."},
            {"type": "translate", "q": "Ghent is bigger than Bruges but smaller than Brussels.",
             "a": "Gent is groter dan Brugge maar kleiner dan Brussel.",
             "tip": "groter dan + maar + kleiner dan. Twee vergelijkingen met maar."},
            {"type": "translate", "q": "The Graslei is the most beautiful place in Ghent.",
             "a": "De Graslei is de mooiste plek in Gent.",
             "tip": "Overtreffende trap vóór zelfstandig naamwoord: de mooiste plek. plek = place."},
            {"type": "reorder", "q": "mooiste / Gent / de / is / stad / van / België",
             "a": "Gent is de mooiste stad van België.",
             "tip": "Gent is + de mooiste stad + van België."},
            {"type": "translate", "q": "I prefer cycling to taking the tram. (use liever)",
             "a": "Ik fiets liever dan dat ik de tram neem.",
             "tip": "liever + dan dat + bijzin. Of eenvoudiger: Ik fiets liever dan de tram nemen."},
        ],

        "jouw_beurt": "Describe Ghent in 6–8 sentences using comparatives and superlatives.\n\n"
                      "Compare real places you know:\n"
                      "• De Graslei vs de Korenlei (mooi)\n"
                      "• Het Citadelpark vs de Korenmarkt (rustig / druk)\n"
                      "• Gent vs Brussel (groot, gezellig)\n"
                      "• Your favourite place (de … -ste plek)\n\n"
                      "Use: groter dan, mooier dan, de mooiste, net zo … als, liever, het beste.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 10 — Inpakken & Wegwezen: Reizen & Toekomst
    # ──────────────────────────────────────────────
    {
        "id": 10,
        "title": "Inpakken & Wegwezen – Reizen & De Toekomst",
        "chapter": "Hoofdstuk 5 – Inpakken & Wegwezen",
        "book_page": "NT2 Drempel 2, H5 p. 79–92",

        "review": "In Session 9 you described Ghent using comparatives and superlatives. "
                  "Now you plan a trip! You'll learn <b>travel vocabulary</b>, how to talk about "
                  "<b>the future</b> (gaan + infinitive & zullen + infinitive), and practise asking "
                  "questions at the station, hotel, and airport. This session also reviews separable verbs "
                  "(inpakken, aankomen, vertrekken) in a travel context.",

        "vocabulary": [
            ("de reis", "trip / journey", "We maken een reis naar Amsterdam."),
            ("de vakantie", "holiday / vacation", "In de zomer heb ik vakantie."),
            ("het vliegtuig", "airplane", "We vliegen met het vliegtuig."),
            ("de trein", "train", "De trein naar Brussel vertrekt om 9 uur."),
            ("het hotel", "hotel", "We logeren in een hotel."),
            ("de koffer", "suitcase", "Ik pak mijn koffer in."),
            ("inpakken", "to pack (sep.)", "Heb je alles ingepakt?"),
            ("vertrekken", "to depart", "De trein vertrekt van spoor 3."),
            ("aankomen", "to arrive (sep.)", "We komen om 12 uur aan."),
            ("boeken", "to book", "Ik boek een hotel online."),
            ("het paspoort", "passport", "Vergeet je paspoort niet!"),
            ("de bestemming", "destination", "Wat is je bestemming?"),
            ("het spoor", "platform / track", "De trein vertrekt van spoor 5."),
            ("de vertraging", "delay", "De trein heeft 10 minuten vertraging."),
        ],

        "grammar_title": "Future Tense — Gaan + infinitive & Zullen + infinitive",

        "grammar_html": """
<h4>1. Two ways to talk about the future</h4>
<table>
  <tr><th>Structure</th><th>Use</th><th>Example</th></tr>
  <tr><td><b>gaan</b> + infinitive</td><td>plans, intentions (most common)</td><td>Ik <b>ga</b> naar Parijs <b>reizen</b>.</td></tr>
  <tr><td><b>zullen</b> + infinitive</td><td>predictions, promises, formal</td><td>Het <b>zal</b> morgen <b>regenen</b>.</td></tr>
  <tr><td>present tense + time word</td><td>near future (very common!)</td><td>Ik <b>vertrek</b> morgen.</td></tr>
</table>

<h4>2. Conjugation: gaan & zullen</h4>
<table>
  <tr><th>Subject</th><th>gaan</th><th>zullen</th></tr>
  <tr><td>ik</td><td>ga</td><td>zal</td></tr>
  <tr><td>jij/je</td><td>gaat</td><td>zult / zal</td></tr>
  <tr><td>hij/zij/het</td><td>gaat</td><td>zal</td></tr>
  <tr><td>wij</td><td>gaan</td><td>zullen</td></tr>
  <tr><td>jullie</td><td>gaan</td><td>zullen</td></tr>
  <tr><td>zij (pl.)</td><td>gaan</td><td>zullen</td></tr>
</table>

<h4>3. Word order: infinitive goes to the END</h4>
<pre>
  Ik ga volgende week naar Amsterdam reizen.
       ↑ gaan (pos. 2)                ↑ infinitive (END)
  
  We zullen een hotel boeken.
       ↑ zullen (pos. 2)    ↑ infinitive (END)
</pre>

<h4>4. Tamil comparison</h4>
<p>Tamil uses "-போகிறேன் (-pōkiṟēṉ)" = "I am going to…" for future plans — very similar to 
Dutch <b>gaan + infinitive</b>! "நான் பாரிஸ் போகப் போகிறேன்" ≈ "Ik ga naar Parijs reizen."
Dutch <b>zullen</b> is more like a prediction or promise — Tamil equivalent would be the simple future "-வேன் (-vēṉ)".</p>

<h4>5. Separable verbs in future tense</h4>
<p>With gaan/zullen, separable verbs stay <b>together</b> as one infinitive at the end:</p>
<table>
  <tr><th>Present (separated)</th><th>Future with gaan (together)</th></tr>
  <tr><td>Ik pak mijn koffer <b>in</b>.</td><td>Ik ga mijn koffer <b>inpakken</b>.</td></tr>
  <tr><td>De trein komt om 9 uur <b>aan</b>.</td><td>De trein gaat om 9 uur <b>aankomen</b>.</td></tr>
  <tr><td>We vertrekken morgen.</td><td>We gaan morgen <b>vertrekken</b>.</td></tr>
</table>
""",

        "grammar_letop": """
<ul>
  <li>❌ Ik ga reizen naar Parijs. → ✅ Ik ga naar Parijs <b>reizen</b>. <br><em>The infinitive goes to the END of the sentence, not right after gaan.</em></li>
  <li>❌ Ik ga mijn koffer <b>in pakken</b>. → ✅ Ik ga mijn koffer <b>inpakken</b>. <br><em>With gaan/zullen, separable verbs stay together as one word at the end.</em></li>
  <li>❌ Ik <b>zal ga</b> naar Amsterdam. → ✅ Ik <b>ga</b> naar Amsterdam reizen. OR Ik <b>zal</b> naar Amsterdam reizen. <br><em>Don't combine gaan + zullen! Use one or the other.</em></li>
  <li>❌ Morgen ik ga vertrekken. → ✅ Morgen <b>ga ik</b> vertrekken. <br><em>Time word first → inversie (verb before subject).</em></li>
  <li>❌ De trein <b>vertrekken</b> om 9 uur. → ✅ De trein <b>vertrekt</b> om 9 uur. <br><em>Present tense still needs conjugation! Infinitive only after gaan/zullen.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>At the station — useful phrases</h4>
<table>
  <tr><th>Dutch</th><th>English</th></tr>
  <tr><td>Eén enkele reis naar Brussel, alstublieft.</td><td>A single ticket to Brussels, please.</td></tr>
  <tr><td>Een retour naar Amsterdam, alstublieft.</td><td>A return ticket to Amsterdam, please.</td></tr>
  <tr><td>Van welk spoor vertrekt de trein?</td><td>From which platform does the train depart?</td></tr>
  <tr><td>De trein heeft 10 minuten vertraging.</td><td>The train is 10 minutes delayed.</td></tr>
  <tr><td>Moet ik overstappen?</td><td>Do I need to transfer?</td></tr>
  <tr><td>Hoe laat komt de trein aan?</td><td>What time does the train arrive?</td></tr>
</table>

<h4>Practice: present vs future</h4>
<table>
  <tr><th>Present</th><th>Future (gaan)</th></tr>
  <tr><td>Ik reis naar Spanje.</td><td>Ik ga naar Spanje reizen.</td></tr>
  <tr><td>We boeken een hotel.</td><td>We gaan een hotel boeken.</td></tr>
  <tr><td>Hij pakt zijn koffer in.</td><td>Hij gaat zijn koffer inpakken.</td></tr>
  <tr><td>De trein vertrekt om 8 uur.</td><td>De trein gaat om 8 uur vertrekken.</td></tr>
  <tr><td>Jullie komen morgen aan.</td><td>Jullie gaan morgen aankomen.</td></tr>
</table>

<h4>Zullen — predictions & promises</h4>
<ul>
  <li>Het <b>zal</b> morgen mooi weer <b>zijn</b>. (prediction)</li>
  <li>Ik <b>zal</b> je een kaartje <b>sturen</b>. (promise)</li>
  <li><b>Zullen</b> we naar het strand <b>gaan</b>? (suggestion: Shall we…?)</li>
  <li>Het <b>zal</b> wel druk <b>zijn</b> op het vliegveld. (expectation)</li>
</ul>
""",

        "grammar_quick": """
<ul>
  <li><b>Gaan + infinitive</b> = plans/intentions (most common future)</li>
  <li><b>Zullen + infinitive</b> = predictions, promises, suggestions (Zullen we…?)</li>
  <li><b>Present + time word</b> = near future (Ik vertrek morgen.)</li>
  <li>Infinitive always goes to the END of the sentence</li>
  <li>Separable verbs stay TOGETHER with gaan/zullen (inpakken, not in…pakken)</li>
  <li>Don't combine gaan + zullen — use one or the other</li>
</ul>
""",

        "exercises": [
            {"type": "fill", "q": "Aan je collega: Ik ___ volgende week naar Parijs reizen. (gaan)", "a": "ga",
             "tip": "ik + gaan = ik ga. Het infinitief 'reizen' staat op het einde."},
            {"type": "fill", "q": "Weerbericht: Het ___ morgen regenen. (zullen)", "a": "zal",
             "tip": "het + zullen = het zal. Voorspelling → zullen."},
            {"type": "choice", "q": "Vakantie plannen: We gaan een hotel ___.",
             "options": ["boeken", "boekt", "geboekt"], "a": "boeken",
             "tip": "Na gaan → infinitief (boeken). Niet vervoegd, niet voltooid deelwoord."},
            {"type": "choice", "q": "Op Gent-Sint-Pieters: Morgen ___ ik naar Amsterdam.",
             "options": ["vertrek", "vertrekt", "vertrekken"], "a": "vertrek",
             "tip": "Tegenwoordige tijd + tijdswoord voor nabije toekomst. ik → vertrek (geen -t)."},
            {"type": "fill", "q": "Thuis: Hij gaat zijn koffer ___. (inpakken)", "a": "inpakken",
             "tip": "Met gaan blijven scheidbare werkwoorden samen: inpakken (niet in … pakken)."},
            {"type": "tf", "q": "'Ik ga reizen naar Spanje' heeft een correcte woordvolgorde.", "a": False,
             "correction": "Fout! Het infinitief gaat naar het EINDE: Ik ga naar Spanje reizen.",
             "tip": "Infinitief altijd op het einde van de zin."},
            {"type": "tf", "q": "'Zullen we naar het strand gaan?' betekent 'Shall we go to the beach?'", "a": True,
             "correction": "Correct! Zullen we…? = Shall we…? (voorstel).",
             "tip": "Zullen we…? is een voorstel."},
            {"type": "tf", "q": "'Morgen ik ga vertrekken' is correct.", "a": False,
             "correction": "Fout! Tijdswoord eerst → inversie: Morgen GA IK vertrekken.",
             "tip": "Tijdswoord op positie 1 → werkwoord op positie 2 → inversie."},
            {"type": "fill", "q": "Een voorstel: ___ we naar de Ardennen gaan dit weekend?", "a": "Zullen",
             "tip": "Voorstel → Zullen we…? (Shall we…?)"},
            {"type": "choice", "q": "Op het station: De trein ___ van spoor 3.",
             "options": ["vertrekt", "vertrekken", "vertrek"], "a": "vertrekt",
             "tip": "De trein (hij) → vertrekt. Tegenwoordige tijd."},
            {"type": "fill", "q": "Aan het loket: Van welk ___ vertrekt de trein naar Brussel?", "a": "spoor",
             "tip": "spoor = platform/track. Van welk spoor…?"},
            {"type": "translate", "q": "I am going to travel to Spain next summer.",
             "a": "Ik ga volgende zomer naar Spanje reizen.",
             "tip": "ik ga + tijd (volgende zomer) + bestemming (naar Spanje) + infinitief op EINDE (reizen)."},
            {"type": "translate", "q": "Shall we book a hotel in Bruges?",
             "a": "Zullen we een hotel in Brugge boeken?",
             "tip": "Voorstel: Zullen we + … + infinitief op einde (boeken)?"},
            {"type": "reorder", "q": "ga / ik / mijn / inpakken / koffer / vanavond",
             "a": "Ik ga vanavond mijn koffer inpakken.",
             "tip": "Ik ga (pos. 2) + tijd (vanavond) + object (mijn koffer) + infinitief EINDE (inpakken)."},
            {"type": "reorder", "q": "de / vertraging / trein / heeft / minuten / 15",
             "a": "De trein heeft 15 minuten vertraging.",
             "tip": "De trein heeft + hoeveelheid + vertraging. Veel gehoord op het station!"},
        ],

        "jouw_beurt": "Plan your dream holiday! Write 6–8 sentences about a trip you want to make.\n\n"
                      "Include:\n"
                      "• Where you're going (Ik ga naar … reizen.)\n"
                      "• How you'll travel (met het vliegtuig / de trein)\n"
                      "• What you'll do there (Ik ga … bezoeken / zwemmen / eten)\n"
                      "• A prediction (Het zal … zijn.)\n"
                      "• A suggestion for a friend (Zullen we …?)\n\n"
                      "Use: gaan + infinitive, zullen + infinitive, inpakken, boeken, aankomen.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 11 — Het Perfectum (Voltooid Tegenwoordige Tijd)
    # ──────────────────────────────────────────────
    {
        "id": 11,
        "title": "Het Perfectum – Voltooid Tegenwoordige Tijd (hebben/zijn + voltooid deelwoord)",
        "chapter": "Hoofdstuk 6 – Grammatica Verdieping",
        "book_page": "NT2 Drempel 2, H6 p. 93–105",

        "review": "In Session 4 you learned the imperfectum ('t kofschip). Now we master the other past tense: "
                  "the <b>perfectum</b> (present perfect). Dutch uses both past tenses but the perfectum is "
                  "more common in <b>spoken Dutch</b> (just like Tamil's முடிந்த காலம்). "
                  "You need: <b>hebben/zijn</b> (conjugated) + <b>voltooid deelwoord</b> (past participle).",

        "vocabulary": [
            ("het voltooid deelwoord", "past participle",
             "Ge-werk-t is het voltooid deelwoord van werken."),
            ("regelmatig", "regular", "Werken is een regelmatig werkwoord."),
            ("onregelmatig", "irregular", "Gaan is een onregelmatig werkwoord."),
            ("hebben", "to have (auxiliary)", "Ik heb gewerkt."),
            ("zijn", "to be (auxiliary)", "Ik ben gegaan."),
            ("al", "already", "Ik heb al gegeten."),
            ("nog niet", "not yet", "Ik heb nog niet gegeten."),
            ("net", "just (now)", "Ik heb net gebeld."),
            ("gisteren", "yesterday", "Gisteren heb ik gefietst."),
            ("vorige week", "last week", "Vorige week ben ik naar Brugge gegaan."),
            ("verhuizen", "to move (house)", "Ik ben naar Gent verhuisd."),
            ("gebeuren", "to happen", "Wat is er gebeurd?"),
        ],

        "grammar_title": "Het Perfectum — hebben/zijn + voltooid deelwoord",

        "grammar_html": """
<h4>1. How to form the perfectum</h4>
<pre>
  subject + hebben/zijn (conjugated) + … + voltooid deelwoord (END)
  Ik <b>heb</b> gisteren in Gent <b>gewandeld</b>.
  Ik <b>ben</b> naar Brugge <b>gegaan</b>.
</pre>

<h4>2. Forming the voltooid deelwoord (past participle)</h4>
<table>
  <tr><th>Type</th><th>Rule</th><th>Example</th></tr>
  <tr><td>Regular ('t kofschip)</td><td><b>ge-</b> + stam + <b>-t</b></td><td>werken → gewerk<b>t</b>, fietsen → gefies<b>t</b></td></tr>
  <tr><td>Regular (other)</td><td><b>ge-</b> + stam + <b>-d</b></td><td>leven → geleefd, wandelen → gewandel<b>d</b></td></tr>
  <tr><td>Irregular (strong)</td><td><b>ge-</b> + changed stem + <b>-en</b></td><td>gaan → gegaan, schrijven → geschreven</td></tr>
  <tr><td>Separable</td><td>prefix + <b>ge</b> + stam + -t/-d/-en</td><td>opbellen → <b>opgebeld</b>, aankomen → <b>aangekomen</b></td></tr>
  <tr><td>Inseparable (be-/ver-/ge-/her-/er-/ont-)</td><td>NO <b>ge-</b></td><td>vertellen → <b>verteld</b>, bezoeken → <b>bezocht</b></td></tr>
</table>

<h4>3. 't kofschip rule for -t or -d</h4>
<p>If the stem ends in <b>t, k, f, s, ch, p</b> → participle ends in <b>-t</b>. Otherwise → <b>-d</b>.</p>
<pre>
  werken → stem: werk (k!) → ge-werk-<b>t</b>
  fietsen → stem: fiets (s!) → ge-fietst → <b>gefietst</b>
  wandelen → stem: wandel (l) → ge-wandel-<b>d</b> → <b>gewandeld</b>
  leven → stem: leef (f!) → ge-leef-<b>t</b> → <b>geleefd</b> ← wait, f → -t? Yes!
</pre>

<h4>4. Hebben or Zijn? — Complete overzicht</h4>
<table>
  <tr><th>Hulpwerkwoord</th><th>Wanneer</th><th>Veelgebruikte werkwoorden</th></tr>
  <tr><td><b>hebben</b></td><td>De meeste werkwoorden (transitief, activiteiten)</td><td>werken, eten, drinken, kopen, maken, bellen, lezen, schrijven, koken, studeren</td></tr>
  <tr><td><b>zijn</b></td><td>Beweging A→B, verandering van toestand, zijn/blijven/worden</td><td>gaan, komen, vertrekken, verhuizen, vallen, rijden, vliegen, worden, zijn, blijven, gebeuren, beginnen, stoppen, opstaan, groeien, sterven, slagen, zakken, genezen, trouwen</td></tr>
</table>

<h4>📋 Complete lijst: zijn-werkwoorden (ben/is/zijn + voltooid deelwoord)</h4>
<table>
  <tr><th>Werkwoord</th><th>Perfectum</th><th>Categorie</th></tr>
  <tr><td>gaan</td><td>ik <b>ben</b> gegaan</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>komen</td><td>ik <b>ben</b> gekomen</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>vertrekken</td><td>ik <b>ben</b> vertrokken</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>verhuizen</td><td>ik <b>ben</b> verhuisd</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>rijden</td><td>ik <b>ben</b> gereden</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>vliegen</td><td>ik <b>ben</b> gevlogen</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>lopen</td><td>ik <b>ben</b> gelopen</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>fietsen</td><td>ik <b>ben</b> gefietst</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>vallen</td><td>ik <b>ben</b> gevallen</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>opstaan</td><td>ik <b>ben</b> opgestaan</td><td>🚶 Beweging A→B</td></tr>
  <tr><td>worden</td><td>ik <b>ben</b> geworden</td><td>🔄 Verandering</td></tr>
  <tr><td>groeien</td><td>ik <b>ben</b> gegroeid</td><td>🔄 Verandering</td></tr>
  <tr><td>sterven</td><td>hij <b>is</b> gestorven</td><td>🔄 Verandering</td></tr>
  <tr><td>beginnen</td><td>ik <b>ben</b> begonnen</td><td>🔄 Verandering</td></tr>
  <tr><td>stoppen</td><td>ik <b>ben</b> gestopt</td><td>🔄 Verandering</td></tr>
  <tr><td>genezen</td><td>ik <b>ben</b> genezen</td><td>🔄 Verandering</td></tr>
  <tr><td>slagen</td><td>ik <b>ben</b> geslaagd</td><td>🔄 Verandering</td></tr>
  <tr><td>zakken</td><td>ik <b>ben</b> gezakt</td><td>🔄 Verandering</td></tr>
  <tr><td>trouwen</td><td>ik <b>ben</b> getrouwd</td><td>🔄 Verandering</td></tr>
  <tr><td>zijn</td><td>ik <b>ben</b> geweest</td><td>⭐ Speciaal</td></tr>
  <tr><td>blijven</td><td>ik <b>ben</b> gebleven</td><td>⭐ Speciaal</td></tr>
  <tr><td>gebeuren</td><td>het <b>is</b> gebeurd</td><td>⭐ Speciaal</td></tr>
</table>
<p><b>Ezelsbruggetje:</b> Als je kunt vragen "waarheen?" of "waarnaar?" → gebruik <b>zijn</b>.<br>
Ik ben naar Gent <b>gegaan</b> (waarheen? → zijn). Ik heb in het park <b>gewandeld</b> (geen richting → hebben).</p>

<h4>5. Tamil comparison</h4>
<p>Tamil perfect: "நான் சாப்பிட்டேன் (nāṉ cāppiṭṭēṉ)" = I ate/have eaten. Tamil merges past tenses into one.
Dutch has TWO past tenses. The perfectum (heb gegeten) is for <b>conversation</b>, the imperfectum (at) is for <b>stories/writing</b>.</p>
""",

        "grammar_letop": """
<ul>
  <li>❌ Ik heb naar Brugge <b>gegaan</b>. → ✅ Ik <b>ben</b> naar Brugge gegaan. <br><em>Gaan = movement A→B → use ZIJN, not hebben.</em></li>
  <li>❌ Ik heb <b>gewerken</b>. → ✅ Ik heb <b>gewerkt</b>. <br><em>Participle ≠ infinitive! ge- + stam + -t (werk → 't kofschip → -t).</em></li>
  <li>❌ Ik heb <b>gebeld op</b>. → ✅ Ik heb <b>opgebeld</b>. <br><em>Separable verb: prefix + ge + stam + ending = OP-ge-bel-d.</em></li>
  <li>❌ Ik heb <b>geverteld</b>. → ✅ Ik heb <b>verteld</b>. <br><em>Inseparable prefix (ver-) → NO ge-! vertellen → verteld.</em></li>
  <li>❌ Ik heb gewandel<b>t</b>. → ✅ Ik heb gewandel<b>d</b>. <br><em>Stem = wandel, 'l' is NOT in 't kofschip → ending is -d.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Common irregular past participles (must memorise!)</h4>
<table>
  <tr><th>Infinitive</th><th>Participle</th><th>Auxiliary</th></tr>
  <tr><td>gaan</td><td>gegaan</td><td>zijn</td></tr>
  <tr><td>komen</td><td>gekomen</td><td>zijn</td></tr>
  <tr><td>zijn</td><td>geweest</td><td>zijn</td></tr>
  <tr><td>hebben</td><td>gehad</td><td>hebben</td></tr>
  <tr><td>doen</td><td>gedaan</td><td>hebben</td></tr>
  <tr><td>zien</td><td>gezien</td><td>hebben</td></tr>
  <tr><td>eten</td><td>gegeten</td><td>hebben</td></tr>
  <tr><td>drinken</td><td>gedronken</td><td>hebben</td></tr>
  <tr><td>schrijven</td><td>geschreven</td><td>hebben</td></tr>
  <tr><td>lezen</td><td>gelezen</td><td>hebben</td></tr>
  <tr><td>nemen</td><td>genomen</td><td>hebben</td></tr>
  <tr><td>worden</td><td>geworden</td><td>zijn</td></tr>
  <tr><td>blijven</td><td>gebleven</td><td>zijn</td></tr>
  <tr><td>beginnen</td><td>begonnen</td><td>zijn</td></tr>
</table>

<h4>Practice: form the participle</h4>
<table>
  <tr><th>Infinitive</th><th>Stam</th><th>'t kofschip?</th><th>Participle</th></tr>
  <tr><td>werken</td><td>werk</td><td>k → yes</td><td>gewerkt</td></tr>
  <tr><td>maken</td><td>maak</td><td>k → yes</td><td>gemaakt</td></tr>
  <tr><td>wonen</td><td>woon</td><td>n → no</td><td>gewoond</td></tr>
  <tr><td>studeren</td><td>studeer</td><td>r → no</td><td>gestudeerd</td></tr>
  <tr><td>reizen</td><td>reis</td><td>s → yes</td><td>gereisd</td></tr>
  <tr><td>opbellen</td><td>bel (sep.)</td><td>l → no</td><td>opgebeld</td></tr>
</table>
""",

        "grammar_quick": """
<ul>
  <li>Perfectum = <b>hebben/zijn</b> + <b>voltooid deelwoord</b> (at END)</li>
  <li>Regular: <b>ge-</b> + stam + <b>-t</b> ('t kofschip) or <b>-d</b> (other)</li>
  <li>Irregular: <b>ge-</b> + changed stem + <b>-en</b> (gegaan, gekomen, geschreven)</li>
  <li>Separable: prefix + ge + rest (opgebeld, aangekomen)</li>
  <li>Inseparable (be-/ver-/ge-/her-/ont-/er-): NO ge- (verteld, bezocht)</li>
  <li><b>Zijn</b>: movement A→B (gaan, komen), state change (worden), zijn/blijven</li>
  <li><b>Hebben</b>: everything else</li>
</ul>
""",

        "exercises": [
            {"type": "fill", "q": "Na het werk: Ik ___ gisteren in het Citadelpark gewandeld. (hebben/zijn)", "a": "heb",
             "tip": "Wandelen = activiteit (niet A→B) → hebben. ik heb."},
            {"type": "fill", "q": "Een dagtrip: Zij ___ naar Brussel gegaan. (hebben/zijn)", "a": "is",
             "tip": "Gaan = beweging A→B → zijn. zij → is."},
            {"type": "fill", "q": "In de trein: Ik heb een boek ___. (lezen → voltooid deelwoord)", "a": "gelezen",
             "tip": "Lezen is onregelmatig: gelezen (ge- + lez- + en)."},
            {"type": "fill", "q": "Aan UGent: We hebben Nederlands ___. (studeren → voltooid deelwoord)", "a": "gestudeerd",
             "tip": "studeren → stam: studeer, r niet in 't kofschip → ge-studeer-d."},
            {"type": "choice", "q": "Over je verhuizing: Ik ___ vorige week naar Gent verhuisd.",
             "options": ["heb", "ben", "was"], "a": "ben",
             "tip": "Verhuizen = verandering van toestand → zijn. Ik ben verhuisd."},
            {"type": "choice", "q": "Wat is het voltooid deelwoord van 'werken'?",
             "options": ["gewerkt", "gewerken", "gewerkd"], "a": "gewerkt",
             "tip": "werken → stam: werk, k = 't kofschip → ge-werk-t."},
            {"type": "choice", "q": "Wat is het voltooid deelwoord van 'opbellen'?",
             "options": ["gebeld op", "opgebeld", "geopbeld"], "a": "opgebeld",
             "tip": "Scheidbaar: prefix + ge + stam + uitgang = op-ge-bel-d."},
            {"type": "tf", "q": "Werkwoorden met onscheidbare prefixen (be-, ver-, ge-, ont-) krijgen GEEN 'ge-' in het voltooid deelwoord.", "a": True,
             "correction": "Correct! vertellen → verteld (niet geverteld). bezoeken → bezocht (niet gebezocht).",
             "tip": "Onscheidbare prefixen: be-, ver-, ge-, her-, ont-, er-."},
            {"type": "tf", "q": "'Ik heb gegaan' is correct Nederlands.", "a": False,
             "correction": "Fout! Gaan gebruikt ZIJN: Ik BEN gegaan. Beweging A→B → altijd zijn.",
             "tip": "Gaan/komen/vertrekken/verhuizen → altijd met zijn."},
            {"type": "tf", "q": "'Ik ben in het Citadelpark gewandeld' is correct.", "a": False,
             "correction": "Fout! Wandelen = activiteit → hebben: Ik HEB in het Citadelpark gewandeld.",
             "tip": "Wandelen (zonder duidelijke A→B) → hebben."},
            {"type": "fill", "q": "Na een ongeluk: Wat is er ___? (gebeuren → voltooid deelwoord)", "a": "gebeurd",
             "tip": "Gebeuren heeft onscheidbaar prefix ge- → geen extra ge-: gebeurd. Hulpww: zijn."},
            {"type": "translate", "q": "I have already eaten. (use perfectum)",
             "a": "Ik heb al gegeten.",
             "tip": "eten → gegeten (onregelmatig). hebben (activiteit). al = already."},
            {"type": "translate", "q": "We have visited the Sint-Baafskathedraal.",
             "a": "We hebben de Sint-Baafskathedraal bezocht.",
             "tip": "bezoeken → bezocht (onscheidbaar prefix be- → geen ge-). hebben (activiteit)."},
            {"type": "reorder", "q": "heb / gisteren / ik / gefietst / naar / UGent",
             "a": "Ik heb gisteren naar UGent gefietst.",
             "tip": "Ik heb (pos. 2) + tijd + bestemming + voltooid deelwoord op EINDE."},
            {"type": "reorder", "q": "is / hij / gekomen / vandaag / niet",
             "a": "Hij is vandaag niet gekomen.",
             "tip": "Hij is + tijd (vandaag) + niet + voltooid deelwoord (gekomen) op einde."},
        ],

        "jouw_beurt": "Write 8 sentences about what you did last weekend using the perfectum.\n\n"
                      "Mix hebben and zijn verbs:\n"
                      "• Ik heb … (gewerkt, gekookt, gestudeerd, gelezen)\n"
                      "• Ik ben … (gegaan, gefietst naar …, gekomen, geweest)\n\n"
                      "Include: al (already), nog niet (not yet), gisteren, vorige week.\n"
                      "Try at least 2 irregular participles and 1 separable verb.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 12 — Perfectum vs Imperfectum: Wanneer welke?
    # ──────────────────────────────────────────────
    {
        "id": 12,
        "title": "Perfectum vs Imperfectum – Wanneer gebruik je welke?",
        "chapter": "Hoofdstuk 6 – Grammatica Verdieping",
        "book_page": "NT2 Drempel 2, H6 p. 105–115",

        "review": "Session 4 covered the imperfectum ('t kofschip, strong verbs). Session 11 covered the perfectum "
                  "(hebben/zijn + voltooid deelwoord). Now the big question: <b>when do you use which?</b> "
                  "This session teaches you the rules and gives you lots of practice switching between both.",

        "vocabulary": [
            ("vroeger", "in the past / formerly", "Vroeger woonde ik in India."),
            ("toen", "then / at that time", "Toen was ik nog een student."),
            ("plotseling", "suddenly", "Plotseling begon het te regenen."),
            ("daarna", "after that", "Daarna zijn we naar huis gegaan."),
            ("eerst", "first", "Eerst heb ik ontbeten."),
            ("tegelijk", "at the same time", "We aten en praatten tegelijk."),
            ("altijd", "always", "Ik at altijd rijst als kind."),
            ("vaak", "often", "We gingen vaak naar het strand."),
            ("het verhaal", "story", "Vertel een verhaal in het imperfectum."),
            ("de herinnering", "memory", "Ik heb mooie herinneringen aan India."),
            ("ondertussen", "meanwhile", "Ondertussen kookte mijn moeder."),
            ("opeens", "all of a sudden", "Opeens viel de stroom uit."),
        ],

        "grammar_title": "Perfectum vs Imperfectum — When to Use Which?",

        "grammar_html": """
<h4>1. The golden rule</h4>
<table>
  <tr><th>Tense</th><th>When</th><th>Think of it as…</th></tr>
  <tr><td><b>Perfectum</b><br>(heb/ben + participle)</td><td>Spoken Dutch, conversations, recent events, results</td><td><b>TALKING</b> about the past</td></tr>
  <tr><td><b>Imperfectum</b><br>(simple past form)</td><td>Written stories, background, habits, descriptions, formal</td><td><b>TELLING a story</b></td></tr>
</table>

<h4>2. Detailed comparison</h4>
<table>
  <tr><th>Situation</th><th>Use</th><th>Example</th></tr>
  <tr><td>Conversation about yesterday</td><td>Perfectum</td><td>"Ik <b>heb</b> gisteren <b>gefietst</b>."</td></tr>
  <tr><td>Writing a story about childhood</td><td>Imperfectum</td><td>"Toen ik klein <b>was</b>, <b>woonde</b> ik in Chennai."</td></tr>
  <tr><td>Background description</td><td>Imperfectum</td><td>"Het <b>regende</b> en het <b>was</b> koud."</td></tr>
  <tr><td>Sudden action in a story</td><td>Perfectum or Imperf.</td><td>"Opeens <b>is</b> hij <b>gevallen</b>." / "Opeens <b>viel</b> hij."</td></tr>
  <tr><td>Regular habits in the past</td><td>Imperfectum</td><td>"We <b>gingen</b> vaak naar het park."</td></tr>
  <tr><td>Completed action with result now</td><td>Perfectum</td><td>"Ik <b>heb</b> mijn huiswerk <b>gemaakt</b>." (= it's done)</td></tr>
</table>

<h4>3. Special verbs: ALWAYS imperfectum in speech too</h4>
<p>Some verbs are almost always used in the imperfectum, even in conversation:</p>
<ul>
  <li><b>zijn</b> → was/waren (not: ben geweest — though technically correct)</li>
  <li><b>hebben</b> → had/hadden (not: heb gehad — sounds unnatural)</li>
  <li><b>modal verbs</b> → kon, moest, wilde, mocht, zou (not perfectum)</li>
</ul>

<h4>4. Tamil comparison</h4>
<p>Tamil has one past tense: "சாப்பிட்டேன்". Dutch has two! Think of it this way:<br>
<b>Perfectum</b> = what you say when WhatsApping a friend about yesterday.<br>
<b>Imperfectum</b> = what you write in a diary or tell in a long story.</p>

<h4>5. Mixing in one text</h4>
<p>In stories, you often MIX both tenses:</p>
<pre>
  Het was (imperf.) een mooie dag. De zon scheen (imperf.).
  Ik ben (perf.) naar de Graslei gegaan.
  Daar heb (perf.) ik koffie gedronken.
  Het was (imperf.) heel gezellig.
</pre>
""",

        "grammar_letop": """
<ul>
  <li>❌ Gisteren ik <b>was</b> thuis. → ✅ Gisteren <b>was ik</b> thuis. <br><em>Time word first → inversie! (was ik, not ik was).</em></li>
  <li>❌ Ik <b>heb geweest</b> ziek. → ✅ Ik <b>was</b> ziek. <br><em>For zijn/hebben/modals, USE IMPERFECTUM even in speech.</em></li>
  <li>❌ Vroeger <b>heb ik gefietst</b> elke dag. → ✅ Vroeger <b>fietste</b> ik elke dag. <br><em>Past habits → imperfectum.</em></li>
  <li>❌ (In a conversation) Gisteren <b>kochte</b> ik een boek. → ✅ Gisteren <b>heb</b> ik een boek <b>gekocht</b>. <br><em>Conversation about recent event → perfectum (more natural).</em></li>
  <li>❌ Hij <b>moest gehad</b> → This doesn't exist! ✅ Hij <b>moest</b> werken. <br><em>Modal verbs don't have a common perfectum form. Use imperfectum: moest, kon, wilde.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Side-by-side: same event, two tenses</h4>
<table>
  <tr><th>Perfectum (conversation)</th><th>Imperfectum (story)</th></tr>
  <tr><td>Ik heb gisteren gewerkt.</td><td>Ik werkte de hele dag.</td></tr>
  <tr><td>We zijn naar Brugge gegaan.</td><td>We gingen naar Brugge.</td></tr>
  <tr><td>Ik heb een boek gelezen.</td><td>Ik las een interessant boek.</td></tr>
  <tr><td>Het heeft geregend.</td><td>Het regende de hele middag.</td></tr>
  <tr><td>Ze heeft gekookt.</td><td>Ze kookte elke avond.</td></tr>
</table>

<h4>Practice: choose the right tense</h4>
<table>
  <tr><th>#</th><th>Context</th><th>Best tense</th></tr>
  <tr><td>1</td><td>Texting friend: "What did you do?"</td><td>Perfectum: Ik heb gesport.</td></tr>
  <tr><td>2</td><td>Writing diary: "The weather was nice."</td><td>Imperfectum: Het weer was mooi.</td></tr>
  <tr><td>3</td><td>Past habit: "I always cycled to school."</td><td>Imperfectum: Ik fietste altijd naar school.</td></tr>
  <tr><td>4</td><td>Result: "I've finished my homework."</td><td>Perfectum: Ik heb mijn huiswerk gemaakt.</td></tr>
  <tr><td>5</td><td>Story background: "It was dark."</td><td>Imperfectum: Het was donker.</td></tr>
</table>

<h4>Imperfectum of common irregular verbs (review)</h4>
<table>
  <tr><th>Infinitief</th><th>Imperfectum (ik)</th><th>Imperfectum (wij)</th></tr>
  <tr style="background:#fff3cd"><td><b>zijn</b></td><td><b>was</b></td><td><b>waren</b></td></tr>
  <tr style="background:#fff3cd"><td><b>hebben</b></td><td><b>had</b></td><td><b>hadden</b></td></tr>
  <tr><td>gaan</td><td>ging</td><td>gingen</td></tr>
  <tr><td>komen</td><td>kwam</td><td>kwamen</td></tr>
  <tr><td>zien</td><td>zag</td><td>zagen</td></tr>
  <tr><td>doen</td><td>deed</td><td>deden</td></tr>
  <tr><td>eten</td><td>at</td><td>aten</td></tr>
  <tr><td>drinken</td><td>dronk</td><td>dronken</td></tr>
  <tr><td>lezen</td><td>las</td><td>lazen</td></tr>
  <tr><td>schrijven</td><td>schreef</td><td>schreven</td></tr>
  <tr><td>nemen</td><td>nam</td><td>namen</td></tr>
  <tr style="background:#e8f4fd"><td><b>kunnen</b> (modaal)</td><td><b>kon</b></td><td><b>konden</b></td></tr>
  <tr style="background:#e8f4fd"><td><b>moeten</b> (modaal)</td><td><b>moest</b></td><td><b>moesten</b></td></tr>
  <tr style="background:#e8f4fd"><td><b>willen</b> (modaal)</td><td><b>wilde/wou</b></td><td><b>wilden/wouden</b></td></tr>
  <tr style="background:#e8f4fd"><td><b>mogen</b> (modaal)</td><td><b>mocht</b></td><td><b>mochten</b></td></tr>
</table>
<p>⚠️ <b>zijn, hebben en modale werkwoorden</b> gebruik je bijna <b>ALTIJD</b> in het imperfectum, ook in gesproken Nederlands:<br>
Ik <b>was</b> moe. Ik <b>had</b> honger. Ik <b>kon</b> niet komen. Ik <b>moest</b> werken.</p>

<h4>Plusquamperfectum met zijn (was/waren + voltooid deelwoord)</h4>
<p>Net als het perfectum met zijn (ben + vd), bestaat ook het plusquamperfectum met zijn:</p>
<table>
  <tr><th>Perfectum (nu relevant)</th><th>Plusquamperfectum (eerder in het verleden)</th></tr>
  <tr><td>Ik <b>ben</b> aangekomen.</td><td>Ik <b>was</b> al aangekomen (toen jij belde).</td></tr>
  <tr><td>Hij <b>is</b> vertrokken.</td><td>Hij <b>was</b> al vertrokken (toen ik kwam).</td></tr>
  <tr><td>Wij <b>zijn</b> verhuisd.</td><td>Wij <b>waren</b> al verhuisd (voor de zomer).</td></tr>
  <tr><td>Ze <b>is</b> gestorven.</td><td>Ze <b>was</b> al gestorven (toen de dokter kwam).</td></tr>
</table>
<p><b>Regel:</b> Perfectum met <b>zijn</b> → Plusquamperfectum ook met <b>zijn</b> (was/waren + vd).<br>
Perfectum met <b>hebben</b> → Plusquamperfectum ook met <b>hebben</b> (had/hadden + vd).</p>
""",

        "grammar_quick": """
<ul>
  <li><b>Perfectum</b> = conversation, recent events, results (heb/ben + participle)</li>
  <li><b>Imperfectum</b> = stories, background, habits, descriptions (simple past form)</li>
  <li><b>zijn/hebben/modals</b>: almost always imperfectum, even in speech (was, had, kon, moest)</li>
  <li>You can MIX tenses in one text (background = imperf., events = perf.)</li>
  <li>Past habits → imperfectum (Ik fietste altijd…)</li>
  <li>WhatsApp to a friend → perfectum (Ik heb gefietst.)</li>
</ul>
""",

        "exercises": [
            {"type": "choice", "q": "WhatsApp naar je vriend: 'Ik ben gisteren naar UGent gefietst.'",
             "options": ["Ik fietste gisteren naar UGent.", "Ik heb gisteren naar UGent gefietst."],
             "a": "Ik heb gisteren naar UGent gefietst.",
             "tip": "Gesprek/berichten → perfectum is natuurlijker."},
            {"type": "choice", "q": "In een verhaal: 'De zon scheen helder.'",
             "options": ["De zon heeft geschenen.", "De zon scheen."],
             "a": "De zon scheen.",
             "tip": "Verhaal/achtergrondbeschrijving → imperfectum."},
            {"type": "choice", "q": "Welke is natuurlijker in een gesprek? 'I was tired.'",
             "options": ["Ik was moe.", "Ik ben moe geweest."],
             "a": "Ik was moe.",
             "tip": "Zijn → bijna altijd imperfectum (was), zelfs in gesprekken."},
            {"type": "fill", "q": "Over je jeugd: Vroeger ___ (wonen, imperfectum) ik in India.", "a": "woonde",
             "tip": "Gewoonte in het verleden → imperfectum. wonen → woonde (regelmatig: woon + de)."},
            {"type": "fill", "q": "Gisteren op het werk: Gisteren ___ (hebben, imperfectum) ik geen tijd.", "a": "had",
             "tip": "hebben → had (imperfectum). Gewoon in gesproken Nederlands."},
            {"type": "fill", "q": "In de boekhandel: Ik ___ vorige week een nieuw boek ___. (kopen, perfectum)", "a": "heb ... gekocht",
             "tip": "kopen → gekocht (onregelmatig). hebben (activiteit): Ik heb … gekocht."},
            {"type": "choice", "q": "Gewoonte: 'We gingen als kind altijd naar het park.'",
             "options": ["We zijn altijd naar het park gegaan.", "We gingen altijd naar het park."],
             "a": "We gingen altijd naar het park.",
             "tip": "Gewoonte in het verleden (altijd) → imperfectum: gingen."},
            {"type": "tf", "q": "Modale werkwoorden (kunnen, moeten, willen) worden meestal in het imperfectum gebruikt.", "a": True,
             "correction": "Correct! kon, moest, wilde zijn standaard. Perfectum van modalen klinkt onnatuurlijk.",
             "tip": "kon, moest, wilde, mocht → imperfectum is normaal."},
            {"type": "tf", "q": "In een verhaal mag je ALLEEN imperfectum gebruiken, nooit mixen met perfectum.", "a": False,
             "correction": "Fout! Mixen is normaal. Achtergrond = imperfectum, gebeurtenissen/resultaten = perfectum.",
             "tip": "Beide verleden tijden werken samen in een tekst."},
            {"type": "tf", "q": "'Ik heb gekunnen' is een natuurlijke zin in het Nederlands.", "a": False,
             "correction": "Fout! Modalen gebruiken bijna altijd imperfectum: Ik kon, niet 'Ik heb gekunnen'.",
             "tip": "Modalen → imperfectum. Perfectum van modalen is zeldzaam."},
            {"type": "fill", "q": "Over je kindertijd: Toen ik klein ___ (zijn), speelde ik elke dag buiten.", "a": "was",
             "tip": "zijn → was (imperfectum). Verhaal over je kindertijd."},
            {"type": "translate", "q": "When I was a child, I lived in Chennai. (use imperfectum)",
             "a": "Toen ik een kind was, woonde ik in Chennai.",
             "tip": "toen + bijzin (was op einde) + hoofdzin inversie (woonde ik)."},
            {"type": "translate", "q": "Yesterday I bought a book and read it. (use perfectum for conversation)",
             "a": "Gisteren heb ik een boek gekocht en gelezen.",
             "tip": "Gesprek → perfectum. gekocht (kopen), gelezen (lezen). Twee deelwoorden delen 'heb'."},
            {"type": "reorder", "q": "was / toen / klein / was / ik / , / ik / in / India / woonde",
             "a": "Toen ik klein was, woonde ik in India.",
             "tip": "Toen + bijzin (ik klein was) + komma + hoofdzin inversie (woonde ik)."},
            {"type": "reorder", "q": "heb / gisteren / Nederlands / ik / gestudeerd",
             "a": "Gisteren heb ik Nederlands gestudeerd.",
             "tip": "Tijd eerst → inversie: Gisteren heb ik + object + deelwoord op einde."},
        ],

        "jouw_beurt": "Write a short text (8–10 sentences) about your life before and after moving to Ghent.\n\n"
                      "Part 1 — Before (use imperfectum):\n"
                      "• Vroeger woonde ik in …\n"
                      "• Ik werkte bij / studeerde aan …\n"
                      "• Het weer was … / Ik at altijd …\n\n"
                      "Part 2 — After moving (use perfectum):\n"
                      "• Ik ben naar Gent verhuisd.\n"
                      "• Ik heb … geleerd / bezocht / ontdekt.\n"
                      "• Ik heb al … gedaan.\n\n"
                      "This exercise practises MIXING both past tenses naturally!",
    },

    # ──────────────────────────────────────────────
    #  SESSION 13 — Als vs Toen (when) + Tijdsbijzinnen
    # ──────────────────────────────────────────────
    {
        "id": 13,
        "title": "Als vs Toen – When in the Past & Present",
        "chapter": "Hoofdstuk 7 – Verbindingswoorden",
        "book_page": "NT2 Drempel 2, H7 p. 116–126",

        "review": "In Session 7 you learned <b>als</b> for conditions (if/when). In Session 12 you practised "
                  "past tenses. Now the tricky part: Dutch has TWO words for 'when': <b>als</b> (present/future/repeated past) "
                  "and <b>toen</b> (one-time past event). Both are bijzin-connectors (verb→end), but they are NOT interchangeable!",

        "vocabulary": [
            ("toen", "when (past, one-time)", "Toen ik aankwam, regende het."),
            ("als", "when / if (present, future, repeated)",
             "Als ik thuiskom, kook ik."),
            ("terwijl", "while", "Terwijl ik kookte, las hij een boek."),
            ("zodra", "as soon as", "Zodra ik klaar ben, bel ik je."),
            ("telkens", "every time", "Telkens als ik fiets, voel ik me goed."),
            ("ooit", "ever", "Heb je ooit sushi gegeten?"),
            ("nooit", "never", "Ik heb nooit in Brussel gewoond."),
            ("eindelijk", "finally", "Eindelijk ben ik aangekomen."),
            ("inmiddels", "by now / meanwhile",
             "Inmiddels woon ik al 2 jaar in Gent."),
            ("destijds", "at that time", "Destijds woonde ik in India."),
            ("sindsdien", "since then", "Sindsdien spreek ik een beetje Nederlands."),
            ("steeds", "increasingly / still",
             "Mijn Nederlands wordt steeds beter."),
        ],

        "grammar_title": "Als vs Toen — Two Words for 'When'",

        "grammar_html": """
<h4>1. The golden rule: als vs toen</h4>
<table>
  <tr><th>Word</th><th>When to use</th><th>Tense in the clause</th></tr>
  <tr><td><b>als</b></td><td>present, future, OR repeated past</td><td>present / imperfectum (repeated)</td></tr>
  <tr><td><b>toen</b></td><td>one-time event in the past</td><td>imperfectum ONLY</td></tr>
</table>

<h4>2. Examples showing the difference</h4>
<table>
  <tr><th>Situation</th><th>Sentence</th><th>Why?</th></tr>
  <tr><td>Present habit</td><td><b>Als</b> ik thuiskom, kook ik.</td><td>Present → als</td></tr>
  <tr><td>Future</td><td><b>Als</b> ik klaar ben, ga ik naar huis.</td><td>Future → als</td></tr>
  <tr><td>Repeated past</td><td><b>Als</b> ik jong was, speelde ik buiten.</td><td>Every time (repeated) → als</td></tr>
  <tr><td>One-time past</td><td><b>Toen</b> ik in Gent aankwam, regende het.</td><td>One moment → toen</td></tr>
  <tr><td>One-time past</td><td><b>Toen</b> ik 18 was, ging ik studeren.</td><td>One moment → toen</td></tr>
</table>

<h4>3. Both are bijzin-connectors</h4>
<pre>
  Als/Toen + subject + … + VERB (end), VERB + subject + rest (inversie).
  
  Toen ik in India woonde, at ik elke dag rijst.
  Als ik honger heb, eet ik een boterham.
</pre>

<h4>4. Tamil comparison</h4>
<p>Tamil "போது (pōtu)" = when, works for both past and present. Dutch splits this into two words!<br>
Think: <b>toen</b> = "அப்போது (appōtu)" (at that specific past time).<br>
<b>Als</b> = "போது (pōtu)" in general (whenever / if).</p>

<h4>5. Terwijl (while) — simultaneous actions</h4>
<p><b>Terwijl</b> = while (two things at the same time). Also a bijzin-connector:</p>
<p><b>Terwijl</b> ik kookte, luisterde hij naar muziek.</p>
""",

        "grammar_letop": """
<ul>
  <li>❌ <b>Toen</b> ik thuiskom, kook ik. → ✅ <b>Als</b> ik thuiskom, kook ik. <br><em>Present situation → als, NOT toen. Toen is ONLY for past.</em></li>
  <li>❌ <b>Als</b> ik gisteren aankwam, regende het. → ✅ <b>Toen</b> ik gisteren aankwam, regende het. <br><em>One-time past event → toen.</em></li>
  <li>❌ Toen ik jong <b>ben</b>, speelde ik buiten. → ✅ Toen ik jong <b>was</b>, … <br><em>Toen always uses IMPERFECTUM, never present tense.</em></li>
  <li>❌ <b>Als</b> ik jong was, <b>ging</b> ik altijd naar het strand. → Actually ✅! <br><em>Repeated past action (altijd) → als is correct here!</em></li>
  <li>❌ Toen ik aankwam, ik was moe. → ✅ Toen ik aankwam, <b>was ik</b> moe. <br><em>After a toen/als-clause → inversie in the main clause.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Quick decision tree: als or toen?</h4>
<pre>
  Is it about the PAST?
  ├── NO → use ALS (present/future)
  └── YES → Was it ONE TIME or REPEATED?
       ├── ONE TIME → use TOEN
       └── REPEATED (altijd, vaak, elke dag) → use ALS
</pre>

<h4>Practice sentences</h4>
<table>
  <tr><th>#</th><th>Sentence</th><th>Als or Toen?</th></tr>
  <tr><td>1</td><td>___ ik klaar ben, ga ik naar huis.</td><td>Als (future)</td></tr>
  <tr><td>2</td><td>___ ik gisteren aankwam, was het druk.</td><td>Toen (one-time past)</td></tr>
  <tr><td>3</td><td>___ we als kind naar school gingen, fietsten we altijd.</td><td>Als (repeated past)</td></tr>
  <tr><td>4</td><td>___ hij 18 werd, ging hij studeren.</td><td>Toen (one-time past)</td></tr>
  <tr><td>5</td><td>___ het regent, neem ik de bus.</td><td>Als (present habit)</td></tr>
</table>

<h4>Terwijl, zodra, telkens als — more time connectors</h4>
<ul>
  <li><b>Terwijl</b> ik studeerde, luisterde ik naar muziek. (while — simultaneous)</li>
  <li><b>Zodra</b> ik klaar ben, bel ik je. (as soon as)</li>
  <li><b>Telkens als</b> ik naar de Graslei ga, drink ik koffie. (every time)</li>
  <li><b>Steeds als</b> het regent, neem ik de tram. (every time — alternative)</li>
</ul>
""",

        "grammar_quick": """
<ul>
  <li><b>Als</b> = when/if → present, future, or REPEATED past</li>
  <li><b>Toen</b> = when → ONE-TIME past event (always with imperfectum)</li>
  <li>Both are bijzin → verb goes to END</li>
  <li>After als/toen-clause → main clause has inversie</li>
  <li><b>Terwijl</b> = while (simultaneous), <b>zodra</b> = as soon as</li>
  <li>Repeated past clue words: altijd, vaak, elke dag, telkens → use als</li>
</ul>
""",

        "exercises": [
            {"type": "choice", "q": "Je vertelt over je aankomst: ___ ik gisteren in Gent aankwam, regende het.",
             "options": ["Als", "Toen", "Terwijl"], "a": "Toen",
             "tip": "Eenmalige gebeurtenis in het verleden (gisteren aankwam) → toen."},
            {"type": "choice", "q": "Dagelijkse gewoonte: ___ ik honger heb, eet ik een boterham.",
             "options": ["Als", "Toen", "Zodra"], "a": "Als",
             "tip": "Herhaling in het heden (elke keer als ik honger heb) → als."},
            {"type": "choice", "q": "Over je kindertijd: ___ we als kind naar school gingen, fietsten we altijd.",
             "options": ["Als", "Toen"], "a": "Als",
             "tip": "Herhaling in het verleden (altijd) → als, ook al is het over het verleden!"},
            {"type": "fill", "q": "Een belangrijk moment: ___ ik 18 werd, ging ik studeren.", "a": "Toen",
             "tip": "Eenmalige gebeurtenis (18 worden gebeurt één keer) → toen."},
            {"type": "fill", "q": "Plannen: ___ ik klaar ben, ga ik naar huis.", "a": "Als",
             "tip": "Toekomst → als."},
            {"type": "tf", "q": "'Toen' kan met de tegenwoordige tijd gebruikt worden.", "a": False,
             "correction": "Fout! Toen vereist ALTIJD het imperfectum. Nooit met de tegenwoordige tijd.",
             "tip": "Toen = alleen verleden tijd (imperfectum)."},
            {"type": "tf", "q": "'Als' kan voor herhaalde acties in het verleden gebruikt worden.", "a": True,
             "correction": "Correct! Als + herhaling in het verleden (altijd, vaak) = 'whenever' in het verleden.",
             "tip": "Herhaling = als, ook in het verleden."},
            {"type": "tf", "q": "'Toen ik naar Gent kom, regende het' is correct.", "a": False,
             "correction": "Fout! Na 'toen' moet imperfectum: Toen ik naar Gent KWAM, regende het.",
             "tip": "Toen vereist imperfectum: kwam, niet kom (tegenwoordige tijd)."},
            {"type": "fill", "q": "Twee dingen tegelijk: ___ ik kookte, luisterde hij naar muziek.", "a": "Terwijl",
             "tip": "Twee dingen tegelijk → terwijl (while)."},
            {"type": "choice", "q": "In een verhaal: Toen ik aankwam, ___ ik moe.",
             "options": ["was", "ben", "ben geweest"], "a": "was",
             "tip": "Toen-context → imperfectum. zijn → was."},
            {"type": "fill", "q": "Aan een collega: ___ ik klaar ben, bel ik je. (as soon as)", "a": "Zodra",
             "tip": "As soon as → zodra. Ook een bijzin-connector."},
            {"type": "translate", "q": "When I arrived in Ghent, it was raining.",
             "a": "Toen ik in Gent aankwam, regende het.",
             "tip": "Eenmalig verleden → toen. aankwam (werkwoord einde), regende het (inversie)."},
            {"type": "translate", "q": "When I am tired, I drink coffee. (present habit)",
             "a": "Als ik moe ben, drink ik koffie.",
             "tip": "Heden/gewoonte → als. ben (werkwoord einde), drink ik (inversie)."},
            {"type": "reorder", "q": "toen / aankwam / ik / in / Gent / , / het / regende",
             "a": "Toen ik in Gent aankwam, regende het.",
             "tip": "Toen + bijzin (werkwoord einde: aankwam) + komma + hoofdzin (inversie: regende het)."},
            {"type": "reorder", "q": "als / heb / ik / honger / , / ik / eet / boterham / een",
             "a": "Als ik honger heb, eet ik een boterham.",
             "tip": "Als + bijzin (werkwoord einde: heb) + komma + hoofdzin (inversie: eet ik)."},
        ],

        "jouw_beurt": "Write 8 sentences about your past and present using als and toen correctly.\n\n"
                      "Use TOEN for:\n"
                      "• Toen ik in India woonde, … (one-time period)\n"
                      "• Toen ik naar Gent verhuisde, …\n"
                      "• Toen ik voor het eerst Nederlands hoorde, …\n\n"
                      "Use ALS for:\n"
                      "• Als ik naar UGent fiets, …\n"
                      "• Als kind ging ik altijd … (repeated past)\n"
                      "• Als ik klaar ben met mijn onderzoek, …\n\n"
                      "Also try: terwijl, zodra.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 14 — Connectors Overview: en, maar, of, dus, toch, hoewel, …
    # ──────────────────────────────────────────────
    {
        "id": 14,
        "title": "Verbindingswoorden – Connectors Overzicht",
        "chapter": "Hoofdstuk 7 – Verbindingswoorden",
        "book_page": "NT2 Drempel 2, H7 p. 126–138",

        "review": "You've learned many connectors one at a time: omdat, want, daarom, als, toen, terwijl. "
                  "Now we bring them ALL together in one overview. You'll learn the three groups "
                  "(coordinating, subordinating, linking adverbs) and add new ones: <b>hoewel, toch, "
                  "doordat, zodat, tenzij</b>. This is THE most important grammar session for writing!",

        "vocabulary": [
            ("hoewel / alhoewel", "although",
             "Hoewel het regende, ging ik fietsen."),
            ("toch", "yet / still / anyway", "Het regende, toch ging ik fietsen."),
            ("doordat", "because (cause-effect)",
             "Doordat het regende, was de straat nat."),
            ("zodat", "so that (purpose)", "Ik studeer hard zodat ik slaag."),
            ("tenzij", "unless", "Ik ga fietsen, tenzij het regent."),
            ("bovendien", "moreover / besides",
             "Het is lekker, bovendien is het gezond."),
            ("echter", "however (formal)",
             "Het weer was slecht. Echter, we gingen toch."),
            ("namelijk", "namely / because (explains)",
             "Ik kom later, ik moet namelijk werken."),
            ("dus", "so / therefore", "Het regent, dus ik neem de bus."),
            ("toch", "yet / anyway", "Ik was moe, toch ben ik gaan sporten."),
            ("zowel … als", "both … and", "Zowel Gent als Brugge is mooi."),
            ("niet alleen … maar ook", "not only … but also",
             "Niet alleen mooi, maar ook gezellig."),
        ],

        "grammar_title": "Three Groups of Connectors — Complete Overview",

        "grammar_html": """
<h4>1. Group A: Coordinating conjunctions (nevenschikkend)</h4>
<p>Connect two main clauses. <b>Normal word order</b> after them.</p>
<table>
  <tr><th>Connector</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><b>en</b></td><td>and</td><td>Ik werk <b>en</b> ik studeer.</td></tr>
  <tr><td><b>maar</b></td><td>but</td><td>Ik wil gaan, <b>maar</b> ik heb geen tijd.</td></tr>
  <tr><td><b>of</b></td><td>or</td><td>Ga je fietsen <b>of</b> neem je de tram?</td></tr>
  <tr><td><b>want</b></td><td>because</td><td>Ik blijf thuis, <b>want</b> ik ben ziek.</td></tr>
  <tr><td><b>dus</b></td><td>so</td><td>Het regent, <b>dus</b> ik neem een paraplu.</td></tr>
</table>

<h4>2. Group B: Subordinating conjunctions (onderschikkend) — bijzin!</h4>
<p>Create a subordinate clause. <b>Verb goes to the END.</b></p>
<table>
  <tr><th>Connector</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><b>omdat</b></td><td>because</td><td>… omdat ik ziek <u>ben</u>.</td></tr>
  <tr><td><b>dat</b></td><td>that</td><td>Ik denk dat hij <u>komt</u>.</td></tr>
  <tr><td><b>als</b></td><td>if / when</td><td>… als het mooi weer <u>is</u>.</td></tr>
  <tr><td><b>toen</b></td><td>when (past)</td><td>… toen ik jong <u>was</u>.</td></tr>
  <tr><td><b>terwijl</b></td><td>while</td><td>… terwijl ik <u>kookte</u>.</td></tr>
  <tr><td><b>hoewel</b></td><td>although</td><td>… hoewel het <u>regende</u>.</td></tr>
  <tr><td><b>doordat</b></td><td>because (cause)</td><td>… doordat de trein <u>vertraagde</u>.</td></tr>
  <tr><td><b>zodat</b></td><td>so that</td><td>… zodat ik het <u>begrijp</u>.</td></tr>
  <tr><td><b>tenzij</b></td><td>unless</td><td>… tenzij het <u>regent</u>.</td></tr>
  <tr><td><b>voordat</b></td><td>before</td><td>… voordat ik <u>vertrek</u>.</td></tr>
  <tr><td><b>nadat</b></td><td>after</td><td>… nadat ik <u>gegeten</u> heb.</td></tr>
</table>

<h4>3. Group C: Linking adverbs (bijwoorden) — inversie!</h4>
<p>Start a new sentence or clause. <b>Verb–subject (inversie)</b> after them.</p>
<table>
  <tr><th>Connector</th><th>Meaning</th><th>Example</th></tr>
  <tr><td><b>daarom</b></td><td>therefore</td><td><b>Daarom</b> <u>ga</u> ik niet.</td></tr>
  <tr><td><b>toch</b></td><td>yet / anyway</td><td><b>Toch</b> <u>ging</u> ik fietsen.</td></tr>
  <tr><td><b>bovendien</b></td><td>moreover</td><td><b>Bovendien</b> <u>is</u> het gezond.</td></tr>
  <tr><td><b>echter</b></td><td>however</td><td><b>Echter</b>, <u>was</u> het koud.</td></tr>
  <tr><td><b>daarna</b></td><td>after that</td><td><b>Daarna</b> <u>ging</u> ik naar huis.</td></tr>
</table>

<h4>4. Tamil comparison</h4>
<p>Tamil connectors don't change word order. Dutch connectors DO — and that's the hard part!<br>
<b>Group A</b> = safe (normal order). <b>Group B</b> = verb to end. <b>Group C</b> = inversie.<br>
Memorise the group, and you'll know the word order!</p>
""",

        "grammar_letop": """
<ul>
  <li>❌ Hoewel het regent, ik ga fietsen. → ✅ Hoewel het regent, <b>ga ik</b> fietsen. <br><em>Hoewel = bijzin-connector. After the bijzin → inversie in main clause.</em></li>
  <li>❌ Doordat ik was ziek, bleef ik thuis. → ✅ Doordat ik ziek <b>was</b>, bleef ik thuis. <br><em>Doordat = bijzin → verb to END of the doordat-clause.</em></li>
  <li>❌ Echter ik ging toch. → ✅ <b>Echter</b> <b>ging</b> ik toch. OR: Ik ging echter toch. <br><em>Echter = linking adverb → inversie. Or place it mid-sentence.</em></li>
  <li>❌ Toch ik ging fietsen. → ✅ <b>Toch ging ik</b> fietsen. <br><em>Toch = linking adverb → inversie (verb before subject).</em></li>
  <li>❌ Ik studeer hard zodat ik <b>slaag</b> het examen. → ✅ … zodat ik het examen <b>slaag</b>. <br><em>Object before verb in bijzin. Or better: zodat ik voor het examen slaag.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Complete connector cheat sheet</h4>
<table>
  <tr><th>Group</th><th>Connectors</th><th>Word order</th></tr>
  <tr><td>A — Coordinating</td><td>en, maar, of, want, dus</td><td>Normal (S + V)</td></tr>
  <tr><td>B — Subordinating</td><td>omdat, dat, als, toen, terwijl, hoewel, doordat, zodat, tenzij, voordat, nadat, of (whether)</td><td>Verb → END</td></tr>
  <tr><td>C — Linking adverbs</td><td>daarom, toch, bovendien, echter, daarna, daardoor, namelijk, dus*</td><td>Inversie (V + S)</td></tr>
</table>
<p><em>*Note: 'dus' can work as both A (normal order) and C (inversie). Both are correct.</em></p>

<h4>Contrast pairs — same meaning, different structure</h4>
<table>
  <tr><th>Meaning</th><th>Group B (bijzin)</th><th>Group C (inversie)</th><th>Group A (normal)</th></tr>
  <tr><td>because</td><td><b>omdat</b> ik ziek ben</td><td>ik ben ziek. <b>Daarom</b> ga ik niet.</td><td>…, <b>want</b> ik ben ziek.</td></tr>
  <tr><td>although / yet</td><td><b>hoewel</b> het regende</td><td>het regende. <b>Toch</b> ging ik.</td><td>het regende, <b>maar</b> ik ging.</td></tr>
  <tr><td>because (cause)</td><td><b>doordat</b> het regende</td><td>het regende. <b>Daardoor</b> was…</td><td>—</td></tr>
</table>

<h4>Practice: identify the group</h4>
<ul>
  <li>"Ik ga niet, <b>want</b> ik ben moe." → Group A (normal order)</li>
  <li>"Ik ga niet <b>omdat</b> ik moe ben." → Group B (verb end)</li>
  <li>"Ik ben moe. <b>Daarom</b> ga ik niet." → Group C (inversie)</li>
  <li>"<b>Hoewel</b> ik moe was, ging ik toch." → Group B + inversie in main</li>
  <li>"Ik was moe. <b>Toch</b> ging ik." → Group C (inversie)</li>
</ul>
""",

        "grammar_quick": """
<ul>
  <li><b>Group A</b> (en, maar, of, want, dus): normal word order</li>
  <li><b>Group B</b> (omdat, dat, als, toen, hoewel, terwijl, doordat, zodat, tenzij, voordat, nadat): verb → END</li>
  <li><b>Group C</b> (daarom, toch, bovendien, echter, daarna, daardoor): inversie (V + S)</li>
  <li>Bijzin first → main clause has inversie</li>
  <li>Contrast pairs: omdat/daarom/want, hoewel/toch/maar, doordat/daardoor</li>
  <li>Memorise the GROUP → you know the word order!</li>
</ul>
""",

        "exercises": [
            {"type": "choice", "q": "Ziekmelding: Ik ga niet, ___ ik ben ziek. (normale volgorde na connector)",
             "options": ["omdat", "want", "daarom"], "a": "want",
             "tip": "Normale volgorde (ik BEN ziek) → Groep A → want."},
            {"type": "choice", "q": "Uitleg aan docent: Ik ga niet ___ ik ziek ben. (werkwoord op einde)",
             "options": ["omdat", "want", "daarom"], "a": "omdat",
             "tip": "Werkwoord op einde (ziek BEN) → Groep B → omdat."},
            {"type": "choice", "q": "In een e-mail: Ik ben ziek. ___ ga ik niet. (inversie)",
             "options": ["Omdat", "Want", "Daarom"], "a": "Daarom",
             "tip": "Nieuwe zin + inversie (ga ik) → Groep C → daarom."},
            {"type": "fill", "q": "Op de fiets in Gent: ___ het regende, ging ik toch fietsen. (although)", "a": "Hoewel",
             "tip": "Although → hoewel. Bijzin (werkwoord einde: regende) + inversie in hoofdzin (ging ik)."},
            {"type": "fill", "q": "Stoer doen: Het regende. ___ ging ik toch fietsen. (yet/anyway)", "a": "Toch",
             "tip": "Yet/anyway → toch (Groep C, inversie: ging ik)."},
            {"type": "fill", "q": "Motivatie: Ik studeer hard ___ ik wil slagen. (so that)", "a": "zodat",
             "tip": "So that (doel) → zodat. Bijzin: werkwoord (slagen/wil) op einde."},
            {"type": "tf", "q": "'Want' en 'omdat' betekenen hetzelfde ('because') maar hebben een verschillende woordvolgorde.", "a": True,
             "correction": "Correct! want = normale volgorde (Groep A), omdat = werkwoord einde (Groep B).",
             "tip": "Beide betekenen 'because', maar de woordvolgorde verschilt."},
            {"type": "tf", "q": "'Toch' stuurt het werkwoord naar het einde van de zin.", "a": False,
             "correction": "Fout! Toch = bijwoordelijk verbindingswoord (Groep C) → INVERSIE (werkwoord-subject), niet werkwoord op einde.",
             "tip": "Toch = Groep C → inversie."},
            {"type": "tf", "q": "'Hoewel het koud was, ik bleef binnen.' is correct.", "a": False,
             "correction": "Fout! Na een hoewel-bijzin → inversie in de hoofdzin: Hoewel het koud was, BLEEF IK binnen.",
             "tip": "Bijzin eerst → inversie in de hoofdzin."},
            {"type": "choice", "q": "Voorwaarde: Ik ga fietsen, ___ het regent. (unless)",
             "options": ["tenzij", "zodat", "hoewel"], "a": "tenzij",
             "tip": "Unless → tenzij. Bijzin (werkwoord einde): tenzij het regent."},
            {"type": "translate", "q": "Although it was cold, I cycled to UGent.",
             "a": "Hoewel het koud was, fietste ik naar UGent.",
             "tip": "Hoewel + bijzin (werkwoord einde: was) + hoofdzin (inversie: fietste ik)."},
            {"type": "translate", "q": "I study hard so that I pass the exam.",
             "a": "Ik studeer hard zodat ik voor het examen slaag.",
             "tip": "zodat + bijzin (werkwoord einde: slaag). voor het examen slagen = pass the exam."},
            {"type": "translate", "q": "It was raining. Nevertheless, I went cycling.",
             "a": "Het regende. Toch ging ik fietsen.",
             "tip": "Toch (Groep C) → inversie: ging ik."},
            {"type": "reorder", "q": "hoewel / regende / het / , / ging / ik / toch / fietsen",
             "a": "Hoewel het regende, ging ik toch fietsen.",
             "tip": "Hoewel + bijzin (werkwoord einde) + komma + hoofdzin (inversie) + toch."},
            {"type": "reorder", "q": "ik / studeer / zodat / slaag / ik / hard / het / examen / voor",
             "a": "Ik studeer hard zodat ik voor het examen slaag.",
             "tip": "Hoofdzin + zodat + bijzin (werkwoord op einde: slaag)."},
        ],

        "jouw_beurt": "Write a paragraph (8–10 sentences) about your daily routine using as many different connectors as possible.\n\n"
                      "Try to use at least one from each group:\n"
                      "• Group A: en, maar, want\n"
                      "• Group B: omdat, als, terwijl, hoewel, zodat\n"
                      "• Group C: daarom, toch, bovendien, daarna\n\n"
                      "Example start: 'Als ik wakker word, ontbijt ik eerst. Daarna fiets ik naar UGent, "
                      "hoewel het soms regent. Ik neem toch de fiets, want het is gezonder.'",
    },

    # ──────────────────────────────────────────────
    #  SESSION 15 — Het woordje ER (deel 1): er + zijn, er + preposition
    # ──────────────────────────────────────────────
    {
        "id": 15,
        "title": "Het woordje ER (1) – Er is/zijn & Er + prepositie",
        "chapter": "Hoofdstuk 8 – Het woordje ER",
        "book_page": "NT2 Drempel 2, H8 p. 139–150",

        "review": "The word <b>er</b> is one of the trickiest parts of Dutch — it has FIVE different uses! "
                  "Don't worry, we split it over two sessions. This session covers the two most common uses: "
                  "<b>er + zijn</b> (there is/are) and <b>er + preposition</b> (replacing 'it' with things). "
                  "Tamil doesn't have an equivalent, so pay extra attention!",

        "vocabulary": [
            ("er", "there (unstressed)", "Er zijn veel fietsen in Gent."),
            ("er is", "there is", "Er is een probleem."),
            ("er zijn", "there are", "Er zijn veel studenten."),
            ("eraan", "to/on it", "Ik denk eraan. (I think about it.)"),
            ("erover", "about it", "We praten erover. (We talk about it.)"),
            ("ermee", "with it", "Ik ben het ermee eens. (I agree with it.)"),
            ("erin", "in it", "Er zit melk erin. (There's milk in it.)"),
            ("erop", "on it", "Ik reken erop. (I count on it.)"),
            ("ernaast", "next to it", "Het café is ernaast."),
            ("ervoor", "for it / in front of it", "Ik betaal ervoor."),
            ("eruit", "out of it", "Het ziet er goed uit. (It looks good.)"),
            ("ervan", "of it / from it", "Ik hou ervan. (I like it.)"),
        ],

        "grammar_title": "Het woordje ER — Five Uses (Part 1: er+zijn & er+preposition)",

        "grammar_html": """
<h4>1. Use 1: Er + zijn = there is / there are</h4>
<p>This is the most common use. <b>Er</b> = "there" (unstressed, existential).</p>
<table>
  <tr><th>Dutch</th><th>English</th></tr>
  <tr><td><b>Er is</b> een park in Gent.</td><td>There is a park in Ghent.</td></tr>
  <tr><td><b>Er zijn</b> veel studenten.</td><td>There are many students.</td></tr>
  <tr><td><b>Er</b> was niemand thuis.</td><td>There was nobody home.</td></tr>
  <tr><td>Hoeveel studenten <b>zijn er</b>?</td><td>How many students are there?</td></tr>
</table>
<p><b>Position rule:</b> Er normally comes right after the verb in questions/inversie, or before the verb in normal sentences.</p>

<h4>2. Use 2: Er + preposition (pronominal adverb)</h4>
<p>When you want to say "about it", "with it", "on it" for <b>things</b> (not people), Dutch uses <b>er + preposition</b>:</p>
<table>
  <tr><th>English</th><th>Dutch (thing)</th><th>Dutch (person)</th></tr>
  <tr><td>about it</td><td><b>erover</b></td><td>over hem/haar</td></tr>
  <tr><td>with it</td><td><b>ermee</b></td><td>met hem/haar</td></tr>
  <tr><td>on it</td><td><b>erop</b></td><td>op hem/haar</td></tr>
  <tr><td>to it</td><td><b>eraan</b></td><td>aan hem/haar</td></tr>
  <tr><td>for it</td><td><b>ervoor</b></td><td>voor hem/haar</td></tr>
  <tr><td>from it</td><td><b>ervan</b></td><td>van hem/haar</td></tr>
  <tr><td>in it</td><td><b>erin</b></td><td>in hem/haar</td></tr>
</table>

<h4>3. Can split: er … preposition</h4>
<p>Er + preposition can SPLIT in a sentence:</p>
<pre>
  Together: Ik denk <b>erover</b>.
  Split:    Ik denk <b>er</b> vaak <b>over</b>.
  Split:    <b>Er</b> denk ik vaak <b>over</b>.
</pre>

<h4>4. Tamil comparison</h4>
<p>Tamil has no word like "er". In Tamil, you say "அங்கே ஒரு பூங்கா இருக்கிறது" (there is a park there). 
Dutch <b>er</b> is lighter — it doesn't mean a physical "there" (that's <b>daar</b>).
For "about it" etc., Tamil uses "அதைப் பற்றி (ataip paṟṟi)". Dutch merges "it" + preposition into one word: <b>erover</b>.</p>
""",

        "grammar_letop": """
<ul>
  <li>❌ Het is een park in Gent. → ✅ <b>Er</b> is een park in Gent. <br><em>"There is" = er is, not het is (which means "it is").</em></li>
  <li>❌ Ik denk over het. → ✅ Ik denk <b>erover</b>. <br><em>For things: use er+preposition, not preposition + het.</em></li>
  <li>❌ Ik praat <b>erover</b> hem. → ✅ Ik praat <b>over hem</b>. <br><em>For PEOPLE: use preposition + hem/haar, NOT er+prep.</em></li>
  <li>❌ Hoeveel studenten er zijn? → ✅ Hoeveel studenten <b>zijn er</b>? <br><em>In questions: er comes AFTER the verb.</em></li>
  <li>❌ Er veel studenten zijn. → ✅ Er <b>zijn</b> veel studenten. <br><em>Normal sentence: er + verb + rest. Verb stays in position 2.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Er + zijn: more examples</h4>
<ul>
  <li><b>Er is</b> een goed restaurant in de Patershol.</li>
  <li><b>Er zijn</b> veel fietsers in Gent.</li>
  <li><b>Er was</b> een ongeluk op de Korenmarkt.</li>
  <li><b>Er waren</b> geen plaatsen meer in de trein.</li>
  <li>Hoeveel cafés <b>zijn er</b> op de Graslei?</li>
  <li><b>Er</b> moet een oplossing <b>zijn</b>. (There must be a solution.)</li>
</ul>

<h4>Er + preposition: practice with common verbs</h4>
<table>
  <tr><th>Verb + preposition</th><th>With thing (er)</th><th>Example</th></tr>
  <tr><td>denken aan</td><td>er<b>aan</b> denken</td><td>Ik denk <b>eraan</b>. (I think about it.)</td></tr>
  <tr><td>praten over</td><td>er<b>over</b> praten</td><td>We praten <b>erover</b>. (We talk about it.)</td></tr>
  <tr><td>wachten op</td><td>er<b>op</b> wachten</td><td>Ik wacht <b>erop</b>. (I wait for it.)</td></tr>
  <tr><td>houden van</td><td>er<b>van</b> houden</td><td>Ik hou <b>ervan</b>. (I like it.)</td></tr>
  <tr><td>beginnen met</td><td>er<b>mee</b> beginnen</td><td>Ik begin <b>ermee</b>. (I start with it.)</td></tr>
  <tr><td>rekenen op</td><td>er<b>op</b> rekenen</td><td>Je kunt <b>erop</b> rekenen. (You can count on it.)</td></tr>
</table>

<h4>Question forms: waar + preposition</h4>
<p>To ask "about what?", "with what?" — use <b>waar + preposition</b>:</p>
<ul>
  <li><b>Waarover</b> praat je? (What are you talking about?)</li>
  <li><b>Waaraan</b> denk je? (What are you thinking about?)</li>
  <li><b>Waarmee</b> begin je? (What do you start with?)</li>
  <li><b>Waarop</b> wacht je? (What are you waiting for?)</li>
</ul>
""",

        "grammar_quick": """
<ul>
  <li><b>Er is / Er zijn</b> = there is / there are</li>
  <li><b>Er + preposition</b> = replaces "preposition + it/that" for THINGS</li>
  <li>For PEOPLE: use preposition + hem/haar (not er+prep)</li>
  <li>Er+prep can split: Ik denk <b>er</b> vaak <b>over</b>.</li>
  <li>Questions: use <b>waar + preposition</b> (waarover, waarmee, waarop)</li>
  <li>In questions/inversie: er comes AFTER the verb (zijn er, is er)</li>
</ul>
""",

        "exercises": [
            {"type": "fill", "q": "Aan een toerist: ___ zijn veel fietsen in Gent.", "a": "Er",
             "tip": "There are = er zijn."},
            {"type": "fill", "q": "Over de Patershol: ___ is een goed restaurant in de Patershol.", "a": "Er",
             "tip": "There is = er is."},
            {"type": "choice", "q": "Aan UGent: Hoeveel studenten ___ op UGent?",
             "options": ["er zijn", "zijn er", "er is"], "a": "zijn er",
             "tip": "Vraag → er komt NA het werkwoord: zijn er."},
            {"type": "fill", "q": "Over je onderzoek: Ik denk ___ (about it, ding).", "a": "eraan",
             "tip": "denken aan + ding → eraan. Ik denk eraan."},
            {"type": "fill", "q": "Op het werk: We praten ___ (about it, ding).", "a": "erover",
             "tip": "praten over + ding → erover."},
            {"type": "choice", "q": "Over een persoon: I talk about HIM. → Ik praat ___.",
             "options": ["erover", "over hem", "over het"], "a": "over hem",
             "tip": "Voor PERSONEN: voorzetsel + hem/haar. NIET er+voorzetsel."},
            {"type": "tf", "q": "'Er is' en 'het is' betekenen hetzelfde.", "a": False,
             "correction": "Fout! Er is = there is (bestaan). Het is = it is (beschrijving). Heel verschillend!",
             "tip": "'Er is een probleem' ≠ 'Het is een probleem'."},
            {"type": "tf", "q": "'Erover' kan gesplitst worden in 'er … over' in een zin.", "a": True,
             "correction": "Correct! Ik denk er vaak over. De splitsing is heel gewoon in het Nederlands.",
             "tip": "Splitsing is normaal: er … over, er … aan, enz."},
            {"type": "tf", "q": "'Ik praat erover' kan over een persoon gaan.", "a": False,
             "correction": "Fout! Er+voorzetsel = alleen voor dingen. Voor personen: voorzetsel + hem/haar/hen.",
             "tip": "Er+voorzetsel = dingen. Voorzetsel + pronomen = personen."},
            {"type": "fill", "q": "Over muziek: Ik hou ___ (of it — houden van + ding).", "a": "ervan",
             "tip": "houden van + ding → ervan. Ik hou ervan."},
            {"type": "fill", "q": "In de les: ___ praat je? (Where are you talking about?)", "a": "Waarover",
             "tip": "Vraag over ding: waar + voorzetsel → waarover."},
            {"type": "translate", "q": "There are many students at UGent.",
             "a": "Er zijn veel studenten op UGent.",
             "tip": "There are = er zijn. op UGent (at UGent)."},
            {"type": "translate", "q": "I am thinking about it. (denken aan)",
             "a": "Ik denk eraan.",
             "tip": "denken aan + ding → eraan."},
            {"type": "reorder", "q": "er / veel / in / Gent / zijn / cafés",
             "a": "Er zijn veel cafés in Gent.",
             "tip": "Er zijn + hoeveelheid + zelfstandig naamwoord + plaats."},
            {"type": "reorder", "q": "denk / ik / er / over / vaak",
             "a": "Ik denk er vaak over.",
             "tip": "Splitsing: er … over met 'vaak' ertussen."},
        ],

        "jouw_beurt": "Write 6 sentences using er.\n\n"
                      "Use er + zijn:\n"
                      "• Er is/zijn … in Gent / op UGent / in mijn wijk\n\n"
                      "Use er + preposition:\n"
                      "• Ik denk eraan / Ik praat erover / Ik hou ervan\n"
                      "• Split one: Ik denk er vaak over.\n\n"
                      "Try: eraan, erover, ermee, erop, ervan.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 16 — Het woordje ER (deel 2): er + quantity, er = daar, passive er
    # ──────────────────────────────────────────────
    {
        "id": 16,
        "title": "Het woordje ER (2) – Hoeveelheid, Plaats & Passief",
        "chapter": "Hoofdstuk 8 – Het woordje ER",
        "book_page": "NT2 Drempel 2, H8 p. 150–160",

        "review": "In Session 15 you learned <b>er + zijn</b> (there is/are) and <b>er + preposition</b> (erover, eraan…). "
                  "Now we cover the remaining three uses of er: <b>er + quantity</b> (I have three OF THEM), "
                  "<b>er = place</b> (there, referring to a mentioned place), and <b>er in passive sentences</b>. "
                  "After this session, you'll know ALL five uses!",

        "vocabulary": [
            ("hoeveel", "how many", "Hoeveel boeken heb je? — Ik heb er vijf."),
            ("een paar", "a few", "Ik heb er een paar gekocht."),
            ("geen", "none / no", "Ik heb er geen."),
            ("veel", "many", "Er zijn er veel."),
            ("weinig", "few", "Ik heb er weinig."),
            ("genoeg", "enough", "Ik heb er genoeg."),
            ("daar", "there (stressed)", "Ik woon daar. → Ik woon er."),
            ("het gebouw", "building", "Het gebouw is mooi. Ik werk er."),
            ("de bibliotheek", "library", "Ken je de Boekentoren? Ik studeer er."),
            ("worden", "to become / passive auxiliary",
             "Er wordt veel gefietst in Gent."),
            ("het aantal", "the number / amount",
             "Het aantal studenten is groot."),
            ("sommige", "some", "Sommige zijn duurder. Ik heb er drie gekocht."),
        ],

        "grammar_title": "Het woordje ER — Five Uses (Part 2: Quantity, Place & Passive)",

        "grammar_html": """
<h4>Overview: All 5 uses of ER</h4>
<table>
  <tr><th>#</th><th>Use</th><th>Example</th><th>Session</th></tr>
  <tr><td>1</td><td>er + zijn (there is/are)</td><td>Er zijn veel fietsen.</td><td>15 ✓</td></tr>
  <tr><td>2</td><td>er + preposition (things)</td><td>Ik denk eraan.</td><td>15 ✓</td></tr>
  <tr><td>3</td><td><b>er + quantity</b></td><td>Ik heb <b>er</b> drie.</td><td>16 ←</td></tr>
  <tr><td>4</td><td><b>er = place (unstressed daar)</b></td><td>Ik werk <b>er</b>.</td><td>16 ←</td></tr>
  <tr><td>5</td><td><b>er in passive</b></td><td><b>Er</b> wordt veel gefietst.</td><td>16 ←</td></tr>
</table>

<h4>3. Use 3: Er + quantity (of them)</h4>
<p>When you mention a number or quantity, Dutch adds <b>er</b> to refer back to the noun:</p>
<table>
  <tr><th>Question</th><th>Answer with er</th><th>Meaning</th></tr>
  <tr><td>Hoeveel boeken heb je?</td><td>Ik heb <b>er</b> vijf.</td><td>I have five (of them).</td></tr>
  <tr><td>Heb je appels?</td><td>Ja, ik heb <b>er</b> drie.</td><td>Yes, I have three (of them).</td></tr>
  <tr><td>Hoeveel broers heb je?</td><td>Ik heb <b>er</b> twee.</td><td>I have two (of them).</td></tr>
  <tr><td>Zijn er restaurants?</td><td>Ja, er zijn <b>er</b> veel.</td><td>Yes, there are many (of them).</td></tr>
</table>
<p><b>Key:</b> You cannot say "Ik heb vijf" alone — you NEED er: "Ik heb <b>er</b> vijf."</p>

<h4>4. Use 4: Er = unstressed 'daar' (place)</h4>
<p>When referring to a place already mentioned, use <b>er</b> (= unstressed 'there'):</p>
<table>
  <tr><th>Context</th><th>With er</th></tr>
  <tr><td>Ken je de Graslei?</td><td>Ja, ik kom <b>er</b> vaak. (I come there often.)</td></tr>
  <tr><td>De Boekentoren is groot.</td><td>Ik studeer <b>er</b> elke dag. (I study there.)</td></tr>
  <tr><td>Gent is leuk.</td><td>Ik woon <b>er</b> graag. (I like living there.)</td></tr>
</table>

<h4>5. Use 5: Er in passive sentences</h4>
<p>When there's no specific subject in a passive sentence, Dutch starts with <b>er</b>:</p>
<pre>
  <b>Er</b> wordt veel gefietst in Gent.   (There is a lot of cycling in Ghent.)
  <b>Er</b> wordt Nederlands gesproken.    (Dutch is spoken here.)
  <b>Er</b> werd hard gewerkt.            (There was hard work. / People worked hard.)
</pre>

<h4>6. Tamil comparison</h4>
<p>"Of them" doesn't exist in Tamil: "எனக்கு ஐந்து புத்தகங்கள் இருக்கின்றன" = I have five books. 
No extra word needed. Dutch REQUIRES <b>er</b> with quantities when the noun is already known: "Ik heb <b>er</b> vijf."</p>
""",

        "grammar_letop": """
<ul>
  <li>❌ Hoeveel boeken heb je? – Ik heb vijf. → ✅ Ik heb <b>er</b> vijf. <br><em>With a quantity and no noun → you MUST add er.</em></li>
  <li>❌ Er zijn er veel restaurants. → ✅ Er zijn <b>er</b> veel. (no noun) OR: Er zijn veel restaurants. (with noun) <br><em>Don't use both er AND the full noun. Choose one.</em></li>
  <li>❌ Ik woon <b>daar</b> graag. (unstressed) → ✅ Ik woon <b>er</b> graag. <br><em>When 'there' is unstressed and refers to a known place → er. Use 'daar' only for emphasis.</em></li>
  <li>❌ Wordt veel gefietst in Gent. → ✅ <b>Er</b> wordt veel gefietst in Gent. <br><em>Passive without subject → start with er.</em></li>
  <li>❌ Ik heb er geen boeken. → ✅ Ik heb <b>geen</b> boeken. OR: Ik heb <b>er geen</b>. <br><em>With the noun: no er needed. Without the noun: er + geen.</em></li>
</ul>
""",

        "grammar_extra": """
<h4>Er + quantity: more practice</h4>
<table>
  <tr><th>Question</th><th>Answer</th></tr>
  <tr><td>Hoeveel kamers heeft je huis?</td><td>Het heeft <b>er</b> vier.</td></tr>
  <tr><td>Heb je vrienden in Gent?</td><td>Ja, ik heb <b>er</b> een paar.</td></tr>
  <tr><td>Hoeveel talen spreek je?</td><td>Ik spreek <b>er</b> drie (Tamil, Engels, Nederlands).</td></tr>
  <tr><td>Zijn er problemen?</td><td>Nee, er zijn <b>er</b> geen.</td></tr>
  <tr><td>Heb je katten?</td><td>Ja, ik heb <b>er</b> twee.</td></tr>
</table>

<h4>Er = place: more examples</h4>
<ul>
  <li>Ken je het Gravensteen? Ik ben <b>er</b> vorige week geweest.</li>
  <li>De Stadshal is mooi. <b>Er</b> worden vaak evenementen georganiseerd.</li>
  <li>Ik ken die winkel. Ik koop <b>er</b> altijd brood.</li>
</ul>

<h4>Multiple er-uses in one sentence</h4>
<p>Sometimes a sentence has TWO uses of er:</p>
<ul>
  <li><b>Er</b> zijn <b>er</b> veel. (er₁ = there are, er₂ = of them)</li>
  <li><b>Er</b> worden <b>er</b> drie verkocht. (er₁ = passive, er₂ = of them)</li>
</ul>

<h4>Decision tree: which er?</h4>
<pre>
  Is there a quantity without a noun?    → er + quantity
  Is there a preposition about a thing?  → er + preposition
  Is there 'there is/are'?              → er + zijn
  Is there a known place?               → er = daar
  Is it a passive without subject?       → passive er
</pre>
""",

        "grammar_quick": """
<ul>
  <li><b>Er + quantity</b>: Ik heb er drie. (of them — REQUIRED when noun is dropped)</li>
  <li><b>Er = place</b>: unstressed "there" (Ik woon er graag.)</li>
  <li><b>Er + passive</b>: Er wordt gefietst. (no specific subject)</li>
  <li>Don't use er + quantity AND the full noun together</li>
  <li>Use <b>daar</b> (stressed) vs <b>er</b> (unstressed) for place</li>
  <li>All 5 uses: er+zijn, er+prep, er+quantity, er=place, er+passive</li>
</ul>
""",

        "exercises": [
            {"type": "fill", "q": "In de winkel: Hoeveel boeken heb je? — Ik heb ___ vijf.", "a": "er",
             "tip": "Hoeveelheid zonder zelfstandig naamwoord → er is verplicht. Ik heb ER vijf."},
            {"type": "fill", "q": "Kennismaken: Hoeveel broers heb je? — Ik heb ___ twee.", "a": "er",
             "tip": "Hoeveelheid (twee) zonder 'broers' te herhalen → er."},
            {"type": "choice", "q": "Over de Graslei: Ken je de Graslei? — Ja, ik kom ___ vaak.",
             "options": ["er", "daar", "het"], "a": "er",
             "tip": "Verwijzing naar bekende plaats (onbeklemtoond) → er. Daar = alleen als je benadrukt."},
            {"type": "choice", "q": "Over fietsen: ___ wordt veel gefietst in Gent.",
             "options": ["Er", "Het", "Daar"], "a": "Er",
             "tip": "Passieve zin zonder specifiek subject → begin met er."},
            {"type": "fill", "q": "In een restaurant: Zijn er restaurants? — Ja, er zijn ___ veel.", "a": "er",
             "tip": "Twee er-gebruiken: er zijn (there are) + er (of them) + veel."},
            {"type": "tf", "q": "Je kunt 'Ik heb vijf' zeggen zonder 'er' als het zelfstandig naamwoord al genoemd is.", "a": False,
             "correction": "Fout! Hoeveelheid zonder zelfstandig naamwoord VEREIST er: Ik heb ER vijf.",
             "tip": "Hoeveelheid zonder zelfstandig naamwoord → er is verplicht."},
            {"type": "tf", "q": "'Er wordt Nederlands gesproken' is een passieve zin met er.", "a": True,
             "correction": "Correct! Passief (wordt gesproken) + geen specifiek subject → er.",
             "tip": "Passief + geen duidelijk subject → er."},
            {"type": "tf", "q": "'Er' en 'daar' zijn altijd inwisselbaar.", "a": False,
             "correction": "Fout! 'Er' is onbeklemtoond, 'daar' is beklemtoond. Ik woon er ≠ Ik woon DAAR (benadrukt).",
             "tip": "Er = onbeklemtoond. Daar = beklemtoond (emphasis)."},
            {"type": "choice", "q": "In de les: Hoeveel talen spreek je? — Ik spreek ___ drie.",
             "options": ["er", "ze", "het"], "a": "er",
             "tip": "Hoeveelheid (drie) verwijzend naar talen → er."},
            {"type": "fill", "q": "Over de Boekentoren: De Boekentoren is groot. Ik studeer ___ elke dag.", "a": "er",
             "tip": "Bekende plaats (Boekentoren) onbeklemtoond → er."},
            {"type": "fill", "q": "Vrienden: Heb je vrienden in Gent? — Ja, ik heb ___ een paar.", "a": "er",
             "tip": "Hoeveelheid (een paar) zonder 'vrienden' te herhalen → er."},
            {"type": "translate", "q": "How many languages do you speak? — I speak three (of them).",
             "a": "Hoeveel talen spreek je? — Ik spreek er drie.",
             "tip": "Hoeveelheid + geen zelfstandig naamwoord → er. Ik spreek er drie."},
            {"type": "translate", "q": "There is a lot of cycling in Ghent. (passive)",
             "a": "Er wordt veel gefietst in Gent.",
             "tip": "Passief + geen subject → Er wordt + voltooid deelwoord."},
            {"type": "reorder", "q": "er / heb / drie / ik / gekocht",
             "a": "Ik heb er drie gekocht.",
             "tip": "Ik heb + er + hoeveelheid + deelwoord. Er + hoeveelheid in het midden."},
            {"type": "reorder", "q": "wordt / er / in / gesproken / Nederlands / Gent",
             "a": "Er wordt Nederlands gesproken in Gent.",
             "tip": "Er + passief (wordt gesproken) + plaats."},
        ],

        "jouw_beurt": "Answer these questions using er, then write 4 free sentences.\n\n"
                      "Answer with er:\n"
                      "• Hoeveel talen spreek je? → Ik spreek er …\n"
                      "• Heb je collega's op UGent? → Ja, ik heb er …\n"
                      "• Ken je het Citadelpark? → Ja, ik kom er …\n\n"
                      "Write 4 more sentences using different er-types:\n"
                      "• Er is/zijn … in Gent\n"
                      "• Ik denk eraan / hou ervan\n"
                      "• Er wordt … (passive)\n"
                      "• Ik heb er … (quantity)",
    },

    # ──────────────────────────────────────────────
    #  SESSION 17 — Voordat & Nadat (before / after)
    # ──────────────────────────────────────────────
    {
        "id": 17,
        "title": "Voordat & Nadat",
        "chapter": "Hoofdstuk 6 – ER & Tijd",
        "book_page": "p. 110-115",
        "review": "In sessie 14 leerde je connectors. Nu focussen we op twee tijdconnectors: "
                  "<b>voordat</b> (before) en <b>nadat</b> (after). Ze maken bijzinnen → "
                  "werkwoord naar het einde!",

        "vocabulary": [
            {"nl": "voordat", "en": "before (conjunction)",
             "example": "Voordat ik vertrek, eet ik."},
            {"nl": "nadat", "en": "after (conjunction)",
             "example": "Nadat ik gegeten had, ging ik weg."},
            {"nl": "eerst", "en": "first", "example": "Ik ga eerst douchen."},
            {"nl": "daarna", "en": "after that / then",
                "example": "Daarna kleed ik me aan."},
            {"nl": "ten slotte", "en": "finally",
                "example": "Ten slotte vertrek ik naar het werk."},
            {"nl": "ondertussen", "en": "meanwhile",
                "example": "Ondertussen regent het."},
            {"nl": "zich klaarmaken", "en": "to get ready",
                "example": "Ik maak me elke dag klaar."},
            {"nl": "aankomen", "en": "to arrive",
                "example": "We komen om 9 uur aan."},
            {"nl": "opstaan", "en": "to get up", "example": "Ik sta om 7 uur op."},
            {"nl": "beginnen met", "en": "to start with",
                "example": "Ik begin met ontbijt."},
            {"nl": "de routine", "en": "the routine",
                "example": "Mijn ochtendRoutine is kort."},
            {"nl": "de afspraak", "en": "the appointment",
                "example": "Ik heb een afspraak bij de dokter."},
        ],

        "grammar_title": "Voordat & Nadat — tijdconnectors (time connectors)",

        "grammar_html": """
<h4>1. Wat zijn voordat en nadat?</h4>
<p>Both are <b>subordinating conjunctions</b> (onderschikkende voegwoorden). They push the verb to the END of the subclause — just like omdat, als, toen, dat.</p>

<table>
<tr><th>Connector</th><th>Meaning</th><th>Formula</th></tr>
<tr><td><b>voordat</b></td><td>before</td><td>Voordat + S + … + <b>V-einde</b>, hoofdzin.</td></tr>
<tr><td><b>nadat</b></td><td>after</td><td>Nadat + S + … + <b>V-einde</b>, hoofdzin.</td></tr>
</table>

<h4>2. Woordvolgorde (Word order)</h4>
<div class="formula-card">
<b>Bijzin eerst → inversie in hoofdzin:</b><br>
Voordat ik <u>vertrek</u>, <b>eet</b> ik ontbijt.<br>
Nadat hij <u>gegeten had</u>, <b>ging</b> hij weg.<br><br>
<b>Hoofdzin eerst → gewone volgorde:</b><br>
Ik eet ontbijt voordat ik <u>vertrek</u>.<br>
Hij ging weg nadat hij <u>gegeten had</u>.
</div>

<h4>3. Nadat + voltooide tijd (perfect tense)</h4>
<p>After <b>nadat</b>, Dutch typically uses <b>one tense further in the past</b> than the main clause:</p>
<table>
<tr><th>Hoofdzin</th><th>Nadat-bijzin</th><th>Example</th></tr>
<tr><td>Presens</td><td>Perfectum</td><td>Ik ga werken nadat ik <b>heb</b> gegeten.</td></tr>
<tr><td>Imperfectum</td><td>Plusquamperfectum (had + vd)</td><td>Ik ging werken nadat ik <b>had</b> gegeten.</td></tr>
</table>
<p>⚠️ In everyday speech, many Dutch speakers use the same tense in both clauses, but in writing (and exams!) the tense shift is important.</p>

<h4>4. Voordat — geen tijdverschuiving nodig</h4>
<p>After <b>voordat</b>, you use the <b>same tense</b> as the main clause — no shift needed:</p>
<ul>
<li>Ik douche <b>voordat</b> ik naar mijn werk <b>ga</b>. (both present)</li>
<li>Ik douchte <b>voordat</b> ik naar mijn werk <b>ging</b>. (both past)</li>
</ul>

<h4>5. Vergelijking: voor/na vs voordat/nadat</h4>
<table>
<tr><th>Type</th><th>Followed by</th><th>Example</th></tr>
<tr><td><b>voor / na</b></td><td>noun / pronoun</td><td>Na <b>het eten</b> ga ik wandelen.</td></tr>
<tr><td><b>voordat / nadat</b></td><td>full clause (S + V)</td><td>Nadat <b>ik heb gegeten</b>, ga ik wandelen.</td></tr>
</table>

<h4>🇮🇳 Tamil comparison</h4>
<p><b>Voordat</b> ≈ "...க்கு முன்னால்" (munnaale) — Naan poga munnaale, saappiduven.<br>
<b>Nadat</b> ≈ "...அப்புறம்" (appuram) / "...பிறகு" (piragu) — Naan saappitta piragu, poveen.</p>
<p>Just like Tamil, the time clause sets the context first, then the main action follows.</p>
""",

        "grammar_letop": [
            {"wrong": "Voordat ik vertrek ik eet ontbijt.",
             "right": "Voordat ik vertrek, eet ik ontbijt.",
             "explain": "When the bijzin comes first, the main clause has INVERSIE: verb before subject."},
            {"wrong": "Nadat ik eet, ga ik werken.",
             "right": "Nadat ik heb gegeten, ga ik werken.",
             "explain": "After nadat, use one tense further back (perfectum if main is presens)."},
            {"wrong": "Na ik heb gegeten, ga ik weg.",
             "right": "Nadat ik heb gegeten, ga ik weg.",
             "explain": "Na + noun (na het eten). Nadat + full clause (nadat ik heb gegeten)."},
            {"wrong": "Voordat ik ga vertrekken, eet ik.",
             "right": "Voordat ik vertrek, eet ik.",
             "explain": "Voordat already signals the time, so no extra gaan+infinitive needed."},
            {"wrong": "Ik ga weg, nadat ik had gegeten.",
             "right": "Ik ga weg nadat ik heb gegeten.",
             "explain": "Main clause is presens → nadat clause uses perfectum (heb), not plusquam (had)."},
        ],

        "grammar_extra": """
<h4>Ochtendschema — Beschrijf met voordat/nadat</h4>
<table>
<tr><th>#</th><th>Activiteit</th><th>Beschrijving</th></tr>
<tr><td>1</td><td>opstaan</td><td>Ik sta om 7 uur op.</td></tr>
<tr><td>2</td><td>douchen</td><td>Nadat ik <b>ben opgestaan</b>, douche ik.</td></tr>
<tr><td>3</td><td>ontbijten</td><td>Voordat ik <b>naar UGent ga</b>, ontbijt ik.</td></tr>
<tr><td>4</td><td>vertrekken</td><td>Nadat ik <b>heb ontbeten</b>, vertrek ik.</td></tr>
<tr><td>5</td><td>aankomen</td><td>Voordat het college <b>begint</b>, kom ik aan.</td></tr>
</table>

<p><b>More examples:</b></p>
<ul>
<li>Voordat ik slaap, lees ik een boek.</li>
<li>Nadat we hadden gewandeld, dronken we koffie in het Citadelpark.</li>
<li>Ik poets mijn tanden voordat ik naar bed ga.</li>
<li>Nadat de les was afgelopen, gingen we naar de mensa.</li>
<li>Voordat je het examen maakt, moet je goed studeren.</li>
</ul>
""",

        "grammar_quick": [
            "Voordat = before → bijzin (verb at end).",
            "Nadat = after → bijzin (verb at end).",
            "Nadat: use one tense further back (presens→perfectum, imperf→plusquamperf).",
            "Voordat: same tense in both clauses.",
            "Bijzin first → comma → inversie in main clause.",
            "Voor/na + noun. Voordat/nadat + full clause.",
        ],

        "exercises": [
            {"type": "fill", "q": "Na het ontbijt: ___ ik heb gegeten, ga ik wandelen.", "a": "Nadat",
             "tip": "Het eten gebeurt EERST, dan wandelen. After = nadat."},
            {"type": "fill", "q": "Inpakken: ___ ik vertrek, moet ik nog inpakken.", "a": "Voordat",
             "tip": "Inpakken gebeurt VÓÓR het vertrek. Before = voordat."},
            {"type": "fill", "q": "Studeren: Nadat hij had ___ (studeren), ging hij slapen.", "a": "gestudeerd",
             "tip": "Had + voltooid deelwoord. Studeren → gestudeerd."},
            {"type": "fill", "q": "Avondroutine: Ik poets mijn tanden voordat ik naar bed ___.", "a": "ga",
             "tip": "Tegenwoordige tijd in beide zinnen met voordat. Ik ga naar bed."},
            {"type": "choice",
             "q": "Op het werk: 'After I have eaten, I go to work.' Welke zin is correct?",
             "options": ["Na ik eet, ga ik werken.",
                         "Nadat ik heb gegeten, ga ik werken.",
                         "Nadat ik eet, ga ik werken.",
                         "Na dat ik eet, ga ik werken."],
             "a": "Nadat ik heb gegeten, ga ik werken.",
             "tip": "Nadat + perfectum als de hoofdzin in het presens staat. Nadat is één woord."},
            {"type": "choice",
             "q": "In een verhaal: Welke zin is correct?",
             "options": ["Voordat hij ging slapen, las hij.",
                         "Voordat hij ging slapen, hij las.",
                         "Voordat hij slapen ging, las hij.",
                         "Voor dat hij ging slapen, las hij."],
             "a": "Voordat hij ging slapen, las hij.",
             "tip": "Bijzin eerst → inversie: las hij (V-S). Werkwoordcluster: ging slapen op het einde."},
            {"type": "choice",
             "q": "Over je planning: 'Ik maak huiswerk voordat ik ga slapen.' Welke is correct?",
             "options": ["Voordat ik ga slapen, maak ik huiswerk.",
                         "Voordat ik ga slapen, ik maak huiswerk.",
                         "Voordat ik slaap ga, maak ik huiswerk.",
                         "Voor dat ik ga slapen, maak ik huiswerk."],
             "a": "Voordat ik ga slapen, maak ik huiswerk.",
             "tip": "Bijzin eerst → inversie: maak ik (V-S). Voordat is één woord!"},
            {"type": "tf", "q": "'Nadat ik eet, ga ik werken' is correct standaard Nederlands.", "a": "Nee",
             "tip": "Na nadat gebruik je perfectum als de hoofdzin presens is: nadat ik heb gegeten."},
            {"type": "tf", "q": "'Voordat ik vertrek, eet ik' heeft een correcte woordvolgorde.", "a": "Ja",
             "tip": "Bijzin (voordat ik vertrek) → komma → inversie (eet ik). Perfect!"},
            {"type": "tf", "q": "'Na het eten ga ik slapen' is een correcte zin.", "a": "Ja",
             "tip": "Na + zelfstandig naamwoord (het eten) is prima. Dit is GEEN bijzin, dus gewoon inversie."},
            {"type": "translate", "q": "Before I go to Ghent, I eat breakfast.",
             "a": "Voordat ik naar Gent ga, ontbijt ik.",
             "tip": "Voordat + S + rest + V-einde, inversie in de hoofdzin."},
            {"type": "translate", "q": "After she had studied, she went to sleep.",
             "a": "Nadat zij had gestudeerd, ging zij slapen.",
             "tip": "Hoofdzin = imperfectum (ging) → nadat-bijzin = plusquamperfectum (had gestudeerd)."},
            {"type": "translate", "q": "I brush my teeth before I go to bed.",
             "a": "Ik poets mijn tanden voordat ik naar bed ga.",
             "tip": "Hoofdzin eerst → geen inversie. Voordat-bijzin: werkwoord op einde (ga)."},
            {"type": "reorder", "q": "nadat / had / ik / gegeten / ging / ik / weg",
             "a": "Nadat ik had gegeten, ging ik weg.",
             "tip": "Nadat + S + had + vd → komma → inversie (ging ik)."},
            {"type": "reorder", "q": "ik / werken / ga / ik / nadat / heb / gegeten",
             "a": "Nadat ik heb gegeten, ga ik werken.",
             "tip": "Nadat + S + heb + vd → komma → inversie (ga ik)."},
        ],

        "jouw_beurt": "Beschrijf je ochtend- of avondroutine met voordat en nadat.\n\n"
                      "Gebruik minstens 3× voordat en 3× nadat:\n"
                      "• Voordat ik naar UGent ga, …\n"
                      "• Nadat ik heb gedoucht, …\n"
                      "• Ik ontbijt voordat …\n"
                      "• Nadat de les was afgelopen, …\n\n"
                      "Bonusvraag: Wat doe je 's avonds voordat je gaat slapen?",
    },

    # ──────────────────────────────────────────────
    #  SESSION 18 — Persoonlijke voornaamwoorden (Pronouns)
    # ──────────────────────────────────────────────
    {
        "id": 18,
        "title": "Persoonlijke voornaamwoorden",
        "chapter": "Hoofdstuk 7 – Voornaamwoorden",
        "book_page": "p. 116-122",
        "review": "Je kent al ik, jij, hij, zij, wij, jullie, zij. Nu leer je het volledige "
                  "systeem: <b>subject</b>, <b>object</b>, <b>bezittelijk</b> (possessive) en "
                  "<b>reflexief</b> (reflexive) voornaamwoorden.",

        "vocabulary": [
            {"nl": "het voornaamwoord", "en": "the pronoun",
                "example": "Ik is een voornaamwoord."},
            {"nl": "het onderwerp", "en": "the subject",
                "example": "Het onderwerp doet de actie."},
            {"nl": "het lijdend voorwerp", "en": "the direct object",
                "example": "Ik zie hem. (hem = LV)"},
            {"nl": "het meewerkend voorwerp", "en": "the indirect object",
                "example": "Ik geef haar een boek."},
            {"nl": "bezittelijk", "en": "possessive",
                "example": "Mijn boek, jouw huis."},
            {"nl": "reflexief", "en": "reflexive",
                "example": "Ik was me. (me = reflexive)"},
            {"nl": "beklemtoond", "en": "stressed / emphatic",
                "example": "MIJ heb je niet gevraagd!"},
            {"nl": "onbeklemtoond", "en": "unstressed",
                "example": "Geef me dat boek even."},
            {"nl": "sturen", "en": "to send", "example": "Ik stuur je een bericht."},
            {"nl": "bellen",
                "en": "to call (phone)", "example": "Hij belt mij elke dag."},
            {"nl": "lenen", "en": "to lend / borrow",
                "example": "Kun je me je pen lenen?"},
            {"nl": "uitnodigen", "en": "to invite",
                "example": "Ik nodig jullie uit voor het feest."},
        ],

        "grammar_title": "Het complete voornaamwoordsysteem (The full pronoun system)",

        "grammar_html": """
<h4>1. Overzichtstabel (Complete overview table)</h4>
<table>
<tr><th>Persoon</th><th>Subject</th><th>Object (onbekl.)</th><th>Object (bekl.)</th><th>Bezittelijk</th><th>Reflexief</th></tr>
<tr><td>ik</td><td>ik</td><td>me</td><td>mij</td><td>mijn</td><td>me / mezelf</td></tr>
<tr><td>jij</td><td>jij / je</td><td>je</td><td>jou</td><td>jouw / je</td><td>je / jezelf</td></tr>
<tr><td>hij</td><td>hij</td><td>'m</td><td>hem</td><td>zijn</td><td>zich / zichzelf</td></tr>
<tr><td>zij (v)</td><td>zij / ze</td><td>d'r / 'r</td><td>haar</td><td>haar</td><td>zich / zichzelf</td></tr>
<tr><td>het</td><td>het</td><td>het / 't</td><td>het</td><td>zijn</td><td>zich / zichzelf</td></tr>
<tr><td>wij</td><td>wij / we</td><td>ons</td><td>ons</td><td>ons / onze</td><td>ons / onszelf</td></tr>
<tr><td>jullie</td><td>jullie</td><td>jullie</td><td>jullie</td><td>jullie / je</td><td>je / jezelf</td></tr>
<tr><td>zij (pl)</td><td>zij / ze</td><td>ze</td><td>hen / hun</td><td>hun</td><td>zich / zichzelf</td></tr>
<tr><td>u (form.)</td><td>u</td><td>u</td><td>u</td><td>uw</td><td>u / uzelf</td></tr>
</table>

<h4>2. Subject vs Object</h4>
<p>The <b>subject</b> does the action. The <b>object</b> receives the action.</p>
<div class="formula-card">
<b>Ik</b> (subject) zie <b>hem</b> (object).<br>
<b>Hij</b> (subject) belt <b>mij</b> (object).<br>
<b>Wij</b> (subject) nodigen <b>jullie</b> (object) uit.
</div>

<h4>3. Beklemtoond vs Onbeklemtoond (Stressed vs Unstressed)</h4>
<p>In everyday speech, Dutch uses the <b>unstressed</b> form. The <b>stressed</b> form is for emphasis or contrast:</p>
<ul>
<li>Geef <b>me</b> dat boek. (normal, unstressed)</li>
<li><b>Mij</b> heb je niet gevraagd! (emphatic, stressed)</li>
<li>Ik bel <b>'m</b> morgen. (unstressed him)</li>
<li>Ik bel <b>hem</b>, niet haar! (stressed, contrast)</li>
</ul>

<h4>4. Bezittelijke voornaamwoorden (Possessive pronouns)</h4>
<table>
<tr><th>Persoon</th><th>Before de-woord</th><th>Before het-woord</th></tr>
<tr><td>ik</td><td>mijn fiets</td><td>mijn boek</td></tr>
<tr><td>jij</td><td>jouw / je fiets</td><td>jouw / je boek</td></tr>
<tr><td>hij</td><td>zijn fiets</td><td>zijn boek</td></tr>
<tr><td>zij</td><td>haar fiets</td><td>haar boek</td></tr>
<tr><td>wij</td><td>onze fiets</td><td>ons boek</td></tr>
<tr><td>jullie</td><td>jullie fiets</td><td>jullie boek</td></tr>
<tr><td>zij (pl)</td><td>hun fiets</td><td>hun boek</td></tr>
</table>
<p>⚠️ <b>Ons</b> before het-words, <b>onze</b> before de-words and plurals!</p>

<h4>5. Reflexieve voornaamwoorden (Reflexive pronouns)</h4>
<p>Used when the subject and object are the same person:</p>
<ul>
<li>Ik was <b>me</b>. (I wash myself)</li>
<li>Hij scheert <b>zich</b>. (He shaves himself)</li>
<li>Wij vergissen <b>ons</b>. (We are mistaken)</li>
</ul>
<p>Add <b>-zelf</b> for emphasis: Ik doe het <b>zelf</b>! / Hij wast <b>zichzelf</b>.</p>

<h4>6. Hen vs Hun (formal distinction)</h4>
<table>
<tr><th>Form</th><th>Use</th><th>Example</th></tr>
<tr><td><b>hen</b></td><td>direct object / after preposition</td><td>Ik zie <b>hen</b>. / voor <b>hen</b></td></tr>
<tr><td><b>hun</b></td><td>indirect object</td><td>Ik geef <b>hun</b> een boek.</td></tr>
</table>
<p>In practice, most Dutch speakers use <b>hen</b> for both or just use <b>ze</b>.</p>

<h4>🇮🇳 Tamil comparison</h4>
<p>Tamil also has subject/object forms: நான் (naan, I) vs என்னை (ennai, me), நீ (nee, you) vs உன்னை (unnai, you-object).<br>
Possessives: என் (en, my), உன் (un, your) — just like mijn, jouw.<br>
Reflexive: Tamil uses தன்னை (thannai, oneself) — similar to zich/zichzelf.</p>
<p>The key difference: Dutch has <b>stressed vs unstressed</b> pairs (me/mij, je/jou) which Tamil doesn't have.</p>
""",

        "grammar_letop": [
            {"wrong": "Ik zie hij.",
             "right": "Ik zie hem.",
             "explain": "After a verb (as object), use the OBJECT form: hem, not hij."},
            {"wrong": "Wij gaan naar ons huis. (de-word: huis? No, het huis!)",
             "right": "Wij gaan naar ons huis.",
             "explain": "Huis = het-word → ons. But: onze auto (de auto = de-word → onze)."},
            {"wrong": "Ik geef hen een cadeau.",
             "right": "Ik geef hun een cadeau.",
             "explain": "Indirect object (to whom?) = hun. Direct object / after preposition = hen."},
            {"wrong": "Hij wast hem. (meaning: he washes himself)",
             "right": "Hij wast zich.",
             "explain": "When subject = object (same person), use reflexive: zich, not hem."},
            {"wrong": "Geef mij het boek. (casual conversation)",
             "right": "Geef me het boek.",
             "explain": "In casual speech, use unstressed me. Mij is only for emphasis or contrast."},
        ],

        "grammar_extra": """
<h4>Vul de juiste vorm in — oefentabel</h4>
<table>
<tr><th>Zin</th><th>Antwoord</th></tr>
<tr><td>Ik zie ___ elke dag. (hij)</td><td>hem</td></tr>
<tr><td>___ fiets staat hier. (wij, de-word)</td><td>Onze</td></tr>
<tr><td>Zij wast ___ 's ochtends.</td><td>zich</td></tr>
<tr><td>Geef ___ dat boek even. (ik, casual)</td><td>me</td></tr>
<tr><td>___ heb je niet uitgenodigd! (ik, emphasis)</td><td>Mij</td></tr>
</table>

<p><b>More examples in context:</b></p>
<ul>
<li>Ken je <b>haar</b>? Ja, ik ken <b>haar</b> van UGent.</li>
<li><b>Ons</b> kantoor is op de derde verdieping. (het kantoor → ons)</li>
<li>Zij vergissen <b>zich</b> vaak. (reflexive, plural zij)</li>
<li>Ik stuur <b>je</b> een e-mail. (unstressed, casual)</li>
<li>Wij hebben <b>hen</b> gisteren gezien. (direct object, stressed)</li>
<li><b>Hun</b> kinderen spelen in het park. (possessive, plural)</li>
</ul>
""",

        "grammar_quick": [
            "Subject = doet de actie (ik, jij, hij). Object = ontvangt de actie (mij, jou, hem).",
            "Unstressed in casual speech (me, je, 'm). Stressed for emphasis (mij, jou, hem).",
            "Bezittelijk: mijn, jouw, zijn, haar, ons/onze, jullie, hun, uw.",
            "Ons before het-words, onze before de-words and plurals.",
            "Reflexief: me, je, zich, ons, je, zich. Add -zelf for emphasis.",
            "Hen = direct object / after preposition. Hun = indirect object (formal rule).",
        ],

        "exercises": [
            {"type": "fill", "q": "Op het werk: Ik zie ___ elke dag. (hij → object)", "a": "hem",
             "tip": "Objectvorm van hij is hem (beklemtoond) of 'm (onbeklemtoond)."},
            {"type": "fill", "q": "In de les: Geef ___ dat boek even. (ik → onbeklemtoond object)", "a": "me",
             "tip": "Onbeklemtoond object van ik = me. Beklemtoond = mij."},
            {"type": "fill", "q": "Over jullie huis: ___ huis is groot. (wij → bezittelijk, het-woord)", "a": "Ons",
             "tip": "Het huis = het-woord → ons. De auto = de-woord → onze."},
            {"type": "fill", "q": "Ochtendroutine: Hij wast ___ elke ochtend. (reflexief)", "a": "zich",
             "tip": "Zichzelf wassen → reflexief. Voor hij/zij/het/zij(mv) is het reflexief zich."},
            {"type": "fill", "q": "Een e-mail: Ik stuur ___ morgen een e-mail. (jij → onbeklemtoond object)", "a": "je",
             "tip": "Onbeklemtoond object van jij = je. Beklemtoond = jou."},
            {"type": "choice",
             "q": "Een uitnodiging: 'We nodigen hen/hun uit.' Welke is correct?",
             "options": ["Wij nodigen zij uit.", "Wij nodigen hen uit.",
                         "Wij nodigen hun uit.", "Wij nodigen ze uit."],
             "a": "Wij nodigen hen uit.",
             "tip": "Hen = lijdend voorwerp (direct object). Ze = informeel. Hen is de veiligste keuze."},
            {"type": "choice",
             "q": "Over de auto: '___ auto staat voor het gebouw.' (wij)",
             "options": ["Ons auto", "Onze auto", "Onzen auto", "Wij auto"],
             "a": "Onze auto",
             "tip": "De auto = de-woord → onze. Het huis = het-woord → ons."},
            {"type": "choice",
             "q": "Een cadeau: 'Ik geef ___ een cadeau.' (zij, meervoud, meewerkend voorwerp)",
             "options": ["hen", "hun", "haar", "ze"],
             "a": "hun",
             "tip": "Meewerkend voorwerp (aan wie ik geef) = hun. Lijdend voorwerp = hen."},
            {"type": "tf", "q": "'Ik zie hij' is correct Nederlands.", "a": "Nee",
             "tip": "Na een werkwoord gebruik je de objectvorm: Ik zie HEM."},
            {"type": "tf", "q": "'Zij wast zich' betekent 'she washes herself'.", "a": "Ja",
             "tip": "Zich = reflexief voor hij/zij/het. Zij wast zichzelf = correct."},
            {"type": "tf", "q": "'Ons kantoor' is correct (het kantoor).", "a": "Ja",
             "tip": "Het kantoor = het-woord → ons. Correct!"},
            {"type": "translate", "q": "I see her every day at university.",
             "a": "Ik zie haar elke dag op de universiteit.",
             "tip": "Haar (object) = haar. Op de universiteit = at university."},
            {"type": "translate", "q": "Give me your book, please.",
             "a": "Geef me je boek, alsjeblieft.",
             "tip": "Informeel: me (onbeklemtoond) + je (bezittelijk). Alsjeblieft = please."},
            {"type": "reorder", "q": "haar / ik / elke / zie / dag",
             "a": "Ik zie haar elke dag.",
             "tip": "S + V + object + tijd. Ik zie haar elke dag."},
            {"type": "reorder", "q": "geef / boek / me / dat / even",
             "a": "Geef me dat boek even.",
             "tip": "Imperatief: Geef + meewerkend voorwerp (me) + lijdend voorwerp (dat boek) + even."},
        ],

        "jouw_beurt": "Schrijf 6 zinnen met voornaamwoorden.\n\n"
                      "Gebruik:\n"
                      "• 2 zinnen met object-voornaamwoorden (me/mij, hem, haar, ons, hen)\n"
                      "  → Ik bel hem elke week. / Zij helpt ons met Nederlands.\n"
                      "• 2 zinnen met bezittelijke voornaamwoorden (mijn, jouw, zijn, haar, ons/onze, hun)\n"
                      "  → Onze les begint om 9 uur. / Hun kinderen spreken al Nederlands.\n"
                      "• 2 zinnen met reflexieve voornaamwoorden (me, je, zich, ons)\n"
                      "  → Ik was me 's ochtends. / Hij vergist zich.\n\n"
                      "Bonus: Schrijf een mini-dialoog (4 zinnen) waarin je minstens 3 verschillende "
                      "voornaamwoordvormen gebruikt.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 19 — Vaste voorzetsels 1 (Fixed prepositions — verbs)
    # ──────────────────────────────────────────────
    {
        "id": 19,
        "title": "Vaste voorzetsels – werkwoorden",
        "chapter": "Hoofdstuk 7 – Voorzetsels",
        "book_page": "p. 123-128",
        "review": "In het Nederlands horen sommige werkwoorden bij een <b>vast voorzetsel</b> "
                  "(fixed preposition). Je kunt dit niet logisch afleiden — je moet ze leren! "
                  "Vergelijk: Engels 'depend ON', 'listen TO'. Nederlands heeft hetzelfde systeem.",

        "vocabulary": [
            {"nl": "het voorzetsel", "en": "the preposition",
                "example": "Op, aan, met zijn voorzetsels."},
            {"nl": "denken aan", "en": "to think of/about",
                "example": "Ik denk aan mijn familie."},
            {"nl": "dromen van", "en": "to dream of",
                "example": "Ik droom van vakantie."},
            {"nl": "wachten op", "en": "to wait for",
                "example": "Ik wacht op de bus."},
            {"nl": "houden van", "en": "to love / like",
                "example": "Ik hou van kaas."},
            {"nl": "luisteren naar", "en": "to listen to",
                "example": "Ik luister naar muziek."},
            {"nl": "beginnen met", "en": "to start with",
                "example": "We beginnen met de les."},
            {"nl": "stoppen met",
                "en": "to stop (doing)", "example": "Ik stop met roken."},
            {"nl": "zoeken naar", "en": "to search for",
                "example": "Ik zoek naar mijn sleutels."},
            {"nl": "lijken op", "en": "to look like / resemble",
                "example": "Hij lijkt op zijn vader."},
            {"nl": "kiezen voor", "en": "to choose for",
                "example": "Ik kies voor Nederlands."},
            {"nl": "zich interesseren voor", "en": "to be interested in",
                "example": "Ik interesseer me voor talen."},
        ],

        "grammar_title": "Vaste voorzetsels bij werkwoorden (Fixed prepositions with verbs)",

        "grammar_html": """
<h4>1. Wat zijn vaste voorzetsels?</h4>
<p>Many Dutch verbs come with a <b>fixed preposition</b> that you must memorize. The preposition often doesn't match the English one!</p>
<div class="formula-card">
<b>English:</b> to wait FOR → <b>Dutch:</b> wachten <b>op</b><br>
<b>English:</b> to think OF → <b>Dutch:</b> denken <b>aan</b><br>
<b>English:</b> to dream OF → <b>Dutch:</b> dromen <b>van</b><br>
<b>English:</b> to listen TO → <b>Dutch:</b> luisteren <b>naar</b>
</div>

<h4>2. De belangrijkste combinaties (Most important combinations)</h4>
<table>
<tr><th>Voorzetsel</th><th>Werkwoord</th><th>English</th><th>Voorbeeld</th></tr>
<tr><td rowspan="4"><b>aan</b></td><td>denken aan</td><td>think of</td><td>Ik denk aan je.</td></tr>
<tr><td>wennen aan</td><td>get used to</td><td>Ik wen aan het weer.</td></tr>
<tr><td>twijfelen aan</td><td>doubt</td><td>Ik twijfel aan zijn verhaal.</td></tr>
<tr><td>deelnemen aan</td><td>participate in</td><td>Ik neem deel aan het project.</td></tr>
<tr><td rowspan="3"><b>op</b></td><td>wachten op</td><td>wait for</td><td>Ik wacht op de tram.</td></tr>
<tr><td>lijken op</td><td>look like</td><td>Zij lijkt op haar moeder.</td></tr>
<tr><td>letten op</td><td>pay attention to</td><td>Let op de spelling!</td></tr>
<tr><td rowspan="3"><b>van</b></td><td>houden van</td><td>love</td><td>Ik hou van Gent.</td></tr>
<tr><td>dromen van</td><td>dream of</td><td>Ik droom van vakantie.</td></tr>
<tr><td>afhangen van</td><td>depend on</td><td>Het hangt van het weer af.</td></tr>
<tr><td rowspan="3"><b>naar</b></td><td>luisteren naar</td><td>listen to</td><td>Luister naar de leraar.</td></tr>
<tr><td>zoeken naar</td><td>search for</td><td>Ik zoek naar een kamer.</td></tr>
<tr><td>kijken naar</td><td>look at / watch</td><td>Ik kijk naar een film.</td></tr>
<tr><td rowspan="3"><b>met</b></td><td>beginnen met</td><td>start with</td><td>Begin met oefening 1.</td></tr>
<tr><td>stoppen met</td><td>stop doing</td><td>Ik stop met roken.</td></tr>
<tr><td>trouwen met</td><td>marry</td><td>Zij trouwt met hem.</td></tr>
<tr><td rowspan="2"><b>voor</b></td><td>kiezen voor</td><td>choose</td><td>Ik kies voor UGent.</td></tr>
<tr><td>zorgen voor</td><td>take care of</td><td>Ik zorg voor mijn kat.</td></tr>
<tr><td rowspan="2"><b>over</b></td><td>praten over</td><td>talk about</td><td>We praten over het examen.</td></tr>
<tr><td>nadenken over</td><td>think about</td><td>Ik denk na over mijn toekomst.</td></tr>
</table>

<h4>3. Er + voorzetsel (revisie van sessie 15)</h4>
<p>When the object is a <b>thing</b> (not a person), replace it with <b>er + voorzetsel</b>:</p>
<table>
<tr><th>Met persoon</th><th>Met ding/abstract</th></tr>
<tr><td>Ik denk <b>aan hem</b>.</td><td>Ik denk <b>eraan</b>. (= aan dat ding/idee)</td></tr>
<tr><td>Ik wacht <b>op haar</b>.</td><td>Ik wacht <b>erop</b>. (= op de bus)</td></tr>
<tr><td>Ik hou <b>van hem</b>.</td><td>Ik hou <b>ervan</b>. (= van kaas)</td></tr>
</table>
<p>⚠️ Only for things! For people, keep the preposition + pronoun: <i>Ik denk aan <b>hem</b></i>.</p>

<h4>4. Vraagwoord: waar + voorzetsel</h4>
<p>To ask about things: <b>waar + voorzetsel</b>:</p>
<ul>
<li><b>Waaraan</b> denk je? — Ik denk eraan.</li>
<li><b>Waarop</b> wacht je? — Ik wacht erop.</li>
<li><b>Waarvan</b> hou je? — Ik hou ervan.</li>
<li><b>Waarnaar</b> luister je? — Ik luister ernaar.</li>
</ul>
<p>For people: <b>Aan wie</b> denk je? <b>Op wie</b> wacht je?</p>

<h4>🇮🇳 Tamil comparison</h4>
<p>Tamil uses postpositions: நான் உன்னை <b>பற்றி</b> நினைக்கிறேன் (pattri = about).<br>
Dutch uses prepositions before the noun: Ik denk <b>aan</b> jou.<br>
The concept is the same — certain verbs require specific words — but the position differs (post vs pre).</p>
""",

        "grammar_letop": [
            {"wrong": "Ik denk over mijn familie.",
             "right": "Ik denk aan mijn familie.",
             "explain": "Denken uses AAN, not over. Nadenken uses over: Ik denk na over mijn toekomst."},
            {"wrong": "Ik wacht voor de bus.",
             "right": "Ik wacht op de bus.",
             "explain": "Wachten + OP. Not voor! (English 'wait for' misleads.)"},
            {"wrong": "Ik luister de muziek.",
             "right": "Ik luister naar de muziek.",
             "explain": "Luisteren always needs NAAR. You can't drop the preposition."},
            {"wrong": "Ik denk aan het. (= I think about it)",
             "right": "Ik denk eraan.",
             "explain": "For things, use er+voorzetsel (eraan), NOT aan het."},
            {"wrong": "Ik hou ervan hem. (= I love him)",
             "right": "Ik hou van hem.",
             "explain": "Er+voorzetsel is only for THINGS. For people: van + pronoun."},
        ],

        "grammar_extra": """
<h4>Oefentabel — Welk voorzetsel?</h4>
<table>
<tr><th>Werkwoord</th><th>Voorzetsel</th><th>Voorbeeldzin</th></tr>
<tr><td>denken</td><td>aan</td><td>Ik denk aan het examen.</td></tr>
<tr><td>wachten</td><td>op</td><td>We wachten op de professor.</td></tr>
<tr><td>houden</td><td>van</td><td>Ik hou van Belgisch bier.</td></tr>
<tr><td>luisteren</td><td>naar</td><td>Luister naar het nieuws.</td></tr>
<tr><td>beginnen</td><td>met</td><td>We beginnen met les 19.</td></tr>
<tr><td>praten</td><td>over</td><td>Ze praten over de vakantie.</td></tr>
<tr><td>zoeken</td><td>naar</td><td>Ik zoek naar een nieuw appartement.</td></tr>
</table>

<p><b>Met er+voorzetsel:</b></p>
<ul>
<li>Denk je aan het examen? → Ja, ik denk <b>eraan</b>.</li>
<li>Wacht je op de tram? → Ja, ik wacht <b>erop</b>.</li>
<li>Hou je van kaas? → Ja, ik hou <b>ervan</b>.</li>
<li>Luister je naar die podcast? → Ja, ik luister <b>ernaar</b>.</li>
<li>Begin je met het project? → Ja, ik begin <b>ermee</b>.</li>
</ul>
""",

        "grammar_quick": [
            "Vaste voorzetsels: werkwoord + vast voorzetsel → uit je hoofd leren!",
            "aan: denken aan, wennen aan. op: wachten op, lijken op. van: houden van, dromen van.",
            "naar: luisteren naar, zoeken naar. met: beginnen met, stoppen met. over: praten over.",
            "Ding → er+voorzetsel: eraan, erop, ervan. Persoon → voorzetsel + pronoun.",
            "Vraag over ding: waar+voorzetsel (waaraan, waarop). Over persoon: voorzetsel + wie.",
            "Let op: English prepositions ≠ Dutch! wait FOR = wachten OP, think OF = denken AAN.",
        ],

        "exercises": [
            {"type": "fill", "q": "Op de halte: Ik wacht ___ de tram. (wait for)", "a": "op",
             "tip": "Wachten + OP (niet voor!). Engels 'for' = Nederlands 'op' hier."},
            {"type": "fill", "q": "Thuis: Zij luistert ___ de radio.", "a": "naar",
             "tip": "Luisteren + NAAR. Altijd — je kunt het niet weglaten."},
            {"type": "fill", "q": "Dromen: Hij droomt ___ een reis naar Japan.", "a": "van",
             "tip": "Dromen + VAN. Dream of = dromen van."},
            {"type": "fill", "q": "Over het examen: Denk je aan het examen? — Ja, ik denk ___.", "a": "eraan",
             "tip": "Ding → er+voorzetsel. Denken aan (het examen) → eraan."},
            {"type": "fill", "q": "Met collega's: We praten ___ onze vakantie.", "a": "over",
             "tip": "Praten + OVER. Talk about = praten over."},
            {"type": "choice",
             "q": "In Gent: 'I'm getting used to the weather in Ghent.'",
             "options": ["Ik wen over het weer in Gent.",
                         "Ik wen aan het weer in Gent.",
                         "Ik wen met het weer in Gent.",
                         "Ik wen voor het weer in Gent."],
             "a": "Ik wen aan het weer in Gent.",
             "tip": "Wennen + AAN. Get used TO = wennen AAN."},
            {"type": "choice",
             "q": "Op de tramhalte: 'What are you waiting for?' (ding)",
             "options": ["Waarop wacht je?", "Waarvoor wacht je?",
                         "Op wat wacht je?", "Voor wie wacht je?"],
             "a": "Waarop wacht je?",
             "tip": "Wachten op + ding → waar+op = waarop. Niet waarvoor."},
            {"type": "choice",
             "q": "In de les: 'I'm interested in languages.'",
             "options": ["Ik interesseer me in talen.",
                         "Ik interesseer me voor talen.",
                         "Ik interesseer me aan talen.",
                         "Ik interesseer me over talen."],
             "a": "Ik interesseer me voor talen.",
             "tip": "Zich interesseren VOOR. Interested IN = interesseren VOOR."},
            {"type": "tf", "q": "'Ik luister de muziek' is correct.", "a": "Nee",
             "tip": "Luisteren heeft altijd NAAR nodig: Ik luister NAAR de muziek."},
            {"type": "tf", "q": "'Ik denk eraan' betekent 'I think about it (een ding)'.", "a": "Ja",
             "tip": "Er+aan = about it (ding). Correct!"},
            {"type": "tf", "q": "'Ik wacht voor de bus' is correct Nederlands.", "a": "Nee",
             "tip": "Wachten + OP, niet voor. Ik wacht OP de bus."},
            {"type": "translate", "q": "I'm searching for a room in Ghent.",
             "a": "Ik zoek naar een kamer in Gent.",
             "tip": "Zoeken + NAAR. Search for = zoeken naar."},
            {"type": "translate", "q": "She looks like her mother.",
             "a": "Zij lijkt op haar moeder.",
             "tip": "Lijken + OP. Look like = lijken op."},
            {"type": "reorder", "q": "van / ik / Belgisch / hou / bier",
             "a": "Ik hou van Belgisch bier.",
             "tip": "S + V + voorzetsel + object. Ik hou van …"},
            {"type": "reorder", "q": "wacht / op / je / waarop / ik / de / tram",
             "a": "Waarop wacht je? Ik wacht op de tram.",
             "tip": "Vraag: Waarop + V + S? Antwoord: S + V + op + object."},
        ],

        "jouw_beurt": "Schrijf 8 zinnen met vaste voorzetsels.\n\n"
                      "Gebruik minstens 6 verschillende werkwoord+voorzetsel combinaties:\n"
                      "• Ik denk aan … / Ik wacht op … / Ik hou van …\n"
                      "• Ik luister naar … / Ik begin met … / Ik zoek naar …\n\n"
                      "Schrijf ook 2 zinnen met er+voorzetsel:\n"
                      "• Hou je van kaas? — Ja, ik hou ervan.\n"
                      "• Denk je aan het examen? — Ja, ik denk eraan.\n\n"
                      "Bonus: Stel 2 vragen met waar+voorzetsel en beantwoord ze.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 20 — Vaste voorzetsels 2 (Fixed prepositions — adjectives & more)
    # ──────────────────────────────────────────────
    {
        "id": 20,
        "title": "Vaste voorzetsels – bijvoeglijk & meer",
        "chapter": "Hoofdstuk 7 – Voorzetsels",
        "book_page": "p. 129-135",
        "review": "In sessie 19 leerde je voorzetsels bij werkwoorden. Nu focussen we op voorzetsels "
                  "bij <b>bijvoeglijke naamwoorden</b> (adjectives) en nog meer werkwoord-combinaties. "
                  "We oefenen ook met <b>er+voorzetsel</b> en <b>waar+voorzetsel</b>.",

        "vocabulary": [
            {"nl": "tevreden over", "en": "satisfied with/about",
                "example": "Ik ben tevreden over mijn resultaat."},
            {"nl": "bang voor", "en": "afraid of",
                "example": "Zij is bang voor spinnen."},
            {"nl": "trots op", "en": "proud of",
                "example": "Ik ben trots op mijn diploma."},
            {"nl": "boos op", "en": "angry at",
                "example": "Hij is boos op zijn collega."},
            {"nl": "blij met", "en": "happy with",
                "example": "Ik ben blij met mijn nieuwe kamer."},
            {"nl": "verliefd op", "en": "in love with",
                "example": "Zij is verliefd op hem."},
            {"nl": "goed in", "en": "good at",
                "example": "Ik ben goed in wiskunde."},
            {"nl": "slecht in", "en": "bad at",
                "example": "Hij is slecht in koken."},
            {"nl": "gewend aan", "en": "used to",
                "example": "Ik ben gewend aan de regen."},
            {"nl": "benieuwd naar", "en": "curious about",
                "example": "Ik ben benieuwd naar het resultaat."},
            {"nl": "afhankelijk van", "en": "dependent on",
                "example": "Het is afhankelijk van het weer."},
            {"nl": "bekend met", "en": "familiar with",
                "example": "Ben je bekend met dit systeem?"},
        ],

        "grammar_title": "Vaste voorzetsels bij bijvoeglijke naamwoorden & verdieping",

        "grammar_html": """
<h4>1. Bijvoeglijk naamwoord + vast voorzetsel</h4>
<p>Just like verbs, many Dutch <b>adjectives</b> come with a fixed preposition. Again, they often differ from English!</p>

<table>
<tr><th>Voorzetsel</th><th>Bijv. naamwoord</th><th>English</th><th>Voorbeeld</th></tr>
<tr><td rowspan="3"><b>op</b></td><td>trots op</td><td>proud of</td><td>Ik ben trots op mijn werk.</td></tr>
<tr><td>boos op</td><td>angry at</td><td>Zij is boos op mij.</td></tr>
<tr><td>verliefd op</td><td>in love with</td><td>Hij is verliefd op haar.</td></tr>
<tr><td rowspan="2"><b>voor</b></td><td>bang voor</td><td>afraid of</td><td>Ik ben bang voor het examen.</td></tr>
<tr><td>klaar voor</td><td>ready for</td><td>Ben je klaar voor de les?</td></tr>
<tr><td rowspan="3"><b>met</b></td><td>blij met</td><td>happy with</td><td>Ik ben blij met dit cadeau.</td></tr>
<tr><td>bekend met</td><td>familiar with</td><td>Ik ben bekend met Gent.</td></tr>
<tr><td>tevreden met</td><td>satisfied with</td><td>Zij is tevreden met haar baan.</td></tr>
<tr><td rowspan="2"><b>over</b></td><td>tevreden over</td><td>satisfied about</td><td>Ik ben tevreden over het resultaat.</td></tr>
<tr><td>ongerust over</td><td>worried about</td><td>Ik ben ongerust over het examen.</td></tr>
<tr><td rowspan="2"><b>aan</b></td><td>gewend aan</td><td>used to</td><td>Ben je gewend aan het weer?</td></tr>
<tr><td>gehecht aan</td><td>attached to</td><td>Ik ben gehecht aan mijn stad.</td></tr>
<tr><td rowspan="2"><b>in</b></td><td>goed in</td><td>good at</td><td>Zij is goed in Nederlands.</td></tr>
<tr><td>geïnteresseerd in</td><td>interested in</td><td>Ik ben geïnteresseerd in talen.</td></tr>
<tr><td><b>naar</b></td><td>benieuwd naar</td><td>curious about</td><td>Ik ben benieuwd naar je verhaal.</td></tr>
<tr><td><b>van</b></td><td>afhankelijk van</td><td>dependent on</td><td>Het hangt af van jou.</td></tr>
</table>

<h4>2. Tevreden MET vs Tevreden OVER</h4>
<p>Both exist! Subtle difference:</p>
<ul>
<li><b>Tevreden met</b> = happy WITH (what you received): Ik ben tevreden met mijn cadeau.</li>
<li><b>Tevreden over</b> = satisfied ABOUT (a result/performance): Ik ben tevreden over je presentatie.</li>
</ul>

<h4>3. Er+voorzetsel bij bijvoeglijk naamwoorden (things)</h4>
<p>The same rule applies: for <b>things</b>, use er+voorzetsel:</p>
<table>
<tr><th>Met persoon</th><th>Met ding</th></tr>
<tr><td>Ik ben boos <b>op hem</b>.</td><td>Ik ben er<b>op</b> boos. (= op die situatie)</td></tr>
<tr><td>Ik ben blij <b>met haar</b>.</td><td>Ik ben er<b>mee</b> blij. (= met dat cadeau)</td></tr>
<tr><td>Ik ben bang <b>voor hem</b>.</td><td>Ik ben er<b>voor</b> bang. (= voor spinnen)</td></tr>
</table>
<p>⚠️ Word order note: er+voorzetsel can split from the adjective:<br>
Ik ben <b>er</b> niet <b>bang voor</b>. / Ik ben er niet bang voor.</p>

<h4>4. Waar+voorzetsel vragen</h4>
<ul>
<li><b>Waarop</b> ben je trots? → Op mijn diploma. / Ik ben er trots op.</li>
<li><b>Waarvoor</b> ben je bang? → Voor spinnen. / Ik ben er bang voor.</li>
<li><b>Waarmee</b> ben je blij? → Met mijn resultaat. / Ik ben ermee blij.</li>
<li><b>Waarover</b> ben je ongerust? → Over het examen.</li>
</ul>

<h4>5. Overzicht: werkwoord + bijv.nw. samen</h4>
<table>
<tr><th>Type</th><th>Voorbeeld</th><th>Er-vorm</th></tr>
<tr><td>Werkwoord + aan</td><td>Ik denk aan het examen.</td><td>Ik denk <b>eraan</b>.</td></tr>
<tr><td>Bijv.nw. + aan</td><td>Ik ben gewend aan de regen.</td><td>Ik ben <b>eraan</b> gewend.</td></tr>
<tr><td>Werkwoord + op</td><td>Ik wacht op de bus.</td><td>Ik wacht <b>erop</b>.</td></tr>
<tr><td>Bijv.nw. + op</td><td>Ik ben trots op mijn werk.</td><td>Ik ben er trots <b>op</b>.</td></tr>
</table>

<h4>🇮🇳 Tamil comparison</h4>
<p>Tamil also has fixed combinations: பயம் (payam, fear) + க்கு (kku) = afraid of.<br>
நான் சிலந்திக்கு <b>பயப்படுகிறேன்</b> = I am afraid of spiders.<br>
Dutch: Ik ben bang <b>voor</b> spinnen.<br>
Same concept: the "preposition" is fixed and must be memorized with the adjective/verb.</p>
""",

        "grammar_letop": [
            {"wrong": "Ik ben trots van mijn diploma.",
             "right": "Ik ben trots op mijn diploma.",
             "explain": "Trots + OP. English 'proud of' uses 'of', but Dutch uses 'op'. Not van!"},
            {"wrong": "Ik ben bang van spinnen.",
             "right": "Ik ben bang voor spinnen.",
             "explain": "Bang + VOOR. Afraid OF = bang VOOR. Not van!"},
            {"wrong": "Hij is goed met koken.",
             "right": "Hij is goed in koken.",
             "explain": "Goed + IN. Good AT = goed IN. Not met!"},
            {"wrong": "Ik ben trots erop.",
             "right": "Ik ben er trots op.",
             "explain": "With adjectives, er+voorzetsel often splits: er … trots op."},
            {"wrong": "Ik ben boos op het. (= angry about the situation)",
             "right": "Ik ben erop boos. / Ik ben er boos op.",
             "explain": "For things, use er+voorzetsel, not op het."},
        ],

        "grammar_extra": """
<h4>Combineer werkwoord- en bijv.nw.-voorzetsels</h4>
<table>
<tr><th>Type</th><th>Combinatie</th><th>Voorbeeld</th></tr>
<tr><td>verb + aan</td><td>denken aan</td><td>Ik denk aan Gent.</td></tr>
<tr><td>adj + aan</td><td>gewend aan</td><td>Ik ben gewend aan de trein.</td></tr>
<tr><td>verb + op</td><td>wachten op</td><td>Wacht op mij!</td></tr>
<tr><td>adj + op</td><td>trots op</td><td>Ik ben trots op je.</td></tr>
<tr><td>verb + van</td><td>houden van</td><td>Ik hou van chocolade.</td></tr>
<tr><td>adj + van</td><td>afhankelijk van</td><td>Het is afhankelijk van het budget.</td></tr>
<tr><td>verb + met</td><td>beginnen met</td><td>Ik begin met studeren.</td></tr>
<tr><td>adj + met</td><td>blij met</td><td>Ik ben blij met mijn kamer.</td></tr>
</table>

<p><b>Er+voorzetsel oefening:</b></p>
<ul>
<li>Ben je gewend aan de regen? → Ja, ik ben <b>eraan</b> gewend.</li>
<li>Ben je blij met je kamer? → Ja, ik ben <b>ermee</b> blij.</li>
<li>Ben je bang voor het examen? → Nee, ik ben er niet bang <b>voor</b>.</li>
<li>Ben je trots op je resultaat? → Ja, ik ben er trots <b>op</b>.</li>
<li>Ben je benieuwd naar het antwoord? → Ja, ik ben <b>ernaar</b> benieuwd.</li>
</ul>
""",

        "grammar_quick": [
            "Bijvoeglijke naamwoorden hebben ook vaste voorzetsels: trots OP, bang VOOR, blij MET.",
            "Goed/slecht + IN. Gewend + AAN. Benieuwd + NAAR. Afhankelijk + VAN.",
            "Tevreden met (what you got) vs tevreden over (a result/performance).",
            "Ding → er+voorzetsel: Ik ben er trots op. Persoon → voorzetsel + pronoun.",
            "Vraag: Waar+voorzetsel? Waarop ben je trots? Waarvoor ben je bang?",
            "Let op: English prepositions ≠ Dutch! proud OF = trots OP, afraid OF = bang VOOR.",
        ],

        "exercises": [
            {"type": "fill", "q": "Na je diploma: Ik ben trots ___ mijn diploma.", "a": "op",
             "tip": "Trots + OP. Proud of = trots op."},
            {"type": "fill", "q": "In de dierentuin: Zij is bang ___ de hond.", "a": "voor",
             "tip": "Bang + VOOR. Afraid of = bang voor."},
            {"type": "fill", "q": "Nieuwe baan: Ben je blij ___ je nieuwe baan?", "a": "met",
             "tip": "Blij + MET. Happy with = blij met."},
            {"type": "fill", "q": "Op school: Hij is goed ___ wiskunde.", "a": "in",
             "tip": "Goed + IN. Good at = goed in."},
            {"type": "fill", "q": "Over het weer: Ik ben ___ gewend. (= used to the rain)", "a": "eraan",
             "tip": "Gewend aan + ding → eraan gewend. Er+voorzetsel voor dingen."},
            {"type": "choice",
             "q": "Op het werk: 'I am curious about the result.'",
             "options": ["Ik ben benieuwd over het resultaat.",
                         "Ik ben benieuwd naar het resultaat.",
                         "Ik ben benieuwd voor het resultaat.",
                         "Ik ben benieuwd aan het resultaat."],
             "a": "Ik ben benieuwd naar het resultaat.",
             "tip": "Benieuwd + NAAR. Curious about = benieuwd naar."},
            {"type": "choice",
             "q": "Op het examen: 'What are you proud of?' (een ding)",
             "options": ["Waarop ben je trots?", "Waarvan ben je trots?",
                         "Waarover ben je trots?", "Waarmee ben je trots?"],
             "a": "Waarop ben je trots?",
             "tip": "Trots op → waar+op = waarop. Voor dingen, gebruik waar+voorzetsel."},
            {"type": "choice",
             "q": "Over je ouders: 'She is dependent on her parents.'",
             "options": ["Zij is afhankelijk op haar ouders.",
                         "Zij is afhankelijk van haar ouders.",
                         "Zij is afhankelijk aan haar ouders.",
                         "Zij is afhankelijk voor haar ouders."],
             "a": "Zij is afhankelijk van haar ouders.",
             "tip": "Afhankelijk + VAN. Dependent on = afhankelijk van."},
            {"type": "tf", "q": "'Ik ben bang van spinnen' is correct.", "a": "Nee",
             "tip": "Bang + VOOR, niet van! Ik ben bang VOOR spinnen."},
            {"type": "tf", "q": "'Ik ben ermee blij' betekent 'I am happy with it'.", "a": "Ja",
             "tip": "Blij met + ding → ermee blij. Correct!"},
            {"type": "tf", "q": "'Ik ben goed met koken' is correct.", "a": "Nee",
             "tip": "Goed + IN, niet met! Ik ben goed IN koken."},
            {"type": "translate", "q": "I am used to the weather in Belgium.",
             "a": "Ik ben gewend aan het weer in België.",
             "tip": "Gewend + AAN. Used to = gewend aan."},
            {"type": "translate", "q": "Are you afraid of the exam?",
             "a": "Ben je bang voor het examen?",
             "tip": "Bang + VOOR. Vraag: inversie (Ben je)."},
            {"type": "reorder", "q": "trots / mijn / op / ben / ik / resultaat",
             "a": "Ik ben trots op mijn resultaat.",
             "tip": "S + V + adj + voorzetsel + object. Ik ben trots op …"},
            {"type": "reorder", "q": "bang / ben / ervoor / niet / ik",
             "a": "Ik ben er niet bang voor.",
             "tip": "Er splitst: Ik ben er niet bang voor. Ontkenning tussen er en de rest."},
        ],

        "jouw_beurt": "Beschrijf jezelf met vaste voorzetsels.\n\n"
                      "Schrijf minstens 8 zinnen:\n"
                      "• Ik ben trots op …\n"
                      "• Ik ben bang voor …\n"
                      "• Ik ben blij met …\n"
                      "• Ik ben goed in …\n"
                      "• Ik ben gewend aan …\n"
                      "• Ik ben benieuwd naar …\n\n"
                      "Gebruik ook 2 zinnen met er+voorzetsel:\n"
                      "• Ben je bang voor het examen? — Nee, ik ben er niet bang voor.\n"
                      "• Ben je blij met je kamer? — Ja, ik ben ermee blij.\n\n"
                      "Bonus: Interview een collega (schrijf 4 vragen met waar+voorzetsel).",
    },

    # ──────────────────────────────────────────────
    #  SESSION 21 — Uiterlijk beschrijven (Describing appearance)
    # ──────────────────────────────────────────────
    {
        "id": 21,
        "title": "Uiterlijk beschrijven",
        "chapter": "Hoofdstuk 8 – Examenvoorbereiding",
        "book_page": "p. 136-142",
        "review": "Op het NT2-examen (Spreken & Schrijven) moet je vaak iemands <b>uiterlijk</b> "
                  "(appearance) beschrijven. In deze sessie leer je alle woorden en structuren die "
                  "je nodig hebt: lengte, haar, ogen, lichaamsbouw, kleding en bijzonderheden.",

        "vocabulary": [
            {"nl": "het uiterlijk", "en": "the appearance",
                "example": "Beschrijf het uiterlijk van deze persoon."},
            {"nl": "de lengte", "en": "the height",
                "example": "Ik ben 1 meter 65. / Zij is klein."},
            {"nl": "de huidskleur", "en": "the skin colour",
                "example": "Ik heb een donkere huid."},
            {"nl": "het haar", "en": "the hair",
                "example": "Zij heeft halflang blond haar."},
            {"nl": "de ogen", "en": "the eyes",
                "example": "Hij heeft groene ogen."},
            {"nl": "de lichaamsbouw", "en": "the build",
                "example": "Zij is slank, gespierd of mollig."},
            {"nl": "de baard / de snor", "en": "the beard / the moustache",
                "example": "Hij heeft een volle baard en een snor."},
            {"nl": "de bril", "en": "the glasses",
                "example": "Ik draag een bril. / Hij draagt lenzen."},
            {"nl": "de lippen", "en": "the lips",
                "example": "Ik heb smalle lippen. / Zij heeft volle lippen."},
            {"nl": "het gezicht", "en": "the face",
                "example": "Mijn gezicht is ovaal. / Zij heeft een rond gezicht."},
            {"nl": "de neus", "en": "the nose",
                "example": "Mijn neus is recht. / Hij heeft een kromme neus."},
            {"nl": "de rimpels", "en": "the wrinkles",
                "example": "Ik heb rimpels op mijn voorhoofd."},
            {"nl": "de sproeten", "en": "the freckles",
                "example": "Hij heeft sproeten op zijn wangen."},
            {"nl": "de moedervlek", "en": "the mole / birthmark",
                "example": "Ik heb een moedervlek op mijn wang."},
            {"nl": "de tatoeage", "en": "the tattoo",
                "example": "Hij heeft een kleine tatoeage op zijn arm."},
            {"nl": "de oorbellen", "en": "the earrings",
                "example": "Zij draagt oorbellen. / Hij draagt grote oorringen."},
            {"nl": "de hoofddoek", "en": "the headscarf",
                "example": "Zij draagt een hoofddoek."},
            {"nl": "de pet / de muts", "en": "the cap / the beanie",
                "example": "Zij draagt een pet. / Hij draagt een muts."},
            {"nl": "slank", "en": "slim / slender", "example": "Zij is slank."},
            {"nl": "mollig", "en": "chubby / plump",
                "example": "Het kind is een beetje mollig."},
        ],

        "grammar_title": "Uiterlijk beschrijven — structuren & woordenschat",

        "grammar_html": """
<h4>1. De basisstructuren (Basic structures)</h4>
<p>There are three main patterns for describing appearance:</p>
<div class="formula-card">
<b>Pattern 1: zijn + bijvoeglijk naamwoord</b><br>
Ik <b>ben</b> lang / klein / slank / mollig / gespierd.<br><br>
<b>Pattern 2: hebben + zelfstandig naamwoord</b><br>
Ik <b>heb</b> bruine ogen / lang haar / een baard.<br><br>
<b>Pattern 3: dragen + accessoire</b><br>
Ik <b>draag</b> een bril / oorbellen / een hoofddoek.
</div>

<h4>2. Volledig overzicht per kenmerk</h4>
<table>
<tr><th>Kenmerk</th><th>Over jezelf (ik)</th><th>Over iemand anders</th></tr>
<tr><td><b>Lengte</b></td><td>Ik ben 1 meter 75. / Ik ben lang.</td><td>Zij is klein. / Hij is groot.</td></tr>
<tr><td><b>Huidskleur</b></td><td>Ik heb een donkere huid.</td><td>Zij heeft een lichte huid.</td></tr>
<tr><td><b>Ogen</b></td><td>Ik heb bruine ogen.</td><td>Hij heeft blauwe/groene ogen.</td></tr>
<tr><td><b>Haar</b></td><td>Ik heb kort zwart haar.</td><td>Zij heeft halflang blond haar.</td></tr>
<tr><td><b>Lichaamsbouw</b></td><td>Ik ben normaal gebouwd.</td><td>Zij is slank/gespierd/mollig.</td></tr>
<tr><td><b>Baard/Snor</b></td><td>Ik heb een stoppelbaard.</td><td>Hij heeft een volle baard en een snor.</td></tr>
<tr><td><b>Bril</b></td><td>Ik draag geen bril.</td><td>Zij draagt een bril. / Hij draagt lenzen.</td></tr>
<tr><td><b>Gezicht</b></td><td>Mijn gezicht is ovaal.</td><td>Zij heeft een rond/lang gezicht.</td></tr>
<tr><td><b>Neus</b></td><td>Mijn neus is recht.</td><td>Hij heeft een kleine/kromme neus.</td></tr>
<tr><td><b>Lippen</b></td><td>Ik heb smalle lippen.</td><td>Zij heeft volle lippen.</td></tr>
<tr><td><b>Rimpels</b></td><td>Ik heb rimpels op mijn voorhoofd.</td><td>Zij heeft geen rimpels. / Hij heeft rimpels rond zijn ogen.</td></tr>
<tr><td><b>Oorbellen</b></td><td>Ik draag geen oorbellen.</td><td>Zij draagt oorbellen. / Hij draagt grote oorringen.</td></tr>
<tr><td><b>Hoofddoek/Pet</b></td><td>Ik draag geen hoofddoek.</td><td>Zij draagt een hoofddoek. / Hij draagt een pet/muts.</td></tr>
<tr><td><b>Tatoeages</b></td><td>Ik heb geen tatoeages.</td><td>Zij heeft veel tatoeages. / Hij heeft een kleine tatoeage op zijn arm.</td></tr>
<tr><td><b>Neuspiercing</b></td><td>Ik heb geen neuspiercing.</td><td>Zij heeft een neuspiercing. / Hij heeft een ringetje in zijn neus.</td></tr>
<tr><td><b>Vlekken</b></td><td>Ik heb geen vlekken op mijn gezicht.</td><td>Zij heeft sproeten op haar wangen. / Hij heeft vlekken op zijn voorhoofd.</td></tr>
<tr><td><b>Moedervlek</b></td><td>Ik heb een moedervlek op mijn wang.</td><td>Zij heeft een moedervlek bij haar oog. / Hij heeft meerdere moedervlekken.</td></tr>
</table>

<h4>3. Haarkleur & haarstijl</h4>
<table>
<tr><th>Kleur</th><th>Stijl</th><th>Lengte</th></tr>
<tr><td>blond</td><td>steil (straight)</td><td>kort</td></tr>
<tr><td>bruin</td><td>krullend (curly)</td><td>halflang</td></tr>
<tr><td>zwart</td><td>golvend (wavy)</td><td>lang</td></tr>
<tr><td>rood</td><td>kroeshaar (frizzy/afro)</td><td>geschoren (shaved)</td></tr>
<tr><td>grijs</td><td>staart (ponytail)</td><td>kaal (bald)</td></tr>
</table>
<p><b>Formule:</b> Ik heb <b>[lengte] [kleur] [stijl]</b> haar.<br>
→ Ik heb <b>lang bruin krullend</b> haar.</p>

<h4>4. Adjectiefvolgorde (Adjective order)</h4>
<p>When stacking adjectives before a noun, Dutch follows: <b>size → colour → style → noun</b>:</p>
<ul>
<li>een <b>lang blond</b> meisje</li>
<li><b>kort zwart krullend</b> haar</li>
<li>een <b>kleine kromme</b> neus</li>
</ul>

<h4>5. Vergelijken (Comparing people — revisie sessie 9)</h4>
<p>You can combine appearance vocabulary with comparatives:</p>
<ul>
<li>Zij is <b>langer dan</b> hij.</li>
<li>Hij heeft <b>donkerder</b> haar dan ik.</li>
<li>Zij is <b>het slankst</b> van de groep.</li>
</ul>

<h4>🇮🇳 Tamil comparison</h4>
<p>Tamil describes appearance similarly: நான் உயரமாக இருக்கிறேன் (I am tall), en: என் கண்கள் கருப்பு (my eyes are black/dark).<br>
The structure is the same: "I am + adj" or "I have + noun". Dutch is very similar here!</p>
""",

        "grammar_letop": [
            {"wrong": "Ik ben bruine ogen.",
             "right": "Ik heb bruine ogen.",
             "explain": "For body parts you OWN, use HEBBEN, not zijn. Ik HEB … ogen/haar/een baard."},
            {"wrong": "Zij heeft lang.",
             "right": "Zij is lang.",
             "explain": "For qualities/characteristics, use ZIJN. Zij IS lang/klein/slank."},
            {"wrong": "Ik heb een lang blond haar.",
             "right": "Ik heb lang blond haar.",
             "explain": "Haar (hair) is uncountable → no een! Just: Ik heb lang blond haar."},
            {"wrong": "Hij heeft bruin ogen.",
             "right": "Hij heeft bruine ogen.",
             "explain": "Ogen is plural → adjective gets -e: bruinE ogen, groenE ogen, blauwE ogen."},
            {"wrong": "Zij draagt een baard.",
             "right": "Zij heeft een baard. / Hij heeft een baard.",
             "explain": "Dragen = wear (for accessories: bril, oorbellen). Hebben = have (for facial hair)."},
        ],

        "grammar_extra": """
<h4>Beschrijf deze mensen</h4>
<p>Oefen met complete beschrijvingen:</p>

<p><b>Persoon A (vrouw, 30):</b></p>
<ul>
<li>Zij is lang en slank.</li>
<li>Zij heeft halflang bruin krullend haar.</li>
<li>Zij heeft groene ogen.</li>
<li>Zij draagt een bril.</li>
<li>Zij heeft sproeten op haar wangen.</li>
<li>Zij draagt oorbellen.</li>
</ul>

<p><b>Persoon B (man, 45):</b></p>
<ul>
<li>Hij is normaal gebouwd en niet zo lang.</li>
<li>Hij heeft kort grijs haar.</li>
<li>Hij heeft bruine ogen en een volle baard.</li>
<li>Hij heeft rimpels rond zijn ogen.</li>
<li>Hij draagt geen bril.</li>
<li>Hij heeft een tatoeage op zijn arm.</li>
</ul>

<p><b>Nuttige zinnen voor het examen:</b></p>
<ul>
<li>Op de foto zie ik een man/vrouw van ongeveer … jaar.</li>
<li>Hij/Zij ziet er … uit. (He/She looks …)</li>
<li>Wat opvalt is … (What stands out is …)</li>
<li>Hij/Zij lijkt op … (He/She looks like …)</li>
</ul>
""",

        "grammar_quick": [
            "ZIJN + eigenschap: Ik ben lang/klein/slank/gespierd/mollig.",
            "HEBBEN + lichaamsdeel: Ik heb bruine ogen / lang haar / een baard.",
            "DRAGEN + accessoire: Ik draag een bril / oorbellen / een hoofddoek.",
            "Haar: [lengte] + [kleur] + [stijl] + haar → kort zwart krullend haar.",
            "Adjectief+e voor de-woorden & plurals: bruinE ogen, langE vrouw.",
            "Haar = uncountable → geen 'een': Ik heb lang blond haar (NOT een lang blond haar).",
        ],

        "exercises": [
            {"type": "fill", "q": "Scenario: je beschrijft een foto op het examen. — Op de foto zie ik een vrouw. Zij ___ bruine ogen en lang haar. (have)", "a": "heeft",
             "tip": "Body parts you own → HEBBEN. Zij HEEFT ogen/haar/een neus."},
            {"type": "fill", "q": "Je beschrijft je buurman. — Mijn buurman ___ lang en gespierd. (is)", "a": "is",
             "tip": "Characteristics/build → ZIJN. Hij IS lang/klein/slank/gespierd."},
            {"type": "fill", "q": "Hij heeft kort ___ haar en een stoppelbaard. (black)", "a": "zwart",
             "tip": "Haar = het-word, uncountable, no article → adjective gets no -e: zwart haar."},
            {"type": "fill", "q": "Mijn zus heeft ___ ogen en volle lippen. (blue, plural)", "a": "blauwe",
             "tip": "Plural noun → adjective gets -e: blauwE ogen, vollE lippen."},
            {"type": "fill", "q": "Op de foto ___ de vrouw een hoofddoek en oorbellen. (wear)", "a": "draagt",
             "tip": "Accessories (bril, oorbellen, hoofddoek) → DRAGEN. Zij DRAAGT."},
            {"type": "choice",
             "q": "Scenario: je beschrijft een collega. Which is correct?",
             "options": ["Zij heb lang bruin krullend haar.",
                         "Zij heeft lang bruin krullend haar.",
                         "Zij heeft lang bruine krullende haar.",
                         "Zij heeft een lang bruin krullend haar."],
             "a": "Zij heeft lang bruin krullend haar.",
             "tip": "Haar is uncountable (no een) + het-word without article → no -e. HEBBEN for body parts."},
            {"type": "choice",
             "q": "'He wears a cap and has a small tattoo on his arm.'",
             "options": ["Hij is een pet en heeft een kleine tatoeage op zijn arm.",
                         "Hij draagt een pet en is een kleine tatoeage op zijn arm.",
                         "Hij draagt een pet en heeft een kleine tatoeage op zijn arm.",
                         "Hij heeft een pet en draagt een kleine tatoeage op zijn arm."],
             "a": "Hij draagt een pet en heeft een kleine tatoeage op zijn arm.",
             "tip": "DRAGEN for accessories (pet). HEBBEN for physical marks (tatoeage). Not zijn!"},
            {"type": "choice",
             "q": "Which adjective order is correct for describing someone's hair?",
             "options": ["krullend lang bruin haar",
                         "lang bruin krullend haar",
                         "bruin lang krullend haar",
                         "lang krullend bruin haar"],
             "a": "lang bruin krullend haar",
             "tip": "Order: length → colour → style → noun. Lang bruin krullend haar."},
            {"type": "tf", "q": "'Zij draagt sproeten op haar wangen' is correct Dutch.", "a": "Nee",
             "tip": "Physical features (sproeten, moedervlek, rimpels) → HEBBEN. Dragen = only for accessories you put ON."},
            {"type": "tf", "q": "'Mijn gezicht is ovaal en mijn neus is recht' is correct.", "a": "Ja",
             "tip": "Shape/form of face or nose → ZIJN. Mijn gezicht IS ovaal. Correct!"},
            {"type": "tf", "q": "'Zij heeft een lang blond haar en bruine ogen' is correct.", "a": "Nee",
             "tip": "Haar is uncountable → no 'een'! Correct: Zij heeft lang blond haar."},
            {"type": "translate", "q": "She is tall and slim. She has green eyes and freckles on her cheeks.",
             "a": "Zij is lang en slank. Zij heeft groene ogen en sproeten op haar wangen.",
             "tip": "ZIJN for build. HEBBEN for body parts. Groene (plural → -e)."},
            {"type": "translate", "q": "He wears glasses and earrings. He has a round face and full lips.",
             "a": "Hij draagt een bril en oorbellen. Hij heeft een rond gezicht en volle lippen.",
             "tip": "DRAGEN for accessories. HEBBEN for features. Rond gezicht (het gezicht, no article in predicate → no -e)."},
            {"type": "reorder", "q": "kort / heeft / zwart / zij / haar / steil / en / een / neuspiercing",
             "a": "Zij heeft kort zwart steil haar en een neuspiercing.",
             "tip": "S + V + [length][colour][style] + haar + en + feature."},
            {"type": "reorder", "q": "bril / een / draagt / hij / en / heeft / baard / volle / een",
             "a": "Hij draagt een bril en heeft een volle baard.",
             "tip": "DRAGEN for bril (accessory), HEBBEN for baard (facial hair). Volle baard (de baard → -e)."},
        ],

        "jouw_beurt": "Beschrijf het uiterlijk van 3 mensen.\n\n"
                      "1. <b>Jezelf:</b> Schrijf minstens 6 zinnen over je eigen uiterlijk.\n"
                      "   → Ik ben … / Ik heb … / Ik draag …\n\n"
                      "2. <b>Een vriend(in) of collega:</b> Schrijf 5 zinnen.\n"
                      "   → Hij/Zij is … / Hij/Zij heeft … / Hij/Zij draagt …\n\n"
                      "3. <b>Een bekend persoon:</b> Beschrijf een BN'er of filmster (5 zinnen).\n"
                      "   → Op de foto zie ik een man/vrouw van ongeveer … jaar.\n\n"
                      "Gebruik: lengte, haar (kleur+lengte+stijl), ogen, lichaamsbouw, "
                      "bijzonderheden (baard, bril, tatoeage, sproeten).",
    },

    # ──────────────────────────────────────────────
    #  SESSION 22 — Waarom Nederlands? (Why Dutch? — Exam topic)
    # ──────────────────────────────────────────────
    {
        "id": 22,
        "title": "Waarom Nederlands?",
        "chapter": "Hoofdstuk 8 – Examenvoorbereiding",
        "book_page": "p. 143-150",
        "review": "Op het NT2-examen wordt vaak gevraagd: <b>Waarom leer je Nederlands?</b> "
                  "In deze sessie leer je hoe je je <b>motivatie</b> uitlegt, over je "
                  "<b>ervaringen</b> met Nederlands vertelt, en je <b>toekomstplannen</b> "
                  "beschrijft. We combineren veel grammatica uit eerdere sessies!",

        "vocabulary": [
            {"nl": "de motivatie", "en": "the motivation",
                "example": "Mijn motivatie is integratie."},
            {"nl": "de reden", "en": "the reason",
                "example": "De reden is dat ik in Gent woon."},
            {"nl": "integreren", "en": "to integrate",
                "example": "Ik wil integreren in de Belgische samenleving."},
            {"nl": "de samenleving", "en": "the society",
                "example": "De Belgische samenleving is meertalig."},
            {"nl": "de inburgering", "en": "the civic integration",
                "example": "Ik volg een inburgeringscursus."},
            {"nl": "het dagelijks leven", "en": "daily life",
                "example": "In het dagelijks leven spreek je Nederlands."},
            {"nl": "de ervaring", "en": "the experience",
                "example": "Mijn ervaring met Nederlands is positief."},
            {"nl": "de uitdaging", "en": "the challenge",
                "example": "De uitspraak is een uitdaging."},
            {"nl": "het doel", "en": "the goal",
                "example": "Mijn doel is B2-niveau."},
            {"nl": "verbeteren", "en": "to improve",
                "example": "Ik wil mijn Nederlands verbeteren."},
            {"nl": "de cursus", "en": "the course",
                "example": "Ik volg een cursus Nederlands bij UGent."},
            {"nl": "meertalig", "en": "multilingual",
                "example": "België is een meertalig land."},
        ],

        "grammar_title": "Motivatie uitleggen — alle grammatica combineren",

        "grammar_html": """
<h4>1. Redenen geven (Giving reasons — revisie)</h4>
<p>Use connectors from session 6 and 14:</p>
<table>
<tr><th>Connector</th><th>Type</th><th>Woordvolgorde</th><th>Voorbeeld</th></tr>
<tr><td><b>omdat</b></td><td>subordinating</td><td>S … V-einde</td><td>Ik leer Nederlands <b>omdat</b> ik in Gent <b>woon</b>.</td></tr>
<tr><td><b>want</b></td><td>coordinating</td><td>S + V + …</td><td>Ik leer Nederlands, <b>want</b> ik <b>woon</b> in Gent.</td></tr>
<tr><td><b>daarom</b></td><td>linking adverb</td><td>V + S (inversie)</td><td>Ik woon in Gent. <b>Daarom</b> <b>leer</b> ik Nederlands.</td></tr>
</table>

<h4>2. Wensen & plannen (Wishes & plans)</h4>
<p>Use <b>willen</b>, <b>hopen</b>, <b>gaan</b> + infinitief:</p>
<div class="formula-card">
<b>Ik wil</b> mijn Nederlands verbeteren.<br>
<b>Ik hoop</b> het B2-examen te halen.<br>
<b>Ik ga</b> een cursus volgen bij UGent.<br>
<b>Ik zou graag</b> vloeiend Nederlands spreken. (conditional)
</div>

<h4>3. Ervaringen vertellen (Talking about experiences)</h4>
<p>Use perfectum (session 11) and imperfectum (session 4):</p>
<ul>
<li>Ik <b>ben begonnen</b> met Nederlands in 2024. (perfectum)</li>
<li>In het begin <b>was</b> het heel moeilijk. (imperfectum)</li>
<li>Nu <b>kan</b> ik al een gesprek voeren. (present)</li>
<li>Vroeger <b>sprak</b> ik alleen Engels op het werk. (imperfectum)</li>
</ul>

<h4>4. Vergelijken: toen vs nu (Then vs now)</h4>
<table>
<tr><th>Toen (vroeger)</th><th>Nu</th></tr>
<tr><td>Ik <b>kon</b> geen Nederlands spreken.</td><td>Ik <b>kan</b> al een gesprek voeren.</td></tr>
<tr><td>Ik <b>begreep</b> niets.</td><td>Ik <b>begrijp</b> veel meer.</td></tr>
<tr><td>Ik <b>sprak</b> alleen Engels.</td><td>Ik <b>spreek</b> ook Nederlands.</td></tr>
<tr><td>Het <b>was</b> heel moeilijk.</td><td>Het <b>is</b> makkelijker geworden.</td></tr>
</table>

<h4>5. Examenvragen & modelantwoorden</h4>
<p>Typical exam questions and how to answer:</p>

<p><b>Q: Waarom leer je Nederlands?</b></p>
<p>→ Ik leer Nederlands omdat ik in Gent woon en werk. Ik wil integreren in de Belgische samenleving. 
Daarom volg ik een cursus bij UGent. In het dagelijks leven heb ik Nederlands nodig: bij de dokter, 
op het gemeentehuis, en met mijn collega's.</p>

<p><b>Q: Wat vind je moeilijk aan Nederlands?</b></p>
<p>→ De uitspraak vind ik het moeilijkst, vooral de 'g' en de 'ui'. Ook de woordvolgorde is een 
uitdaging, omdat het werkwoord soms naar het einde moet. Maar ik word elke dag beter!</p>

<p><b>Q: Wat zijn je plannen?</b></p>
<p>→ Ik ga het B2-examen doen. Daarna wil ik misschien een Nederlandstalige opleiding volgen. 
Ik hoop dat ik vloeiend Nederlands kan spreken over een paar jaar.</p>

<h4>6. Nuttige uitdrukkingen</h4>
<ul>
<li>Aan de ene kant … aan de andere kant … (on the one hand … on the other …)</li>
<li>Niet alleen … maar ook … (not only … but also …)</li>
<li>Hoe meer ik oefen, hoe beter het gaat. (the more I practice, the better it goes)</li>
<li>Stap voor stap maak ik vooruitgang. (step by step I make progress)</li>
</ul>

<h4>🇮🇳 Tamil comparison</h4>
<p>This session is about expressing yourself — your situation as a Tamil speaker in Ghent.<br>
Compare: நான் ஹெண்ட்-ல வசிக்கிறேன், அதனால நெதர்லாந்து மொழி படிக்கிறேன்.<br>
= Ik woon in Gent, daarom leer ik Nederlands.<br>
The structure is similar — reason + consequence. Use this session to tell YOUR story!</p>
""",

        "grammar_letop": [
            {"wrong": "Ik leer Nederlands omdat ik woon in Gent.",
             "right": "Ik leer Nederlands omdat ik in Gent woon.",
             "explain": "Omdat = bijzin → verb to the END. Omdat ik in Gent WOON."},
            {"wrong": "Ik leer Nederlands want ik in Gent woon.",
             "right": "Ik leer Nederlands, want ik woon in Gent.",
             "explain": "Want = coordinating → normal word order (S+V). Want ik WOON in Gent."},
            {"wrong": "Daarom ik leer Nederlands.",
             "right": "Daarom leer ik Nederlands.",
             "explain": "Daarom = linking adverb → inversie! Daarom LEER IK Nederlands."},
            {"wrong": "Ik hoop te het examen halen.",
             "right": "Ik hoop het examen te halen.",
             "explain": "Te comes before the infinitive: te halen. Object (het examen) before te."},
            {"wrong": "In het begin het was moeilijk.",
             "right": "In het begin was het moeilijk.",
             "explain": "Time/place at start → inversie: was het (V-S), not het was."},
        ],

        "grammar_extra": """
<h4>Jouw verhaal — bouwstenen (Building blocks for YOUR story)</h4>

<p><b>Introductie:</b></p>
<ul>
<li>Ik heet … en ik kom uit Tamil Nadu, India.</li>
<li>Ik woon sinds … in Gent.</li>
<li>Ik werk als onderzoeker aan UGent.</li>
</ul>

<p><b>Motivatie:</b></p>
<ul>
<li>Ik leer Nederlands omdat ik in Vlaanderen woon.</li>
<li>Ik wil integreren in de Belgische samenleving.</li>
<li>In het dagelijks leven heb ik Nederlands nodig.</li>
<li>Ik wil mijn collega's beter begrijpen.</li>
</ul>

<p><b>Ervaringen:</b></p>
<ul>
<li>In het begin was het heel moeilijk.</li>
<li>De uitspraak vond ik het moeilijkst.</li>
<li>Nu kan ik al een gesprek voeren bij de bakker.</li>
<li>Ik heb al veel geleerd in de B1-cursus.</li>
</ul>

<p><b>Moeilijkheden:</b></p>
<ul>
<li>De woordvolgorde is soms verwarrend.</li>
<li>Er zijn veel uitzonderingen.</li>
<li>De 'g' en de 'ui' zijn moeilijk uit te spreken.</li>
</ul>

<p><b>Toekomst:</b></p>
<ul>
<li>Ik wil het B2-examen halen.</li>
<li>Ik hoop vloeiend Nederlands te spreken.</li>
<li>Ik ga meer Nederlandse boeken lezen.</li>
</ul>
""",

        "grammar_quick": [
            "Omdat + S … V-einde: omdat ik in Gent woon.",
            "Want + S V …: want ik woon in Gent. (normal order)",
            "Daarom + V S: Daarom leer ik Nederlands. (inversie!)",
            "Plannen: Ik wil/ga/hoop + infinitief. Ik zou graag … (conditional).",
            "Ervaringen: perfectum (ik ben begonnen) + imperfectum (het was moeilijk).",
            "Vergelijk toen/nu: Vroeger kon ik niet … Nu kan ik al …",
        ],

        "exercises": [
            {"type": "fill", "q": "Aan je docent: Ik leer Nederlands ___ ik in Gent woon. (because — bijzin)", "a": "omdat",
             "tip": "Because + werkwoord-einde = omdat. Want heeft normale woordvolgorde."},
            {"type": "fill", "q": "Aan een vriend: Ik woon in Gent. ___ leer ik Nederlands.", "a": "Daarom",
             "tip": "Therefore = daarom. Daarna inversie: daarom LEER IK."},
            {"type": "fill", "q": "In de les: Ik ___ mijn Nederlands verbeteren. (want to)", "a": "wil",
             "tip": "Willen + infinitief. Ik WIL verbeteren."},
            {"type": "fill", "q": "Over je eerste jaar: In het begin ___ het heel moeilijk. (was — past)", "a": "was",
             "tip": "Imperfectum van zijn: was. In het begin was het moeilijk."},
            {"type": "fill", "q": "Over het examen: Ik hoop het examen te ___. (pass/achieve)", "a": "halen",
             "tip": "Een examen halen = slagen. Hopen + te + infinitief."},
            {"type": "choice",
             "q": "In een e-mail aan CVO: Welke zin heeft de juiste woordvolgorde?",
             "options": ["Ik leer Nederlands omdat ik woon in Gent.",
                         "Ik leer Nederlands omdat ik in Gent woon.",
                         "Ik leer Nederlands omdat in Gent ik woon.",
                         "Ik leer Nederlands omdat woon ik in Gent."],
             "a": "Ik leer Nederlands omdat ik in Gent woon.",
             "tip": "Omdat = bijzin → werkwoord op het EINDE: omdat ik in Gent WOON."},
            {"type": "choice",
             "q": "Op het examen: 'Daarom ___ Nederlands.' Vul in.",
             "options": ["ik leer", "leer ik", "ik leer ik", "leren ik"],
             "a": "leer ik",
             "tip": "Daarom = bijwoord → inversie: V + S. Daarom LEER IK."},
            {"type": "choice",
             "q": "In een motivatiebrief: Welke zin is correct?",
             "options": ["Ik hoop te het examen halen.",
                         "Ik hoop het examen te halen.",
                         "Ik hoop het examen halen te.",
                         "Ik hoop te halen het examen."],
             "a": "Ik hoop het examen te halen.",
             "tip": "Object vóór te + infinitief: het examen TE HALEN."},
            {"type": "tf", "q": "'Daarom ik leer Nederlands' heeft de juiste woordvolgorde.", "a": "Nee",
             "tip": "Daarom → inversie: Daarom LEER IK (V-S), niet ik leer (S-V)."},
            {"type": "tf", "q": "'Ik ben begonnen met Nederlands in 2024' gebruikt het perfectum correct.", "a": "Ja",
             "tip": "Beginnen gebruikt ZIJN: Ik ben begonnen. Correct!"},
            {"type": "tf", "q": "'Ik wil dat mijn Nederlands verbeteren' is correct.", "a": "Nee",
             "tip": "Willen + infinitief direct: Ik wil mijn Nederlands verbeteren. Geen 'dat' nodig."},
            {"type": "translate", "q": "I learn Dutch because I work in Ghent.",
             "a": "Ik leer Nederlands omdat ik in Gent werk.",
             "tip": "Omdat = bijzin → werkwoord-einde: omdat ik in Gent WERK."},
            {"type": "translate", "q": "In the beginning it was very difficult.",
             "a": "In het begin was het heel moeilijk.",
             "tip": "Tijdsbepaling vooraan → inversie: was het (V-S)."},
            {"type": "reorder", "q": "Nederlands / omdat / leer / woon / ik / ik / Gent / in",
             "a": "Ik leer Nederlands omdat ik in Gent woon.",
             "tip": "Hoofdzin: Ik leer Nederlands + omdat-bijzin: ik in Gent woon (V-einde)."},
            {"type": "reorder", "q": "hoop / het / ik / te / examen / halen",
             "a": "Ik hoop het examen te halen.",
             "tip": "Ik hoop + object + te + infinitief: het examen te halen."},
        ],

        "jouw_beurt": "Schrijf je eigen 'Waarom Nederlands?' verhaal (minstens 12 zinnen).\n\n"
                      "Structuur:\n"
                      "1. <b>Introductie</b> (3 zinnen): Wie ben je? Waar kom je vandaan? Waar woon je?\n"
                      "   → Ik heet … Ik kom uit … Ik woon in Gent sinds …\n\n"
                      "2. <b>Motivatie</b> (3 zinnen): Waarom leer je Nederlands?\n"
                      "   → Ik leer Nederlands omdat … / Ik wil … / In het dagelijks leven …\n\n"
                      "3. <b>Ervaringen</b> (3 zinnen): Hoe gaat het? Wat is moeilijk/makkelijk?\n"
                      "   → In het begin was … / Nu kan ik … / De woordvolgorde vind ik …\n\n"
                      "4. <b>Toekomst</b> (3 zinnen): Wat zijn je plannen?\n"
                      "   → Ik wil … / Ik hoop … te … / Ik ga …\n\n"
                      "Gebruik: omdat, want, daarom, willen, hopen+te, perfectum, vergelijk toen/nu.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 23 — Vroeger vertellen (Talking about the past)
    # ──────────────────────────────────────────────
    {
        "id": 23,
        "title": "Vroeger vertellen",
        "chapter": "Hoofdstuk 8 – Examenvoorbereiding",
        "book_page": "p. 151-158",
        "review": "Op het examen moet je vaak over <b>vroeger</b> vertellen: je jeugd, je land, "
                  "hoe het leven was voordat je naar België kwam. Deze sessie combineert "
                  "<b>imperfectum</b> (sessie 4), <b>perfectum</b> (sessie 11-12), "
                  "<b>toen</b> (sessie 13) en <b>voordat/nadat</b> (sessie 17).",

        "vocabulary": [
            {"nl": "vroeger", "en": "in the past / formerly",
                "example": "Vroeger woonde ik in India."},
            {"nl": "de jeugd", "en": "the youth / childhood",
                "example": "Mijn jeugd was fijn."},
            {"nl": "opgroeien", "en": "to grow up",
                "example": "Ik ben opgegroeid in Tamil Nadu."},
            {"nl": "de herinnering", "en": "the memory",
                "example": "Ik heb mooie herinneringen aan mijn jeugd."},
            {"nl": "verhuizen",
                "en": "to move (house)", "example": "Ik ben naar België verhuisd."},
            {"nl": "missen", "en": "to miss",
                "example": "Ik mis mijn familie soms."},
            {"nl": "de gewoontes", "en": "the habits/customs",
                "example": "De gewoontes zijn hier anders."},
            {"nl": "de traditie", "en": "the tradition",
                "example": "We hebben veel tradities in India."},
            {"nl": "het verschil", "en": "the difference",
                "example": "Het verschil tussen India en België is groot."},
            {"nl": "wennen aan", "en": "to get used to",
                "example": "Ik moest wennen aan het weer."},
            {"nl": "de basisschool", "en": "primary school",
                "example": "Op de basisschool leerde ik Tamil."},
            {"nl": "destijds", "en": "at that time",
                "example": "Destijds had ik geen computer."},
        ],

        "grammar_title": "Vroeger vertellen — verleden tijden combineren",

        "grammar_html": """
<h4>1. Welke verleden tijd gebruik je?</h4>
<table>
<tr><th>Situatie</th><th>Tijd</th><th>Voorbeeld</th></tr>
<tr><td>Achtergrond / beschrijving / gewoontes</td><td><b>Imperfectum</b></td><td>Vroeger <b>woonde</b> ik in Chennai.</td></tr>
<tr><td>Eenmalige actie / gebeurtenis</td><td><b>Perfectum</b></td><td>In 2022 <b>ben</b> ik naar België <b>verhuisd</b>.</td></tr>
<tr><td>Eén moment in het verleden</td><td><b>Toen + imperf.</b></td><td><b>Toen</b> ik klein <b>was</b>, speelde ik buiten.</td></tr>
<tr><td>Actie vóór een andere actie</td><td><b>Nadat + plusquam.</b></td><td><b>Nadat</b> ik <b>had</b> gestudeerd, ging ik werken.</td></tr>
</table>

<h4>2. Structuur voor 'Vroeger vertellen'</h4>
<div class="formula-card">
<b>Opening:</b> Vroeger woonde ik in … / Toen ik jong was, …<br>
<b>Beschrijving:</b> Mijn familie was … / We hadden … / Ik ging elke dag …<br>
<b>Gebeurtenissen:</b> Op een dag heb ik … / In [jaar] ben ik …<br>
<b>Vergelijking:</b> In India was … maar in België is …<br>
<b>Afsluiting:</b> Nu woon ik in Gent en …
</div>

<h4>3. Tijdsuitdrukkingen voor het verleden</h4>
<table>
<tr><th>Nederlands</th><th>English</th><th>Voorbeeld</th></tr>
<tr><td>vroeger</td><td>in the past</td><td>Vroeger speelde ik cricket.</td></tr>
<tr><td>toen</td><td>then / when (past)</td><td>Toen was alles anders.</td></tr>
<tr><td>destijds</td><td>at that time</td><td>Destijds had ik geen auto.</td></tr>
<tr><td>als kind</td><td>as a child</td><td>Als kind las ik veel boeken.</td></tr>
<tr><td>in die tijd</td><td>in those days</td><td>In die tijd was er geen internet.</td></tr>
<tr><td>op een dag</td><td>one day</td><td>Op een dag besloot ik te verhuizen.</td></tr>
<tr><td>eerst… daarna…</td><td>first… then…</td><td>Eerst studeerde ik, daarna ging ik werken.</td></tr>
</table>

<h4>4. Vergelijken: vroeger vs nu (revisie sessie 22)</h4>
<table>
<tr><th>Vroeger (imperfectum)</th><th>Nu (presens)</th></tr>
<tr><td>Ik <b>woonde</b> in India.</td><td>Ik <b>woon</b> in België.</td></tr>
<tr><td>Ik <b>sprak</b> alleen Tamil en Engels.</td><td>Ik <b>spreek</b> ook Nederlands.</td></tr>
<tr><td>Ik <b>at</b> elke dag rijst.</td><td>Ik <b>eet</b> ook brood en kaas.</td></tr>
<tr><td>Het <b>was</b> altijd warm.</td><td>Het <b>is</b> vaak koud en regenachtig.</td></tr>
<tr><td>Ik <b>kende</b> niemand hier.</td><td>Ik <b>ken</b> al veel mensen.</td></tr>
</table>

<h4>5. Verhalende alinea — model</h4>
<p><i>Vroeger woonde ik in Chennai, in het zuiden van India. Mijn familie was groot — ik had drie broers 
en twee zussen. Als kind speelde ik elke dag buiten met mijn vrienden. Op school leerde ik Tamil, 
Engels en Hindi. Toen ik 22 was, ben ik naar de universiteit gegaan. Nadat ik was afgestudeerd, 
heb ik een baan gevonden als onderzoeker. In 2022 ben ik naar België verhuisd. In het begin was 
het moeilijk — ik kende niemand en het weer was heel anders. Maar nu woon ik al drie jaar in Gent 
en ik voel me hier thuis.</i></p>

<h4>🇮🇳 Tamil comparison</h4>
<p>Tamil past tense: நான் சென்னையில் வாழ்ந்தேன் (I lived in Chennai) — one past form.<br>
Dutch has TWO past forms (imperfectum + perfectum) which is confusing at first!<br>
Rule of thumb: for STORIES about the past, imperfectum is your friend. For SINGLE events, use perfectum.</p>
""",

        "grammar_letop": [
            {"wrong": "Vroeger ik woonde in India.",
             "right": "Vroeger woonde ik in India.",
             "explain": "Vroeger at the start → inversie! Vroeger WOONDE IK (V-S)."},
            {"wrong": "Toen ik was klein, speelde ik buiten.",
             "right": "Toen ik klein was, speelde ik buiten.",
             "explain": "Toen = bijzin → verb at END: toen ik klein WAS."},
            {"wrong": "In 2022 ik ben naar België verhuisd.",
             "right": "In 2022 ben ik naar België verhuisd.",
             "explain": "Time phrase first → inversie: In 2022 BEN IK (V-S)."},
            {"wrong": "Vroeger heb ik in India gewoond. (for background)",
             "right": "Vroeger woonde ik in India.",
             "explain": "Background/habits in the past → imperfectum (woonde), not perfectum."},
            {"wrong": "Nadat ik studeerde, ging ik werken.",
             "right": "Nadat ik had gestudeerd, ging ik werken.",
             "explain": "Nadat + main in imperfectum → bijzin in plusquamperfectum (had gestudeerd)."},
        ],

        "grammar_extra": """
<h4>Jouw verleden — bouwstenen per thema</h4>

<p><b>Jeugd:</b></p>
<ul>
<li>Ik ben opgegroeid in … (I grew up in …)</li>
<li>Als kind had ik … / speelde ik … / ging ik elke dag naar …</li>
<li>Mijn ouders waren … / Mijn vader werkte als …</li>
<li>Op de basisschool leerde ik …</li>
</ul>

<p><b>School & studie:</b></p>
<ul>
<li>Ik ging naar school in …</li>
<li>Mijn lievelingsvak was …</li>
<li>Nadat ik was afgestudeerd, …</li>
<li>Ik heb gestudeerd aan de universiteit van …</li>
</ul>

<p><b>Verhuizen naar België:</b></p>
<ul>
<li>In [jaar] ben ik naar België verhuisd.</li>
<li>Ik ben naar Gent gekomen omdat …</li>
<li>In het begin moest ik wennen aan …</li>
<li>Het verschil tussen India en België is …</li>
</ul>

<p><b>Vergelijkingen India ↔ België:</b></p>
<ul>
<li>In India was het altijd warm, maar in België is het vaak koud.</li>
<li>In India at ik elke dag rijst, hier eet ik ook brood.</li>
<li>De tradities zijn heel anders — in India vierden we Diwali, hier vieren ze Kerstmis.</li>
</ul>
""",

        "grammar_quick": [
            "Achtergrond/gewoontes → imperfectum: Vroeger woonde ik, ik speelde, het was.",
            "Eenmalige gebeurtenis → perfectum: Ik ben verhuisd, ik heb gestudeerd.",
            "Toen ik … was → bijzin (V-einde) + imperfectum.",
            "Nadat + plusquamperfectum (had + vd) als de hoofdzin in imperfectum is.",
            "Tijdswoorden: vroeger, destijds, als kind, in die tijd, op een dag.",
            "Vergelijk vroeger/nu: Vroeger woonde ik … Nu woon ik …",
        ],

        "exercises": [
            {"type": "fill", "q": "Over je jeugd: Vroeger ___ ik in India. (live — imperfectum)", "a": "woonde",
             "tip": "Wonen → woonde (regelmatig: woon + de). Achtergrond → imperfectum."},
            {"type": "fill", "q": "Over je verhuis: In 2022 ___ ik naar België verhuisd. (zijn — perfectum)", "a": "ben",
             "tip": "Verhuizen gebruikt ZIJN: Ik BEN verhuisd. Eenmalige gebeurtenis → perfectum."},
            {"type": "fill", "q": "In een verhaal: Toen ik klein ___, speelde ik buiten. (zijn — imperf.)", "a": "was",
             "tip": "Toen-bijzin: werkwoord op het einde. Zijn → was. Toen ik klein WAS."},
            {"type": "fill", "q": "Aan je docent: Nadat ik ___ gestudeerd, ging ik werken. (hebben — plusquam.)", "a": "had",
             "tip": "Nadat + plusquamperfectum: had + voltooid deelwoord. Had gestudeerd."},
            {"type": "fill", "q": "Over je kindertijd: Als kind ___ ik elke dag buiten. (play — imperf.)", "a": "speelde",
             "tip": "Spelen → speelde (regelmatig: speel + de). Gewoonte in het verleden → imperfectum."},
            {"type": "choice",
             "q": "Aan een nieuwe collega: 'Vroeger sprak ik alleen Tamil.' Welke is correct?",
             "options": ["Vroeger heb ik alleen Tamil gesproken.",
                         "Vroeger sprak ik alleen Tamil.",
                         "Vroeger ik sprak alleen Tamil.",
                         "Vroeger spreek ik alleen Tamil."],
             "a": "Vroeger sprak ik alleen Tamil.",
             "tip": "Achtergrond/gewoonte → imperfectum (sprak). Vroeger vooraan → inversie (sprak ik)."},
            {"type": "choice",
             "q": "Op het examen: Welke tijd is correct? 'Nadat ik ___, ging ik werken.'",
             "options": ["studeerde", "heb gestudeerd", "had gestudeerd", "studeer"],
             "a": "had gestudeerd",
             "tip": "Hoofdzin = imperfectum (ging) → nadat-bijzin = plusquamperfectum (had gestudeerd)."},
            {"type": "choice",
             "q": "In een brief: 'Op een dag besloot ik naar België te verhuizen.' Welke is correct?",
             "options": ["Op een dag besloot ik naar België te verhuizen.",
                         "Op een dag ik besloot naar België te verhuizen.",
                         "Op een dag besloot ik te naar België verhuizen.",
                         "Op een dag besloot ik naar België verhuizen te."],
             "a": "Op een dag besloot ik naar België te verhuizen.",
             "tip": "Tijd vooraan → inversie (besloot ik). Te vóór infinitief: te verhuizen."},
            {"type": "tf", "q": "'Vroeger ik woonde in India' heeft de juiste woordvolgorde.", "a": "Nee",
             "tip": "Vroeger vooraan → inversie: Vroeger WOONDE IK (V-S), niet ik woonde (S-V)."},
            {"type": "tf", "q": "'Ik ben opgegroeid in Tamil Nadu' is correct perfectum.", "a": "Ja",
             "tip": "Opgroeien gebruikt ZIJN: Ik ben opgegroeid. Correct!"},
            {"type": "tf", "q": "'Toen ik was klein' heeft de juiste woordvolgorde.", "a": "Nee",
             "tip": "Toen-bijzin: werkwoord op het EINDE. Toen ik klein WAS (niet was klein)."},
            {"type": "translate", "q": "When I was young, I played outside every day.",
             "a": "Toen ik jong was, speelde ik elke dag buiten.",
             "tip": "Toen-bijzin (V-einde: was) + komma + inversie (speelde ik)."},
            {"type": "translate", "q": "In the beginning I had to get used to the weather.",
             "a": "In het begin moest ik wennen aan het weer.",
             "tip": "Tijd vooraan → inversie (moest ik). Wennen aan = gewend raken."},
            {"type": "reorder", "q": "woonde / vroeger / in / ik / India",
             "a": "Vroeger woonde ik in India.",
             "tip": "Vroeger vooraan → inversie: woonde ik. Vroeger woonde ik in India."},
            {"type": "reorder", "q": "ben / naar / 2022 / ik / in / verhuisd / België",
             "a": "In 2022 ben ik naar België verhuisd.",
             "tip": "Tijd vooraan → inversie: ben ik. Verhuizen = zijn: ben verhuisd."},
        ],

        "jouw_beurt": "Schrijf je eigen 'Vroeger' verhaal (minstens 15 zinnen).\n\n"
                      "Vertel over:\n"
                      "1. <b>Je jeugd</b> (4 zinnen): Waar ben je opgegroeid? Hoe was je familie?\n"
                      "   → Ik ben opgegroeid in … Als kind … Mijn ouders …\n\n"
                      "2. <b>School</b> (3 zinnen): Waar ging je naar school? Wat was je lievelingsvak?\n"
                      "   → Ik ging naar … Op school leerde ik …\n\n"
                      "3. <b>Verhuizen</b> (4 zinnen): Wanneer en waarom ben je naar België gekomen?\n"
                      "   → In [jaar] ben ik … Ik ben gekomen omdat …\n\n"
                      "4. <b>Vergelijking</b> (4 zinnen): Wat is anders? Wat mis je?\n"
                      "   → In India was … maar hier … Ik mis soms …\n\n"
                      "Gebruik: imperfectum, perfectum, toen, nadat, vroeger, destijds.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 24 — Spreken oefenen (Speaking practice)
    # ──────────────────────────────────────────────
    {
        "id": 24,
        "title": "Spreken oefenen",
        "chapter": "Hoofdstuk 8 – Examenvoorbereiding",
        "book_page": "p. 159-165",
        "review": "Het NT2 spreekexamen test je <b>mondelinge vaardigheden</b>: jezelf voorstellen, "
                  "een situatie beschrijven, je mening geven, en reageren op vragen. In deze sessie "
                  "oefen je alle spreektaken met <b>modelantwoorden</b> en <b>nuttige zinnen</b>.",

        "vocabulary": [
            {"nl": "het spreekexamen", "en": "the speaking exam",
                "example": "Het spreekexamen duurt 20 minuten."},
            {"nl": "zich voorstellen", "en": "to introduce oneself",
                "example": "Stel je eerst voor."},
            {"nl": "de mening", "en": "the opinion",
                "example": "Wat is je mening over dit onderwerp?"},
            {"nl": "het onderwerp", "en": "the topic / subject",
                "example": "Het onderwerp is gezondheid."},
            {"nl": "beschrijven", "en": "to describe",
                "example": "Beschrijf de foto."},
            {"nl": "reageren", "en": "to respond / react",
                "example": "Reageer op deze situatie."},
            {"nl": "uitleggen", "en": "to explain",
                "example": "Leg uit waarom je dat vindt."},
            {"nl": "het argument", "en": "the argument",
                "example": "Geef minstens twee argumenten."},
            {"nl": "het voordeel", "en": "the advantage",
                "example": "Een voordeel is dat het gezond is."},
            {"nl": "het nadeel", "en": "the disadvantage",
                "example": "Een nadeel is de prijs."},
            {"nl": "volgens mij", "en": "in my opinion",
                "example": "Volgens mij is sport belangrijk."},
            {"nl": "aan de ene kant … aan de andere kant", "en": "on the one hand … on the other hand",
             "example": "Aan de ene kant is het leuk, aan de andere kant is het duur."},
        ],

        "grammar_title": "Spreekexamen — strategieën en structuren",

        "grammar_html": """
<h4>1. De spreektaken op het examen</h4>
<table>
<tr><th>Taak</th><th>Wat moet je doen?</th><th>Tijd</th></tr>
<tr><td>1. Jezelf voorstellen</td><td>Naam, land, woonplaats, werk, hobby's</td><td>2 min</td></tr>
<tr><td>2. Foto beschrijven</td><td>Wat zie je? Wie? Waar? Wat doen ze?</td><td>2 min</td></tr>
<tr><td>3. Situatie/rollenspel</td><td>Bellen, afspraak maken, klacht, informatie vragen</td><td>3 min</td></tr>
<tr><td>4. Mening geven</td><td>Onderwerp + vóór/tegen + argumenten</td><td>3 min</td></tr>
</table>

<h4>2. Taak 1: Jezelf voorstellen — structuur</h4>
<div class="formula-card">
<b>Naam & afkomst:</b> Ik heet … Ik kom uit … (India/Tamil Nadu).<br>
<b>Woonplaats:</b> Ik woon in Gent sinds …<br>
<b>Werk/studie:</b> Ik werk als onderzoeker aan UGent.<br>
<b>Familie:</b> Ik ben getrouwd / Ik woon alleen / met mijn partner.<br>
<b>Talen:</b> Ik spreek Tamil, Engels en ik leer Nederlands.<br>
<b>Hobby's:</b> In mijn vrije tijd … / Ik hou van …
</div>

<h4>3. Taak 2: Foto beschrijven — zinnen</h4>
<ul>
<li><b>Algemeen:</b> Op de foto zie ik … / De foto toont …</li>
<li><b>Personen:</b> Er zijn [aantal] personen. / Ik zie een man/vrouw van ongeveer … jaar.</li>
<li><b>Uiterlijk:</b> Hij/Zij heeft … haar en … ogen. (sessie 21)</li>
<li><b>Locatie:</b> Ze zijn in een park / op straat / in een restaurant.</li>
<li><b>Actie:</b> Ze zijn aan het [infinitief]. / Hij/Zij zit/staat/loopt …</li>
<li><b>Sfeer:</b> Het ziet er gezellig/druk/rustig uit.</li>
</ul>

<h4>4. Taak 3: Situatie/rollenspel — functies</h4>
<table>
<tr><th>Functie</th><th>Nuttige zinnen</th></tr>
<tr><td>Bellen</td><td>Goedendag, u spreekt met … / Ik bel omdat …</td></tr>
<tr><td>Afspraak maken</td><td>Kan ik een afspraak maken? / Schikt het op …?</td></tr>
<tr><td>Klacht</td><td>Ik wil graag klagen over … / Er is een probleem met …</td></tr>
<tr><td>Informatie vragen</td><td>Kunt u mij vertellen …? / Ik zou graag weten …</td></tr>
<tr><td>Bedanken</td><td>Dank u wel. / Hartelijk bedankt voor uw hulp.</td></tr>
</table>

<h4>5. Taak 4: Mening geven — structuur</h4>
<div class="formula-card">
<b>Stelling herhalen:</b> Het onderwerp is … / De vraag is of …<br>
<b>Mening:</b> Ik vind dat … / Volgens mij … / Ik denk dat …<br>
<b>Argument 1:</b> Ten eerste … / Een voordeel is dat …<br>
<b>Argument 2:</b> Bovendien … / Daarnaast …<br>
<b>Tegenargument:</b> Aan de andere kant … / Maar sommige mensen vinden …<br>
<b>Conclusie:</b> Al met al denk ik dat … / Daarom vind ik …
</div>

<h4>6. Verbindingswoorden voor spreken</h4>
<table>
<tr><th>Functie</th><th>Woorden</th></tr>
<tr><td>Opsomming</td><td>ten eerste, ten tweede, bovendien, daarnaast, ook</td></tr>
<tr><td>Contrast</td><td>maar, echter, aan de andere kant, toch</td></tr>
<tr><td>Reden</td><td>omdat, want, daarom, namelijk</td></tr>
<tr><td>Voorbeeld</td><td>bijvoorbeeld, zoals, denk maar aan</td></tr>
<tr><td>Conclusie</td><td>al met al, kortom, dus, daarom</td></tr>
</table>

<h4>🇮🇳 Tamil comparison</h4>
<p>Tamil speaking structure is similar: introduction → argument → conclusion.<br>
முதலில் (mudhalil) = ten eerste, மேலும் (meelum) = bovendien, ஆனால் (aanaal) = maar.<br>
The key difference: Dutch expects you to be structured and concise. Practice with a timer!</p>
""",

        "grammar_letop": [
            {"wrong": "Ik vind dat sport is belangrijk.",
             "right": "Ik vind dat sport belangrijk is.",
             "explain": "Dat = bijzin → verb at END: dat sport belangrijk IS."},
            {"wrong": "Volgens mij sport is gezond.",
             "right": "Volgens mij is sport gezond.",
             "explain": "Volgens mij at the start → inversie: IS sport (V-S)."},
            {"wrong": "Op de foto ik zie een man.",
             "right": "Op de foto zie ik een man.",
             "explain": "Prepositional phrase first → inversie: Op de foto ZIE IK (V-S)."},
            {"wrong": "Ik wil graag klagen over mijn buurman is te luid.",
             "right": "Ik wil graag klagen omdat mijn buurman te luid is.",
             "explain": "To give a reason, use omdat + bijzin. Don't just append a main clause."},
            {"wrong": "Aan de ene kant het is leuk. Aan de andere kant het is duur.",
             "right": "Aan de ene kant is het leuk. Aan de andere kant is het duur.",
             "explain": "Both phrases start the sentence → inversie both times: IS het (V-S)."},
        ],

        "grammar_extra": """
<h4>Modelantwoorden per taak</h4>

<p><b>Taak 1 — Jezelf voorstellen (model):</b></p>
<p><i>Goedendag, ik heet [naam] en ik kom uit India, meer specifiek uit Tamil Nadu. 
Ik woon in Gent sinds 2022. Ik werk als onderzoeker aan de Universiteit Gent. 
Ik spreek Tamil, Engels en ik leer nu Nederlands — ik zit in B1 deel 2. 
In mijn vrije tijd hou ik van koken en wandelen. Ik kook graag Indiase gerechten 
voor mijn vrienden. Ik vind Gent een mooie stad om in te wonen.</i></p>

<p><b>Taak 4 — Mening geven (model over 'Sport'):</b></p>
<p><i>De vraag is of sport belangrijk is. Ik vind dat sport heel belangrijk is voor 
iedereen. Ten eerste is sport gezond — het is goed voor je lichaam en je geest. 
Bovendien kun je door sport nieuwe mensen ontmoeten. Aan de andere kant kost sport 
soms veel geld en tijd. Maar al met al denk ik dat de voordelen groter zijn dan 
de nadelen. Daarom vind ik dat iedereen minstens twee keer per week moet sporten.</i></p>

<p><b>Nuttige 'fill-in' formules:</b></p>
<ul>
<li>Ik vind dat … belangrijk/goed/slecht is, omdat …</li>
<li>Niet alleen … maar ook …</li>
<li>Hoe meer je …, hoe beter/gezonder het is.</li>
<li>Dat is de reden waarom ik …</li>
</ul>
""",

        "grammar_quick": [
            "Taak 1 (voorstellen): naam, land, woonplaats, werk, talen, hobby's.",
            "Taak 2 (foto): Op de foto zie ik … / Ze zijn aan het … / Het ziet er … uit.",
            "Taak 3 (situatie): Bellen, afspraak, klacht, info → specifieke formules.",
            "Taak 4 (mening): Stelling → mening → argumenten → contra → conclusie.",
            "Inversie na: volgens mij, op de foto, aan de ene kant, ten eerste.",
            "Dat-bijzin: Ik vind dat … IS. Verb at end!",
        ],

        "exercises": [
            {"type": "fill", "q": "Op het examen: Ik vind ___ sport belangrijk is.", "a": "dat",
             "tip": "Ik vind DAT … = I think that … Dat introduceert een bijzin."},
            {"type": "fill", "q": "In een discussie: Volgens mij ___ Nederlands een mooie taal. (is)", "a": "is",
             "tip": "Volgens mij vooraan → inversie: IS Nederlands (V-S)."},
            {"type": "fill", "q": "Foto beschrijven: Op de foto ___ ik een vrouw met lang haar. (see)", "a": "zie",
             "tip": "Voorzetsel vooraan → inversie: Op de foto ZIE IK."},
            {"type": "fill", "q": "In je betoog: Ten eerste is sport gezond. ___ kun je mensen ontmoeten. (moreover)", "a": "Bovendien",
             "tip": "Bovendien = moreover/daarnaast. Gevolgd door inversie: kun je."},
            {"type": "fill", "q": "Je conclusie: Al met al ___ ik dat sport belangrijk is.", "a": "denk",
             "tip": "Al met al = alles bij elkaar. Al met al DENK IK dat … (inversie)."},
            {"type": "choice",
             "q": "Mening geven: Welke zin heeft de juiste woordvolgorde?",
             "options": ["Volgens mij sport is gezond.",
                         "Volgens mij is sport gezond.",
                         "Volgens mij gezond sport is.",
                         "Sport volgens mij is gezond."],
             "a": "Volgens mij is sport gezond.",
             "tip": "Volgens mij vooraan → inversie: IS sport (V vóór S)."},
            {"type": "choice",
             "q": "Over het weer: 'Ik denk dat het weer in België koud is.' Welke is correct?",
             "options": ["Ik denk dat het weer in België is koud.",
                         "Ik denk dat het weer in België koud is.",
                         "Ik denk dat koud is het weer in België.",
                         "Ik denk het weer dat in België koud is."],
             "a": "Ik denk dat het weer in België koud is.",
             "tip": "Dat-bijzin → werkwoord op het EINDE: dat het weer in België koud IS."},
            {"type": "choice",
             "q": "Welk signaalwoord betekent 'aan de andere kant'?",
             "options": ["bovendien", "daarom", "aan de andere kant", "kortom"],
             "a": "aan de andere kant",
             "tip": "Aan de andere kant = on the other hand. Bovendien = moreover. Daarom = therefore."},
            {"type": "tf", "q": "'Op de foto ik zie een man' is correct.", "a": "Nee",
             "tip": "Voorzetsel vooraan → inversie: Op de foto ZIE IK (V-S)."},
            {"type": "tf", "q": "'Ik vind dat sport belangrijk is' heeft de juiste woordvolgorde.", "a": "Ja",
             "tip": "Dat-bijzin: werkwoord op het einde → belangrijk IS. Correct!"},
            {"type": "tf", "q": "'Bovendien' betekent 'however'.", "a": "Nee",
             "tip": "Bovendien = moreover/daarnaast. However = echter/maar."},
            {"type": "translate", "q": "In my opinion, learning Dutch is important.",
             "a": "Volgens mij is Nederlands leren belangrijk.",
             "tip": "Volgens mij → inversie: IS … belangrijk."},
            {"type": "translate", "q": "On the one hand it is fun, on the other hand it is expensive.",
             "a": "Aan de ene kant is het leuk, aan de andere kant is het duur.",
             "tip": "Beide delen → inversie: IS het (V-S) in beide deelzinnen."},
            {"type": "reorder", "q": "vind / dat / belangrijk / ik / sport / is",
             "a": "Ik vind dat sport belangrijk is.",
             "tip": "Ik vind + dat-bijzin (V-einde): dat sport belangrijk IS."},
            {"type": "reorder", "q": "mij / is / volgens / taal / Nederlands / mooie / een",
             "a": "Volgens mij is Nederlands een mooie taal.",
             "tip": "Volgens mij → inversie: IS Nederlands een mooie taal."},
        ],

        "jouw_beurt": "Oefen alle 4 de spreektaken.\n\n"
                      "1. <b>Stel je voor</b> (6 zinnen): naam, land, woonplaats, werk, talen, hobby.\n\n"
                      "2. <b>Beschrijf een foto</b> (5 zinnen): Kies een foto op je telefoon.\n"
                      "   → Op de foto zie ik … / Er zijn … / Ze zijn aan het …\n\n"
                      "3. <b>Situatie</b> (4 zinnen): Je wilt een afspraak bij de dokter. Bel!\n"
                      "   → Goedendag, u spreekt met … / Ik wil graag een afspraak …\n\n"
                      "4. <b>Mening</b> (6 zinnen): 'Is thuiswerken goed?' Geef je mening.\n"
                      "   → Ik vind dat … / Ten eerste … / Bovendien … / Aan de andere kant … / "
                      "Al met al …\n\n"
                      "Tip: Lees je antwoorden hardop (read aloud)! Gebruik een timer: 2-3 min per taak.",
    },

    # ──────────────────────────────────────────────
    #  SESSION 25 — Proefexamen (Mock Exam)
    # ──────────────────────────────────────────────
    {
        "id": 25,
        "title": "Proefexamen",
        "chapter": "Hoofdstuk 8 – Examenvoorbereiding",
        "book_page": "Herhaling",
        "review": "Dit is het <b>proefexamen</b>! Alle grammatica en woordenschat uit 24 sessies "
                  "komen samen. Doe deze oefeningen als een echte test: zonder hulp, met een timer "
                  "(30 minuten). Succes! 🎓",

        "vocabulary": [
            {"nl": "het proefexamen", "en": "the mock exam",
                "example": "Het proefexamen is een goede voorbereiding."},
            {"nl": "de herhaling", "en": "the revision / review",
                "example": "Dit is een herhaling van alles."},
            {"nl": "de score", "en": "the score",
                "example": "Mijn score is 12 op 15."},
            {"nl": "slagen (voor)", "en": "to pass (an exam)",
             "example": "Ik wil slagen voor het examen."},
            {"nl": "zakken (voor)", "en": "to fail (an exam)",
             "example": "Ik wil niet zakken!"},
            {"nl": "de kennis", "en": "the knowledge",
                "example": "Je kennis van Nederlands is goed."},
            {"nl": "oefenen", "en": "to practise",
                "example": "Je moet elke dag oefenen."},
            {"nl": "de vaardigheid", "en": "the skill",
                "example": "Spreken is een belangrijke vaardigheid."},
            {"nl": "de woordenschat", "en": "the vocabulary",
                "example": "Je woordenschat is uitgebreid."},
            {"nl": "de grammatica", "en": "the grammar",
                "example": "De grammatica is soms moeilijk."},
            {"nl": "het resultaat", "en": "the result",
                "example": "Ik ben tevreden over mijn resultaat."},
            {"nl": "volhouden", "en": "to persevere / keep going",
                "example": "Hou vol! Je kunt het!"},
        ],

        "grammar_title": "Proefexamen — alles samengevat",

        "grammar_html": """
<h4>📋 Overzicht: alle grammatica in 24 sessies</h4>
<table>
<tr><th>Sessie</th><th>Onderwerp</th><th>Kernregel</th></tr>
<tr><td>1</td><td>Al eens / Nog nooit</td><td>Perfectum: hebben/zijn + voltooid deelwoord</td></tr>
<tr><td>2</td><td>Mening + bijzin</td><td>Ik vind dat … + V-einde</td></tr>
<tr><td>3</td><td>Inversie</td><td>V2-regel: werkwoord altijd op plek 2</td></tr>
<tr><td>4</td><td>Imperfectum</td><td>'t kofschip → stam+te(n). Anders → stam+de(n)</td></tr>
<tr><td>5</td><td>Om … te …</td><td>Doel uitdrukken: om + te + infinitief</td></tr>
<tr><td>6</td><td>Omdat / Want / Daarom</td><td>Omdat (V-end), want (S+V), daarom (inversie)</td></tr>
<tr><td>7</td><td>Als (if / when)</td><td>Als + bijzin → inversie in hoofdzin</td></tr>
<tr><td>8</td><td>Bij de dokter</td><td>Reflexieve werkwoorden: zich voelen, zich wassen</td></tr>
<tr><td>9</td><td>Vergelijkingen</td><td>Comparatief: -er. Superlatief: -st / meest</td></tr>
<tr><td>10</td><td>Toekomst</td><td>Gaan/zullen + infinitief</td></tr>
<tr><td>11</td><td>Perfectum</td><td>Hebben/zijn + voltooid deelwoord (details)</td></tr>
<tr><td>12</td><td>Perf. vs Imperf.</td><td>Eenmalig → perf. Achtergrond → imperf.</td></tr>
<tr><td>13</td><td>Als vs Toen</td><td>Als = herhaling/toekomst. Toen = eenmalig verleden</td></tr>
<tr><td>14</td><td>Connectors</td><td>3 groepen: nevenschikkend, onderschikkend, bijwoord</td></tr>
<tr><td>15-16</td><td>ER</td><td>5 functies: er+zijn, er+vz, er+hoeveelheid, er=plaats, er+passief</td></tr>
<tr><td>17</td><td>Voordat / Nadat</td><td>Tijdconnectors + bijzin (V-end) + tijdverschuiving</td></tr>
<tr><td>18</td><td>Voornaamwoorden</td><td>Subject/object/bezittelijk/reflexief</td></tr>
<tr><td>19-20</td><td>Vaste voorzetsels</td><td>Werkwoord+vz, bijv.nw.+vz, er+vz, waar+vz</td></tr>
<tr><td>21</td><td>Uiterlijk</td><td>Zijn + eigenschap, hebben + lichaamsdeel, dragen + accessoire</td></tr>
<tr><td>22</td><td>Waarom Nederlands?</td><td>Omdat/want/daarom + willen/hopen + toen vs nu</td></tr>
<tr><td>23</td><td>Vroeger vertellen</td><td>Imperf. + perf. + toen + nadat combineren</td></tr>
<tr><td>24</td><td>Spreken</td><td>4 taken: voorstellen, foto, situatie, mening</td></tr>
</table>

<h4>⚡ Snelle geheugensteun — De 5 belangrijkste regels</h4>
<ol>
<li><b>V2-regel:</b> Het werkwoord staat ALTIJD op positie 2 in de hoofdzin.</li>
<li><b>Bijzin:</b> Na omdat, dat, als, toen, voordat, nadat → werkwoord naar het EINDE.</li>
<li><b>Inversie:</b> Als iets anders dan het subject vooraan staat → V-S (verb before subject).</li>
<li><b>Perfectum:</b> hebben/zijn + voltooid deelwoord. Beweging/verandering → zijn.</li>
<li><b>Adjectief:</b> +e vóór de-woorden en meervoud. Geen -e vóór het-woord zonder artikel.</li>
</ol>

<h4>🇮🇳 Tamil speaker tips voor het examen</h4>
<ul>
<li>Tamil is SOV, Dutch is SVO — let altijd op de werkwoordpositie!</li>
<li>Tamil heeft geen artikelen (de/het) — oefen de/het extra!</li>
<li>Tamil heeft postposities, Dutch heeft preposities — de volgorde is omgekeerd.</li>
<li>Lees de vraag goed en neem 10 seconden om na te denken voordat je antwoordt.</li>
</ul>
""",

        "grammar_letop": [
            {"wrong": "Ik denk dat hij is een goede leraar.",
             "right": "Ik denk dat hij een goede leraar is.",
             "explain": "Dat-bijzin → verb at END. Dat hij een goede leraar IS."},
            {"wrong": "Gisteren ik heb een boek gelezen.",
             "right": "Gisteren heb ik een boek gelezen.",
             "explain": "Time adverb first → inversie: Gisteren HEB IK (V-S)."},
            {"wrong": "Ik wacht voor de tram omdat ik wil gaan naar het centrum.",
             "right": "Ik wacht op de tram omdat ik naar het centrum wil gaan.",
             "explain": "Wachten OP (not voor). Omdat-bijzin: verb cluster at end (wil gaan)."},
            {"wrong": "Zij heeft lang blond haar en ze is bruine ogen.",
             "right": "Zij heeft lang blond haar en ze heeft bruine ogen.",
             "explain": "Physical features → HEBBEN (ogen, haar). Characteristics → ZIJN (lang, slank)."},
            {"wrong": "Vroeger ik woonde in India en ik sprak alleen Tamil.",
             "right": "Vroeger woonde ik in India en sprak ik alleen Tamil.",
             "explain": "Vroeger first → inversie (woonde ik). Second clause after en also keeps inversie if vroeger applies."},
        ],

        "grammar_extra": """
<h4>Examentips</h4>
<ul>
<li><b>Lezen:</b> Lees de vraag twee keer. Onderstreep de sleutelwoorden.</li>
<li><b>Schrijven:</b> Maak eerst een korte planning (3 punten). Schrijf dan. Controleer je werkwoordpositie!</li>
<li><b>Spreken:</b> Neem 10 seconden denktijd. Spreek duidelijk. Gebruik connectors.</li>
<li><b>Luisteren:</b> Luister naar de intonatie. Let op signaalwoorden (maar, want, daarom).</li>
</ul>

<h4>Laatste revisie — veelgemaakte fouten</h4>
<table>
<tr><th>Fout</th><th>Correct</th><th>Regel</th></tr>
<tr><td>Ik denk dat … is …</td><td>Ik denk dat … … is.</td><td>Bijzin: V-einde</td></tr>
<tr><td>Gisteren ik heb …</td><td>Gisteren heb ik …</td><td>Inversie na tijdswoord</td></tr>
<tr><td>Ik wacht voor …</td><td>Ik wacht op …</td><td>Vast voorzetsel</td></tr>
<tr><td>Ik ben … ogen</td><td>Ik heb … ogen</td><td>Hebben + lichaamsdeel</td></tr>
<tr><td>Vroeger ik …</td><td>Vroeger … ik</td><td>Inversie na vroeger</td></tr>
</table>
""",

        "grammar_quick": [
            "V2: werkwoord altijd op positie 2 in de hoofdzin.",
            "Bijzin (omdat/dat/als/toen/voordat/nadat): werkwoord naar het EINDE.",
            "Inversie: tijd/plaats/bijzin vooraan → V-S in de hoofdzin.",
            "Perfectum: hebben/zijn + vd. Beweging/verandering → zijn.",
            "Vaste voorzetsels: leer ze uit je hoofd! wachten OP, denken AAN, etc.",
            "Adjectief +e: vóór de-woorden & meervoud. Geen -e vóór het-woord zonder artikel.",
        ],

        "exercises": [
            {"type": "fill", "q": "Aan je docent: Ik leer Nederlands ___ ik in Gent woon. (because — bijzin)", "a": "omdat",
             "tip": "Because + V-einde = omdat. Omdat ik in Gent WOON."},
            {"type": "fill", "q": "In je dagboek: Gisteren ___ ik naar de markt geweest. (zijn — perfectum)", "a": "ben",
             "tip": "Gaan/zijn gebruikt ZIJN in perfectum: ik BEN geweest. Gisteren BEN IK (inversie)."},
            {"type": "fill", "q": "Over je jeugd: Vroeger ___ ik elke dag rijst. (eat — imperfectum)", "a": "at",
             "tip": "Eten → imperfectum: at (onregelmatig). Vroeger at ik (inversie)."},
            {"type": "fill", "q": "Foto beschrijven: Zij heeft lang ___ haar. (blond — geen lidwoord, het-woord)", "a": "blond",
             "tip": "Het haar zonder lidwoord → geen -e op bijvoeglijk naamwoord: lang blond haar."},
            {"type": "fill", "q": "Op de halte: Ik wacht ___ de bus. (wait for)", "a": "op",
             "tip": "Wachten + OP. Niet voor! Vast voorzetsel."},
            {"type": "choice",
             "q": "Over je kindertijd: 'Toen ik jong was, speelde ik buiten.' Welke is correct?",
             "options": ["Als ik jong was, speelde ik buiten.",
                         "Toen ik jong was, speelde ik buiten.",
                         "Toen ik jong was, ik speelde buiten.",
                         "Wanneer ik jong was, speelde ik buiten."],
             "a": "Toen ik jong was, speelde ik buiten.",
             "tip": "Eenmalig verleden = toen (niet als). Bijzin vooraan → inversie: speelde ik."},
            {"type": "choice",
             "q": "Op het examen: Welke zin is 100% correct?",
             "options": ["Ik vind dat hij een goede leraar is.",
                         "Ik vind dat hij is een goede leraar.",
                         "Ik vind dat is hij een goede leraar.",
                         "Ik vind hij dat een goede leraar is."],
             "a": "Ik vind dat hij een goede leraar is.",
             "tip": "Dat-bijzin → werkwoord op het EINDE: dat hij een goede leraar IS."},
            {"type": "choice",
             "q": "Over Gent: 'Er zijn veel studenten in Gent.' Welke gebruikt 'er' correct?",
             "options": ["Het zijn veel studenten in Gent.",
                         "Er zijn veel studenten in Gent.",
                         "Daar zijn veel studenten in Gent.",
                         "Er is veel studenten in Gent."],
             "a": "Er zijn veel studenten in Gent.",
             "tip": "Er + zijn (meervoud: studenten → zijn, niet is). Er zijn = there are."},
            {"type": "tf", "q": "'Ik ben trots op mijn resultaat' gebruikt het juiste voorzetsel.", "a": "Ja",
             "tip": "Trots + OP. Proud of = trots op. Correct!"},
            {"type": "tf", "q": "'Nadat ik eet, ga ik werken' is correct standaard-Nederlands.", "a": "Nee",
             "tip": "Nadat heeft een tijdverschuiving nodig: Nadat ik HEB GEGETEN (perfectum), ga ik werken."},
            {"type": "tf", "q": "'Hij wast zich' betekent 'he washes himself'.", "a": "Ja",
             "tip": "Zich = reflexief voor hij/zij. Zich wassen = to wash oneself. Correct!"},
            {"type": "translate", "q": "I have lived in Ghent for two years because I work at UGent.",
             "a": "Ik woon al twee jaar in Gent omdat ik aan UGent werk.",
             "tip": "Voor duur: al + tijd. Omdat-bijzin: werkwoord-einde (werk). Aan UGent = at UGent."},
            {"type": "translate", "q": "In my opinion, Dutch is more difficult than English.",
             "a": "Volgens mij is Nederlands moeilijker dan Engels.",
             "tip": "Volgens mij → inversie (IS Nederlands). Comparatief: moeilijk → moeilijker."},
            {"type": "reorder", "q": "dat / denk / ik / mooie / is / een / Gent / stad",
             "a": "Ik denk dat Gent een mooie stad is.",
             "tip": "Ik denk + dat-bijzin: dat Gent een mooie stad IS (V-einde)."},
            {"type": "reorder", "q": "vroeger / in / woonde / India / ik / nu / maar / in / woon / ik / Gent",
             "a": "Vroeger woonde ik in India, maar nu woon ik in Gent.",
             "tip": "Vroeger → inversie (woonde ik). Maar = nevenschikkend, nu vooraan → inversie (woon ik)."},
        ],

        "jouw_beurt": "🎓 PROEFEXAMEN — Schrijftoets (30 minuten)\n\n"
                      "Beantwoord ALLE vragen in volledige zinnen.\n\n"
                      "<b>Deel 1 — Jezelf voorstellen (5 zinnen):</b>\n"
                      "Wie ben je? Waar kom je vandaan? Wat doe je in België?\n\n"
                      "<b>Deel 2 — Uiterlijk beschrijven (5 zinnen):</b>\n"
                      "Beschrijf het uiterlijk van een vriend of familielid.\n\n"
                      "<b>Deel 3 — Vroeger vs Nu (5 zinnen):</b>\n"
                      "Hoe was je leven vroeger? Hoe is het nu anders?\n\n"
                      "<b>Deel 4 — Mening (5 zinnen):</b>\n"
                      "'Is het belangrijk om Nederlands te leren in Vlaanderen?' "
                      "Geef je mening met argumenten.\n\n"
                      "<b>Checklist:</b>\n"
                      "☐ Heb ik omdat/want/daarom correct gebruikt?\n"
                      "☐ Staat het werkwoord op positie 2 (V2)?\n"
                      "☐ Heb ik inversie na tijdswoorden?\n"
                      "☐ Heb ik perfectum en imperfectum correct gebruikt?\n"
                      "☐ Heb ik vaste voorzetsels correct gebruikt?",
    },
]

# ---------------------------------------------------------------------------
# DATA NORMALISATION — ensure every session has consistent field formats
# ---------------------------------------------------------------------------


for _s in SESSIONS:
    # --- 1. vocabulary: convert tuples → dicts, rename "example" → "ex" ---
    _raw_vocab = _s.get("vocabulary", [])
    _fixed_vocab = []
    for _v in _raw_vocab:
        if isinstance(_v, (list, tuple)):
            _fixed_vocab.append({"nl": _v[0], "en": _v[1],
                                 "ex": _v[2] if len(_v) > 2 else ""})
        elif isinstance(_v, dict):
            _d = dict(_v)
            if "example" in _d and "ex" not in _d:
                _d["ex"] = _d.pop("example")
            if "ex" not in _d:
                _d["ex"] = ""
            _fixed_vocab.append(_d)
        else:
            _fixed_vocab.append({"nl": str(_v), "en": "", "ex": ""})
    _s["vocabulary"] = _fixed_vocab

    # --- 2. review: convert string → list[{q, a}] ---
    _rev = _s.get("review", [])
    if isinstance(_rev, str) and _rev.strip():
        _cards = [{"q": "📖 What is this session about?", "a": _rev}]
        # Generate vocab-based review cards
        if _fixed_vocab:
            _rnd.seed(_s.get("id", 0))  # reproducible
            _sample = _fixed_vocab[:]
            _rnd.shuffle(_sample)
            for _item in _sample[:4]:
                _cards.append({
                    "q": f"Hoe zeg je '{_item['en']}' in het Nederlands?",
                    "a": f"<b>{_item['nl']}</b>"
                    + (f" — {_item['ex']}" if _item.get("ex") else ""),
                })
        _s["review"] = _cards
    elif not isinstance(_rev, list):
        _s["review"] = []

    # --- 3. grammar_letop: convert list[dict] → HTML string ---
    _letop = _s.get("grammar_letop", "")
    if isinstance(_letop, list) and _letop and isinstance(_letop[0], dict):
        _parts = []
        for _item in _letop:
            _w = _item.get("wrong", "")
            _r = _item.get("right", "")
            _e = _item.get("explain", "")
            _parts.append(
                f'<div class="letop-item">'
                f'<span class="wrong">✗ {_w}</span><br>'
                f'<span class="right">✓ {_r}</span><br>'
                f'<span class="explain">→ {_e}</span>'
                f'</div>'
            )
        _s["grammar_letop"] = "\n".join(_parts)

# Clean up temporary names
del _rnd, _s, _raw_vocab, _fixed_vocab, _v, _d, _rev, _cards, _sample, _item
del _letop, _parts, _w, _r, _e
