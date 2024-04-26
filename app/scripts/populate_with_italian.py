from app import db, create_app
from app.models import Verb

app = create_app()
app.app_context().push()  # This line is necessary to run the script outside of Flask app context



common_verbs_dict = {
    "ESSERE": {
        "io": {"Italian": "sono", "English": "I am"},
        "tu": {"Italian": "sei", "English": "you are (informal)"},
        "lui/lei/Lei": {"Italian": "è", "English": "he/she/you are (formal)"},
        "noi": {"Italian": "siamo", "English": "we are"},
        "voi": {"Italian": "siete", "English": "you are (plural)"},
        "loro": {"Italian": "sono", "English": "they are"}
    },
    "AVERE": {
        "io": {"Italian": "ho", "English": "I have"},
        "tu": {"Italian": "hai", "English": "you have (informal)"},
        "lui/lei/Lei": {"Italian": "ha", "English": "he/she/you have (formal)"},
        "noi": {"Italian": "abbiamo", "English": "we have"},
        "voi": {"Italian": "avete", "English": "you have (plural)"},
        "loro": {"Italian": "hanno", "English": "they have"}
    },
    "FARE": {
        "io": {"Italian": "faccio", "English": "I do/make"},
        "tu": {"Italian": "fai", "English": "you do/make (informal)"},
        "lui/lei/Lei": {"Italian": "fa", "English": "he/she/you do/make (formal)"},
        "noi": {"Italian": "facciamo", "English": "we do/make"},
        "voi": {"Italian": "fate", "English": "you do/make (plural)"},
        "loro": {"Italian": "fanno", "English": "they do/make"}
    },
    "DIRE": {
        "io": {"Italian": "dico", "English": "I say"},
        "tu": {"Italian": "dici", "English": "you say (informal)"},
        "lui/lei/Lei": {"Italian": "dice", "English": "he/she/you say (formal)"},
        "noi": {"Italian": "diciamo", "English": "we say"},
        "voi": {"Italian": "dite", "English": "you say (plural)"},
        "loro": {"Italian": "dicono", "English": "they say"}
    },
    "OTTENERE": {
        "io": {"Italian": "ottengo", "English": "I get"},
        "tu": {"Italian": "ottieni", "English": "you get (informal)"},
        "lui/lei/Lei": {"Italian": "ottiene", "English": "he/she/you get (formal)"},
        "noi": {"Italian": "otteniamo", "English": "we get"},
        "voi": {"Italian": "ottenete", "English": "you get (plural)"},
        "loro": {"Italian": "ottengono", "English": "they get"}
    },
    "FABBRICARE": {
            "io": {"Italian": "fabbrico", "English": "I make"},
            "tu": {"Italian": "fabbrichi", "English": "you make (informal)"},
            "lui/lei/Lei": {"Italian": "fabbrica", "English": "he/she/you make (formal)"},
            "noi": {"Italian": "fabbrichiamo", "English": "we make"},
            "voi": {"Italian": "fabbricate", "English": "you make (plural)"},
            "loro": {"Italian": "fabbricano", "English": "they make"}
    },
    "ANDARE": {
        "io": {"Italian": "vado", "English": "I go"},
        "tu": {"Italian": "vai", "English": "you go (informal)"},
        "lui/lei/Lei": {"Italian": "va", "English": "he/she/you go (formal)"},
        "noi": {"Italian": "andiamo", "English": "we go"},
        "voi": {"Italian": "andate", "English": "you go (plural)"},
        "loro": {"Italian": "vanno", "English": "they go"}
    },
    "CONOSCERE": {
        "io": {"Italian": "conosco", "English": "I know"},
        "tu": {"Italian": "conosci", "English": "you know (informal)"},
        "lui/lei/Lei": {"Italian": "conosce", "English": "he/she/you know (formal)"},
        "noi": {"Italian": "conosciamo", "English": "we know"},
        "voi": {"Italian": "conoscete", "English": "you know (plural)"},
        "loro": {"Italian": "conoscono", "English": "they know"}
    },
    "PRENDERE": {
        "io": {"Italian": "prendo", "English": "I take"},
        "tu": {"Italian": "prendi", "English": "you take (informal)"},
        "lui/lei/Lei": {"Italian": "prende", "English": "he/she/you take (formal)"},
        "noi": {"Italian": "prendiamo", "English": "we take"},
        "voi": {"Italian": "prendete", "English": "you take (plural)"},
        "loro": {"Italian": "prendono", "English": "they take"}
    },
    "VEDERE": {
        "io": {"Italian": "vedo", "English": "I see"},
        "tu": {"Italian": "vedi", "English": "you see (informal)"},
        "lui/lei/Lei": {"Italian": "vede", "English": "he/she/you see (formal)"},
        "noi": {"Italian": "vediamo", "English": "we see"},
        "voi": {"Italian": "vedete", "English": "you see (plural)"},
        "loro": {"Italian": "vedono", "English": "they see"}
    },
    "VENIRE": {
        "io": {"Italian": "vengo", "English": "I come"},
        "tu": {"Italian": "vieni", "English": "you come (informal)"},
        "lui/lei/Lei": {"Italian": "viene", "English": "he/she/you come (formal)"},
        "noi": {"Italian": "veniamo", "English": "we come"},
        "voi": {"Italian": "venite", "English": "you come (plural)"},
        "loro": {"Italian": "vengono", "English": "they come"}
    },
    "PENSARE": {
        "io": {"Italian": "penso", "English": "I think"},
        "tu": {"Italian": "pensi", "English": "you think (informal)"},
        "lui/lei/Lei": {"Italian": "pensa", "English": "he/she/you think (formal)"},
        "noi": {"Italian": "pensiamo", "English": "we think"},
        "voi": {"Italian": "pensate", "English": "you think (plural)"},
        "loro": {"Italian": "pensano", "English": "they think"}
    },
    "GUARDARE": {
        "io": {"Italian": "guardo", "English": "I look"},
        "tu": {"Italian": "guardi", "English": "you look (informal)"},
        "lui/lei/Lei": {"Italian": "guarda", "English": "he/she/you look (formal)"},
        "noi": {"Italian": "guardiamo", "English": "we look"},
        "voi": {"Italian": "guardate", "English": "you look (plural)"},
        "loro": {"Italian": "guardano", "English": "they look"}
    },
    "VOLERE": {
        "io": {"Italian": "voglio", "English": "I want"},
        "tu": {"Italian": "vuoi", "English": "you want (informal)"},
        "lui/lei/Lei": {"Italian": "vuole", "English": "he/she/you want (formal)"},
        "noi": {"Italian": "vogliamo", "English": "we want"},
        "voi": {"Italian": "volete", "English": "you want (plural)"},
        "loro": {"Italian": "vogliono", "English": "they want"}
    },
    "DARE": {
        "io": {"Italian": "do", "English": "I give"},
        "tu": {"Italian": "dai", "English": "you give (informal)"},
        "lui/lei/Lei": {"Italian": "dà", "English": "he/she/you give (formal)"},
        "noi": {"Italian": "diamo", "English": "we give"},
        "voi": {"Italian": "date", "English": "you give (plural)"},
        "loro": {"Italian": "danno", "English": "they give"}
    },"USARE": {
        "io": {"Italian": "uso", "English": "I use"},
        "tu": {"Italian": "usi", "English": "you use (informal)"},
        "lui/lei/Lei": {"Italian": "usa", "English": "he/she/you use (formal)"},
        "noi": {"Italian": "usiamo", "English": "we use"},
        "voi": {"Italian": "usate", "English": "you use (plural)"},
        "loro": {"Italian": "usano", "English": "they use"}
    },
    "TROVARE": {
        "io": {"Italian": "trovo", "English": "I find"},
        "tu": {"Italian": "trovi", "English": "you find (informal)"},
        "lui/lei/Lei": {"Italian": "trova", "English": "he/she/you find (formal)"},
        "noi": {"Italian": "troviamo", "English": "we find"},
        "voi": {"Italian": "trovate", "English": "you find (plural)"},
        "loro": {"Italian": "trovano", "English": "they find"}
    },
    "CHIEDERE": {
        "io": {"Italian": "chiedo", "English": "I ask"},
        "tu": {"Italian": "chiedi", "English": "you ask (informal)"},
        "lui/lei/Lei": {"Italian": "chiede", "English": "he/she/you ask (formal)"},
        "noi": {"Italian": "chiediamo", "English": "we ask"},
        "voi": {"Italian": "chiedete", "English": "you ask (plural)"},
        "loro": {"Italian": "chiedono", "English": "they ask"}
    },
    "LAVORARE": {
        "io": {"Italian": "lavoro", "English": "I work"},
        "tu": {"Italian": "lavori", "English": "you work (informal)"},
        "lui/lei/Lei": {"Italian": "lavora", "English": "he/she/you work (formal)"},
        "noi": {"Italian": "lavoriamo", "English": "we work"},
        "voi": {"Italian": "lavorate", "English": "you work (plural)"},
        "loro": {"Italian": "lavorano", "English": "they work"}
    },
    "SEMBRARE": {
        "io": {"Italian": "sembro", "English": "I seem"},
        "tu": {"Italian": "sembri", "English": "you seem (informal)"},
        "lui/lei/Lei": {"Italian": "sembra", "English": "he/she/you seem (formal)"},
        "noi": {"Italian": "sembriamo", "English": "we seem"},
        "voi": {"Italian": "sembrate", "English": "you seem (plural)"},
        "loro": {"Italian": "sembrano", "English": "they seem"}
    },
    "SENTIRE": {
        "io": {"Italian": "sento", "English": "I feel"},
        "tu": {"Italian": "senti", "English": "you feel (informal)"},
        "lui/lei/Lei": {"Italian": "sente", "English": "he/she/you feel (formal)"},
        "noi": {"Italian": "sentiamo", "English": "we feel"},
        "voi": {"Italian": "sentite", "English": "you feel (plural)"},
        "loro": {"Italian": "sentono", "English": "they feel"}
    },
    "PROVARE": {
        "io": {"Italian": "provo", "English": "I try"},
        "tu": {"Italian": "provi", "English": "you try (informal)"},
        "lui/lei/Lei": {"Italian": "prova", "English": "he/she/you try (formal)"},
        "noi": {"Italian": "proviamo", "English": "we try"},
        "voi": {"Italian": "provate", "English": "you try (plural)"},
        "loro": {"Italian": "provano", "English": "they try"}
    },
    "PARTIRE": {
        "io": {"Italian": "parto", "English": "I leave"},
        "tu": {"Italian": "parti", "English": "you leave (informal)"},
        "lui/lei/Lei": {"Italian": "parte", "English": "he/she/you leave (formal)"},
        "noi": {"Italian": "partiamo", "English": "we leave"},
        "voi": {"Italian": "partite", "English": "you leave (plural)"},
        "loro": {"Italian": "partono", "English": "they leave"}
    },
    "CHIAMARE": {
        "io": {"Italian": "chiamo", "English": "I call"},
        "tu": {"Italian": "chiami", "English": "you call (informal)"},
        "lui/lei/Lei": {"Italian": "chiama", "English": "he/she/you call (formal)"},
        "noi": {"Italian": "chiamiamo", "English": "we call"},
        "voi": {"Italian": "chiamate", "English": "you call (plural)"},
        "loro": {"Italian": "chiamano", "English": "they call"}
    },
    "RIDERE": {
        "io": {"Italian": "rido", "English": "I laugh"},
        "tu": {"Italian": "ridi", "English": "you laugh (informal)"},
        "lui/lei/Lei": {"Italian": "ride", "English": "he/she/you laugh (formal)"},
        "noi": {"Italian": "ridiamo", "English": "we laugh"},
        "voi": {"Italian": "ridete", "English": "you laugh (plural)"},
        "loro": {"Italian": "ridono", "English": "they laugh"}
    },
    "CONTINUARE": {
        "io": {"Italian": "continuo", "English": "I continue"},
        "tu": {"Italian": "continui", "English": "you continue (informal)"},
        "lui/lei/Lei": {"Italian": "continua", "English": "he/she/you continue (formal)"},
        "noi": {"Italian": "continuiamo", "English": "we continue"},
        "voi": {"Italian": "continuate", "English": "you continue (plural)"},
        "loro": {"Italian": "continuano", "English": "they continue"}
    },
    "COMPRARE": {
        "io": {"Italian": "compro", "English": "I buy"},
        "tu": {"Italian": "compri", "English": "you buy (informal)"},
        "lui/lei/Lei": {"Italian": "compra", "English": "he/she/you buy (formal)"},
        "noi": {"Italian": "compriamo", "English": "we buy"},
        "voi": {"Italian": "comprate", "English": "you buy (plural)"},
        "loro": {"Italian": "comprano", "English": "they buy"}
    },
    "SUGGERIRE": {
        "io": {"Italian": "suggerisco", "English": "I suggest"},
        "tu": {"Italian": "suggerisci", "English": "you suggest (informal)"},
        "lui/lei/Lei": {"Italian": "suggerisce", "English": "he/she/you suggest (formal)"},
        "noi": {"Italian": "suggeriamo", "English": "we suggest"},
        "voi": {"Italian": "suggerite", "English": "you suggest (plural)"},
        "loro": {"Italian": "suggeriscono", "English": "they suggest"}
    },
    "APRIRE": {
        "io": {"Italian": "apro", "English": "I open"},
        "tu": {"Italian": "apri", "English": "you open (informal)"},
        "lui/lei/Lei": {"Italian": "apre", "English": "he/she/you open (formal)"},
        "noi": {"Italian": "apriamo", "English": "we open"},
        "voi": {"Italian": "aprite", "English": "you open (plural)"},
        "loro": {"Italian": "aprono", "English": "they open"}
    },
    "CAMMINARE": {
        "io": {"Italian": "cammino", "English": "I walk"},
        "tu": {"Italian": "cammini", "English": "you walk (informal)"},
        "lui/lei/Lei": {"Italian": "cammina", "English": "he/she/you walk (formal)"},
        "noi": {"Italian": "camminiamo", "English": "we walk"},
        "voi": {"Italian": "camminate", "English": "you walk (plural)"},
        "loro": {"Italian": "camminano", "English": "they walk"}
    },
    "ASCOLTARE": {
        "io": {"Italian": "ascolto", "English": "I listen"},
        "tu": {"Italian": "ascolti", "English": "you listen (informal)"},
        "lui/lei/Lei": {"Italian": "ascolta", "English": "he/she/you listen (formal)"},
        "noi": {"Italian": "ascoltiamo", "English": "we listen"},
        "voi": {"Italian": "ascoltate", "English": "you listen (plural)"},
        "loro": {"Italian": "ascoltano", "English": "they listen"}
    },
    "CORRERE": {
        "io": {"Italian": "corro", "English": "I run"},
        "tu": {"Italian": "corri", "English": "you run (informal)"},
        "lui/lei/Lei": {"Italian": "corre", "English": "he/she/you run (formal)"},
        "noi": {"Italian": "corriamo", "English": "we run"},
        "voi": {"Italian": "correte", "English": "you run (plural)"},
        "loro": {"Italian": "corrono", "English": "they run"}
    },
    "RISPONDERE": {
        "io": {"Italian": "rispondo", "English": "I answer"},
        "tu": {"Italian": "rispondi", "English": "you answer (informal)"},
        "lui/lei/Lei": {"Italian": "risponde", "English": "he/she/you answer (formal)"},
        "noi": {"Italian": "rispondiamo", "English": "we answer"},
        "voi": {"Italian": "rispondete", "English": "you answer (plural)"},
        "loro": {"Italian": "rispondono", "English": "they answer"}
    },
    "METTERE": {
        "io": {"Italian": "metto", "English": "I place"},
        "tu": {"Italian": "metti", "English": "you place (informal)"},
        "lui/lei/Lei": {"Italian": "mette", "English": "he/she/you place (formal)"},
        "noi": {"Italian": "mettiamo", "English": "we place"},
        "voi": {"Italian": "mettete", "English": "you place (plural)"},
        "loro": {"Italian": "mettono", "English": "they place"}
    },
    "VIAGGIARE": {
        "io": {"Italian": "viaggio", "English": "I travel"},
        "tu": {"Italian": "viaggi", "English": "you travel (informal)"},
        "lui/lei/Lei": {"Italian": "viaggia", "English": "he/she/you travel (formal)"},
        "noi": {"Italian": "viaggiamo", "English": "we travel"},
        "voi": {"Italian": "viaggiate", "English": "you travel (plural)"},
        "loro": {"Italian": "viaggiano", "English": "they travel"}
    },
    "ESPRIMERE": {
        "io": {"Italian": "esprimo", "English": "I express"},
        "tu": {"Italian": "esprimi", "English": "you express (informal)"},
        "lui/lei/Lei": {"Italian": "esprime", "English": "he/she/you express (formal)"},
        "noi": {"Italian": "esprimiamo", "English": "we express"},
        "voi": {"Italian": "esprimete", "English": "you express (plural)"},
        "loro": {"Italian": "esprimono", "English": "they express"}
    },
    "CONCENTRARE": {
        "io": {"Italian": "concentro", "English": "I concentrate"},
        "tu": {"Italian": "concentri", "English": "you concentrate (informal)"},
        "lui/lei/Lei": {"Italian": "concentra", "English": "he/she/you concentrate (formal)"},
        "noi": {"Italian": "concentriamo", "English": "we concentrate"},
        "voi": {"Italian": "concentrate", "English": "you concentrate (plural)"},
        "loro": {"Italian": "concentrano", "English": "they concentrate"}
    },
    "PREPARARE": {
        "io": {"Italian": "preparo", "English": "I prepare"},
        "tu": {"Italian": "prepari", "English": "you prepare (informal)"},
        "lui/lei/Lei": {"Italian": "prepara", "English": "he/she/you prepare (formal)"},
        "noi": {"Italian": "prepariamo", "English": "we prepare"},
        "voi": {"Italian": "preparate", "English": "you prepare (plural)"},
        "loro": {"Italian": "preparano", "English": "they prepare"}
    },
    "PIANIFICARE": {
        "io": {"Italian": "pianifico", "English": "I plan"},
        "tu": {"Italian": "pianifichi", "English": "you plan (informal)"},
        "lui/lei/Lei": {"Italian": "pianifica", "English": "he/she/you plan (formal)"},
        "noi": {"Italian": "pianifichiamo", "English": "we plan"},
        "voi": {"Italian": "pianificate", "English": "you plan (plural)"},
        "loro": {"Italian": "pianificano", "English": "they plan"}
    },
    "TENTARE": {
        "io": {"Italian": "tento", "English": "I attempt"},
        "tu": {"Italian": "tenti", "English": "you attempt (informal)"},
        "lui/lei/Lei": {"Italian": "tenta", "English": "he/she/you attempt (formal)"},
        "noi": {"Italian": "tentiamo", "English": "we attempt"},
        "voi": {"Italian": "tentate", "English": "you attempt (plural)"},
        "loro": {"Italian": "tentano", "English": "they attempt"}
    },
    "SPOSARE": {
        "io": {"Italian": "sposo", "English": "I marry"},
        "tu": {"Italian": "sposi", "English": "you marry (informal)"},
        "lui/lei/Lei": {"Italian": "sposa", "English": "he/she/you marry (formal)"},
        "noi": {"Italian": "sposiamo", "English": "we marry"},
        "voi": {"Italian": "sposate", "English": "you marry (plural)"},
        "loro": {"Italian": "sposano", "English": "they marry"}
    },
    "ESPERIRE": {
        "io": {"Italian": "esperisco", "English": "I experience"},
        "tu": {"Italian": "esperisci", "English": "you experience (informal)"},
        "lui/lei/Lei": {"Italian": "esperisce", "English": "he/she/you experience (formal)"},
        "noi": {"Italian": "esperiamo", "English": "we experience"},
        "voi": {"Italian": "esperite", "English": "you experience (plural)"},
        "loro": {"Italian": "esperiscono", "English": "they experience"}
    },"RACCOMANDARE": {
        "io": {"Italian": "raccomando", "English": "I recommend"},
        "tu": {"Italian": "raccomandi", "English": "you recommend (informal)"},
        "lui/lei/Lei": {"Italian": "raccomanda", "English": "he/she/you recommend (formal)"},
        "noi": {"Italian": "raccomandiamo", "English": "we recommend"},
        "voi": {"Italian": "raccomandate", "English": "you recommend (plural)"},
        "loro": {"Italian": "raccomandano", "English": "they recommend"}
    },
    "CAVALCARE": {
        "io": {"Italian": "cavalco", "English": "I ride"},
        "tu": {"Italian": "cavalchi", "English": "you ride (informal)"},
        "lui/lei/Lei": {"Italian": "cavalca", "English": "he/she/you ride (formal)"},
        "noi": {"Italian": "cavalchiamo", "English": "we ride"},
        "voi": {"Italian": "cavalcate", "English": "you ride (plural)"},
        "loro": {"Italian": "cavalcano", "English": "they ride"}
    },
    "DOMANDARE": {
        "io": {"Italian": "domando", "English": "I question"},
        "tu": {"Italian": "domandi", "English": "you question (informal)"},
        "lui/lei/Lei": {"Italian": "domanda", "English": "he/she/you question (formal)"},
        "noi": {"Italian": "domandiamo", "English": "we question"},
        "voi": {"Italian": "domandate", "English": "you question (plural)"},
        "loro": {"Italian": "domandano", "English": "they question"}
    },
    "MIGLIORARE": {
        "io": {"Italian": "miglioro", "English": "I enhance"},
        "tu": {"Italian": "migliori", "English": "you enhance (informal)"},
        "lui/lei/Lei": {"Italian": "migliora", "English": "he/she/you enhance (formal)"},
        "noi": {"Italian": "miglioriamo", "English": "we enhance"},
        "voi": {"Italian": "migliorate", "English": "you enhance (plural)"},
        "loro": {"Italian": "migliorano", "English": "they enhance"}
    },
    "TELEFONARE": {
        "io": {"Italian": "telefono", "English": "I telephone"},
        "tu": {"Italian": "telefoni", "English": "you telephone (informal)"},
        "lui/lei/Lei": {"Italian": "telefona", "English": "he/she/you telephone (formal)"},
        "noi": {"Italian": "telefoniamo", "English": "we telephone"},
        "voi": {"Italian": "telefonate", "English": "you telephone (plural)"},
        "loro": {"Italian": "telefonano", "English": "they telephone"}
    }}

# def populate_verbs():
#     for verb, conjugations in common_verbs_dict.items():
#         new_verb = Verb(infinitive=verb, conjugations=conjugations)
#         db.session.add(new_verb)
#     db.session.commit()

if __name__ == '__main__':
    verb = Verb.query.filter_by(infinitive='TELEFONARE').first()
    if verb:
        print(verb.conjugations)
