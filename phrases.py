# define ANJAs vocabulary
responses = [
[r'Ich brauche (.*)',
    ["Warum brauchst du {0}?",
    "Würde es dir wirklich helfen, {0} zu bekommen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r'Warum machst du nicht ([^\?]*)\??',
    ["Glaubst du wirklich, dass ich nicht {0} kann?",
    "Vielleicht werde ich irgendwann {0}.",
    "Willst du wirklich, dass ich {0} mache?"]],

    [r'Warum kann ich nicht ([^\?]*)\??',
    ["Denkst du, dass du in der Lage sein solltest, {0}?",
    "Wenn du {0} könntest, was würdest du tun?",
    "Ich weiß nicht -- warum kannst du nicht {0}?",
    "Hast du es wirklich versucht?"]],

    [r'Ich kann nicht (.*)',
    ["Wie weißt du, dass du nicht {0} kannst?",
    "Vielleicht könntest du {0}, wenn du es versuchst.",
    "Was würde es für dich bedeuten, {0} zu können?"]],

    [r'Ich bin (.*)',
    ["Bist du zu mir gekommen, weil du {0} bist?",
    "Wie lange bist du schon {0}?",
    "Warum glaubst du, dass du {0} bist?"]],

    [r'Bist du ([^\?]*)\??',
    ["Warum ist es wichtig, ob ich {0} bin?",
    "Würdest du es bevorzugen, wenn ich nicht {0} wäre?",
    "Vielleicht glaubst du, dass ich {0} bin.",
    "Ich könnte {0} sein -- was denkst du?"]],

    [r'Was (.*)',
    ["Warum fragst du das?",
    "Wie würde dir eine Antwort darauf helfen?",
    "Was denkst du?"]],

    [r'Wie (.*)',
    ["Wie denkst du?",
    "Vielleicht kannst du deine eigene Frage beantworten.",
    "Was möchtest du wirklich wissen?"]],

    [r'Weil (.*)',
    ["Ist das der wirkliche Grund?",
    "Welche anderen Gründe fallen dir ein?",
    "Gilt dieser Grund auch für etwas anderes?",
    "Wenn {0}, was muss sonst noch wahr sein?"]],

    [r'(.*) entschuldigung (.*)',
    ["Es gibt viele Situationen, in denen keine Entschuldigung nötig ist.",
    "Was fühlst du, wenn du dich entschuldigst?"]],

    [r'Ich denke (.*)',
    ["Zweifelst du an {0}?",
    "Denkst du wirklich so?",
    "Aber du bist dir nicht sicher, dass {0}?"]],

    [r'(.*) Freund (.*)',
    ["Erzähl mir mehr über deinen Freund.",
    "Wie lange kennst du deinen Freund schon?"]],

    [r'(.*) Freundin (.*)',
     ["Erzähl mir mehr über deine Freundin.",
      "Wie lange kennst du deine Freundin schon?"]],

    [r'(.*) Freunde (.*)',
     ["Erzähl mir mehr über deine Freunde.",
      "Wenn du an einen Freund denkst, was fällt dir ein?",
      "Warum erzählst du mir nicht von einem Freund aus deiner Kindheit?"]],

    [r'Ja',
    ["Du scheinst ziemlich sicher zu sein.",
    "OK, aber kannst du das etwas genauer erklären?"]],

    [r'Nein',
     ["Wieso nicht?",
      "Bist du dir sicher?"]],

    [r'Ich fühle mich (.*)',
     ["Weshalb fühlst du dich {0}?",
      "Woher kommen diese Gefühle?",
      "Was ist die Ursache, dass du dich {0} fühlst?"]],

    [r'(?i)(?!nicht)(.*) gut (.*)',
     ["Es freut mich das zu hören.",
      "Wie lange ist das schon so?"]],

    [r'(?i)(?!nicht)(.*) super (.*)',
     ["Es freut mich das zu hören!",
      "Das ist toll!"]],

    [r'(?i)(?!nicht)(.*) schlecht (.*)',
     ["Es tut mir leid, dass du so fühlst.",
      "Wie geht es dir dabei?"]],

    [r'Mir geht es (.*)',
     ["Weshalb fühlst du dich {0}?",
      "Woher kommen diese Gefühle?",
      "Und wie kommt das?"]],

    [r'(.*)\?',
     ["Warum fragst du das?",
      "Bitte überlege, ob du deine eigene Frage beantworten kannst.",
      "Vielleicht liegt die Antwort in dir selbst?",
      "Warum sagst du es mir nicht?"]],

    [r'(.*)',
     ["Ändern wir ein wenig den Fokus... Erzähl mir von deiner Familie.",
      "Ahaaaa und wie fühlst du dich dabei? :writing_hand:"]]
]