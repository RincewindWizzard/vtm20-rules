from collections import namedtuple
Background = namedtuple('Background', ['name', 'levels', 'description'])
backgrounds = [
  Background(
    name = "Allies",
    levels = [
      'One ally of moderate infuence and power',
      'Two allies, both of moderate power',
      'Three allies, one of whom is quite infuential',
      'Four allies, one of whom is very infuential',
      'Five allies, one of whom is extremely infuential'
    ],
    description = """Allies are mortals who support and help you - family, friends or even a mortal organization that owes you some loyalty. Although allies aid you willingly, without coaxing or coercion, they are not always available to offer assistance; they have their own concerns and can do only so much for the sake of your relationship. However, they might have some useful Background Traits of their own, and could provide you with indirect access to their contacts, infuence or resources. Allies are typically persons of infuence and power in your home city. They can be of almost any sort, depending on what your Storyteller will allow. You may have friends in the precinct morgue, at a prominent blog, among the high society of local celebrities or at a construction site. Your Allies might be a clan of nomads who move their mobile home camp around the area, or they might be a family of generations of police officers. You may even count the mayor himself among your friends, depending on how many dots you spend on this Trait. Your Allies are generally trustworthy (though they probably don’t know that you’re a vampire or even that vampires exist). However, nothing comes for free. If you wind up drawing favors from your friend in the Cosa Nostra, he’ll probably ask you to do him a favor in kind in the future. This often leads to the beginning of a story. Allies may be pooled among a coterie of characters."""
  ),
  Background(
    name = "Alternate Identity",
    levels = [
      'You are new at this identity game. Sometimes you slip and forget your other persona.',
      'You are well grounded in your alternate identity. You are convincing enough to play the part of a doctor, lawyer, funeral salesman, drug-smuggler or a capable spy.',
      'You have a fair reputation as your alternate persona and get name-recognition in the area where you have infiltrated.',
      'Your alternate identity has respect and trust within your area of infiltration.',
      'You command respect in your area of infiltration, and you may even have accumulated a bit of infuence. You have the trust (or at least the recognition) of many powerful individuals within your area.'
    ],
    description = """You maintain an alternate identity, complete with papers, birth certificates or any other documentation you desire. Only a few may know your real name or identity. Your alternate persona may be highly involved in organized crime, a member of the opposite Sect, a con artist who uses alternate identities for her game or you may simply gather information about the enemy. Indeed, some vampires may know you as one individual while others believe you to be someone else entirely."""
  ),
  Background(
    name = "Black Hand Membership",
    levels = [
      'You are a grunt; you may call upon one Black Hand member once per story.',
      'You are known and respected in the Black Hand; you may call upon two Black Hand members once per story.',
      'You are held in the Black Hand’s regard; you may call upon five Black Hand members once per story.',
      'You are a hero among members of the Black Hand; you may call upon seven Black Hand members twice per story (but you’d better have just cause - if it seems you’re becoming soft, you may lose points in this Background). You may also lead large numbers of Hand members into action should it ever become necessary.',
      'You are part of Black Hand legend; you may call upon 12 Black Hand members twice per story (but see the preceding caution). You may also lead large numbers of Hand members into action should it ever become necessary. The Seraphim may even seek your counsel on matters of import.'
    ],
    description = """This Background is for Sabbat characters only.
You are a member of the feared Black Hand, the body of soldiers and assassins that serves the Sabbat fervently. Having this Background indicates that you are a full-fledged member of the organization, and you have all the responsibilities and benefits that accompany membership. You may call upon members of the Black Hand to aid you, should you ever need it. Of course, this ability is a two-way street, and other Hand members may call upon you to aid them. Thus, you may find yourself assigned to perform assassinations, lend martial aid, or even further the political ends of the Hand as a diplomat or spy. You may also be required to attend crusades that take you away from your pack. All members of the Black Hand must heed the call of another Hand member, especially the superiors of the faction. Being a member of the Black Hand is a prestigious matter, and other members of the Sabbat respect the organization. When dealing with other Sabbat, should you choose to reveal your affiliation with the Hand, you may add your rating in this Background to any Social dice pools, even after Status or other Abilities have been taken into account. Most Hand members, however, choose not to reveal their allegiance. The Black Hand is also remarkably adept at hunting down Sabbat who claim membership in the Sect but do not truly belong - liars, beware."""
  ),
  Background(
    name = "Contacts",
    levels = [
      'One major contact',
      'Two major contacts',
      'Three major contacts',
      'Four major contacts',
      'Five major contacts'
    ],
    description = """You know people all over the city. When you start making phone calls around your network, the amount of information you can dig up is impressive. Rather than friends you can rely on to help you, like Allies, Contacts are largely people whom you can bribe, manipulate or coerce into offering information. You also have a few major Contacts - associates who can give you accurate information in their fields of expertise. You should describe each major contact in some detail before the game begins. In addition to your major contacts, you also have a number of minor contacts spread throughout the city. Your major contact might be in the district attorney’s office, while your minor contacts might include beatcops, DMV clerks, club bouncers or members of an online social network. You don’t need to detail these various “passing acquaintances” before play. Instead, to successfully get in touch with a minor contact, you should roll your Contacts rating (difficulty 7). You can reach one minor contact for each success. Of course, you still have to convince them to give you the information you need, assuming they can get it. Contacts may be pooled within the characters’ co-terie."""
  ),
  Background(
    name = "Domain",
    levels = [
      'A single small building, such as a single-family home or a social establishment - enough for a basic haven.',
      'A church, factory, warehouse, mid-rise or other large structure - a location with ready but easily controllable access to the outside world.',
      'A high-rise, city block, or an important intersection - a location or area that offers areas for concealment as well as controlled access.',
      'A sewer subsection, a network of service tunnels, the enclave of homes on a hill overlooking the city - a place with inherently protective features, such as an isolated mountain road, bridge-only access, or vigilant private security force.',
      'An entire neighborhood, an ethnic subdivision like “Chinatown” or “Little Italy,” or a whole suburb. As noted previously, characters in a coterie can share their domain resources for better results. Six to eight dots secure all of a small town or a distinct city region as a domain. Ten to 15 dots secure an important but not geographically huge city sector, such as “the docks” or “Highland Park”. A large city itself might be a hundred-plus Domain points, as with Atlanta, Dallas, Geneva or Baghdad. A city such as New York, London, Paris, Rome, Sao Paolo or Shanghai would require many hundreds of Domain points.'
    ],
    description = """Domain is physical territory (usually within the chronicle’s central city) to which your character controls access for the purpose of feeding. Some Kindred refer to their domain as hunting grounds, and most jealously guard their domains, even invoking the Tradition of the same name to protect their claims. As part of this Background, the character’s claim to the domain is recognized by the Prince or some other Kindred authority in the city where it is located. The Kindred who claims the domain can’t keep the living inhabitants from going about their business, nor does she exercise any direct infuence over them, but she can keep watch herself and mind their comings and goings. She can also have Allies or Retainers specifically look for unfamiliar vampires and alert her when they find some. Domain refers specifically to the geography (in most cases a neighborhood or street) and properties on it, as opposed to the people who may dwell there (which is the emphasis of Herd). Domain plays an importantpart in Kindred society - vampires who lack significant Domain seldom earn respect - but it isn’t an automatic entitlement to status among the Damned. You may designate one or more dots in Domain to increase the security of your character’s territory rather than its size. Each dot so assigned to security provides a +1 difficulty penalty to efforts to intrude into the domain by anyone your character hasn’t specifically allowed in, and a -1 difficulty bonus to efforts by your character to identify and track intruders in the domain. A Domain of one dot’s size and two dots’ security, for instance, is small but quite resistant to intrusion, as opposed to a Domain rating of three dots’ size with no extraordinary security. Each level of Domain reduces the difficulty of hunting checks by one for your character and those whom the character allows in. It also adds to your starting (not maximum) blood pool. If you use the domain security option, each dot of domain security raises the difficulty of hunting checks by one for uninvited vampires. See p. 259 for more information on hunting. Domain (both size and security) can be used with pooled Background points."""
  ),
  Background(
    name = "Fame",
    levels = [
      'You’re known to a select sub-culture - local club-goers, industry bloggers, or the Park Avenue set, for instance.',
      'Random people start to recognize your face; you’re a minor celebrity such as a small-time criminal or a local news anchor.',
      'You have greater renown; perhaps you’re a senator or an entertainer who regularly gets hundreds of thousands of YouTube hits.',
      'A full-blown celebrity; your name is often recognized by the average person on the street.',
      'You’re a household word. People name their children after you.'
    ],
    description = """You enjoy widespread recognition in mortal society, perhaps as an entertainer, writer, or athlete. People may enjoy just being seen with you. This gives you all manner of privileges when moving in mortal society, but can also attract an unwanted amount of attention now that you’re no longer alive. The greatest weapon fame has to offer is the ability to sway public opinion - as modern media constantly proves. Fame isn’t always tied to entertainment: A heinous criminal in a high-profile trial probably has a certain amount of fame, as do a lawmaker and a scientist who has made a popularized discovery. This Background is obviously a mixed blessing. You can certainly enjoy the privileges of your prestige - getting the best seats, being invited to events you’d otherwise miss, getting appointments with the elite - but you’re sometimes recognized when you’d rather not be. However, your enemies can’t just make you disappear without causing an undue stir, and you find it much easier to hunt in populated areas as people flock to you (reduce the difficulties of hunting rolls by one for each dot in Fame). Additionally, your Storyteller might permit you to reduce difficulties of certain Social rolls against particularly star-struck or impressionable people."""
  ),
  Background(
    name = "Generation",
    levels = [
      'Twelfth Generation: 11 blood pool, can spend 1 blood point per turn',
      'Eleventh Generation: 12 blood pool, can spend 1 blood point per turn',
      'Tenth Generation: 13 blood pool, can spend 1 blood point per turn',
      'Ninth Generation: 14 blood pool, can spend 2 blood points per turn',
      'Eighth Generation: 15 blood pool, can spend 3 blood points per turn',
      'Seventh Generation: 20 blood pool, can spend 4 blood points per turn',
      'Sixth Generation: 30 blood pool, can spend 6 blood points per turn',
      'Fifth Generation: 40 blood pool, can spend 8 blood points per turn',
      'Fourth Generation: 50 blood pool, can spend 10 blood points per turn'
    ],
    description = """This Background represents your Generation: the purity of your blood, and your proximity to the First Vampire. A high Generation rating may represent a powerful sire or a decidedly dangerous taste for diablerie. If you don’t take any dots in this Trait, you begin play as a Thirteenth Generation vampire. See p. 270 for further information."""
  ),
  Background(
    name = "Herd",
    levels = [
      'Three vessels',
      'Seven vessels',
      '15 vessels',
      '30 vessels',
      '60 vessels'
    ],
    description = """You have built a group of mortals from whom you can feed without fear. A herd may take many forms, from circles of kinky clubgoers to actual cults built around you as a god-figure. In addition to providing nourishment, your herd might come in handy for minor tasks, though they are typically not very controllable, closely connected to you, or particularly skilled (for more effective pawns, purchase Allies or Retainers). Your Herd rating adds dice to your rolls for hunting; see p. 259 for further details. Players may purchase pooled Herd with Background points."""
  ),
  Background(
    name = "Influence",
    levels = [
      'Moderately infuential; a factor in city politics',
      'Well-connected; a force in state politics',
      'Position of infuence; a factor in regional politics',
      'Broad personal power; a force in national politics',
      'Vastly infuential; a factor in global politics'
    ],
    description = """You have pull in the mortal community, whether through wealth, prestige, political office, blackmail or supernatural manipulation. Kindred with high Influence can sway, and in rare cases even control, the political and social processes of human society. Infuence represents the sum of your opinion- or policy-swaying power in your community, particularly among the police and bureaucracy. In some cases, cultivating Influence is a path to generating Resources (see below). Some rolls may require you to use Infuence in place of an Ability, particularly when attempting to sway minor bureaucrats. It’s easier to institute sweeping changes on a local level than a worldwide scale (e.g., having an “abandoned” building demolished is relatively easy, while starting a war is a bit more difficult). Infuence can be used with pooled Background points."""
  ),
  Background(
    name = "Mentor",
    levels = [
      'Mentor is an ancilla of little infuence, or a Ductus or Pack Priest.',
      'Mentor is respected: an elder or highly-decorated veteran, for instance.',
      'Mentor is heavily infuential, such as a member of the Primogen or a Bishop.',
      'Mentor has a great deal of power over the city: a Prince or Archbishop, for example.',
      'Mentor is extraordinarily powerful, perhaps even a Justicar or Cardinal.'
    ],
    description = """This Trait represents a Kindred or group of Kindred who looks out for you, offering guidance or aid once in a while. A mentor may be powerful, but his power need not be direct. Depending on the number of dots in this Background, your mentor might be nothing more than a vampire with a remarkable information network, or might be a centuries-old creature with tremendous influence and supernatural power. He may offer advice, speak to the Prince or Archbishop on your behalf, steer other elders clear of you, or warn you when you’re walking into situations you don’t understand. Most often your mentor is your sire, but it could well be any Cainite with an interest in your wellbeing. A high Mentor rating could even represent a group of like-minded vampires, such as the elders of the city’s Tremere chantry or a Black Hand cell. Bear in mind that this Trait isn’t a “Get out of Jail Free” card. Your mentor won’t necessarily arrive like the cavalry whenever you’re endangered (and if she does, you’re likely to lose a dot or more in this Background after rousing her ire). What’s more, she might occasionally expect something in return for her patronage, which can lead to a number of interesting stories. A mentor typically remains aloof, giving you useful information or advice out of camaraderie, but will abandon you without a thought if you prove an unworthy or troublesome protégé."""
  ),
  Background(
    name = "Resources",
    levels = [
      'Sufficient. You can maintain a typical residence in the style of the working class with stability, even if spending sprees come seldom.',
      'Moderate. You can display yourself as a member in good standing of the middle class, with the occasional gift and indulgence seemly for a person of even higher station. You can maintain a servant or hire specific help as necessary. A fraction of your resources are available in cash, readily portable property (like jewelry or furniture) and other valuables (such as a car or modest home) that let you maintain a standard of living at the one-dot level wherever you happen to be, for up to six months.',
      'Comfortable. You are a prominent and established member of your community, with land and an owned dwelling, and you have a reputation that lets you draw on credit at very generous terms. You likely have more tied up in equity and property than you do in ready cash. You can maintain a one-dot quality of existence wherever you are without difficulty, for as long as you choose.',
      'Wealthy. You rarely touch cash, as most of your assets exist in tangible forms that are themselves more valuable and stable than paper money. You hold more wealth than many of your local peers (if they can be called such a thing). When earning your Resources doesn’t enjoy your usual degree of attention, you can maintain a three-dot existence for up to a year, and a two-dot existence indefinitely.',
      'Extremely Wealthy. You are the model to which others strive to achieve, at least in the popular mind. Television shows, magazine spreads and gossip websites speculate about your clothing, the appointments of your numerous homes, and the luxury of your modes of transportation. You have vast and widely distributed assets, perhaps tied to the fates of nations, each with huge staffs and connections to every level of society through a region. You travel with a minimum of three-dot comforts, more with a little effort. Corporations and governments sometimes come to you to buy into stocks or bond programs.'
    ],
    description = """Resources are valuable goods whose disposition your character controls. These assets may be actual cash, but as this Background increases, they’re more likely to be investments, property or earning capital of some sort - land, industrial assets, stocks and bonds, commercial inventories, criminal infrastructure, contraband, even taxes or tithes. Remember that vampires don’t need to arrange for any food except blood and their actual needs (as opposed to wants) for shelter are very easily accommodated. Resources for vampires go mostly to pay for luxuries and the associated expenses of developing and maintaining Status, Infuence, and other Backgrounds. A character with no dots in Resources may have enough clothing and supplies to get by, or she may be destitute and squatting in a refrigerator box under an overpass. You receive a basic allowance each month based on your rating, so be certain to detail exactly where this money comes from, be it a job, trust fund or dividends (Storytellers, decide for your locality and any relevant time period what an appropriate amount of cash this monthly allowance is). After all, a Kindred’s fortune may well run out over the course of the chronicle, depending on how well he maintains it. You can also sell your less liquid resources if you need the cash, but this can take weeks or even months, depending on what exactly you’re trying to sell. Art buyers don’t just pop out of the woodwork, after all.
Players may purchase Resources for their characters with pooled Background points."""
  ),
  Background(
    name = "Retainers",
    levels = [
      'One retainer',
      'Two retainers',
      'Three retainers',
      'Four retainers',
      'Five retainers'
    ],
    description = """Not precisely Allies or Contacts, your retainers are servants, assistants or other people who are your loyal and steadfast companions. Many vampires’ servants are ghouls (p. 496) - their supernatural powers and blood bond-enforced loyalty make them the servants of choice. Retainers may also be people whom you’ve repeatedly Dominated until they have no free will left, or followers so enthralled with your Presence that their loyalty borders on blind fanaticism. Some vampires, particularly those with the Animalism Discipline, use animal ghouls as retainers. You must maintain some control over your retainers, whether through a salary, the gift of your vitae, or the use of Disciplines. Retainers are never “blindly loyal no matter what” - if you treat them poorly without exercising strict control, they might well turn on you. Retainers may be useful, but they should never be flawless. A physically powerful ghoul might be rebellious, inconveniently dull-witted, or lacking in practical skills. A loyal manservant might be physically weak or possess no real personal initiative or creativity. This Background isn’t an excuse to craft an unstoppable bodyguard or pet assassin - it’s a method to bring more fully-developed characters into the chronicle, as well as to reflect the followers for which the Kindred are notorious. Generally, retainers are more like Renfield than Anita Blake. (If the player and Storyteller agree, a player may create a more competent single Retainer by combining more points in this Background, putting more eggs in one basket, as the saying goes). Players can spend pooled Background points on Retainers."""
  ),
  Background(
    name = "Rituals",
    levels = [
      'You know a few of the auctoritas ritae (your choice).',
      'You know some of the auctoritas ritae (your choice) and a few ignoblis ritae (your choice).',
      'You know all of the auctoritas ritae and some ignoblis ritae (your choice). Also, you may create your own ignoblis ritae, given enough time (consult your Storyteller for development time and game effects).',
      'You know all the auctoritas ritae and many ignoblis ritae (your choice). You may create your own ignoblis ritae, given enough time (consult your Storyteller for development time and game effects). You are also familiar with the functions of numerous regional and pack-specific ignoblis ritae, even if you cannot perform them.',
      'You know all the auctoritas ritae and dozens of ignoblis ritae (your choice). You may create your own ignoblis ritae, given enough time (consult your Storyteller for development time and game effects). You are also familiar with the functions of almost all regional and pack-specific ignoblis ritae, even if you cannot perform them; if it’s been written down or passed around in lore, you’ve heard of it.'
    ],
    description = """This Background is for Sabbat characters only.
You know the ritae and rituals of the Sabbat, and you can enact many of them. This Background is vital to being a Pack Priest - without this Background, ritae will not function. This Background is actually a supernatural investment, drawing on the magic of the eldest Tzimisce sorcerers. Sabbat vampires who are not their pack’s priests should have an outstanding reason for acquiring this Background, as Pack Priests are loath to share their secrets with more secular members of the Sect. Some example rituals include the Vaulderie (p. 288), as well as those presented in the Appendix (p. 507)."""
  ),
  Background(
    name = "Status",
    levels = [
      'Known: a neonate/Pack Priest',
      'Respected: an ancilla/respected Ductus',
      'Infuential: an elder/Templar',
      'Powerful: a member of the Primogen/a Bishop',
      'Luminary: a Prince/Archbishop'
    ],
    description = """You have something of a reputation and standing (earned or unearned) within the local community of Kindred. Status among Camarilla society is as often derived from your sire’s status and the respect due your particular bloodline as it is by personal achievement. Among the Sabbat, status is more likely to stem from the reputation of your pack or the zeal of your outlook. Elders are known for having little respect for their juniors; this Background can mitigate that somewhat. High status within the Camarilla does not transfer to Sabbat society (and will most likely make you a notorious target for your Sect’s rivals), and vice versa. Similarly, Autarkis generally have zero Status, unless they have somehow garnered so much power and attention that they are considered forces to be reckoned with. You may have occasion to roll your Status in conjunction with a Social Trait; this refects the positive effects of your prestige. Note that Caitiff characters may not purchase Status during character creation. Caitiff are the lowest of the low, and any respect they achieve must be earned during the course of the chronicle."""
  )
]

backgrounds = dict((background.name, background) for background in backgrounds)
