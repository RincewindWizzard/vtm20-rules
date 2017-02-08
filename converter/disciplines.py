from collections import namedtuple
Discipline = namedtuple('Discipline', ['name', 'sorcery', 'powers', 'description'])
Power = namedtuple('Power', ['name', 'discipline', 'level', 'description'])
disciplines = [
  Discipline(
    name='Visceratika',
    sorcery=False,
    powers= [
      Power(
        name='Skin of the Chameleon',
        discipline='visceratika',
        level=1,
        description="""This basic power has saved countless Gargoyles breaching the Masquerade - and has allowed just as many to ambush unsuspecting intruders. When Skin of the Chameleon is in effect, the Gargoyle’s skin takes on the color and texture of the surrounding environment. This coloration changes reflexively as long as the Gargoyle maintains a walking pace or slower. More rapid movement causes the Gargoyle’s appearance to blur, negating the camouflaging effect. If this power is used while the Gargoyle is in flight, his skin becomes a reasonable facsimile of the night sky (though it will not shift to mimic nearby skyscrapers or star patterns, and a black silhouette against a brightly lit skyline is likely to be noticed).
_System_: The player spends one blood point. For the rest of the scene, the Gargoyle’s Stealth dice pool is increased by five. This power is subject to the limitations described above. Any ground movement faster than a walk negates this power’s effect, as does flight (at the Storyteller’s discretion)."""
      ),
      Power(
        name='Scry the Hearthstone',
        discipline='visceratika',
        level=2,
        description="""The Gargoyles’ first function for the Tremere was that of guardian and watchdog. This power allows them to know instinctively where anyone is inside a given structure. It even allows the Gargoyle to detect characters concealed by magical means, if the Slave is perceptive enough.
_System_: The player spends a Willpower point to activate this power, which remains in effect as long as the Gargoyle is within or in contact with the target structure, or until the next sunset. Scry the Hearthstone may be used on anything up to the size of a cave complex, a large theatre, a parking garage, or a mansion. The character gains an innate sense of the location and approximate size and physical condition of all living (or unliving) beings within the structure. To pinpoint a specific individual’s location with this power, the player must succeed in a ^Perception + Awareness^ roll (difficulty 6). If the subject is attempting to hide, he may oppose this roll with a roll of Wits + Stealth (difficulty 6). Scry the Hearthstone may be used to detect the presence of characters who are under Obfuscate or similar powers. In this case, the Gargoyle only knows that there is someone present - she cannot actually see the individual in question. To determine the Gargoyle’s ability to detect Obfuscated characters, compare the relative levels of the Gargoyle’s Visceratika minus one and the intruder’s Obfuscate as per the “Seeing the Unseen” sidebar on p.142."""
      ),
      Power(
        name='Bond with the Mountain',
        discipline='visceratika',
        level=3,
        description="""The Gargoyle sinks into a stone surface, disappearing into the rock until he wishes to reappear. This power allowed Gargoyles to invade their masters’ enemies’ strongholds, fight until sunrise, then meld with the rocks or stone walls and reappear the next evening. In modern nights, it can take the place of a haven for itinerant Runaways. Unlike the Earth Meld power (p.199) which it resembles, Bond with the Mountain does not conceal the Gargoyle completely. A faint outline of his body can be seen in the rock where he hides.
_System_: The player spends two blood points, and the merge takes four turns to complete. This power functions in a fashion similar to the Protean 3 power of Earth Meld, and may only be performed upon bare rock or a similar substance. However, the Gargoyle does not sink fully into the substance with which he merges, and his outline can be detected within the stone with a successful Perception + Alertness roll (difficulty 9). A Gargoyle attacked while Bonded with the Mountain has triple his normal soak dice pool against all forms of attack. However, if he sustains three or more lethal health levels of damage from a single attack, he is forced out of his bond and suffers disorientation similar to that experienced by an Earth Melded character whose slumber is interrupted."""
      ),
      Power(
        name='Armor of Terra',
        discipline='visceratika',
        level=4,
        description="""At this level of Visceratika, the Gargoyle’s skin hardens and becomes truly rock-like to the touch. The Slave becomes harder to harm, even with fire, and grows inured to injury. A non-Gargoyle learning this level of Visceratika would find her skin becoming gray and rock-like, putting lie to the claim that the Discipline doesn’t carry the risk of the Gargoyle’s curse.
_System_: This power is automatic and requires no roll; it is always in effect. A vampire with Armor of Terra has one extra soak die for all aggravated and lethal attacks and two for all bashing attacks, reduces all wound penalties by one, and halves the damage dice pool of any fire-based source of injury (this Discipline does not change the rules for Rötschreck, however). The difficulty of all touch-based Perception rolls is increased by two, due to the desensitization of the character’s skin."""
      ),
      Power(
        name='Flow Within the Mountain',
        discipline='visceratika',
        level=5,
        description="""The Gargoyle is no longer restricted to hiding within stone. Now, he can flow through stone like lava working its way down a mountainside, emerging from the hiding place at any point he wishes. Since this power works on cement or concrete as well as rock, the streets of a modern metropolis afford a Gargoyle some very interesting assassination tools.
_System_: Once the character has used Bond with the Mountain, the player spends two more blood points to activate Flow Within the Mountain for the duration of the scene. The Gargoyle can move within stone and cement (otherwise using the same rules as the Protean power Earth Control, p.200). The character can also use this power to walk through a stone wall and emerge on the other side without first using Bond with the Mountain. In this case, the player spends one blood point and rolls Strength (difficulty 8; Potence adds dice or successes normally). The Gargoyle may flow through a maximum thickness in feet equal to the number of successes rolled, or 30 times the number of successes rolled in centimeters. If the wall or barrier is thicker than this, the character is trapped within it until he is chiseled out or uses Flow Within the Mountain to escape."""
      )
    ],
    description="""
Visceratika is an extension of the Gargoyles’ natural affinity for stone and earth. Certain Visceratika powers closely resemble some aspects of Protean and, to a lesser extent, Vicissitude. Tremere in a position to know insist that this is pure coincidence, but the few among the Gargoyles who retain scholarly aspirations insist that the Gangrel and Tzimisce blood used to create the bloodline still maintains a certain hold over its members.

For many years, Visceratika was regarded as endemic to the Gargoyle condition, just like the repulsive visage and the wings with which other Kindred associate the bloodline. That is, vampires - including the Tremere - believed that they couldn’t have the one without the others. Supposedly this isn’t true, and provided one can find a Gargoyle tutor, any vampire can learn the Discipline. Of course, that assumes one can find a willing tutor - the Gargoyles aren’t eager to reveal these secrets. Furthermore, few Kindred want to bet that the Tremere are wrong and risk waking up with wings and horns.
"""
  ),
  Discipline(
    name='Dementation',
    sorcery=False,
    powers= [
      Power(
        name='Passion',
        discipline='dementation',
        level=1,
        description="""The vampire stirs his victim’s emotions, either heightening them to a fevered pitch or blunting them until the target is completely desensitized. The Cainite may not choose which emotion is affected; she may only amplify or dull emotions already present in the target. In this way, a vampire can inflame mild irritation into quivering rage or atrophy true love into casual interest.
_System_: The character talks to her victim, and the vampire’s player rolls ^Charisma + Empathy^ (difficulty equals the victim’s Humanity or Path rating). The number of successes determines the duration of the altered state of feeling. Effects of this power might include one- or two-point additions or subtractions to difficulties of frenzy rolls, Virtue rolls, rolls to resist Presence powers, etc.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One turn</td></tr><tr><td>2 successes</td><td>One hour</td></tr><tr><td>3 successes</td><td>One night</td></tr><tr><td>4 successes</td><td>One week</td></tr><tr><td>5 successes</td><td>One month</td></tr><tr><td>6+ successes</td><td>Three months</td></tr></table>"""
      ),
      Power(
        name='The Haunting',
        discipline='dementation',
        level=2,
        description="""The vampire manipulates the sensory centers of his victim’s brain, fooding the victim’s senses with visions, sounds, scents, or feelings that aren’t really there. The images, regardless of the sense to which they appeal, are only feeting “glimpses”, barely perceptible to the victim. The vampire using Dementation cannot control what the victim perceives, but may choose which sense is affected. The “haunting” effects occur mainly when the victim is alone, and mostly at night. They may take the form of the subject’s repressed fears, guilty memories, or anything else that the Storyteller finds dramatically appropriate. The effects are never pleasant or unobtrusive, however. The Storyteller should let her imagination run wild when describing these sensory impressions; the victim may well feel as if she is going mad, or as if the world is.
_System_: After the vampire speaks to the victim, the player spends a blood point and rolls ^Manipulation + Subterfuge^ (difficulty of his victim’s Perception + Self-Control/Instinct). The number of successes determines the length of the sensory “visitations”. The precise effects are up to the Storyteller, though particularly eerie or harrowing apparitions can certainly reduce dice pools for a turn or two after the manifestation.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One night</td></tr><tr><td>2 successes</td><td>Two nights</td></tr><tr><td>3 successes</td><td>One week</td></tr><tr><td>4 successes</td><td>One month</td></tr><tr><td>5 successes</td><td>Three months</td></tr><tr><td>6+ successes</td><td>One year</td></tr></table>"""
      ),
      Power(
        name='Eyes of Chaos',
        discipline='dementation',
        level=3,
        description="""This peculiar power allows the vampire to take advantage of the feeting clarity hidden in insanity. She may scrutinize the “patterns” of a person’s soul, the convolutions of a vampire’s inner nature, or even random events in nature itself. The Kindred with this power can discern the most well-hidden psychoses, or gain insight into a person’s true self. Malkavians with this power often have (or claim to have) knowledge of the moves and countermoves of the great Jyhad, or the patterns of fate.
_System_: This power allows a vampire to determine a person’s true Nature, among other things. The vampire concentrates for a turn, then her player rolls ^Perception + Occult^. The difficulty depends on the intricacy of the pattern. Discerning the Nature of a stranger would be difficulty 9, a casual acquaintance would be an 8, and an established ally a 6. The vampire could also read the message locked in a coded missive (difficulty 7), or even see the doings of an invisible hand in such events as the pattern of falling leaves (difficulty 6). Almost anything might contain some hidden insight, no matter how trivial or meaningless. The patterns are present in most things, but are often so intricate they can keep a vampire spell-bound for hours while she tries to understand their message. This is a potent power, subject to adjudication. Storytellers, this power is an effective way to introduce plot threads for a chronicle, reveal an overlooked clue, foreshadow important events, or communicate critical information a player seeks. Important to its use, though, is delivering the information properly. Secrets revealed via Eyes of Chaos are never simple facts; they’re tantalizing symbols adrift in a sea of madness. Describe the results of this power in terms of allegory: “The man before you appears as a crude marionette, with garish features painted in bright stage make-up, and strings vanishing up into the night sky”. Avoid stating plainly, “You learn that this ghoul is the minion of a powerful Methuselah”."""
      ),
      Power(
        name='Voice of Madness',
        discipline='dementation',
        level=4,
        description="""By merely addressing his victims aloud, the Kindred can drive targets into fits of blind rage or fear, forcing them to abandon reason and higher thought. Victims are plagued by hallucinations of their subconscious demons, and try to flee or destroy their hidden shames. Tragedy almost always follows in the wake of this power’s use, though offending Malkavians often claim that they were merely encouraging people to act “according to their natures”. Unfortunately for the vampire concerned, he runs a very real risk of falling prey to his own voice’s power.
_System_: The player spends a blood point and makes a ^Manipulation + Empathy^ roll (difficulty 7). One target is affected per success, although all potential victims must be listening to the vampire’s voice. Affected victims fly immediately into frenzy or a blind fear like Rötschreck. Kindred or other creatures capable of frenzy, such as Lupines, may make a frenzy check or Rötschreck test (Storyteller’s choice as to how they are affected) at +2 difficulty to resist the power. Mortals are automatically affected and don’t remember their actions while berserk. The frenzy or fear lasts for a scene, though vampires and Lupines may test as usual to snap out of it. The vampire using Voice of Madness must also test for frenzy or Rötschreck upon invoking this power, though his difficulty to resist is one lower than normal. If the initial roll to invoke this power is a failure, however, the roll to resist the frenzy is one higher than normal. If the roll to invoke this power is a botch, the frenzy or Rötschreck response is automatic."""
      ),
      Power(
        name='Total Insanity',
        discipline='dementation',
        level=5,
        description="""The vampire coaxes the madness from the deepest recesses of her target’s mind, focusing it into an over-whelming wave of insanity. This power has driven countless victims, vampire and mortal alike, to unfortunate ends.
_System_: The Kindred must gain her target’s undivided attention for at least one full turn to enact this power. The player spends a blood point and rolls ^Manipulation + Intimidation^ (difficulty of her victim’s current Willpower points). If the roll is successful, the victim is afflicted with five derangements of the Storyteller’s choice (see p.290). The number of successes determines the duration.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One turn</td></tr><tr><td>2 successes</td><td>One night</td></tr><tr><td>3 successes</td><td>One week</td></tr><tr><td>4 successes</td><td>One month</td></tr><tr><td>5+ successes</td><td>One year</td></tr></table>On a botch ... well, the Storyteller can decide what a vampire inflicts upon herself by attempting to incite the primal hells lurking within the darkest recesses of a victim’s mind. The victim (or the target of a botch) can spend a number of Willpower points equal to the successes rolled to end the duration prematurely. The Storyteller decides when such Willpower points can be spent (such as after a therapy session or after a friend has managed to prove a particular delusion to be false)."""
      ),
      Power(
        name='Lingering Malaise',
        discipline='dementation',
        level=6,
        description="""While lesser Dementation powers allow a vampire to inflict temporary (though often long-lasting) madness upon a victim, elders of the Clan have developed the ability to infect the minds of their victims with permanent maladies. Lingering Malaise causes permanent psychological shifts within the victim, making him, as one Gangrel elder remarked, “an honorary Lunatic”.
_System_: The character speaks to his victim for at least a minute, describing the derangement that Lingering Malaise will inflict. The player rolls ^Manipulation + Empathy^ (difficulty equal to the victim’s current Willpower points); the victim resists with a Willpower roll (using his permanent Willpower at difficulty 8). If the user of Lingering Malaise scores more successes, the victim gains a permanent derangement chosen by the individual who inflicts it. Lingering Malaise may only be used to inflict one derangement per night on any given victim, though multiple attempts may be made until the derangement takes hold."""
      ),
      Power(
        name='Shattered Mirror',
        discipline='dementation',
        level=6,
        description="""Although Dementation’s low-level effects are primarily to initiate or promote insanity rather than to create it spontaneously, some of its more potent manifestations are not as subtle. The wielder of this fearsome power can transfer her own deranged mindset into the psyche of a hapless victim, spreading her own brand of insanity like a virus.
_System_: The vampire must establish eye contact (p.152) with her intended victim to apply this power. The player then rolls ^Charisma + Subterfuge^ (difficulty equal to the target’s current Willpower points) resisted by the target’s Wits + Self-Control/Instinct (difficulty equal to the Dementation user’s current ^Willpower^ points). If the aggressor wins, the target gains all of her derangements and Mental Flaws for a period of time determined by the number of net successes the aggressor scored:
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>one hour</td></tr><tr><td>2 successes</td><td>one night</td></tr><tr><td>3 successes</td><td>one week</td></tr><tr><td>4 successes</td><td>one month</td></tr><tr><td>5 successes</td><td>six months</td></tr><tr><td>6+ successes</td><td>one year per success over 5</td></tr></table>"""
      ),
      Power(
        name='Restructure',
        discipline='dementation',
        level=7,
        description="""The elder with this fearsome power has the ability to twist his victims’ psyches at their most basic levels, warping their very beings. The subject of Restructure retains her memories, but her outlook on life changes completely, as if she has undergone a sudden epiphany or religious conversion. This effect goes much deeper than the implantation of a derangement; it actually performs a complete rewrite of the victim’s personality.
_System_: As the description says, this power allows the vampire to change his target’s Nature to one more suitable to his ends. To accomplish this, the character must make eye contact (p.152) with his intended victim. The player rolls ^Manipulation + Subterfuge^ (difficulty equals the victim’s Wits + Subterfuge). If he rolls a number of successes equal to or greater than the target’s Self-Control/Instinct, the target’s Nature changes to whatever the player using Restructure desires. This effect is permanent and can be undone only by another application of Restructure (though subtle differences from the character’s original Nature may still remain, as it is impossible for such a fundamental change to occur flawlessly). A botch on this roll changes the character’s own Nature to that of his intended victim."""
      ),
      Power(
        name='Personal Scourge',
        discipline='dementation',
        level=8,
        description="""Similar to the Auspex power of Psychic Assault (p.141), this fearsome ability allows the elder to turn the very strength of her victim’s mind against him, inflicting physical harm with the power of his own will. Victims of this self-powered attack spontaneously erupt in lacerations and bruises, spraying blood in every direction and howling in agony. Those who have observed such an attack with Auspex note that the victim’s aura swirls with violent psychosis and erupts outward in writhing appendages - a sight that can make even the most jaded Tzimisce quail.
_System_: The vampire must touch or establish eye contact (p.152) with her target. The player rolls ^Manipulation + Empathy^ (difficulty equal to the target’s Stamina + Self-Control/Instinct) and spends two Willpower points. For a number of turns equal to the number of successes rolled, the victim rolls his own permanent Willpower as lethal damage against himself. This damage can be soaked with his own Humanity or Path of Enlightenment (difficulty 6); Fortitude does not add to this soak dice pool, nor does body armor. He may take no actions during this time other than thrashing and gibbering; this includes spending blood to heal."""
      ),
      Power(
        name='Lunatic Eruption',
        discipline='dementation',
        level=9,
        description="""This fearsome ability is only known to have been applied a few times in recorded Kindred history, most spectacularly during the final nights of the last battle of Carthage. It is effectively a psychic nuclear bomb, used to incite every intelligent being within several miles (kilometers) into an orgy of bloodlust and rage. It is suspected that the Malkavians have used the threat of this power as a bargaining chip in several key negotiations.
_System_: The player spends four Willpower points and rolls ^Stamina + Intimidation^ (difficulty 8). The area of effect is determined by the number of successes scored:
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One city block</td></tr><tr><td>2 successes</td><td>An entire neighborhood</td></tr><tr><td>3 successes</td><td>A large downtown area</td></tr><tr><td>4 successes</td><td>Several neighborhoods</td></tr><tr><td>5 successes</td><td>An entire metropolitan area (approximately 30 miles or 45 kilometers)</td></tr><tr><td>6+ successes</td><td>An additional 10 miles or 15 kilometers for every success past 5.</td></tr></table>Within this area, all sentient creatures fall prey to their baser instincts. Mortals spontaneously riot, looting and burning between bouts of mass violence. Kindred enter hunger-induced frenzies, draining dry as many vessels as they can sink their fangs into. An entire city can quite literally be driven temporarily insane by this power. Lunatic Eruption’s effects persist until the next sunrise, and anyone entering its area of effect (centered on the site at which it was used, not on the character who applied it) falls under its spell. However, momentum may carry the violence spawned by this power much farther - and keep it going much longer - than the power itself can force. Victims of Lunatic Eruption may resist with Self-Control/Instinct rolls (difficulty equal to the Dementation user’s permanent ^Willpower^ rating); each success provides one hour of lucidity, which most wise individuals use to leave the power’s area of effect (leaving the “blast radius” removes the power’s infuence). The source of Lunatic Eruption may be pinpointed if a character is using Heightened Senses or an equivalent power at the time it is used; this is automatic and requires no roll. However, this grants no knowledge of what actually happened - the observer simply “feels” a massive psychic shockwave explode from the character using the power."""
      )
    ],
    description="""
Dementation is the Discipline that allows a vampire to focus and channel madness into the minds of those around him. Though it’s the natural legacy of the Malkavians, practitioners of Dementation need not actually be mad to use the Discipline... but it helps.

Disturbingly, Dementation doesn’t actually make their victims mad, but rather it seems to break down the doors to the hidden darkness of the target’s mind, releasing into the open whatever is found there. The Malkavians claim that this is because insanity is the next logical step in mental evolution, a transhumanist advancement of what modern people consider consciousness. Other Kindred scoff that this reasoning is an outright justification for the chaos that Dementation brings. They don’t scoff too loudly, however, lest the Malkavian advance their consciousness next.
"""
  ),
  Discipline(
    name='Quietus',
    sorcery=False,
    powers= [
      Power(
        name='Silence of Death',
        discipline='quietus',
        level=1,
        description="""Many Assamites claim never to have heard their targets’ death screams. Silence of Death imbues the vampire with a mystical silence that radiates from her body, muting all noise within a certain vicinity. No sound occurs inside this zone, though sounds originating outside the area of effect may be heard by anyone in it. Rumors abound of certain skilled Assamite viziers who have the ability to silence a location rather than a circumference that follows them, but no proof of this has been forthcoming.
_System_: This power (which costs one blood point to activate) maintains a 20-foot (6-meter) radius of utter stillness around the Kindred for one hour."""
      ),
      Power(
        name='Scorpion’s Touch',
        discipline='quietus',
        level=2,
        description="""By changing the properties of her blood, a vampire may create powerful venom that strips her prey of his resilience. This power is greatly feared by other Kindred, and all manner of hideous tales concerning methods of delivery circulate among trembling coteries. Kindred with Quietus are known to deliver the poison by coating their weapons with it, blighting their opponents with a touch, or spitting it like a cobra. An apocryphal account speaks of a proud Prince who discovered an Assamite plotting her exsanguination and began to diablerize her would-be assassin. Halfway through the act, she learned that she had ingested a dire quantity of tainted blood and was then unable to resist the weakened hashashiyyin’s renewed attack.
_System_: To convert a bit of her blood to poison, the Kindred’s player spends at least one blood point and rolls ^Willpower^ (difficulty 6). If this roll is successful, and the vampire successfully hits (but not necessarily damages) her opponent, the target loses a number of Stamina points equal to the number of blood points converted into poison - vampires attempting to drink the blood of the Kindred with Scorpion’s Touch are automatically considered to be “successfully hit”. The victim may resist the poison with a Stamina + Fortitude roll (difficulty 6); successes achieved on the resistance roll subtract from the vampire’s successes. The maximum number of blood points a Kindred may convert at any one time is equal to her Stamina. The number of successes scored indicates the duration of the Stamina loss.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One turn</td></tr><tr><td>2 successes</td><td>One hour</td></tr><tr><td>3 successes</td><td>One day</td></tr><tr><td>4 successes</td><td>One month</td></tr><tr><td>5 successes</td><td>Permanently (though Stamina maybe bought back up with experience)</td></tr></table>If a mortal’s Stamina falls to zero through use of Scorpion’s Touch, she becomes terminally ill and loses any immunity to diseases, her body succumbing to sickness within the year unless she somehow manages to increase her Stamina again. If a Kindred’s Stamina falls to zero, the vampire enters torpor and remains that way until one of her Stamina points returns. If a Kindred is permanently reduced to zero Stamina, she may recover from torpor only through mystical means. To afflict someone with the poison, the Cainite must touch her target’s flesh or hit him with something that carries the venom. Many Assamites lubricate their weapons with the excretion, while others pool the toxin in their hands (or fleck their lips with the poison, for a “kiss of death”) and press it to their opponents. Weapons so envenomed must be of the melee variety - arrows, sling stones, bullets, thrown weapons, and the like cannot carry enough of the stuff to do damage, or it drips off in flight. Players whose vampires wish to spit at their targets must make a ^Stamina + Athletics^ roll (difficulty 6). No more than two blood points’ worth of poison may be expectorated, and a Kindred may spit a distance of 10 feet (3 meters) for each point of Strength (and Potence) the character possesses. Vampires with Quietus are immune to their own poison, but not the blood-venom of other Kindred with this power."""
      ),
      Power(
        name='Dagon’s Call',
        discipline='quietus',
        level=3,
        description="""This terrible power allows a vampire to drown her target in his own blood. By concentrating, the Kindred bursts her target’s blood vessels and fills his lungs with vitae that strangles him from within. The blood actually constricts the target’s body from the inside as it floods through his system; thus, it works even on unbreathing Kindred. Until the target collapses in agony or death throes, this power has no visible effect, and many Kindred like it because it leaves no trace of their presence.
_System_: The vampire must touch her target prior to using Dagon’s Call. Within an hour thereafter, the vampire may issue the call, though she need not be in the presence or even in the line of sight of her target. Invoking the power costs one Willpower point. The Kindred’s player makes a contested Stamina roll against the target’s Stamina; the difficulty of each roll is equal to the opponent’s permanent Willpower rating. The number of successes the vampire using Dagon’s Call achieves is the amount of lethal damage, in health levels, the victim suffers. For an additional point of Willpower spent in the next turn, the vampire may continue using Dagon’s Call by engaging in another contested Stamina roll. So long as the Kindred’s player continues to spend Willpower, the character may continue rending her opponent from within."""
      ),
      Power(
        name='Baal’s Caress',
        discipline='quietus',
        level=4,
        description="""The penultimate use of blood as a weapon (short of diablerie itself), Baal’s Caress allows the Kindred to transmute her blood into a virulent ichor that destroys any living or undead flesh it touches. In nights of yore, when Assamites led the charges of Saracen legions, the Assassins were often seen licking their blades, slicing open their tongues and lubricating their weapons with this foul secretion. Baal’s Caress may be used to augment any bladed weapon; everything from poisoned knives and swords to tainted fingernails and claws has been reported.
_System_: Baal’s Caress does not increase the damage done by a given weapon, but that weapon inflicts aggravated damage rather than normal. No roll is necessary to activate this power, but one blood point is consumed per hit. For example, if a Cainite poisons his knife and strikes his opponent (even if he inflicts no damage), one blood point’s worth of lubrication disappears. For this reason, many vampires choose to coat their weapons with a significant quantity of blood. If the vampire misses, no tainted blood is consumed."""
      ),
      Power(
        name='Taste of Death',
        discipline='quietus',
        level=5,
        description="""A refinement of Baal’s Caress, Taste of Death allows the Cainite to spit caustic blood at her target. The blood coughed forth with this power burns flesh and corrodes bone; some vampires have been reported to vomit voluminous streams of vitae that reduce their targets to heaps of sludge.
_System_: The vampire may spit up to 10 feet (3 meters) for each dot of Strength and Potence he possesses. Hitting the target requires a ^Stamina + Athletics^ roll (difficulty 6). Each blood point spewed at the target inflicts two dice of aggravated damage, and there is no limit (other than the vampire’s capacity and per-turn expenditure maximum) to the quantity of blood with which a target may be deluged."""
      ),
      Power(
        name='Blood Sweat',
        discipline='quietus',
        level=6,
        description="""Although vampires do not have functioning sebaceous glands, they are still capable of sweating at times of extreme stress. This “sweat” is actually a thin sheen of blood on the Cainite’s forehead and palms. Most Kindred see blood sweat as an admission of fear or guilt. The vampire who has mastered Blood Sweat is capable of inducing these feelings in a subject to a preternatural degree. The victim experiences a torrential outpouring of vitae if he harbors the tiniest shred of remorse for any action he has ever undertaken.
_System_: The character must be within line of sight of the subject and spend three turns concentrating. The player spends a Willpower point and rolls ^Manipulation + Intimidation^ (difficulty equal to the target’s current Willpower points). The target loses one blood point per success. Mortals sustain injury as if they had lost blood from being fed upon. The target actually “sweats out” the lost blood in a sudden rush of sanguinary perspiration that soaks his clothes. Large amounts may even form puddles at his feet. Blood lost through this process is considered dead, inert mortal blood, and provides minimal nutrition (half normal) for Cainites desperate enough to lick it up from the foor or wring it out of towels. It provides no sustenance for the individual from whom it emerged. In addition to the blood loss, the victim is overcome by a sense of remorse and guilt for his past transgressions (if he has a strong conscience) or an overwhelming compulsion to brag (if he is of sufficiently coarse moral character). The severity of this impulse depends on the number of successes rolled: One success could cause a slight twinge of conscience, while five successes may result in the subject breaking down and pouring out a full confession of his crimes. This effect is more story-oriented than mechanical, and the Storyteller is the final authority on what the victim feels compelled to confess or boast. Note that this power’s existence is not widely known. Vampires and mortals alike tend to shrink away from someone who begins spontaneously sweating blood, and experiencing such an affliction may panic even the staunchest individual."""
      ),
      Power(
        name='Selective Silence',
        discipline='quietus',
        level=6,
        description="""Although Silence of Death is an effective tool for the battlefield and the court alike, it is indiscriminate in its effects. The assassin who uses it in preparation for firing a shotgun also silences the radio over which her comrades might warn her of an oncoming guard. The courtier who suppresses a room full of dissenting voices is likewise unable to speak her own mind. Selective Silence allows the skilled Cainite to overcome these limitations by silencing only those individuals or objects that she wants to silence. When using this power, most individuals exhale a thin mist of blood that clings to the selected subjects, gradually evaporating as Selective Silence’s effects fade. Some vampires also use a similar technique when invoking Silence of Death, in which case the mist surrounds them and moves with them.
_System_: The player spends two blood points and rolls ^Stamina + Stealth^ (difficulty 7). Each success allows for one individual or object that the character can silence with this use of the power. Each subject must be within 20 yards or meters of the character. Objects larger than a man count as more than one subject: a heavy machine gun counts as two, a car as three, and a small aircraft as five. Objects larger than a private jet or creatures larger than an elephant cannot be silenced through the use of this power. Each subject is completely silenced for a number of minutes equal to the character’s permanent ^Willpower^. Nothing it does generates sound, though the secondary effects of its actions will do so normally. For example, a gun silenced with this power will not produce an audible explosion when fired, but its bullets still make noise as they break the sound barrier. A silenced victim can scream all he likes and not make a sound, but may be able to summon help by smashing a window."""
      ),
      Power(
        name='Ripples of the Heart',
        discipline='quietus',
        level=6,
        description="""According to Assamite lore, this technique originated with a Byzantine scholar who wanted to protect his herd from the thirst of other Cainites. Ripples of the Heart allows a Cainite to leave emotions within the bloodstream of any mortal from whom he feeds. Any other vampire who subsequently drinks from that mortal experiences those emotions as if they were his own.
_System_: The character drinks at least one blood point from the subject mortal then spends a minute in physical contact with the subject while concentrating on the emotion he wishes to leave in her blood. The player spends a point of Willpower and rolls ^Charisma + Empathy^ (difficulty 7 under normal circumstances, 5 if the subject is currently experiencing the intended emotion, 9 if he is currently experiencing a strong opposite emotion). The subject’s blood carries the weight of the intended emotion for one lunar month per success rolled. A mortal’s blood can only carry one emotion at a time. Subsequent attempts to use Ripples of the Heart on the same individual have no effect until the previous application has worn off. Any vampire who drinks from a vessel under the effects of Ripples of the Heart must succeed in a Self-Control/Instinct roll (difficulty of the mortal’s current Willpower points) as soon as she swallows the first blood point. If she fails this roll, the vitae-borne emotion immediately overtakes her. The strength of the emotion depends on how many blood points she drinks. One blood point results in a momentary mood swing, two causes a significant shift in demeanor, and three or more generates a complete change in emotional state. Depending on the circumstances and the precise emotion, the effects of this may be spectacular or catastrophic. A vampire overtaken by romantic passion may temporarily believe she is in love with the mortal(or any other convenient bystander). One who drinks from a hate-infused vessel may rend her prey to shreds, and one who takes a draught of a mortal touched with fear may run away screaming. The vampire remains subject to the emotion for a number of hours equal to the mortal’s permanent Willpower, though she is still subject to other feelings after the initial rush of sensation. The mortal who is under the effects of Ripples of the Heart is unaware of the power’s effects on him, though he is slightly predisposed toward the emotion in question while the power is in effect. The vampire who used Ripples of the Heart on a mortal is immune to anyeffects from that use."""
      ),
      Power(
        name='Purification',
        discipline='quietus',
        level=6,
        description="""Although most mortal cultures affix negative connotations to the spilling of blood, most Assamites - indeed, most vampires - have quite the opposite reaction to it. For them, blood is an unlife-affirming and reinvigorating substance. Purification works on this principle, using the power of vitae to cleanse and restore. Rather than purging foreign taints from the body, Purification allows its wielder to cleanse other individuals’ minds and souls of stains, including those left by the mind control of other Kindred. The vampire using this power expels his own blood through his skin and allows it to soak through his subject, slowly dissipating. As it does so, it carries away spiritual impurities and outside infuences.
_System_: The character touches the forehead of her intended subject, and both parties spend a minimum of five minutes in deep concentration. The player spends a number of blood points equal to the subject’s permanent Willpower. The subject rolls Willpower once for every external supernatural infuence (a vampiric Discipline, usually) to which his mind has been subjected. The difficulty equals the level of the power in question +4 (or a difficulty of 7 if the power level is unknown, such as one used by a different kind of supernatural creature). A success nullifies that effect. Purification has its limits. It can remove directly intrusive infuences such as Dominate-implanted commands, Dementation-generated derangements, or the imperatives caused by elder vampires’ Presence. It cannot dispel infuences that are transmitted by blood, including a blood bond or the dispositions imparted by one’s Clan or bloodline, nor can it erase those caused by purely mundane techniques such as persuasion, hypnosis, or brainwashing, or genuine emotional states such as love and hate. It can remove mind-altering blood magic effects, but either the character wielding Purification or the power’s beneficiary must have a level of Thaumaturgy equal to or greater than that with which the effect was placed. A character cannot use Purification on herself."""
      ),
      Power(
        name='Baal’s Bloody Talons',
        discipline='quietus',
        level=7,
        description="""The toxin generated by Baal’s Caress is not enough to significantly harm some truly fearsome foes. This progressive development of that lesser technique allows its user to envenom his weapon with a blood-based poison so potent that it corrodes the very weapon that bears it, eating away at the strongest metal in a minute or less. However, its effects on its victims are spectacular enough to make the loss of even the most treasured blades worthwhile. This power’s effects are of very limited duration, as the substance it creates will quickly evaporate away.
_System_: The character coats an edged weapon with her own blood, as per Baal’s Caress. The player spends one or more blood points and rolls ^Willpower^ (difficulty 7). The weapon now does aggravated damage. It also gains a number of additional damage dice equal to the number of successes rolled plus the number of blood points spent. These extra dice fade at a rate of one per turn as the poison dissipates, drips off, and reacts with the weapon’s material. Once the extra damage dice are all gone, the weapon’s base damage dice begin to fade at the same rate. The weapon breaks if used when its base damage is reduced to the wielder’s Strength or less. The only weapons that can resist this corrosion are those created with a supernatural power of a level equal to or greater than the character’s Quietus rating, though even this is subject to the Storyteller’s discretion. Baal’s Bloody Talons is subject to the same limitations as Baal’s Caress, except the limit on the number of successful strikes that do aggravated damage. A weapon affected by Baal’s Bloody Talons does aggravated damage with every successful attack until it is destroyed. At the Storyteller’s discretion, the character may use the venom this power produces for other purposes, such as burning through a padlock or destroying an incriminating tape. He may not, however, store this poison for later use - even if a container proves resistant to it, the substance becomes inert within a few minutes of leaving its creator’s body."""
      ),
      Power(
        name='Poison the Well of Life',
        discipline='quietus',
        level=7,
        description="""Beyond leaving emotional traces in a subject’s blood, the master of this Quietus power can now taint that same vitae, making it into a deadly poison for any other Cainite who drinks from that mortal. Some vampires use Poison the Well of Life to guard their own herds against “poachers” or to ward specific vessels against indiscriminate feeding. Others have been known to employ it as a subtle trap for other vampires, turning herds against their owners.
_System_: The character touches the mortal he wishes to taint and smears a streak of his own vitae on the victim’s skin. The player spends three blood points and rolls ^Stamina + Occult^ (difficulty 7). For a number of months equal to the number of successes, any other vampire who drinks that mortal’s blood sustains two health levels of aggravated damage for every blood point imbibed. This damage manifests as a combination of acid burns and something akin to toxic shock. While a mortal is poisonous to vampires, his body’s alchemical balance is slightly altered toward toxicity. He gains two extra points of Stamina for the purposes of resisting the effects and damage of poisons and acids. However, his bodily excretions, especially his sweat, are slightly more noxious than normal. He suffers a one die penalty to all Social dice pools if whomever he chooses to interact with has a particularly sensitive nose and is close enough to smell him."""
      ),
      Power(
        name='Songs of Distant Vitae',
        discipline='quietus',
        level=8,
        description="""Blood magic practitioners and individuals skilled at Auspex have long known that vitae can carry residual impressions of emotion and personality. This power invokes those impressions to overwhelm its victim with “remembered” images and sensations drawn from the vessels who held that blood before the vampire fed from them. Particularly strong-willed or hardened subjects may shrug off these visions as daydreams, but those who are less self-possessed can be permanently changed by the experience. A side effect of the use of this power is the partial destruction of the vitae from which the images are drawn. Some viziers theorize that this is the result of motes of the vessels’ consciousness making an effort to escape their usurper.
_System_: The character touches his target and spends a turn in concentration. The player spends four blood points and rolls ^Wits + Intimidation^ in a contested roll against the victim’s permanent Willpower (difficulty 7). If the target has committed diablerie within a number of nights equal to the character’s Perception, the attacker gains one automatic success. The result depends on the number of net successes the attacker rolls. Note that in all invocations of this power, the sensations that the subject relives are expressly negative and terrifying - for example, he experiences none of the pleasure that would normally accompany the Kiss when he flashes back to such an event. In addition to the effects listed below, the subject of a successful attack loses a number of blood points equal to the number of successes rolled. This vitae oozes from his body in warm red trickles that do no damage but are certain to terrify onlookers.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>Botch</td><td>The attacker enters a flashback sequence in which he relives his last feeding from the vessel’s point of view. If the player rolled three or more 1’s, the character acquires a permanent derangement related to feeding.</td></tr><tr><td>Failure</td><td>The target is unharmed and immune to this power for a number of nights equal to his Willpower.</td></tr><tr><td>1 success</td><td>The target experiences a brief (10-second/3-turn) flashback sequence in which he relives his last feeding from the vessel’s point of view. During this time, he is at +2 difficulty to all rolls.</td></tr><tr><td>2 successes</td><td>The target experiences a brief montage (15 seconds/5 turns) of flashbacks during which his viewpoint flashes between various feedings from the vessels’ points of view. During this time, he is at +3 difficulty to all rolls. Once the initial rush of sensation passes, he is unsettled and at +1 difficulty to all rolls until he succeeds on a Self-Control/Instinct roll (difficulty 8), which he may attempt once per scene.</td></tr><tr><td>3 successes</td><td>The target experiences a composite memory, assembled by his own subconscious, of the terror that various vessels felt while being stalked and fed upon. He must succeed in a Courage roll (difficulty 8) or instantly enter Rötschreck. If he succeeds in this roll, he is still at +3 difficulty on all actions for the rest of the scene due to the distraction that his visions impose.</td></tr><tr><td>4 successes</td><td>The target is stunned and completely unable to act for a number of turns equal to 8 - his Self-Control/Instinct as he is bombarded by a sequence of the most terrifying memories of his various vessels. Once this initial onslaught subsides, he must roll Courage (difficulty 9) or enter Rötschreck. If he fails this roll, he must roll Self-Control/Instinct (difficulty 8) or gain the Sanguinary Animism derangement.</td></tr><tr><td>5 successes</td><td>The target is thrown into a nightmarish reenactment of the greatest fears of every individual upon whom he has ever fed. He must make a successful Self-Control/Instinct roll (difficulty 9) or fall into torpor for (10 - the target’s Stamina) nights, at the end of which he loses half his permanent Willpower and gains the derangement Sanguinary Animism. If he succeeds on the Self-Control/Instinct roll, he enters Rötschreck for the rest of the night, during which time his greatest fear is of his own image. At the end of the night, he must succeed at a Willpower roll (difficulty 9) or lose a permanent Willpower point and gain the derangement Sanguinary Animism.</td></tr></table>"""
      ),
      Power(
        name='Condemn the Sins of the Father',
        discipline='quietus',
        level=9,
        description="""Although the Second City’s judges recognized that heritage does not equal guilt, they also encountered many situations in which a vampire’s entire brood had committed the same crime. In such cases, the judges often decreed the same punishment for all transgressors. This technique, which modern viziers believe to have originated at that time, allows its wielder to administer such judgments. Through Condemn the Sins of the Father, a Cainite can apply lesser Quietus powers to an entire lineage.
_System_: After successfully using any lesser Quietus power on another vampire, the player spends a permanent Willpower point and 10 blood points and rolls ^Stamina + Occult^. The difficulty of this roll is equal to four plus the number of Generations of the original target’s descendants that the player wants to affect, up to a maximum difficulty of 10. If the roll succeeds, every descendant of the original target within the specified range of Generations suffers the same effects that the original target experienced, resisting with his own relevant Traits. The player may exempt a number of potential subjects from this effect equal to twice the character’s Wits, but the character must know their faces or have tasted their vitae."""
      )
    ],
    description="""
The Discipline of silent death, Quietus is practiced by those of Clan Assamite. Based on elements of blood, poison, vitae control, and pestilence, Quietus focuses on the destruction of a target through a variety of means. This Discipline doesn’t always cause a <i>quick</i> death, but the Assamites rely on its lethality to hide their involvement with their victims.
"""
  ),
  Discipline(
    name='Melpominee',
    sorcery=False,
    powers= [
      Power(
        name='The Missing Voice',
        discipline='melpominee',
        level=1,
        description="""The character can “throw” her voice anywhere within her line of sight. This enables the Daughter to carry on surreptitious conversations, sing duets with herself, or cause any number of distractions. This power can also be combined with other Melpominee powers to disguise their source (and some Daughters use it to conceal the fact that Melpominee powers do not function through recorded media).
_System_: This power functions automatically as long as the character wills it. However, using The Missing Voice while performing any action other than speech or singing incurs a penalty of two dice on that action due to the disruption of the character’s concentration."""
      ),
      Power(
        name='Phantom Speaker',
        discipline='melpominee',
        level=2,
        description="""The Daughter can project her voice to any individual she has personally met. Distance is no object, but it must be night wherever the target presently is. The vampire can sing, talk, or otherwise project her voice in any way she sees fit (including other uses of Melpominee), but she cannot hear what she is saying, and therefore suffers a +1 difficulty to any rolls accompanying her utterance. For instance, the vampire could project her voice to an enemy in an attempt to intimidate him, but would suffer a +1 to the difficulty of the ^Charisma + Intimidation^ roll.
_System_: The player rolls ^Wits + Performance^ (difficulty 7) and spends a blood point. Each success allows one turn of speech; three or more successes allow speech for an entire scene."""
      ),
      Power(
        name='Madrigal',
        discipline='melpominee',
        level=3,
        description="""Music has the power to sway the listener, engendering specific emotions through artful lyrics, pounding crescendo, or haunting melody. The Daughters of Cacophony can tap into music’s power, forcing listeners to feel whatever they wish. The emotion becomes so powerful that the listener must act, though what a listener does isn’t something the Siren can directly control.
_System_: The player rolls ^Charisma + Performance^ (difficulty 7). Each success instills the chosen emotion in a fifth of the Kindred’s audience (more than five successes have no additional effect). The Storyteller decides precisely which members of the audience are affected. Characters may resist this power for the duration of the scene with the expenditure of a Willpower point, but only if they have reason to believe that they are being controlled by outside individuals. The song the vampire sings must also reflect the emotion she wishes to engender - no one’s going to mob the concert security no matter how well she sings “High Hopes”, but they might if she performs “I Predict a Riot”.
Affected individuals should act in accordance with their Natures - enraged Conformists would join a riot but not start one, aroused Bravos may force their attentions on the object of their desire, and jealous Directors may send cronies after their rivals.
Multiple Daughters may use this Discipline in concert."""
      ),
      Power(
        name='Siren’s Beckoning',
        discipline='melpominee',
        level=4,
        description="""The Daughters of Cacophony don’t spread madness as surely (or as visibly) as the Malkavians, but their songs are definitely detrimental to one’s sanity. With this power, the Daughter can drive any listener to madness. Most of the time, the victim is too fascinated to realize that he should leave the area and block out the music from his mind.
_System_: Siren’s Beckoning requires an extended, resisted roll. The player rolls ^Manipulation + Performance^ (difficulty equal to the target’s current Willpower); the victim resists with a Willpower roll (difficulty equal to the singer’s ^Appearance + Performance^). If the singer accumulates five more successes than the victim at any point, the hapless soul acquires a new derangement or Psychological Flaw of the Storyteller’s choice. This derangement normally lasts for one night, with an additional night per success over five. With a total of 20 net successes, the Daughter can make it permanent. Multiple Daughters may use this Discipline in concert."""
      ),
      Power(
        name='Virtuosa',
        discipline='melpominee',
        level=5,
        description="""Most of the low-level Melpominee powers can only be used on one target at a time. When the Daughter reaches this level of mastery in her Discipline, she can “entertain” a wider audience. Each member of the audience hears the same message.
_System_: The Daughter may use Phantom Speaker or Siren’s Beckoning on a number of targets equal to her ^Stamina + Performance^. The player must spend one blood point for every five targets beyond the first."""
      ),
      Power(
        name='Shattering Crescendo',
        discipline='melpominee',
        level=6,
        description="""The Daughter can sing powerfully enough to rend flesh, split skin, and crack bone. While some Kindred unfortunate enough to witness this power make reference to the fact that even mortal singers can shatter glass at the right frequency, others note that volume and intensity don’t seem to matter when a Daughter employs Shattering Crescendo. The Siren can sing a soothing lullaby and still kill a target.
_System_: Use of this power requires that the victim be within hearing range (characters with hearing difficulties - or Heightened Senses - are affected at the same range as other victims). The player spends one blood point and rolls ^Manipulation + Performance^ (difficulty of the target’s Stamina + Fortitude). Each success inflicts one health level of aggravated damage, which may not be soaked. If using this power on an inanimate object, the Storyteller determines how many dice (if any) the object may use to “soak” and how many successes are needed to completely shatter it.
Multiple Daughters may use this Discipline in concert."""
      ),
      Power(
        name='Persistent Echo',
        discipline='melpominee',
        level=7,
        description="""The Daughter can sing, speak, or even use a Melpominee power and leave the effect hanging in the air, waiting for someone to come along and hear it. The character can control who can trigger her latent song, meaning that combined with Shattering Crescendo or Siren’s Beckoning, this power can be used as a trap.
_System_: The player rolls ^Stamina + Performance^ (difficulty 8) and spends a blood point. Each success yields one turn of speech that may be left to be heard later. If the player wishes to time-delay another Melpominee power, the roll for that power must be made at +1 difficulty. The echo stays suspended for a maximum number of nights equal to twice the vampire’s ^Stamina + Performance^ before fading.
The Kindred may choose to make the echo audible to anyone who stands in her position for the duration of the power - in effect, an endlessly looped mystic recording. Conversely, she may choose for it to fade away once it is heard for the first time. She may also choose to leave it dormant until activated by the presence of a specific individual with whom she is familiar. If the echo is made a one-time-only effect, all traces of the power disappear once the vampire’s words echo to the intended recipient.
If a character uses Heightened Senses in an area where an “unactivated” echo exists, he will hear a faint murmur. Three successes on a ^Perception + Occult^ roll (difficulty 8) are necessary to hear the message, and a botch on this roll will deafen the listener for the rest of the night.
Multiple Daughters may use this Discipline in concert."""
      )
    ],
    description="""
Named for Melpomene, the Greek Muse of tragedy, the unique Discipline of the Daughters of Cacophony is one of speech and song. The powers of this Discipline explore the various uses of the voice for both benefit and harm. As is the case with mortal art, it is not always clear which of those directions these powers take. No character may have a rating in Melpominee higher than her Performance rating. Melpominee affects the subject’s soul as well as the ears; thus, it works perfectly well on deaf subjects, and has caused at least one known breach of the Masquerade due to this effect. Additionally, the powers of Melpominee work only on those who are present when it is used - Daughters of Cacophony cannot record Melpominee effects, send them across radio waves, or have them streamed over the Internet.

Daughters of Cacophony can use some of the powers of the Melpominee Discipline in concert, as it were. If more than one Siren uses the same level of this Discipline simultaneously, the difficulty for the roll falls by one for each Daughter involved beyond the first. The difficulty cannot fall lower than 3, however. The Discipline levels that can benefit from this rule are noted below.
"""
  ),
  Discipline(
    name='Fortitude',
    sorcery=False,
    powers= [
      Power(
        name='Fortitude 1',
        discipline='fortitude',
        level=1,
        description="""Add 1 die to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 1 die."""
      ),
      Power(
        name='Fortitude 2',
        discipline='fortitude',
        level=2,
        description="""Add 2 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 2 dice."""
      ),
      Power(
        name='Fortitude 3',
        discipline='fortitude',
        level=3,
        description="""Add 3 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 3 dice."""
      ),
      Power(
        name='Fortitude 4',
        discipline='fortitude',
        level=4,
        description="""Add 4 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 4 dice."""
      ),
      Power(
        name='Fortitude 5',
        discipline='fortitude',
        level=5,
        description="""Add 5 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 5 dice."""
      ),
      Power(
        name='Fortitude 6',
        discipline='fortitude',
        level=6,
        description="""Add 6 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 6 dice."""
      ),
      Power(
        name='Personal Armor',
        discipline='fortitude',
        level=6,
        description="""Nobody likes to get hit, not even Cainites. The easiest way to ensure that one is not hit (or shot, or stabbed) repeatedly is to take the weapon with which one is assaulted away from one’s attacker and break it. That’s where Personal Armor comes in. This application of Fortitude, derived from one popular in the 12<sup>th</sup> century, causes anything that strikes a Kindred who employs Personal Armor to shatter on impact.
_System_: With the expenditure of two blood points, a vampire can add preternatural hardness to his flesh. Every time an attack is made on the Kindred using Personal Armor (one which he fails to dodge), his player rolls Fortitude (difficulty 8). If the roll grants more successes than the attacker rolled, then the weapon used to make the attack shatters against the vampire’s flesh (“Magical” weapons may be resistant to this effect, at the Storyteller’s discretion). The vampire still takes normal damage if the attack is successful, even if the weapon shatters in the process, though this damage may be soaked. If the attack roll botches, any normal weapon automatically shatters. A hand-to-hand attack causes the attacker equal damage to that suffered by the defender when Personal Armor comes into play. If the attacker misses entirely, she still takes one level of bashing damage. The effects of this power last for the duration of the scene."""
      ),
      Power(
        name='Fortitude 7',
        discipline='fortitude',
        level=7,
        description="""Add 7 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 7 dice."""
      ),
      Power(
        name='Shared Strength',
        discipline='fortitude',
        level=7,
        description="""It’s one thing to laugh off bullets, rather another to watch the ricochets mow down everyone around you. Many Kindred have wished, at one time or another, that they could lend their monstrous vitality to those around them. Those few vampires who have mastered Shared Strength can - if only for a little while.,br.System: Shared Strength duplicates a portion of a vampire’s Fortitude (one dot for every point of blood the vampire spends) to another being. Activating the power requires a ^Stamina + Survival^ roll (difficulty 8, increased to 9 if the target is not a normal mortal), and the expenditure of a point of Willpower. Furthermore, the vampire must mark his target by pressing a drop of his blood onto the target’s forehead. This stain remains visible as long as the power is in effect, the duration of which is determined by the initial roll.
<table><tr><th>Successes</th><th>Duration</th></tr><tr><td>1</td><td>One turn</td></tr><tr><td>2</td><td>One scene</td></tr><tr><td>3</td><td>One hour</td></tr><tr><td>4</td><td>One night</td></tr><tr><td>5</td><td>One week</td></tr><tr><td>6</td><td>One month</td></tr><tr><td>7</td><td>One year</td></tr></table>The target of this power need not be willing to accept the benefit to receive it, and the bestowing vampire can end the effect at any time for no cost. Particularly sadistic Kindred have come up with any number of ways in which a target’s “devil’s mark” and supernatural endurance can be used to land him in a great deal of trouble. A vampire can never bestow more levels of Fortitude than he himself possesses."""
      ),
      Power(
        name='Fortitude 8',
        discipline='fortitude',
        level=8,
        description="""Add 8 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 8 dice."""
      ),
      Power(
        name='Adamantine',
        discipline='fortitude',
        level=8,
        description="""Adamantine functions as a more potent version of Personal Armor.
_System_: This power mimics the effects of Personal Armor, save that the vampire who uses it takes no damage from attacks that shatter on her skin."""
      ),
      Power(
        name='Fortitude 9',
        discipline='fortitude',
        level=9,
        description="""Add 9 dice to all Stamina rolls for the purpose of soaking normal damage. Soak aggravated damage with 9 dice."""
      )
    ],
    description="""
Although all vampires have an unnatural constitution that make them much sturdier than mortals, Fortitude bestows a resilience that would make an action movie hero envious. Vampires with this Discipline can shrug off agonizing trauma and make the most bone-shattering impact look like a flesh wound. The power even offers protection against the traditional banes of vampires, such as sunlight and fire, and the Gangrel, Ravnos, and Ventrue all find that edge incredibly useful.

_System:_ A character’s rating in Fortitude adds to his Stamina for the purposes of soaking normal damage (bashing and lethal). A character with this Discipline may also use his dots in Fortitude to soak aggravated damage, though Kindred cannot normally soak things like vampire bites, werewolf claws, magical effects, fire, sunlight, or massive physical trauma. See p. 272, for further details on soaking and damage.
"""
  ),
  Discipline(
    name='Presence',
    sorcery=False,
    powers= [
      Power(
        name='Awe',
        discipline='presence',
        level=1,
        description="""Those near the vampire suddenly desire to be closer to her and become receptive to her point of view. Awe is extremely useful for mass communication. It matters little what is said - the hearts of those affected lean toward the vampire’s opinion. The weak want to agree with her; even if the strong-willed resist, they soon find themselves outnumbered. Awe can turn a chancy deliberation into a certain resolution in the vampire’s favor almost before her opponents know that the tide has turned. Despite the intensity of this attraction, those so smitten do not lose their sense of self-preservation. Danger breaks the spell of fascination, as does leaving the area. Those subject to Awe will remember how they felt in the vampire’s presence, however. This will infuence their reactions should they ever encounter her again.
_System_: The player spends a blood point and rolls ^Charisma + Performance^ (difficulty 7). The number of successes rolled determines how many people are affected, as noted on the chart below. If there are more people present than the character can infuence, Awe affects those with lower Willpower ratings first. The power stays in effect for the remainder of the scene or until the character chooses to drop it.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One person</td></tr><tr><td>2 successes</td><td>Two people</td></tr><tr><td>3 successes</td><td>Six people</td></tr><tr><td>4 successes</td><td>20 people</td></tr><tr><td>5 successes</td><td>Everyone in the vampire’s immediate vicinity (an entire auditorium, a mob).</td></tr></table>Those affected can use Willpower points to overcome the effect, but must continue spending Willpower every scene for as long as they remain in the same area as the vampire. As soon as an individual spends a number of Willpower points equal to the successes rolled, he shakes off the Awe completely and remains unaffected for the rest of the night."""
      ),
      Power(
        name='Dread Gaze',
        discipline='presence',
        level=2,
        description="""While all Kindred can frighten others by physically revealing their true vampiric natures - baring claws and fangs, glaring with malevolence, hissing loudly with malice - this power focuses these elements to insanely terrifying levels. Dread Gaze engenders unbearable terror in its victim, stupefying him into madness, immobility, or reckless flight. Even the most stalwart individual will fall back from the vampire’s horrific visage.
_System_: The player rolls ^Charisma + Intimidation^ (difficulty equal to the victim’s Wits + Courage). Success indicates the victim is cowed, while failure means the target is startled but not terrified by the sight. Three or more successes means he runs away in abject fear; victims who have nowhere to run claw at the walls, hoping to dig a way out rather than face the vampire. Moreover, each success subtracts one from the target’s action dice pools next turn. The character may attempt Dread Gaze once per turn against a single target, though she may also perform it as an extended action, adding her successes in order to subjugate the target completely. Once the target loses enough dice that he cannot perform any action, he’s so shaken and terrified that he curls up on the ground and weeps. Failure during the extended action means the attempt falters. The character loses all her collected successes and can start over next turn, while the victim may act normally again. A botch at any time indicates the target is not at all impressed - perhaps even finding the vampire’s antics comical - and remains immune to any further uses of Presence by the character for the rest of the story."""
      ),
      Power(
        name='Entrancement',
        discipline='presence',
        level=3,
        description="""This power bends others’ emotions, making them the vampire’s willing servants. Due to what these individuals see as true and enduring devotion, they heed the vampire’s every desire. Since this is done willingly, instead of having their wills sapped, these servants retain their creativity and individuality. While these obedient minions are more personable and spirited than the mind-slaves created by Dominate, they’re also somewhat unpredictable. Further, since Entrancement is of a temporary duration, dealing with a lapsed servant can be troublesome. A wise Kindred either disposes of those she Entrances after they serve their usefulness, or binds them more securely by a blood bond (made much easier by the minion’s willingness to serve).
_System_: The player spends a blood point and rolls ^Appearance + Empathy^ (difficulty equal to the target’s current Willpower points); the number of successes determines how long the subject is Entranced, as per the chart below. (Subjects can still spend Willpower to temporarily resist, like any other Presence power). The Storyteller may wish to make the roll instead, since the character is never certain of the strength of her hold on the victim. The vampire may try to keep the subject under her thrall, but can do so only after the initial Entrancement wears off. Attempting this power while Entrancement is already in operation has no effect.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>Botch</td><td>Subject cannot be entranced for the rest of the story.</td></tr><tr><td>Failure</td><td>Subject cannot be entranced for the rest of the night.</td></tr><tr><td>1 success</td><td>One hour</td></tr><tr><td>2 successes</td><td>One day</td></tr><tr><td>3 successes</td><td>One week</td></tr><tr><td>4 successes</td><td>One month</td></tr><tr><td>5 successes</td><td>One year</td></tr></table>"""
      ),
      Power(
        name='Summon',
        discipline='presence',
        level=4,
        description="""This impressive power enables the vampire to call to herself any person whom she has ever met. This call can go to anyone, mortal or supernatural, across any distance within the physical world. The subject of the Summons comes as fast as he is able, possibly without even knowing why. He knows intuitively how to find his Summoner - even if the vampire moves to a new location, the subject redirects his own course as soon as he can. After all, he’s coming to the vampire herself, not to some predetermined site. Although this power allows the vampire to call someone across a staggering distance, it is most useful when used locally. Even if the desired person books the next available fight, getting to Kyoto from Milwaukee can still take far longer than the vampire needs. Obviously, the individual’s financial resources are a factor; if he doesn’t have the money to travel quickly, it will take him a far greater time to get there. The subject thinks mainly of reaching the vampire, but does not neglect his own well-being. This is less of a consideration if he only has to cross a room, unless he must get through a gang of gun-wielding punks to do so. The individual retains his survival instincts, and while he won’t shirk physical violence to reach the vampire’s side, he won’t subject himself to suicidal situations. The Summoning dissipates at dawn. Unless the subject is trained to continue toward the vampire after the first call, the immortal must Summon each night until the target arrives. Still, as long as the vampire is willing and able, she is assured to greet her desired subject some night - as long as nothing happens to him along the way, of course.
_System_: The player spends a blood point and rolls ^Charisma + Subterfuge^. The base difficulty is 5; this increases to difficulty 7 if the subject was met only briefy. If the character used Presence successfully on the target in the past, this difficulty drops to 4, but if the attempt was unsuccessful, the difficulty rises to 8. The number of successes indicates the subject’s speed and attitude in responding:
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>Botch</td><td>Subject cannot be Summoned by that vampire for the rest of the story.</td></tr><tr><td>Failure</td><td>Subject cannot be Summoned by that vampire for the rest of the night.</td></tr><tr><td>1 success</td><td>Subject approaches slowly and hesitantly.</td></tr><tr><td>2 successes</td><td>Subject approaches reluctantly and is easily thwarted by obstacles.</td></tr><tr><td>3 successes</td><td>Subject approaches with reasonable speed.</td></tr><tr><td>4 successes</td><td>Subject comes with haste, overcoming any obstacles in his way.</td></tr><tr><td>5 successes</td><td>Subject rushes to the vampire, doing anything to get to her.</td></tr></table>"""
      ),
      Power(
        name='Majesty',
        discipline='presence',
        level=5,
        description="""At this stage, the vampire can augment her supernatural mien a thousandfold. The attractive become paralyzingly beautiful; the homely become hideously twisted. Majesty inspires universal respect, devotion, fear - or all those emotions at once - in those around the vampire. The weak scramble to obey her every whim, and even the most dauntless find it almost impossible to deny her. People affected find the vampire so formidable that they dare not risk her displeasure. Raising their voices to her is difficult; raising a hand against her is unthinkable. Those few who shake off the vampire’s potent mystique enough to oppose her are shouted down by the many under her thrall, before the immortal need even respond.
Under Majesty’s infuence, hearts break, power trembles, and the bold shake. Wise Kindred use this power with caution against mortal and immortal alike. While Majesty can cow infuential politicians and venerable Primogen, the vampire must be careful that doing so doesn’t come back to haunt her. After all, a dignitary brought low before others loses his usefulness quickly, while a humiliated Kindred has centuries to plan revenge.
_System_: No roll is required on the part of the vampire, but she must spend a Willpower point. A subject must make a Courage roll (difficulty equal to the vampire’s ^Charisma + Intimidation^, to a maximum of 10) if he wishes to be rude or simply contrary to the vampire. Success allows the individual to act normally for the moment, although he feels the weight of the vampire’s displeasure crushing down on him. A subject who fails the roll aborts his intended action and even goes to absurd lengths to humble himself before the vampire, no matter who else is watching. The effects of Majesty last for one scene."""
      ),
      Power(
        name='Love',
        discipline='presence',
        level=6,
        description="""The blood bond is one of the most powerful tools in an elder’s inventory. However, more and more childer are aware of how to avoid being bound, so alternatives are needed. The Presence power called Love is one such alternative, as it simulates the effects of the bond without any of the messy side effects. While not as sure a method of control as a true blood bond, nor as long-lasting, Love is still an extremely potent means of command.
_System_: The player spends a blood point and rolls ^Charisma + Subterfuge^ (difficulty equal to the target’s current Willpower points). Success on the roll indicates that the victim feels as attached to the character as if he were blood bound to her. Each success also reduces the victim’s dice pool by one die for any Social rolls to be made against the character. A botch makes the target immune to all of the character’s Presence powers for the rest of the night. This power lasts for one scene and can be applied to the same victim over multiple scenes in the same night."""
      ),
      Power(
        name='Paralyzing Glance',
        discipline='presence',
        level=6,
        description="""Some elders have honed their mastery of Dread Gaze to such a degree that they are said to be able to paralyze with a look. The power’s name is something of a misnomer, as victims of this power are not precisely paralyzed in a physical sense, but rather frozen with sheer terror.
_System_: The character must make eye contact (p.152) with her intended victim. The player then rolls ^Manipulation + Intimidation^ (difficulty equal to the target’s current Willpower points). Success renders the victim so terrified that he falls into a whimpering, catatonic state, unable to take any actions except curling into a fetal position and gibbering incoherently. The condition lasts for a length of time determined by the number of successes rolled. If the victim’s life is directly threatened (by assault, impending sunrise, etc.), the poor wretch may attempt to break out of his paralysis with a Courage roll (difficulty equal to the character’s Intimidation + 3). One success ends the paralysis. A botch sends the victim into a continuous state of Rötschreck for the rest of the night.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Three turns</td></tr><tr><td>2 successes</td><td>Five minutes</td></tr><tr><td>3 successes</td><td>Remainder of the scene</td></tr><tr><td>4 successes</td><td>One hour</td></tr><tr><td>5 successes</td><td>Rest of the night</td></tr><tr><td>6+ successes</td><td>A week (or more, at Storyteller discretion)</td></tr></table>"""
      ),
      Power(
        name='Spark of Rage',
        discipline='presence',
        level=6,
        description="""A vampire possessing this power can shorten tempers and bring old grudges and irritations to the boiling point with a minimum of effort. Spark of Rage causes disagreements and fights, and can even send other vampires into frenzy.
_System_: The player spends a blood point and rolls ^Manipulation + Subterfuge^ (difficulty 8). The number of individuals affected is determined by how many successes are rolled. If this power is used in a crowd, those affected are the people in closest proximity to the character. A vampire affected by this power must spend a Willpower point or roll Self-Control/Instinct (difficulty equal to the character’s ^Manipulation + Subterfuge^); failure sends the target into a frenzy. A botch by the vampire using Spark of Rage sends the invoking character into immediate frenzy.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Two people</td></tr><tr><td>2 successes</td><td>Four people</td></tr><tr><td>3 successes</td><td>Eight people</td></tr><tr><td>4 successes</td><td>20 people</td></tr><tr><td>5 successes</td><td>Everyone in the character’s immediate vicinity</td></tr></table>"""
      ),
      Power(
        name='Cooperation',
        discipline='presence',
        level=7,
        description="""Any elder knows that Kindred are the most difficult beings in existence to force to work together. Peaceful coexistence is not a common tenet of vampiric society. With that in mind, this power can be used to nudge those affected by it into a fragile spirit of camaraderie. Some cynical (or realistic) Ventrue claim that their Clan’s mastery of this Presence effect is the sole reason that anything is ever accomplished in Camarilla conclaves. Ventrue who voice this opinion too loudly also tend to have numerous chances to test just how effective Cooperation is.
_System_: To invoke Cooperation, the player spends a blood point and rolls ^Charisma + Leadership^ (difficulty 8). The number of individuals affected is determined by how many successes the player rolls. Cooperation lasts for the remainder of the scene in which it is invoked, though particularly strong users of Presence may create longer-lasting feelings of non-aggression (at Storyteller discretion) by spending Willpower. While this poweris in effect, all those under its infuence are more favorably disposed toward one another and are more willing to extend trust or make cooperative plans. For the most part, players should simply roleplay Co-operation’s effects, but there are some concrete ramifications to the power’s use. For example, Self-Control/Instinct difficulties to resist frenzy in response to insults from within the target group are decreased by three, and certain Social Flaws may be decreased in impact for the duration of Cooperation.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Two people</td></tr><tr><td>2 successes</td><td>Four people</td></tr><tr><td>3 successes</td><td>Eight people</td></tr><tr><td>4 successes</td><td>20 people</td></tr><tr><td>5 successes</td><td>Everyone in the character’s immediate vicinity</td></tr></table>"""
      ),
      Power(
        name='Ironclad Command',
        discipline='presence',
        level=8,
        description="""Any individual can normally resist the powers of Presence for a brief time through an effort of will. Some elder Toreador and Ventrue have developed such force of personality that their powers of Presence cannot be resisted without truly heroic efforts.
_System_: This power is always in effect once it has been learned. A mortal may not spend Willpower to resist the character’s Presence (for purposes of this power, the definition of “mortal” does not include supernaturally active humans such as ghouls or those who possess True Faith). A supernatural being must roll Willpower (difficulty of the character’s Willpower + 2; difficulties over 10 mean that the roll cannot even be attempted) the first time he attempts to spend a Willpower point to overcome the character’s Presence. For the rest of the night, the maximum number of Willpower points he can spend to resist the vampire’s Presence powers is equal to the number of successes he rolled. A botch doubles the character’s Presence dice pools against the hapless victim for the remainder of the night."""
      ),
      Power(
        name='Pulse of the City',
        discipline='presence',
        level=9,
        description="""A vampire who has developed her Presence to this terrifying degree can control the emotional climate of the entire region around her, up to the size of a large city. This power is always in effect on a low level, attuning those who dwell in the area to the Kindred’s mood, but it can also be used to project a specific emotion into the minds of every being in the area. Pulse of the City affects residents much more strongly than tourists, and also has a significant impact on those individuals who might be elsewhere at the time but who still have strong ties to the affected city.
_System_: The character must be present in the city in question, and have at least a casual, personal knowledge of its streets and makeup (maps won’t help). The player spends a Willpower point and rolls ^Charisma + Streetwise^ (difficulty 9, though specializations or Storyteller fiat may decrease this difficulty if the character is intimately familiar with a particular city). The number of successes indicates how long mortal residents are affected by the particular emotion that the character broadcasts; visitors with no ties to the area and supernatural beings are affected for a duration one success step lower. The character can choose to terminate this effect at any time before it expires.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One minute</td></tr><tr><td>2 successes</td><td>10 minutes</td></tr><tr><td>3 successes</td><td>One hour</td></tr><tr><td>4 successes</td><td>One day</td></tr><tr><td>5 successes</td><td>One week</td></tr></table>Pulse of the City can be used by a character in torpor."""
      )
    ],
    description="""
Presence is the Discipline of emotional manipulation. Vampires with this power can inspire passionate fervor or unreasoning terror in mortals and Kindred alike. In addition, unlike most Disciplines, some of Presence’s powers can be used on entire crowds at one time. Presence can transcend race, religion, gender, class, and (most importantly) supernatural nature. As such, this subtle power is one of the most useful Disciplines a vampire can possess.

Anyone can resist Presence for one scene by spending a Willpower point and succeeding on a Willpower roll (difficulty 8), but the affected individual must keep spending points until he is no longer in the presence of the vampire (or, in the case of Summon, until the effect wears off). Vampires three or more Generations lower than the wielder need only spend a single Willpower to ignore the Presence for an entire night and need not roll Willpower to do so.

The major drawback of Presence is that it controls only the emotions. It causes others to feel a certain way toward the vampire, but does not give her outright control over them. While people weigh strongly the orders that the vampire declares, their minds are still their own. Suicidal or ridiculous directives don’t sound any more sensible just because the person giving them is unusually fascinating. Still, inspired eloquence or significant wealth used in combination with this Discipline can enable the vampire to urge others along a desired course.

The Brujah, Followers of Set, Toreador, and Ventrue Clans are all adept in this Discipline. The Ventrue are arguably the most skilled with its application, however, due to their ability to use Presence and Dominate in efficient combination.
"""
  ),
  Discipline(
    name='Temporis',
    sorcery=False,
    powers= [
      Power(
        name='Hourglass of the Mind',
        discipline='temporis',
        level=1,
        description="""Masters of Temporis value patience and clarity. Time is too complex and dangerous to manipulate incautiously or on a whim. Thus, the first power of Temporis focuses entirely on perception and serves as a permanent alteration of a vampire’s senses.
_System_: Once purchased, this Discipline gives a vampire a perfect sense of time. The vampire knows events to the nearest second or better. Moreover, the Cainite knows whenever the flow of time is mystically disturbed by use of Celerity, greater levels of Temporis, mortal wizardry, or stranger things. Sensing disturbances is instinctive and reflexive, though it requires a successful ^Perception + Awareness^ roll (difficulty 6 for most phenomena, as modified by the Storyteller for distance and intensity)."""
      ),
      Power(
        name='Recurring Contemplation',
        discipline='temporis',
        level=2,
        description="""A vampire with this power may trap a target’s mind into reviewing a set of events over and over until interrupted. This power is extremely subtle and ill-suited to combat or other situations rich in sensory stimuli. However, a cunning vampire can trick a sentry into reliving the tedium of his uneventful watch even as the Cainite draws close enough to strike or slip past. Other uses include the maddening infliction of déjà vu to induce paranoia or make a victim question her senses and her sanity.
_System_: The vampire concentrates on a single victim in his line of sight. The player rolls ^Manipulation + Occult^ (difficulty equal to the victim’s current Willpower). With any successes, the victim falls into a light trance and relives the most recent experiences that preceded her fugue. Alternately, the vampire may evoke another set of specific memories and circumstances from the victim’s past, provided that he has some means of telepathically drawing them forth. The recurring events must be relatively benign, insofar as nothing noteworthy happens or nothing happens that would demand the victim’s immediate action. Thus, in the example of the sentry, the vampire could entrance him and walk past unobserved, but not if the sentry spotted him before invoking the power. Ordinarily, the fugue lasts one minute per success. If the vampire’s player spends a blood point to fuel this power, determine the trance’s duration according to the following chart:
<table><tr><th>Successes</th><th>Duration</th></tr><tr><td>1 success</td><td>one minute</td></tr><tr><td>2 successes</td><td>10 minutes</td></tr><tr><td>3 successes</td><td>one hour</td></tr><tr><td>4 successes</td><td>six hours</td></tr><tr><td>5+ successes</td><td>one day</td></tr></table>Entranced victims are oblivious to their surroundings and the actual flow of time around them. However, the fugue ends immediately if the victim suffers any damage or experiences a sudden jolt to her senses, such as a thunderclap or even a gentle nudge. Normal conversation does not break the trance, although shouting does."""
      ),
      Power(
        name='Leaden Moment',
        discipline='temporis',
        level=3,
        description="""With this power, a vampire may begin to alter the flow of time itself rather than mere perception of events. The vampire gestures and slows the desired object almost to a dead stop. This power can slow incoming bullets to the pace of drifting clouds, or cause an enemy warrior to see the battlefield quicken to a blur of dizzying carnage even as his every motion slows to a crawl.
_System_: The player spends one blood point and rolls ^Intelligence + Occult^. The difficulty depends on the size and nature of the target: a single thrown brick is only difficulty 4, while a crazed ghoul has a difficulty of 9. Targets larger than an adult human cannot be affected with Leaden Moment. It is possible to affect small, closely grouped inanimate objects of the same nature as a single object, though this increases the difficulty by two or more at the Storyteller’s discretion (a hail of bullets might be difficulty 9). This power maybe activated reflexively as a defensive action against projectiles, but otherwise requires a full action on the vampire’s initiative. Though failure carries no special penalty apart from wasting blood, a botch means the vampire mistakenly slows himself rather than the target, counting every 1 as a success for that purpose.
If the vampire succeeds, the object slows to one-half its true speed. Every two successes beyond the first reduce this speed by one additional factor, so three successes slows the target to one third its speed, five successes yields quarter speed, etc. The actual mechanics of such slowing depend on the situation. For projectiles, multiply any successes to hit and final damage by the speed factor, rounded down. Similarly apply the speed modifier to the successes of other actions involving Dexterity, Wits, or Strength for slowed characters. Characters with Celerity may spend one blood point to negate one factor of speed reduction at the expense of the usual extra action provided - for example, one blood point cancels a reduction to one half speed, two blood points cancel one third, etc. Leaden Moment lasts one turn for every two successes rolled, rounded up."""
      ),
      Power(
        name='Patience of the Norns',
        discipline='temporis',
        level=4,
        description="""The vampire can now suspend an inanimate object in time, keeping it frozen in perfect stasis as time passes at normal speed around it. As with lesser Temporis powers, this stasis has both combat and non-combat applications. True Brujah warriors may halt bullets outright rather than merely slowing their approach or casually sidestep a collapsing building. Higher-level variationson this power preserve precious scrolls and artifacts without risk of mold or decay. If any solid object or non-trivial volume of liquid touches a frozen object that did not touch it at the moment of suspension, the item re-enters time with the same properties and velocity as when it stopped. Thus, touching a suspended object with anything more substantial than a raindrop releases it exactly as it was before it stopped.
_System_: The player spends two blood points and rolls ^Intelligence + Occult^ (difficulty 6). The vampire must be able to perceive the object that he’s suspending, so the player may need to make a ^Perception + Alertness^ roll at a difficulty determined by the Storyteller in order to freeze fast-moving objects. If an object exceeds the speed of mortal perception, superhuman perception such as Auspex is required in order to see and stop it (as such, bullets can be stopped with this power, but only if the vampire has at least a dot of Auspex). Objects frozen by this power remain halted according to the number of successes rolled:
<table><tr><th>Successes</th><th>Duration</th></tr><tr><td>1 success</td><td>one turn</td></tr><tr><td>2 successes</td><td>one minute</td></tr><tr><td>3 successes</td><td>10 minutes</td></tr><tr><td>4 successes</td><td>one hour</td></tr><tr><td>5 successes</td><td>one day</td></tr><tr><td>6+ successes</td><td>one week per success over 5</td></tr></table>Suspended objects retain all energy in their suspension, releasing none to the outside universe. A suspended knife has no kinetic energy as far as the rest of the world is concerned and hangs suspended in mid-air until the power is interrupted or the duration expires. Suspended alchemical or chemical processes also halt, including fire. However, any physical contact more substantial than a falling raindrop breaks the suspension."""
      ),
      Power(
        name='Clotho’s Gift',
        discipline='temporis',
        level=5,
        description="""With this power, a vampire momentarily accelerates time through himself. In this brief instant, he moves with the preternatural speed of Celerity. Unlike that Discipline, however, the time dilation of Clotho’s Gift permits any type of action. A vampire may still move or strike faster than the eye can see, but also think, plan, and even invoke other Disciplines that require full concentration. Only the last presents a danger, as it overtaxes the vampire’s unliving stasis.
_System_: The player spends three blood points and rolls ^Intelligence + Occult^ (difficulty 7). For a number of turns equal to half the vampire’s Temporis rating, rounded up, the character may take a number of extra actions at her full dice pool equal to the number of successes rolled. These actions follow the timing rules associated with Celerity, but may be used to take any action. A vampire may use the actions granted by Clotho’s Gift to activate Disciplines multiple times, even Disciplines that cannot be used more than once in a turn (such as Dominate or Thaumaturgy). However, for every action spent activating a Discipline, the vampire suffers one level of unsoakable lethal damage. Only one important exception exists: Any attempt to stack extra actions through Celerity, subsequent applications of Clotho’s Gift or other powers results in immediate Final Death, as the vampire collapses into ash as though burned by the sun."""
      ),
      Power(
        name='Kiss of Lachesis',
        discipline='temporis',
        level=6,
        description="""True Brujah with this power gain limited mastery over the physical age of objects and individuals. It is a trivial matter to accelerate time in a compressed rush, aging a target decades or even centuries in the blink of an eye. It is far more difficult to absorb and unweave entropy, lessening time’s hold. This power does not reverse history in any way; it merely reverses or accelerates the effects of time in terms of wear and tear. Moreover, a target cannot regress to an earlier or incomplete state of being. For inanimate objects, this is the point at which they were assembled. For living beings, it is either adult maturity or the time of birth (or its equivalent). For the undead and other corpses, it is the moment of death.
_System_: In order for the vampire to age a target, the player spends two blood points and rolls ^Manipulation + Occult^. The difficulty equals the target’s true physical age in decades or effective physical age in the case of target’s that have aged unnaturally, such as by means of this power. This difficulty cannot rise higher than 10 or drop below 4. The vampire touches the target and concentrates for a turn. The Cainite may age the target a maximum number of years as determined by the following table, although his player may choose to apply a lesser effect. The Storyteller remains the final arbiter of time’s effect on an object, but living beings aged past their natural lifespan quickly perish.
<table><tr><th>Successes</th><th>Elapsed Time</th></tr><tr><td>1 success</td><td>up to one year</td></tr><tr><td>2 successes</td><td>up to five years</td></tr><tr><td>3 successes</td><td>up to 10 years</td></tr><tr><td>4 successes</td><td>up to 50 years</td></tr><tr><td>5 successes</td><td>up to 100 years</td></tr><tr><td>6+ successes</td><td>up to one century per success over 5</td></tr></table>Removing the effects of time requires greater effort, increasing the difficulty of the activation roll by one. In addition, the vampire suffers one level of unsoakable lethal damage for every success her player chooses to apply. As noted, objects cannot return to an earlier or incomplete state. A silver coin may lose its tarnish and seem newly minted, but it will not revert to an unformed block of metal. Likewise, while an adult may revert to the cusp of his adulthood or a child to a new-born, neither could regress to a pre-natal state. Also, this power only accounts for damage and wear due to time. A child amputee reverted to a baby will not regenerate her missing arm, nor will a broken sword become anything but finely crafted shards. In either application, this power does not change a subject’s mental or mystical properties. Sentient beings retain all memories and any derangements. A vampire regressed to the point of death remains a vampire, not an inanimate corpse - and the regressed Cainite still remembers all Disciplines and keeps any changes in Generation due to diablerie. However, a vampire aged far enough pales considerably or loses any signs of diablerie from his aura."""
      ),
      Power(
        name='Cheat the Fates',
        discipline='temporis',
        level=7,
        description="""Where a vampire with Clotho’s Gift may accelerate with respect to the world, a vampire with this power may step outside of time entirely. During this brief sojourn, the Cainite perceives the world frozen at a stand-still. He can walk about at a leisurely pace to sidestep blows or retreat without being observed. He may even exert force, such as by striking a blow, though no damage is resolved until he re-enters time. However, this power wreaks terrible destruction on a vampire’s unliving body. Used incautiously, a vampire may saunter out of time, only to fall to ash when he returns.
_System_: The player spends one Willpower point and three blood points, and then rolls ^Wits + Occult^ (difficulty 7). This power may be activated reflexively as a defensive action; however, such hasty use reduces the maximum duration to a single turn. Failure does nothing apart from wasting effort and blood, while a botch inflicts one level of aggravated damage for every 1 rolled. If successful, the vampire steps out of time for a number of turns equal to the successes rolled (outside of combat, a turn still only lasts three to five seconds for the purposes of this power). These turns occur for the vampire only while the rest of the world stands still. He may take any action or actions during this time, as many as desired, but he has no access to Disciplines - even innate or perpetual Disciplines such as Potence. The vampire must direct every aspect of Caine’s Curse toward holding back time. If the vampire attacks someone in this state, the target cannot dodge or parry. Resolve the attack normally but do not apply damage. However, if the vampire suffers injury, such as by exposure to sunlight or walking through a frozen flame, apply this damage immediately. The vampire may end his sojourn at any point or wait until the full duration of the power passes, at which point time resumes. Before anything else happens, including resolution of damage inflicted by the vampire, roll one die for every turn the vampire moved out of time. The difficulty is equal to the vampire’s Temporis rating. For every success, the Cainite suffers one level of unsoakable aggravated damage. Apply this damage concurrently with damage suffered by halted victims and continue play on the same turn and initiative the vampire stepped out of time."""
      ),
      Power(
        name='Clio’s Kiss',
        discipline='temporis',
        level=8,
        description="""One of the most subtle manifestations of Temporis’ higher levels, this power allows a vampire to reach into the past and summon events, objects, or even individuals. Clio’s Kiss, named for the muse of history, is the power to bypass the flow of time and bring something - or someone - forward to the present. Some True Brujah scholars use this to observe history as it truly occurred, while others look to the past for aid or to retrieve lost possessions. At least two coordinated attempts by the True Brujah to summon their Antediluvian progenitor have met with catastrophic failure. No one knows if a Sage capable of this power remains. The hope is that Clio’s Kiss faded from knowledge - the bloodline cannot afford a third attempt.
_System_: The player spends half of the character’s current blood pool, rounded up, and rolls ^Stamina + Occult^ (difficulty 8). This power automatically fails if the player spends fewer than five blood points. The number of successes determines the maximum amount of time through which the character may reach:
<table><tr><th>Successes</th><th>Time</th></tr><tr><td>1 success</td><td>24 hours</td></tr><tr><td>2 successes</td><td>one month</td></tr><tr><td>3 successes</td><td>one year</td></tr><tr><td>4 successes</td><td>10 years</td></tr><tr><td>5+ successes</td><td>one century per success over 4</td></tr></table>When a vampire uses this power successfully, the scene she seeks to retrieve materializes around her, briefy supplanting the current environment. This change extends to a maximum volume of a ballroom or similarly proportioned outdoor space (at Storyteller’s discretion). The power affects everyone inside this area by granting them awareness of the summoned events, but the vampire is the only person who may choose to interact with the scene (though he may remain invisible and disembodied). All others must remain incorporeal observers until time reasserts itself and the scene fades. They may move about to change their vantage point, but can take no other action.
If the vampire wants to remove an object or individual from the scene, bringing them forward to the present, the player must spend a dot of Willpower. Once this is done, the conjured scene fades away and present reality returns. Only the summoned object or person remains.
This power can never alter the course of history in any significant manner. Should an object or person have a meaningful role yet to play at the time it is removed, the weight of time crashes upon the vampire and he vanishes in its current. Whether such folly results in destruction or propels the vampire far into the future remains unknown and likely unknowable. Like-wise, any changes the vampire makes to a summoned scene unravel as soon as he departs. Like a play, time may be altered by the removal of extras, but the script stays the same - however cruel a fate, Carthage must be destroyed. As always, the Storyteller remains the final judge of what this power can achieve and need not reveal all limitations until a vampire attempts a change. It is possible to summon a person from a point close to his death, assuming he perished without observers. Likewise, a manuscript destroyed when the Library of Alexandria burned can be called after it is last read. Calling the very library from Alexandria would be impossible, not only for its size but also the necessity and significance of its ruins. Finally, the previous form of a currently existing object cannot be summoned, if only because its continued existence validates a role in history. Storytellers need not consider every ramification of paradox, but this power has tremendous potential for abuse and should be adjudicated accordingly."""
      ),
      Power(
        name='Tangle Atropos’ Hand',
        discipline='temporis',
        level=9,
        description="""This manifestation of Temporis is at once the most flagrant and subtle twist of time - the power of second chances. The existence of such power is only a theory and a fearfully whispered rumor, for who can ever know when or how time itself unraveled and changed?
_System_: The player spends a dot of Willpower and three blood points and rolls ^Wits + Occult^ (difficulty 8). Every additional point of permanent Willpower spent beyond the first adds one automatic success to the roll. Use of this power is reflexive and may be done at any moment, even on a turn in which the vampire has used other Disciplines. If successful, the Cainite’s mind flashes back to his earlier self with full memory of the events that transpired and now only might transpire. This rewind encompasses one turn for every success rolled, and inflicts an equal number of levels of unsoakable aggravated damage. Assuming the vampire does nothing, every event plays out exactly as before. Once the vampire takes a new action of any sort, time shifts to encompass a new future and fate is no longer fixed."""
      )
    ],
    description="""
The True Brujah bloodline claims a peculiar Discipline that allows them some control over the flow of time. Masters of Temporis often grow ever more detached from the passage of ages. This, combined with the natural tendency for Sages to grow emotionally and spiritually distant, makes True Brujah elders exceptionally dangerous. They know that all life is finite, and so they feel no compunction about ending it.
"""
  ),
  Discipline(
    name='Animalism',
    sorcery=False,
    powers= [
      Power(
        name='Feral Whispers',
        discipline='animalism',
        level=1,
        description="""This power is the basis from which all other Animalism abilities grow. The vampire creates an empathic connection with a beast, thereby allowing him to communicate or issue simple commands. The Kindred locks eyes with the animal, transmitting his desires through sheer force of will. Although it isn’t necessary to actually “speak” in chirps, hisses, or barks, some vampires find that doing so helps strengthen the connection with the animal. Eye contact must be maintained the entire time; if it’s broken, the Kindred must re-establish contact to continue communication. The simpler the creature, the more difficult it becomes to connect with the animal’s Beast. Mammals, predatory birds, and larger reptiles are relatively easy to communicate with. Insects, invertebrates, and most fish are just too simple to connect with.
Feral Whispers provides no guarantees that an animal will want to deal with the vampire, nor does it ensure that the animal will pursue any requests the vampire makes of it. Still, it does at least make the creature better disposed toward the Kindred. The manner in which the vampire presents his desires to the animal often depends on the type of creature. A Kindred can often bully smaller beasts into heeding commands, but he’s better off couching orders for large predators as requests.
If the vampire successfully uses the power, the animal performs the command to the best of its ability and intellect. Only the very brightest creatures understand truly complex directives (orders dealing with conditional situations or requiring abstract logic). Commands that the animal does understand remain deeply implanted, however, and guide its behavior for sometime.
_System_: No roll is necessary to talk with an animal, but the character must establish eye contact (see p.152) first. Issuing commands requires a ^Manipulation + Animal Ken^ roll. The difficulty depends on the creature: Predatory mammals (wolves, cats, vampire bats) are difficulty 6, other mammals and predatory birds (rats, owls) are difficulty 7, and other birds and reptiles (pigeons, snakes) are difficulty 8. This difficulty is reduced by one if the character speaks to the animal in its “native tongue”, and can be adjusted further by circumstances and roleplaying skill (we highly recommend that all communication between characters and animals be roleplayed).
The number of successes the player achieves dictates how strongly the character’s command affects the animal. One success is sufficient to have a cat follow an individual and lead the character to the same location, three successes are enough to have a raven spy on a target for weeks, and five successes ensure that a grizzly ferociously guards the entrance to the character’s wilderness haven for some months. The character’s Nature plays a large part in how he approaches these conversations. The character might try intimidating, teasing, cajoling or rationalizing. The player should understand that he does not simply play his character in these situations, but the Beast Within as well. Using this power cannot force an animal to do something against its nature, or to force a creature to risk its life. While the aforementioned grizzly would stand guard to the vampire’s haven and even fight for it, it would not do so against obviously superior numbers or something overwhelmingly supernatural. A predatory bird might be convinced to harry a target, but would definitely not hold ground. A docile dog or skittish cat would have no problem with reporting something it had seen, but it wouldn’t enter combat unless given no other option - though it would likely agree to stand and fight and then flee at the first opportunity, if a harsh Kindred demanded it."""
      ),
      Power(
        name='Beckoning',
        discipline='animalism',
        level=2,
        description="""The vampire’s connection to the Beast grows strong enough that he may call out in the voice of a specific type of animal - howling like a wolf, shrilling like a raven, etc. This call mystically summons creatures of the chosen type. Since each type of animal has a different call, Beckoning works for only a single species at a time. All such animals within earshot are summoned, and some percentage of them will heed the Beckoning if it is successful. While the vampire has no further control over the beasts who answer, the animals who do are favorably disposed toward him and are at least willing to listen to the Kindred’s concerns. (The vampire can then use Feral Whispers on individual animals to command them, which may be at a decreased difficulty at Storyteller discretion).
_System_: The player rolls ^Charisma + Survival^ (difficulty 6) to determine the response to the character’s call; consult the table below. Only animals that can hear the cry will respond. If the Storyteller decides no animals of that type are within earshot, the summons goes unanswered. The call can be as specific as the player desires. A character could call for all bats in the area, for only the male bats nearby, or for only the albino bat with the notched ear he saw the other night.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>A single animal responds.</td></tr><tr><td>2 successes</td><td>One-quarter of the animals within earshot respond.</td></tr><tr><td>3 successes</td><td>Half of the animals respond.</td></tr><tr><td>4 successes</td><td>Most of the animals respond.</td></tr><tr><td>5 successes</td><td>All of the animals respond.</td></tr></table>"""
      ),
      Power(
        name='Quell the Beast',
        discipline='animalism',
        level=3,
        description="""As the supreme predators of the natural world, Kindred are highly attuned to the bestial nature that dwells within every mortal heart. A vampire who develops this power may assert his will over a mortal (animal or human) subject, subduing the Beast within her. This quenches all powerful, strong emotions - hope, fury, love, fear - within the target. The Kindred must either touch his subject or stare into her eyes to channel his will effectively. Mortals who lack the fire of their inner Beasts are quite tractable, reacting to even stressful situations with indifference. Even the most courageous or maddened mortal becomes apathetic and listless, while an especially sensitive individual may suffer from a phobic derangement while under the power’s infuence. Different Clans evoke this power in different ways, though the effect itself is identical. Tzimisce call it Cowing the Beast, since they force the mortal’s weaker spirit to shrivel in fear before the Kindred’s own inner Beast. Nosferatu refer to it as Song of Serenity, since they soothe the subject’s Beast into a state of utter complacency, thus allowing them to feed freely. Gangrel know the power as Quell the Beast, and force the mortal spirit into a state of fear or apathy as befits the individual vampire’s nature.
_System_: The player rolls ^Manipulation + Intimidation^ if forcing down the Beast through fear, or ^Manipulation + Empathy^ if soothing it into complacency. The difficulty of the roll is 7 in either case. This is an extended action requiring as many total successes as the target has Willpower. Failure indicates that the player must start over from the beginning, while a botch indicates that the vampire may not affect that subject’s Beast for the remainder of the scene. When a mortal’s Beast is cowed or soothed, she can no longer use or regain Willpower. She ceases all struggles, whether mental or physical. She doesn’t even defend herself if assaulted, though the Storyteller may allow a Willpower roll if the mortal believes her life is truly threatened. To recover from this power, the mortal’s player rolls Willpower (difficulty 6) once per day until she accumulates enough successes to equal the vampire’s ^Willpower^. Kindred cannot be affected by this power. Though a vampire’s Beast cannot be cowed with this ability, the Storyteller may allow characters to use the “soothing” variation of this power to pull a vampire out of frenzy. With three or more successes, the frenzying vampire may roll again to pull herself out of frenzy, using the same difficulty as the stimulus that caused the frenzy originally."""
      ),
      Power(
        name='Subsume the Spirit',
        discipline='animalism',
        level=4,
        description="""By locking his gaze with that of an animal, the vampire may mentally possess the creature. Some elders believe that since animals don’t have souls but spirits, the vampire can move his own soul into the animal’s body. Many younger vampires think it a matter of transferring one’s consciousness into the animal’s mind. In either case, it’s agreed that the beast’s weaker spirit (or mind) is pushed aside by the Kindred’s own consciousness. The vampire’s body falls into a motionless state akin to torpor while his mind takes control of the animal’s actions, remaining this way until the Kindred’s consciousness returns. Some haughty Tzimisce eschew this power, considering it debasing to enter the body of a lesser creature. When they do stoop to using it, they possess only predators. Conversely, Gangrel revel in connecting to the natural world in this way. They delight in sampling different animals’ natures.
_System_: The player rolls ^Manipulation + Animal Ken^ (difficulty 8) as the character looks into the animal’s eyes (see sidebar on p.152). The number of successes allows the character to employ some mental Disciplines while possessing the animal, as noted below.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Cannot use Disciplines</td></tr><tr><td>2 successes</td><td>Can use Auspex and other sensory powers</td></tr><tr><td>3 successes</td><td>Can also use Presence and other powers of emotional manipulation</td></tr><tr><td>4 successes</td><td>Can also use Dementation, Dominate, and other powers of mental manipulation</td></tr><tr><td>5 successes</td><td>Can also use Chimerstry, Necromancy, Thaumaturgy, and other mystical powers</td></tr></table>This power entwines the character’s consciousness closely with the animal’s spirit, so much so that the character may continue to think and feel like that animal even after breaking the connection. This effect continues until the character spends a total of seven nights or three Willpower points to resist and finally overcome the animal nature. This should be role-played, though the character will be affected to a lesser degree if the player chooses to spend Willpower. At the end of any particularly exciting incident during possession, the player rolls ^Wits + Empathy^ (difficulty 8) for the character to retain his own mind. Failure indicates that the character’s mind returns to his own body, but still thinks in purely animalistic terms. A botch returns the character to his body, and also sends him into frenzy. The character may travel as far from his own physical body as he chooses while possessing the animal. The character retains no conscious connection with his vampire body during this time, though. The vampire may also venture out during the day, albeit in the animal’s body. However, the character’s own body must be awake to do so, requiring a successful roll to remain awake (see p.262). If the character leaves the animal’s body (by choice, if his body falls asleep, or after sustaining significant injury), the vampire’s consciousness returns to his physical form instantaneously. Although the vampire has no conscious link to his body while possessing the animal, he does form a sympathetic bond. Anything the animal feels, the vampire also experiences, from pleasure to pain. In fact, any damage the animal’s body sustains is also applied to the character’s body, though the Kindred body may soak as normal. If the animal dies before the vampire’s soul can flee from the body, the character’s body falls into torpor. Presumably this is in sympathetic response to the massive trauma of death, but some Kindred believe that the vampire’s soul is cast adrift during this time and must find its way back to the body."""
      ),
      Power(
        name='Drawing Out the Beast',
        discipline='animalism',
        level=5,
        description="""At this level of Animalism, the Kindred has a keen understanding of the Beast Within, and is able to release his feral urges upon another mortal or vampire. The recipient of the vampire’s Beast is instantly overcome by frenzy. This is an unnatural frenzy, however, as the victim is channeling the Kindreds own fury. As such, the vampire’s own behavior, expressions, and even speech patterns are evident in the subject’s savage actions. Gangrel and Tzimisce are especially fond of unleashing their Beasts onto others. Gangrel do so to stir their ghouls into inspired heights of savagery during combat. Tzimisce care less about who receives their Beast than retaining their own composure.
_System_: The player must announce his preferred target (since it must be someone within sight, Drawing Out the Beast cannot be used if the vampire is alone), then roll ^Manipulation + Self-Control/Instinct^ (difficulty 8). Refer to the table below for the results:
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>The character transfers the Beast, but unleashes it upon a random individual.</td></tr><tr><td>2 successes</td><td>The character is stunned by the effort and may not act next turn, but transfers the Beast successfully. Alternatively, the character may act normally during the turn, but must spend a Willpower point or suffer a single level of lethal damage.</td></tr><tr><td>3+ successes</td><td>The character transfers the Beast successfully.If the attempt fails, the character himself immediately enters frenzy. As the character relaxes in expectation of relieving his savage urges, the Beast takes thatopportunity to dig deeper. In this case, the frenzy lasts twice as long as normal and is twice as difficult to shrug off; its severity also increases exponentially. Botching this roll is even more catastrophic; the heightened frenzy grows so extreme that not even expending Willpower curbs its duration or effects. The character is a hapless victim to the terrible fury of his Beast, and may well hurl herself into a savage, flesh-rending rampage that leaves the Masquerade (and unfortunate nearby onlookers) in tatters.</td></tr></table>If the character leaves the target’s presence before the frenzy expends itself, the vampire loses his Beast, perhaps permanently. While no longer vulnerable to frenzy, the character cannot use or regain Willpower and becomes increasingly lethargic. To recover the Beast, he must find the person who now possesses it (who likely isn’t enjoying herself very much) and coax the Beast into its proper vessel. The most effective way to do so is to behave in ways that make the Beast want to return - however, this isn’t a guarantee that it will wish to do so. Alternatively, the character can simply kill the host (thus causing the Beast to return to the vampire immediately)."""
      ),
      Power(
        name='Animal Succulence',
        discipline='animalism',
        level=6,
        description="""Most vampires find the blood of animals flat, tasteless and lacking in nutritional value. Some Gangrel and Nosferatu, however, have refined their understanding of the spirits of such “lesser prey” to the point that they are able to draw much more sustenance from beasts than normal Kindred can. This power does not allow an elder to subsist solely on the blood of animals, but it does allow him to go for extended periods of time without taking vitae from humans or other Kindred.
_System_: No roll is needed; once learned, this power is always in effect. Animal Succulence allows a character to count each blood point drawn from an animal as two in her blood pool. This does not increase the size of the vampire’s blood pool, just the nutritional value of animal blood. Animal Succulence does not allow a character to completely ignore his craving for the blood of “higher” prey; in fact, it heightens his desire for “real food”. Every three times (rounded down) the character drinks from an animal, a cumulative +1 difficulty is applied to the next Self-Control/Instinct roll the player makes when the character is confronted with the possibility of dining on human or Kindred blood. Animal Succulence does not increase the blood point value of the blood of other supernatural creatures (Gangrel, werecreatures, and so on) who have taken animal forms, nor does it change the vampire’s feeding preferences (such as the Ventrue have)."""
      ),
      Power(
        name='Shared Soul',
        discipline='animalism',
        level=6,
        description="""This power allows a character to probe the mind of any one animal she touches. Shared Soul can be very disconcerting to both parties involved, as each participant is completely immersed in the thoughts and emotions of the other. With enough effort or time, each participant can gain a complete understanding of the other’s mind. Shared Soul is most often used to extract an animal’s memories of a specific event, but some Gangrel use this power as a tool in the search for enlightenment, feeling they come to a better understanding of their own Beasts through rapport with true beasts. Too close of a bond, however, can leave the two souls entangled after the sharing ends, causing the vampire to adopt mannerisms, behavior patterns, or even ethics (or lack thereof) similar to those of the animal.
_System_: The character touches the intended subject creature, and the player rolls ^Perception + Animal Ken^ (difficulty 6). The player spends a Willpower point for every turn past the first that contact is maintained. Locating a specific memory takes six turns, minus one turn for every success on the roll. A complete bond takes 10 turns, minus one turn for every success on the roll. A botch on this roll may, at the Storyteller’s discretion, send the vampire into a frenzy or give the character a derangement related to the behavior patterns of the animal (extreme cowardice if the vampire contacted the soul of mouse, bloodlust if the subject was a rabid dog, and so forth)."""
      ),
      Power(
        name='Species Speech',
        discipline='animalism',
        level=6,
        description="""The basic power Feral Whispers (Animalism 1) allows character to communicate with only one animal at a time. With Species Speech, a character can enter into psychic communion with all creatures of a certain species that are present. Species Speech is most often used after an application of The Beckoning (Animalism 2), which can draw a crowd of likely subjects.
_System_: The player rolls ^Manipulation + Animal Ken^ (difficulty 7) to establish contact with the targeted group of animals. Once the character establishes contact, the player makes a second roll to issue commands. There is no practical upper limit on the number of animals that can be commanded with this power, although all of the intended subjects must be in the vampire’s immediate vicinity. Only one species of animal can be commanded at a time; thus, if a character is standing in the middle of the reptile house at the zoo, she could command all of the Komodo dragons, all of the boa constrictors, or all of the skinks, but she could not simultaneously give orders to every reptile or snake present. Species Speech functions much like Feral Whispers in all other respects. Note: Players (and Storytellers) shouldn’t get too wrapped up in species differences like northern diamondback rattlesnakes and southeastern diamondback rattlesnakes. At Storyteller discretion, the expenditure of an additional Willpower point allows the character’s commands to extend to members of a similar species to the one initially commanded."""
      ),
      Power(
        name='Conquer the Beast',
        discipline='animalism',
        level=7,
        description="""Masters of Animalism have a much greater understanding of both beasts in general and the Beast in particular. Those who have developed this power can master their own Beasts to a degree impossible for lesser Kindred to attain. Conquer the Beast allows the vampire both to control her frenzies and to enter them at will. Some elders say that the development of this power is one of the first steps on the road to Golconda.
_System_: The character can enter frenzy at will. The player rolls ^Willpower^ (difficulty 7). Success sends the character into a controlled frenzy. He can choose his targets at will, but gains limited Dominate and wound penalty resistance and Rötschreck immunity as per the normal frenzy rules (p.298). A botch on the roll sends the vampire into an uncontrolled frenzy which Conquer the Beast may not be used to end. The player may also roll ^Willpower^ (difficulty 9) to enable the character to control an involuntary frenzy. In this case, a Willpower point must be spent for every turn that the vampire remains in frenzy. The player may make Self-Control/Instinct rolls as normal to end a frenzy, but if the vampire runs out of Willpower points before the frenzy ends, he drops into an uncontrolled frenzy again. A botch on the Willpower roll raises the difficulty of the vampire’s Self-Control/Instinct rolls by two and renders Conquer the Beast unusable for the remainder of the night."""
      ),
      Power(
        name='Taunt the Caged Beast',
        discipline='animalism',
        level=8,
        description="""Some Kindred are so attuned to the Beast that they can unleash it in another individual at will. Vampires who have developed this power are able to send adversaries into frenzy with a finger’s touch and the resultant momentary contact with the victim’s Beast. The physical contact allows the vampire’s own Beast to reach out and awaken that of the victim, enraging it by threatening its territory.
_System_: The character touches the target. The player spends a Willpower point and rolls ^Manipulation + Empathy^ (difficulty 7). The victim makes a Self-Control/Instinct roll (difficulty 5 + the number of successes); failure results in an immediate frenzy. A botch causes the character to unleash his own Beast and frenzy instead. This power may be used on those individuals who are normally incapable of frenzy, sending ordinary humans into murderous rages worthy of the most bloodthirsty Brujah berserker."""
      ),
      Power(
        name='Unchain the Beast',
        discipline='animalism',
        level=9,
        description="""The self-destructive nature of Cainites can be turned against them by an elder who possesses this formidable power. With a glance, the vampire can awaken the Beasts of her enemies, causing physical injury and excruciating agony as the victim’s own violent impulses manifest in physical form to tear him apart from within. A target of this power erupts into a fountain of blood and gore as claw and bite wounds from an invisible source spontaneously tear his flesh asunder.
_System_: The character makes eye contact (see p.152) with the intended victim. The player spends three blood points and rolls ^Manipulation + Intimidation^ (difficulty of the victim’s Self-Control/Instinct + 4). Each success inflicts one health level of aggravated damage, which can be soaked normally. A botch inflicts one health level of lethal damage to the invoking character for each “1” rolled. This damage can also be soaked normally."""
      )
    ],
    description="""
The Beast resides within all creatures, from scuttling cockroaches to scabrous rats up through untamed wolves and even powerful Kindred elders. Animalism allows the vampire to amplify his intensely primordial nature. He can not only communicate with animals, but can also force his will upon them, directing such beasts to do as he commands. As the vampire grows in power, he can even control the Beast within mortals and other supernaturals.

Beasts grow distinctly agitated in the presence of a vampire who lacks this Discipline or the Skill of Animal Ken, often to the point of attacking or running from the vampire. In contrast, vampires possessing Animalism exude a dominant vibe to lower creatures, which attracts them.

Animalism is commonly found with vampires of the Gangrel and Nosferatu Clans. Manipulation and Charisma are important for the use of Animalism powers; the stronger the vampire’s personality, the more influence he has over animals.
"""
  ),
  Discipline(
    name='Celerity',
    sorcery=False,
    powers= [
      Power(
        name='Celerity 1',
        discipline='celerity',
        level=1,
        description="""Add 1 die  to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Celerity 2',
        discipline='celerity',
        level=2,
        description="""Add 2 dice to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Celerity 3',
        discipline='celerity',
        level=3,
        description="""Add 3 dice to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Celerity 4',
        discipline='celerity',
        level=4,
        description="""Add 4 dice to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Celerity 5',
        discipline='celerity',
        level=5,
        description="""Add 5 dice to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Celerity 6',
        discipline='celerity',
        level=6,
        description="""Add 6 dice to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Projectile',
        discipline='celerity',
        level=6,
        description="""Despite the fact that a vampire with Celerity moves at incredible speeds, any bullets he fires or knives he throws while in this state don’t move any faster than they normally would. Scientifically minded Kindred have been baffed by the phenomenon for centuries, but more pragmatic ones have found a way to work around it. Projectile enables a vampire to take his preternatural speed and transfer it into something he has thrown, fired, or launched.
_System_: Projectile requires the expenditure of a blood point. In addition, the player must decide how many levels of his character’s Celerity he is putting into the speed of the launched object. Thus, a character with Celerity 6 in addition to Projectile could decide to put three dots’ worth of speed into a knife he is throwing, and use the other three dots as dice or potential extra actions as per normal. Each dot of Celerity infused into a thrown object becomes an automatic success to the attack’s damage roll, assuming the weapon or projectile actually hits."""
      ),
      Power(
        name='Celerity 7',
        discipline='celerity',
        level=7,
        description="""Add 7 dice to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Flower of Death',
        discipline='celerity',
        level=7,
        description="""In combat, speed kills. A proper application of Celerity in combat can turn even the meekest Cainite into a walking abattoir. How much more deadly, then, is a vampire with the ability to utilize his preternatural speed to the utmost in combat? Flower of Death allows a vampire to take his Celerity and apply it in full to each hand-to-hand or melee attack he makes.
_System_: Flower of Death costs four blood points, but the spectacular effect is well worth it. Once the power is in effect, the vampire’s bonus dice for Dexterity rolls get added to every dice pool for attack the character makes (even if the roll doesn’t use Dexterity) until the end of the scene. Further, even if the Kindred uses some of his Celerity dots for extra actions during the scene, these extra dice are still available. The effect is limited to hand-to-hand or melee weapon attacks - firearms, bows, and other ranged weapons are excluded - but does grant the attacker additional dice for damage rolls.
Flower of Death is not cumulative - it is impossible to “layer” uses of the power over one another to create astronomical dice pools."""
      ),
      Power(
        name='Celerity 8',
        discipline='celerity',
        level=8,
        description="""Add 8 dice to DEX rolls. Activate with blood for an additional action per turn."""
      ),
      Power(
        name='Zephyr',
        discipline='celerity',
        level=8,
        description="""Zephyr produces an effect vaguely similar to one of the legendary comic book-style uses of enhanced speed, allowing its practitioner to run so fast he can run across water. Particularly successful applications of Zephyr allow a vampire to go so far as to run up walls and, in at least one recorded instance, across a ceiling.
_System_: Zephyr requires the expenditure of one point of blood and one point of Willpower. Unfortunately, Zephyr requires such extremes of concentration that it cannot be combined with any form of attack, or indeed, with most any sort of action at all. If a character using Zephyr feels the need to do something else while moving at such tremendous speeds, a ^Willpower^ roll (difficulty 8) is required. Needless to say, botches at Zephyr speed can be spectacular in all the wrong ways.
Most times, a vampire moving at such a rate of speed is barely visible, appearing more as a vampire-shaped blur than anything else. Observers must succeed on a Perception + Alertness roll (difficulty 7) to get a decent look at a Kindred zooming past in this fashion."""
      ),
      Power(
        name='Celerity 9',
        discipline='celerity',
        level=9,
        description="""Add 9 dice to DEX rolls. Activate with blood for an additional action per turn."""
      )
    ],
    description="""
Not all vampires are slow, meticulous creatures. When needed, some vampires can move fast - really fast. Celerity allows Assamites, Brujah, and Toreadors to move with astonishing swiftness, becoming practically a blur. The Assamites use their speed in conjunction with stealth to strike quickly and viciously from the shadows before they are noticed. Brujah, on the other hand, simply like the edge that the power gives them against overwhelming odds. The Toreador are more inclined to use Celerity to provide an air of unnatural grace to live performances or for an extra push to complete a masterpiece on time, but they can be as quick to draw blood as any assassin or punk when angered.

_System:_ Each point of Celerity adds one die to every Dexterity-related dice roll. In addition, the player can spend one blood point to take an extra action up to the number of dots he has in Celerity at the beginning of the relevant turn; this expenditure can go beyond her normal Generation maximum. Any dots used for extra actions, however, are no longer available for Dexterity-related rolls during that turn. These additional actions must be physical (e.g., the vampire cannot use a mental Discipline like Dominate multiple times in one turn), and extra actions occur at the end of the turn (the vampire’s regular action still takes place per her initiative roll).

Normally, a character without Celerity must divide their dice if she wants to take multiple actions in a single turn, as per p. 248. A character using Celerity performs his extra actions (including full movement) without penalty, gaining a full dice pool for each separate action. Extra actions gained through Celerity may not in turn be split into multiple actions, however. 
"""
  ),
  Discipline(
    name='Thanatosis',
    sorcery=False,
    powers= [
      Power(
        name='Hag’s Wrinkles',
        discipline='thanatosis',
        level=1,
        description="""Perpetual rot makes the character’s flesh malleable. The Samedi can open large folds in her flesh, storing objects in them like a kangaroo’s pouch. She can also massage the slimy flaps of fatty tissue to alter her appearance slightly (though this does nothing for the smell). Other Kindred can learn this Discipline, of course, but if they do not possess the “advantage” of having skin that already falls in droops and folds, large wrinkles and bulges may be visible.
_System_: This power requires one turn to shape the wrinkles and the expenditure of a blood point. If the power is used to distort a character’s features, the Samedi player must roll ^Stamina + Subterfuge^ (difficulty 8). Success raises the difficulty to visually identify the character by one and lasts for one hour per success rolled. If the character is attempting to hide a small object (a wallet, a letter, a small pistol), the roll and duration are the same, but all rolls made to see if the object is detected (for example, a pat-down search or a security guard’s visual inspection) are at +2 difficulty."""
      ),
      Power(
        name='Putrefaction',
        discipline='thanatosis',
        level=2,
        description="""The character can, with a touch, inflict decay upon a target. Hair falls out, teeth loosen, flesh rots and fungus grows on the skin. This power works on targets living and undead, and is obviously quite unsettling both physically and psychologically.
_System_: This power first requires that the character touch his intended target. The player then rolls ^Dexterity + Medicine^ (difficulty of the target’s Stamina + Fortitude) and spends a blood point. Success inflicts one health level of lethal damage on the target and removes one point of the victim’s Appearance. This Appearance loss returns to vampires at the rate of one point per night, but is permanent for mortals (though plastic surgery can correct mortals’ physical disfigurement). If a mortal suffers three or more health levels of damage from repeated uses of this power in one scene, gangrene or other ailments may occur. Putrefaction can also be used on plants, in which case the target becomes blighted and withered. It cannot, however, be used on inanimate objects such as cars or wooden stakes."""
      ),
      Power(
        name='Ashes to Ashes',
        discipline='thanatosis',
        level=3,
        description="""The character collapses into a thick, sticky white powder. While in this form, the character cannot move and is only dimly aware of her surroundings, but is immune to fire and sunlight (meaning that this power is an effective escape in some situations). The character must take care, though - if the ashes are scattered, she might never be able to reform.
_System_: The transformation to ashes requires one turn and the expenditure of two blood points. While the character is in ash form, the player must make a ^Perception + Alertness^ roll (difficulty 9) for any scene in which she wishes her character to be aware of her surroundings. Reforming from the heap of ashes takes one turn. If the character is in a confined space (such as an urn), she explodes from it in a suitably dramatic manner as she brings herself back to full size. If a Samedi is scattered while in this form, one health level and one blood point are lost for each tenth (roughly) of the character that has been dissipated. Five blood points are required to heal each health level lost in this manner. At the Storyteller’s discretion, the Samedi may be missing limbs or vital organs (though never the head or the heart) until the missing health levels are healed."""
      ),
      Power(
        name='Withering',
        discipline='thanatosis',
        level=4,
        description="""The Stiff can shrivel and render useless an opponent’s limb. This power works on Kindred as well as mortals. Kindred, of course, are horrified by the power, as they tend to think of their bodies as immortal and invulnerable to such ravages.
_System_: The Samedi must touch the limb he intends to shrivel. The player spends a Willpower point and rolls ^Manipulation + Medicine^ (difficulty equal to the victim’s Stamina + Fortitude). Three successes are required for this power to shrink a limb. With one or two successes, the victim takes one health level of bashing damage, which may be soaked normally, but is otherwise unaffected (If the Withering attempt is successful, the subject suffers no health level of damage, but rather the withering of the limb itself).
The effects of Withering fade after one night if a vampire or other supernatural creature is the victim, but mortals (including mages) are permanently afflicted unless some type of supernatural healing is used. If this power is used on an arm or leg, the limb instantly becomes useless. If this power is used on an opponent’s head, mortal victims die instantly. Kindred lose two points from all Mental Attributes while their heads are shrunken and are unable to use any Disciplines except Celerity, Fortitude, and Potence. Multiple uses of this power on the same appendage have no additional effect."""
      ),
      Power(
        name='Necrosis',
        discipline='thanatosis',
        level=5,
        description="""A more horrific and potent form of Putrefaction, this power causes flesh to decay and slough off, exposing the bone beneath. Use of this power can render an opponent unable to move from lack of muscle tissue.
_System_: The Samedi must make contact with the victim. The player spends two blood points and rolls ^Dexterity + Medicine^ (difficulty of the target’s Stamina + Fortitude). The victim takes a number of health levels of lethal damage equal to the number of successes rolled and suffers additional effects as listed below.
<table><tr><th>Successes</th><th>Effects</th></tr><tr><td>1 success</td><td>No additional effects</td></tr><tr><td>2 successes</td><td>Lose one point of Appearance</td></tr><tr><td>3 successes</td><td>Lose a point each of Appearance and Dexterity</td></tr><tr><td>4 successes</td><td>Lose a point each of Appearance, Dexterity, and Strength</td></tr><tr><td>5+ successes</td><td>Lose two points of Appearance and one each of Dexterity and Strength </td></tr></table>Attributes lost in this manner are regained when all damage from the Necrosis attack is healed. If a victim is reduced to zero Strength or Dexterity, he is unable to move except for weak flailing and crawling but may still use Disciplines and spend blood points normally."""
      ),
      Power(
        name='Creeping Infection',
        discipline='thanatosis',
        level=6,
        description="""Rumors state that Samedi, especially elders, are infectious, that their presence or touch causes a wasting disease. This power might be the source of these rumors. Creeping Infection allows the Samedi to use Putrefaction, Withering, or Necrosis, but prevent the Discipline from taking effect until the Samedi is well away. This power allows for subtle curses, or insurance against someone who might hire the Samedi and then refuse to pay up.
_System_: The player must successfully roll for a use of Putrefaction, Withering, or Necrosis, as above, and may delay the effect for a number of months equal to the Samedi’s Stamina. The player may spend a blood point at any time during this period in order to activate the dormant power. If the Creeping Infection is not used before the end of its duration, it fades away with no effect."""
      ),
      Power(
        name='Dust to Dust',
        discipline='thanatosis',
        level=7,
        description="""With this power, the Samedi retains cohesion, awareness, and mobility while in ash form. While not as impressive as the Tzimisce Horrid Form, a clever Stiff can find many tactical uses for such a power.
_System_: While a pile of ash, the Samedi remains fully conscious and may use any Discipline powers that being a pile of dust would permit (for instance, Majesty will make the pile of dust very impressive, and no maid in her right mind would dare sweep it up). The character cannot be blown apart by high winds, and any deliberate attempt to separate the pile of ash may be resisted with a die pool equaling the character’s combined Strength, Stamina, Potence, and Fortitude. The character may move voluntarily at a speed no higher than that at which a pile of normal dust would be blown by the wind, even if he is indoors. He does not have to move in the direction of the prevailing air currents, and may “flatten” himself by spreading his ashes thinly so as to slip under doors and through cracks. This power functions like Ashes to Ashes in all other respects."""
      ),
      Power(
        name='Putrescent Servitude',
        discipline='thanatosis',
        level=8,
        description="""The practice of creating zombified servants is an old one in vodoun, though most powerful Samedi can perform feats of reanimation that put the finest houngan to shame. The Stiff can raise a recently dead person as an undead servant. The zombie can’t think critically or move faster than a quick walk, but it is tough, strong, and unquestioningly loyal.
_System_: The first application of this power allows the Samedi to feed some of her blood to a recently dead corpse (maximum time since death equal to the Samedi’s Stamina in weeks) in order to animate it. Three blood points must be spent to bring the corpse back to a semblance of life. A reanimated corpse has the same Physical Attributes as it did in life. It is capable of limited reasoning (reduce all Mental Attributes by one), but free thought is beyond it and the only person it can clearly understand is its master or an individual who its master has directed it to obey. Reanimated corpses possess two levels of Fortitude and three extra health levels. They suffer no dice pool penalties from wounds until they lose their last health level, at which point they collapse and cannot be reanimated again. A reanimated corpse crumbles to dust at the third sunrise after its creation. Its “lifespan” can be extended by feeding it more blood at creation - one blood point per extra night.
This power can also be used on a mortal. The Samedi creates a ghoul in the normal fashion, by feeding the subject one blood point. The player then rolls ^Manipulation + Medicine^ (difficulty equal to the mortal’s permanent Willpower). Three or more successes are required to turn the mortal into a zombie. If this roll succeeds, the mortal loses all free will, becoming completely subjugated to the Samedi’s command. The mortal may try to break free once per night by rolling his Willpower (difficulty equal to the Samedi’s ^Manipulation + Leadership^). If the mortal frees himself, he is still considered a ghoul but regains his free will and normal Mental and Social Attributes (see below). A mortal who botches his Willpower roll or who becomes blood-bound to the Samedi may never again attempt to break free.
A mortal under the infuence of Putrescent Servitude becomes pale and corpse-like. He loses one point from all Social and Mental Attributes (to a minimum value of one). He gains three extra health levels and takes no dice pool penalties from injuries until he reaches Incapacitated, at which point he collapses. One more lethal wound will kill him once he reaches this point. The mortal also gains one level of Potence, as a normal ghoul would, and has the potential to learn other Disciplines if the Samedi feels inclined to teach him. A ghoul zombie who goes a month without vampiric blood loses all benefits of being a ghoul, as would normally occur. He also loses all effects of this power and regains his free will, though he may still be blood-bound to his master."""
      )
    ],
    description="""
This Discipline is an exclusive development of the Samedi bloodline, and it is tied intrinsically to the Stiffs’ identity and history. Although Thanatosis appears to deal closely with death and the energies of decay, no Giovanni have ever claimed mastery of this power. Outsiders assume the Giovanni must be interested in learning this Discipline. However, the Giovanni view the Samedi with distrust and loathing, while the Samedi take on the Giovanni is usually expressed by muttering a curse on the Clan and spitting blood. Thus, the possibility of an exchange of information approaches nil.
"""
  ),
  Discipline(
    name='Dominate',
    sorcery=False,
    powers= [
      Power(
        name='Command',
        discipline='dominate',
        level=1,
        description="""The vampire locks eyes with the subject and speaks a one-word command, which the subject must obey instantly. The order must be clear and straightforward: run, agree, fall, yawn, jump, laugh, surrender, stop, scream, follow. If the command is at all confusing or ambiguous, the subject may respond slowly or perform the task poorly. The subject cannot be ordered to do something directly harmful to herself, so a command like “die” is ineffective. The command may be included in a sentence, thereby concealing the power’s use from others. This effort at subtlety still requires the Kindred to make eye contact at the proper moment and stress the key word slightly. An alert bystander - or even the victim - may notice the emphasis. Still, unless she’s conversant with supernatural powers, the individual is likely to attribute the utterance and the subsequent action to bizarre coincidence.
_System_: The player rolls ^Manipulation + Intimidation^ (difficulty equals the target’s current Willpower points). More successes force the subject to act with greater vigor or for a longer duration (continue running for a number of turns, go off on a laughing jag, scream uncontrollably). Remember, too, that being commanded to go against one’s Nature confounds the use of this power. Being told to “sleep!” in a dangerous situation or “attack!” in police custody may not have the desired effect, or indeed, any effect at all."""
      ),
      Power(
        name='Mesmerize',
        discipline='dominate',
        level=2,
        description="""With this power, a vampire can verbally implant a false thought or hypnotic suggestion in the subject’s subconscious mind. Both Kindred and target must be free from distraction, since Mesmerize requires intense concentration and precise wording to be effective. The vampire may activate the imposed thought immediately or establish a stimulus that will trigger it later. The victim must be able to understand the vampire, though the two need to maintain eye contact only as long as it takes to implant the idea. Mesmerize allows for anything from simple, precise directives (handing over an item) to complex, highly involved ones (taking notes of someone’s habits and relaying that information at an appointed time). It is not useful for planting illusions or false memories (such as seeing a rabbit or believing yourself to be on fire). A subject can have only one suggestion implanted at any time.
_System_: The player rolls ^Manipulation + Leadership^ (difficulty equal to the target’s current Willpower points). The number of successes determines how well the suggestion takes hold in the victim’s subconscious. If the vampire scores one or two successes, the subject cannot be forced to do anything that seems strange to her (she might walk outside, but is unlikely to steal a car). At three or four successes, the command is effective unless following it endangers the subject. At five successes or greater, the vampire can implant nearly any sort of command. No matter how strong the Kindred’s will, his command cannot force the subject to harm herself directly or defy her innate Nature. So, while a vampire who scored five successes could make a 98-pound weakling attack a 300-pound bouncer, he could not make the mortal shoot herself in the head. If a vampire tries to Mesmerize a subject before the target fulfills a previously implanted directive, compare the successes rolled to those gained during the implanting of the first suggestion. Whichever roll had the greater number of successes is the command that now governs in the target’s behavior; the other suggestion is wiped clean. If the successes rolled are equal, the newer command supplants the old one."""
      ),
      Power(
        name='The Forgetful Mind',
        discipline='dominate',
        level=3,
        description="""After capturing the subject’s gaze, the vampire delves into the subject’s memories, stealing or re-creating them at his whim. The Forgetful Mind does not allow for telepathic contact; the Kindred operates much like a hypnotist, asking directed questions and drawing out answers from the subject. The degree of memory alteration depends on what the vampire desires. He may alter the subject’s mind only slightly (quite effective for eliminating memories of the victim meeting or even being fed upon by the vampire) or utterly undo the victim’s memories of her past. The degree of detail used has a direct bearing on how strongly the new memories take hold, since the victim’s subconscious mind resists the alteration. A simplistic or incomplete false memory (“You went to the movies last night”) crumbles much more quickly than does one with more attention to detail (“You thought about texting your girlfriend while you were in line at the new movie theater, but you knew you’d have to turn your phone off once you got inside. You liked the movie well enough, but the plot seemed weak. You were tired after it ended, so you went home, watched a little late-night television, and went to bed”).
Even in its simplest applications, The Forgetful Mind requires tremendous skill and finesse. It’s a relatively simple matter to rife through a victim’s psyche and rip out the memories of the previous night without knowing what the subject did that evening. Doing so leaves a gap in the victim’s mind, however - a hole that can give rise to further problems down the road. The Kindred may describe new memories, but these recollections seldom have the same degree of realism that the subject’s original thoughts held. As such, this power isn’t always completely effective. The victim may remember being bitten, but believe it to be an animal attack. Greater memories may return in pieces as dreams, or through sensory triggers like a familiar odor or spoken phrase. Even so, months or years may pass before the subject regains enough of her lost memories to make sense of the fragments. A vampire can also sense when a subject’s memories were altered through use of this power, and even restore them, as a hypnotist draws forth suppressed thoughts.
_System_: The player states what sorts of alteration he wants to perform, then rolls ^Wits + Subterfuge^ (difficulty equal to the target’s current Willpower points). Any success pacifies the victim for the amount of time it takes the vampire to perform the verbal alteration, provided the vampire does not act aggressively toward her. The table below indicates the degree of modification possible to the subject’s memory. If the successes rolled don’t allow for the extent of change the character desired, the Storyteller reduces the resulting impact on the victim’s mind.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>May remove a single memory;lasts one day.</td></tr><tr><td>2 successes</td><td>May remove, but not alter, memory permanently.</td></tr><tr><td>3 successes</td><td>May make slight changes to memory.</td></tr><tr><td>4 successes</td><td>May alter or remove entire scenefrom subject’s memory.</td></tr><tr><td>5 successes</td><td>May reconstruct entire periods of subject’s life.</td></tr></table>To restore removed memories or sense false ones in a subject, the character’s Dominate rating must be equal to or higher than that of the vampire who made the alteration. In that situation, the player must make a ^Wits + Empathy^ roll (difficulty equal to the original vampire’s permanent Willpower rating) and score more successes than his predecessor did. However, the Kindred cannot use The Forgetful Mind to restore his own memories if they were stolen in such a way."""
      ),
      Power(
        name='Conditioning',
        discipline='dominate',
        level=4,
        description="""Through sustained manipulation, the vampire can make a subject more pliant to the Kindred’s will. Over time, the victim becomes increasingly susceptible to the vampire’s infuence while simultaneously growing more resistant to the corrupting efforts of other Kindred. Gaining complete control over a subject’s mind is no small task, taking weeks or even months to accomplish. Kindred often fill their retainers’ heads with subtle whispers and veiled urges, thereby ensuring these mortals’ loyalty. Yet vampires must pay a high price for the minds they ensnare. Servants Dominated in this way lose much of their passion and individuality. They follow the vampire’s orders quite literally, seldom taking initiative or showing any imagination. In the end, such retainers become like automatons or the walking dead.
_System_: The player rolls ^Charisma + Leadership^ (difficulty equal to the target’s current Willpower points) once per scene. Conditioning is an extended action, for which the Storyteller secretly determines the number of successes required. It typically requires between five and 10 times the subject’s Self-Control/Instinct rating. Targets with more empathic Natures may require a lower number of successes, while those with willful Natures require a higher total. Only through roleplaying may a character discern whether his subject is conditioned successfully.
A target may become more tractable even before becoming fully conditioned. Once the vampire accumulates half the required number of successes, the Storyteller may apply a lower difficulty to the vampire’s subsequent uses of Dominate. After being conditioned, the target falls so far under the vampire’s infuence that the Kindred need not make eye contact or even be present to retain absolute control. The subject does exactly as she is told (including taking actions that would injure herself), as long as her master can communicate with her verbally. No command roll is necessary unless the subject is totally isolated from the vampire’s presence (in a different room, over the phone). Even if a command roll fails, the target will still likely carry out part of the orders given, simply because her master wishes it.
After the subject is fully conditioned, other Kindred find her more difficult to Dominate. Such conditioning raises others’ difficulties by two (to a maximum of 10). It is possible, though difficult, to shake Conditioning. The subject must be separated entirely from the vampire to whom she was in thrall. This period of separation varies depending on the individual, but the Storyteller may set it at six months, less a number of weeks equal to the subject’s permanent Willpower rating (so a person with 5 Willpower must stay away from the vampire for just under five months). The subject regains her personality slowly during this time, though she may still lapse into brief spells of listlessness, despair, or even anger. If the vampire encounters the target before that time passes, a single successful ^Charisma + Leadership^ roll (difficulty of the target’s current Willpower points) on the part of the vampire completely reasserts the dominance. If the subject makes it through the time period without intervention by her master, the target regains her former individuality. Even so, the vampire may reestablish conditioning more easily than the first time, since the subject is now predisposed to falling under the Kindred’s mental control. New attempts require half the total number of successes than the last bout of conditioning did (which means the subject reaches the threshold for reduced difficulties sooner, as well)."""
      ),
      Power(
        name='Possession',
        discipline='dominate',
        level=5,
        description="""At this level of Dominate, the force of the Kindred’s psyche is such that it can utterly supplant the mind of a mortal subject. Speaking isn’t required, but the vampire must capture the victim’s gaze. During the psychic struggle, the contestants’ eyes are locked on one another. Once the Kindred overwhelms the subject’s mind, the vampire moves his consciousness into the victim’s body and controls it as easily as he uses his own. The mortal falls into a mental fugue while under possession. She is aware of events only in a distorted, dreamlike fashion. In turn, the vampire’s mind focuses entirely on controlling his mortal subject. His own body lies in a torpid state, defenseless against any actions made toward it. Vampires cannot possess one another in this fashion, as even the weakest Kindred’s mind is strong enough to resist such straightforward mental dominance. Only through a blood bond can one vampire control another to this degree. Supernatural creatures also cannot be possessed in this way, although ghouls that have drunk from the vampire using Possession can.
_System_: The vampire must completely strip away the target’s Willpower prior to possessing her. The player spends a Willpower point, then rolls ^Charisma + Intimidation^, while the subject rolls his Willpower in a resisted action (difficulty 7 for each). For each success the vampire obtains over the victim’s total, the target loses a point of temporary Willpower. Only if the attacker botches can the subject escape her fate, since this makes the target immune to any further Dominate attempts by that vampire for the rest of the story. Once the target loses all her temporary Willpower, her mind is open. The vampire rolls ^Manipulation + Intimidation^ (difficulty 7) to determine how fully he assumes control of the mortal shell. Similar to the Animalism power Subsume the Spirit, multiple successes allow the character to utilize some mental Disciplines, noted on the chart below. (Vampires possessing ghouls can use the physical Disciplines the ghoul possesses,but not the mental ones).
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Cannot use Disciplines</td></tr><tr><td>2 successes</td><td>Can use Auspex and other sensorypowers</td></tr><tr><td>3 successes</td><td>Can also use Presence and other powers of emotional manipulation</td></tr><tr><td>4 successes</td><td>Can also use Dementation, Dominate, and other powers of mental manipulation</td></tr><tr><td>5 successes</td><td>Can also use Chimerstry, Necromancy, Thaumaturgy, and other mystical powers</td></tr></table>The character may travel as far from his body as he is physically able while possessing the mortal. The vampire may also venture out during the day in the mortal form. However, the vampire’s own body must be awake to do so, requiring a successful roll to remain awake (see p.262). If the vampire leaves the mortal shell (by choice, if his body falls asleep, through supernatural expulsion, after sustaining significant injury, etc.), his consciousness returns to his physical form in an instant.
Once freed from possession, the mortal regains mental control of herself. This can happen in an instant, or the victim may lie comatose for days while her psyche copes with the violation.
The vampire experiences everything the mortal body feels during possession, from pleasure to pain. In fact, any damage the victim’s body sustains is also applied to the character’s body (though the Kindred may soak as normal). If the mortal dies before the vampire’s soul can flee from the body, the character’s body falls into torpor. Presumably this is in sympathetic response to the massive trauma of death, though some Kindred believe that the vampire’s soul is cast adrift during this time and must find its way back to the body.
The Kindred can remain in the mortal’s body even if his own torpid form is destroyed, though such a pathetic creature is not likely to exist for long. At each sunrise, the vampire must roll Courage (difficulty 8) or be expelled from the body. If forced from the mortal body, the vampire tumbles into the astral plane, his soul permanently lost in the spirit world. A vampire trapped in a mortal body may not be “re-Embraced”. If the Embrace occurs to such a creature, he simply meets Final Death."""
      ),
      Power(
        name='Chain the Psyche',
        discipline='dominate',
        level=6,
        description="""Not content with merely commanding their subjects, some elders apply this power to ensure obedience from recalcitrant victims. Chain the Psyche is a Dominate technique that inflicts incapacitating pain on a target who attempts to break the vampire’s commands.
_System_: The player spends a blood point when her character applies Dominate to a subject. Any attempt that the subject makes to act against the vampire’s implanted commands or to recover stolen memories causes intense pain. When such an attempt is made, the Storyteller rolls the character’s ^Manipulation + Intimidation^ (difficulty equal to the subject’s  Stamina + Empathy). Each success equals one turn that the victim is unable to act, as she is wracked with agony. Each application of Chain the Psyche crushes a number of resistance attempts equal to the character’s Manipulation rating, after which the effect fades."""
      ),
      Power(
        name='Loyalty',
        discipline='dominate',
        level=6,
        description="""With this power in effect, the elder’s Dominate is so strong that other vampires find it almost impossible to break with their own commands. Despite the name, Loyalty instills no special feelings in the victim - the vampire’s commands are simply implanted far more deeply than normal.
_System_: Any other vampire attempting to employ Dominate on a subject who has been Dominated by a vampire with Loyalty has a +3 difficulty modifier to his rolls and must spend an additional Willpower point."""
      ),
      Power(
        name='Obedience',
        discipline='dominate',
        level=6,
        description="""While most Kindred must employ Dominate through eye contact, some powerful elders may command loyalty with the lightest brush of a hand.
_System_: The character can employ all Dominate powers through touch instead of eye contact (although eye contact still works). Skin contact is necessary - simply touching the target’s clothing or something she is holding will not suffice. The touch does not have to be maintained for the full time it takes to issue a Dominate command, though repeated attempts to Dominate a single target require the character to touch the subject again."""
      ),
      Power(
        name='Mass Manipulation',
        discipline='dominate',
        level=7,
        description="""A truly skilled elder may command small crowds through the use of this power. By manipulating the strongest minds within a given group, a gathering maybe directed to the vampire’s will.
_System_: The player declares that he is using this power before rolling for the use of another Dominate power. The difficulty of the roll is that which would be required to Dominate the most resistant member of the target group - if he cannot be Dominated, no one in his immediate vicinity can. For every success past that needed to inflict the desired result on the first target, the player may choose one additional target to receive the same effect in its entirety. The vampire needs to make eye contact only with the initial target."""
      ),
      Power(
        name='Still the Mortal Flesh',
        discipline='dominate',
        level=7,
        description="""Despite its name, this power may be employed on vampires as well as mortals, and it has left more than one unfortunate victim writhing in agony - or unable to do even that. A vampire who has developed this power is able to override her victim’s body as easily as his mind in order to cut off his senses or even stop his heart. It is rumored that this power once came more easily to the Kindred, but modern medicine has made the bodies and spirits of mortals more resistant to such manipulations.
_System_: The player rolls ^Manipulation + Medicine^ (difficulty equal to the target’s current Willpower points + 2; a difficulty over 10 means that this power cannot affect the target at all). The effect lasts for one turn per success. The player must choose what function of the target’s body is being cut off before rolling. She may affect any of the body’s involuntary functions; breathing, circulation, perspiration, sight, and hearing are all viable targets. While Still the Mortal Flesh is in effect, a vampire can either stop any one of those functions entirely or cause them to fluctuate erratically. The exact effects of any given bodily function being shut off are left to the Storyteller. Most mortals panic if suddenly struck blind, but only the shutdown of the heart will kill a target on the spot. Vampires are unaffected by loss of heartbeat or breathing, but may be rendered deaf and blind as easily as mortals."""
      ),
      Power(
        name='Far Mastery',
        discipline='dominate',
        level=8,
        description="""This refinement of Obedience (though the character need not have learned Obedience first) allows the use of Dominate on any subject that the vampire is familiar with, at any time, over any distance. If the elder knows where his target is, he may issue commands as if he were standing face-to-face with his intended victim.
_System_: The player spends a Willpower point and rolls ^Perception + Empathy^ (difficulty equal to the subject’s Wits + Stealth) to establish contact. If this roll succeeds, Dominate may be used as if the character had established eye contact with the target. A second Willpower point must be spent in order for a vampire to use this power on another vampire or other supernatural being."""
      ),
      Power(
        name='Speak Through the Blood',
        discipline='dominate',
        level=9,
        description="""The power structures of Methuselahs extend across continents and centuries. This power allows such ancients to wield control over their descendants, even those far outside their geographic spheres of infuence. Speak Through the Blood allows an elder to issue commands to every vampire whose lineage can be traced to her - even if the two have never met. Thus, entire broods act to further the goals of sleeping ancients whose existences they may be completely unaware of. The vampires affected by this power rarely act directly to pursue the command they were given, but over a decade or so, their priorities slowly shift until the fulfillment of the Methuselah’s command is among their long-term goals. Speak Through the Blood, because it takes effect so slowly, is rarely recognized as an outside infuence, and its victims rationalize their behavior as “growing and changing”, or something to that effect.
_System_: The player spends a permanent Willpower point and rolls ^Manipulation + Leadership^. The difficulty of this roll is equal to four plus the number of Generations to which the command is to be passed. Unless the character is aware of the location and present agenda of every descendant of his - a highly unlikely event - he may only issue general commands, such as “work for the greater glory of Clan Malkavian” or “destroy all those who seek to extinguish the light of knowledge”. Speak Through the Blood can be used by a vampire in torpor. Commands issued through this power last for one decade per success on the roll. Difficulties over 10 require one additional success for each point past 10, making it that much more difficult to issue long-lasting commands stretching down to the ends of one’s lineage. A vampire who has reached Golconda is not affected by this power, and is completely unaware that it has been used. Her childer, however, are affected normally unless they are also enlightened. Ghouls of the victims of this power are also affected, but to a lesser extent."""
      )
    ],
    description="""
Dominate is one of the most dreaded of Disciplines. It is a vampire’s ability to influence another person’s thoughts and actions through her own force of will. Dominate requires that the vampire capture her victim’s gaze (see p. 152); as such, it may be used against only one subject at a time. Further, commands must be issued verbally, although simple orders may be made with signs - for example, a pointed finger and forceful expression to indicate “Go!” However, the subject won’t comply if he can’t understand the vampire, no matter how powerful the Kindred’s will is.

Perhaps unsurprisingly, vampires to which Dominate comes naturally tend to be from willful, domineering Clans. The Giovanni, Lasombra, Tremere, and Ventrue all consider an iron will to be a boon, and are eager to impose that iron will on any who would move against them.



_Eye Contact_
Many myths and stories exist about a vampire’s mystical ability to put people under her spell by looking deeply into her victim’s eyes. The persistence of such stories through the ages isn’t surprising, since a number of Kindred Disciplines powers (most notably Dominate) require eye contact in order to work. Other vampires, learning of this requirement, have attempted everything from wearing mirrored sunglasses to gouging out their own eyes in order to prevent an elder from exerting his will upon them.
<p.But Kindred are not so easily thwarted. The need for eye contact stems from the aggressor Kindred’s need to see his victim’s soul, and the eyes are the traditionally known as the windows to the soul. While the vampire needs to capture his target’s attention, the target’s eyes need not be present for such a power to work (although the arts of the Tzimisce make this somewhat challenging at times) - they only need to find the soul of his victim laid bare.

A target trying to avoid eye contact can make a Willpower roll against a difficulty equal to Dominate user’s Manipulation + Intimidation (or other appropriate combination for other Disciplines or specific situations, at the Storyteller’s discretion). The difficulty may be reduced for mitigating factors: -1 in the case of the target obscuring his eyes slightly (such as closing her eyes or wearing dark sunglasses) up to a -3 for the eyes being completely unseen (such as with a thick blindfold or having her eyes torn out). Ultimately, however, it is up to the Storyteller to decide whether eye contact is established in a particular case.
"""
  ),
  Discipline(
    name='Koldunic Sorcery',
    sorcery=False,
    powers= [
      Power(
        name='Koldunic Sorcery 1',
        discipline='koldunic sorcery',
        level=1,
        description="""Koldunic Sorcery 1"""
      ),
      Power(
        name='Koldunic Sorcery 2',
        discipline='koldunic sorcery',
        level=2,
        description="""Koldunic Sorcery 2"""
      ),
      Power(
        name='Koldunic Sorcery 3',
        discipline='koldunic sorcery',
        level=3,
        description="""Koldunic Sorcery 3"""
      ),
      Power(
        name='Koldunic Sorcery 4',
        discipline='koldunic sorcery',
        level=4,
        description="""Koldunic Sorcery 4"""
      ),
      Power(
        name='Koldunic Sorcery 5',
        discipline='koldunic sorcery',
        level=5,
        description="""Koldunic Sorcery 5"""
      ),
      Power(
        name='Koldunic Sorcery 6',
        discipline='koldunic sorcery',
        level=6,
        description="""Koldunic Sorcery 6"""
      ),
      Power(
        name='Koldunic Sorcery 7',
        discipline='koldunic sorcery',
        level=7,
        description="""Koldunic Sorcery 7"""
      ),
      Power(
        name='Koldunic Sorcery 8',
        discipline='koldunic sorcery',
        level=8,
        description="""Koldunic Sorcery 8"""
      ),
      Power(
        name='Koldunic Sorcery 9',
        discipline='koldunic sorcery',
        level=9,
        description="""Koldunic Sorcery 9"""
      )
    ],
    description="""
The actual casting of Koldunic sorcery requires more than a clumsy exertion of will. Such magic demands perfection of form and mastery of the appropriate lore. The caster’s player spends one blood point and rolls (Attribute) + Occult against a difficulty of the power’s level + 3, with the specific Attribute listed for each path or “way.” Vampires always use the base Attribute, ignoring any bonuses gained from blood expenditure or other Disciplines. All kolduns must select one of the ways listed below as their primary path.
"""
  ),
  Discipline(
    name='Obtenebration',
    sorcery=False,
    powers= [
      Power(
        name='Shadow Play',
        discipline='obtenebration',
        level=1,
        description="""This power grants the vampire limited control over shadows and other ambient darkness. Though the vampire cannot truly “create” darkness, she can overlap and stretch existing shadows, creating patches of gloom. This power also allows Kindred to separate shadows from their casting bodies and even shape darkness into the shadows of things that are not there. Once a Kindred takes control of darkness or shadow, it gains a mystical tangibility. By varying accounts cold or hellishly hot and cloying, the darkness may be used to aggravate or even smother victims. Certain callous Lasombra claim to have choked mortals to death with their own shadows.
_System_: This power requires no roll, but a blood point must be spent to activate it. Shadow Play lasts for one scene and requires no active concentration. Kindred cloaking themselves in shadow gain an extra die in their Stealth dice pools and add one to the difficulties of ranged weapon attacks against them. Vampires who use the darkness to make themselves more terrifying add one die to Intimidation dice pools. Opponents plagued by flapping shadows and strangling darkness subtract one die from all Stamina dice pools (including soak). Mortals, ghouls, and other air-breathers reduced to zero Stamina by strangling shadows begin to asphyxiate; vampires lose all appropriate dice but are otherwise unaffected. Only one target or subject maybe affected by this power at any given time, though some modicum of concealment is offered to a relatively motionless group. The unnatural appearance of this power proves extremely disconcerting to mortals and animals (and, at the Storyteller’s discretion, Kindred who have never seen it before). Whenever this power is invoked withina mortal’s vicinity, that individual must make a Courage roll (difficulty 8) or suffer a one die penalty to all dice pools for the remainder of the scene, due to fear of the monstrous shadows."""
      ),
      Power(
        name='Shroud of Night',
        discipline='obtenebration',
        level=2,
        description="""The vampire can create a cloud of inky blackness. The cloud completely obscures light and even sound to some extent. Those who have been trapped within it (and survived) describe the cloud as viscous and unnerving. This physical manifestation lends credence to those Lasombra who claim that their darkness is something other than mere shadow. The tenebrous cloud may even move, if the creating Kindred wishes, though this requires complete concentration.
_System_: The player rolls ^Manipulation + Occult^ (difficulty 7). Success on the roll generates darkness roughly 10 feet (three meters) in diameter, though the amorphous cloud constantly shifts and undulates, sometimes even extending shadowy tendrils. Each additional success doubles the diameter of the cloud (though the vampire may voluntarily reduce the area she wishes to cover). The cloud may be invoked at a distance of up to 50 yards/meters, though creating darkness outside the vampire’s line of sight adds two to the difficulty of the roll and requires a blood point’s expenditure. The tarry mass actually extinguishes light sources it engulfs (with the exception of fire), and muffles sounds until they are indistinguishable. Those within the cloud lose all sense of sight and feel as though they’ve been immersed in pitch. Sound also warps and distorts within the cloud, making it nearly impossible to accomplish anything (+2 difficulty, as per Blind Fighting on p.274). Even those possessed of Heightened Senses, Eyes of the Beast, Tongue of the Asp, and similar powers suffer the penalty for blindness due to the unnatural darkness. Additionally, being surrounded by the Shroud of Night reduces Stamina-based dice pools by two dice, as the murk smothers and agitates the victims. This effect is not cumulative with Shadow Play, although targets asphyxiate as per Shadow Play if they reach 0 Stamina; more than one unfortunate mortal has “drowned” in darkness. Mortals and animals surrounded by the Shroud of Night must make Courage rolls per Shadow Play, above, or panic and flee."""
      ),
      Power(
        name='Arms of the Abyss',
        discipline='obtenebration',
        level=3,
        description="""Refining his control over darkness, the Kindred can create prehensile tentacles that emerge from patches of dim lighting. These tentacles may grasp, restrain, and constrict foes.
_System_: The player spends a blood point and makes a simple (never extended) ^Manipulation + Occult^ roll (difficulty 7); each success enables the creation of a single tentacle. Each tentacle is six feet (two meters) long and possesses Strength and Dexterity ratings equal to the invoking vampire’s Obtenebration Trait - Potence and Celerity dots are added to these Strength and Dexterity ratings, respectively. If the vampire chooses, she may spend a blood point either to increase a single tentacle’s Strength or Dexterity by one or to extend its length by another six feet or two meters. Each tentacle has four health levels, is affected by fire and sunlight as if it were a vampire, and soaks bashing and lethal damage using the vampire’s ^Stamina + Fortitude^. Aggravated damage may not be soaked. Tentacles may constrict foes, inflicting (Strength +1) lethal damage per turn. Breaking the grasp of a tentacle requires the victim to win a resisted Strength roll against the tentacle (difficulty 6 for each). However, tentacles cannot be used for any kind of manipulation, such as typing or driving. All tentacles need not emanate from the same source - so long as there are multiple patches of suitable darkness, there are sources for the Arms of the Abyss. Controlling the tentacles does not require complete concentration; if the Kindred is not incapacitated or in torpor, she may control tentacles while carrying out other actions."""
      ),
      Power(
        name='Black Metamorphosis',
        discipline='obtenebration',
        level=4,
        description="""The Cainite calls upon his inner darkness and infuses himself with it, becoming a monstrous hybrid of matter and shadow. His body becomes mottled with spots of tenebrous shade, and wispy tentacles extrude from his torso and abdomen. Though still humanoid, the vampire takes on an almost demonic appearance, as the darkness within him bubbles to the surface.
_System_: The player spends two blood points and makes a ^Manipulation + Courage^ roll (difficulty 7) - vampires of lower Generation may have to take two turns to make the transition. Failure indicates the vampire cannot undergo the Black Metamorphosis (though he spends the blood points nonetheless). A botch inflicts two unsoakable health levels of lethal damage on the vampire as darkness ravages his undead body.
While under the effects of the Black Metamorphosis, the vampire possesses four tentacles similar to those evoked via Arms of the Abyss (though their Strength and Dexterity ratings are equal to the vampire’s own Attributes, including dice from Celerity and Potence). These tentacles, combined with the bands of darkness all over the Kindred’s body, subtract two dice from the Stamina and soak dice pools of opponents physically touched in combat, for as long as the vampire remains in contact with the victim. This is not cumulative with other powers in Obtenebration, although targets can asphyxiate at Stamina 0, as per Shadow Play. The vampire may make an additional attack without penalty by using the tentacles (for a total of two attacks, not one additional attack per tentacle). Additionally, the vampire can sense his surroundings fully even in pitch darkness. The vampire’s head and extremities sometimes appear to fade away into nothingness, while at other times they seem swathed in otherworldly darkness. This, combined with the wriggling tentacles writhing from his body, creates an unsettling sight. Mortals, animals, and other creatures not accustomed to this sort of display must make Courage rolls (difficulty 8) or succumb to a panic that amounts to Rötschreck (though it is inspired by the darkness rather than fire). Many Kindred cultivate this devilish aspect, and the Black Metamorphosis adds three dice to the invoking Kindred’s Intimidation dice pools."""
      ),
      Power(
        name='Tenebrous Form',
        discipline='obtenebration',
        level=5,
        description="""At this level, the Kindred’s mastery of darkness is so extensive that she may physically become it. Upon activation of this power, the vampire becomes an inky, amoeboid patch of shadow. Vampires in this form are practically invulnerable and may slither through cracks and crevices. In addition, the shadow-vampire gains the ability to see in natural darkness.
_System_: The transformation costs three blood points (which may need to occur over three turns, depending on the vampire’s Generation). The vampire is immune to physical attacks while in the tenebrous form (though she still takes aggravated damage from fire and sunlight), but may not herself physically attack. She may, however, envelop and ooze over others, affecting them in the same manner as a Shroud of Night, in addition to using mental Disciplines. Vampires in Tenebrous Form may even slither up walls and across ceilings or “drip” darkness upward - they have no mass and are thus unaffected by gravity. Rötschreck difficulties from fire and sunlight do increase by one for vampires in this form, as the light is even more painful to their shadowy bodies.
Mortals (and others not used to such displays) who witness the vampire transform into unholy shadow require Courage rolls (difficulty 8) in order to avoid the debilitating terror described under Black Metamorphosis."""
      ),
      Power(
        name='The Darkness Within',
        discipline='obtenebration',
        level=6,
        description="""This power allows the Cainite to call forth the darkness contained in her black soul. This enormous, turbulent shadow vomits from the vampire’s mouth, though some vampires are said to cut themselves and let the blackness seep from their veins. The shadow-cloud engulfs a chosen target, burning it with a soul-scarring chill and siphoning its blood away in torrents.
_System_: The player makes a ^Willpower^ roll (difficulty 6) and spends a blood point. The resulting shadow envelops the target and, though it does not physically harm the victim, it may strike terror into him. Individuals observing the Darkness Within, whether as targets or onlookers, may suffer from the terror described under Black Metamorphosis, unless they are already familiar with the Kindred’s power.
Individuals touched by The Darkness Within lose one point of blood per turn, though targets may resist this effect by succeeding on a Stamina roll (difficulty 6) each turn the target remains in contact with the cloud.
The Cainite invoking The Darkness Within must devote all her attention to maintaining the cloud. If the vampire is attacked, the darkness immediately returns to her through whatever orifice it originated. The Cainite can summon the darkness back at any time, gaining a number of blood points equal to one-half the number the shadow siphoned from its victims (round up). Taking blood from another in this fashion is similar to drinking from that vampire, and blood bonds may result. Additionally, the Darkness Within may take blood from only one individual per turn, though it may be in contact with many."""
      ),
      Power(
        name='Shadowstep',
        discipline='obtenebration',
        level=6,
        description="""The vampire has such fine control over the darkness that he may become it briefy and reform himself from other darkness close by. The vampire may Shadowstep through walls, floors, and even mystical barriers. The Cainite simply steps “into” a shadow and re-emerges from another shadow a short distance away (or next to the barrier, if there is no shadow on the other side).
_System_: The player rolls ^Dexterity + Occult^, and on a successful roll, the character may emerge from another shadow no more than 50 feet (or 15 meters) away. Failing the roll means simply that the character cannot step through the shadow-realm, while a botch signifies the character has become trapped between shadows (which fiendish Storytellers should have a heyday with). Pulling another individual through the shadow requires a ^Strength + Occult^ roll, with consequences for failure similar to failing by oneself."""
      ),
      Power(
        name='Shadow Twin',
        discipline='obtenebration',
        level=7,
        description="""The vampire’s control over darkness has progressed to such a degree that he may bestow upon it a limited degree of sentience. By animating his own shadow or that of another, the Cainite can actually “free” the shadow cast by light. While this power is active, the subject casts no shadow, as it has left to pursue the vampire’s commands.
This power can unnerve mortals and even a few inexperienced vampires. The Kindred wielding Obtenebration commands the individual’s shadow; some vampires report having seen mortals literally scared to death, as their shadows leapt away to taunt or menace them.
_System_: The player spends a blood point and makes a ^Willpower^ roll (difficulty 8). If the roll succeeds, the shadow springs to unholy freedom for one hour per success (though it disappears at sunrise regardless of how many successes the vampire had). The Shadow Twin has Attribute and Ability ratings equal to half those of its parent body; they won’t do much talking or thinking, so Mental and Social Traits don’t matter much, though Wits may come into play. Additionally, the Shadow Twin has an Obtenebration score equal to one half of that of the vampire who animated it (rounded down). Mortals and vampires unused to Obtenebration require a Courage roll upon witnessing this, as per Shadow Play. The twin may separate itself from the parent and travel up to 50 feet or 15 meters away, crawling through crevices or sliding up walls. It may attack and be attacked, though it takes and does only half damage (again, round down). Flame and supernatural attacks (such as vampire fangs, mystical powers, etc.) do full damage. If the Shadow Twin is killed, its parent loses half her Willpower points and must roll to avoid Rötschreck (difficulty 9)."""
      ),
      Power(
        name='Oubliette',
        discipline='obtenebration',
        level=8,
        description="""By creating a “chamber” of pure darkness, the Cainite may entrap or smother her enemies. No air exists in this shadow-trap, and mortals suffocate within its chilling void. Even vampires have little recourse once trapped - they may leave only at their captor’s whim. The Oubliette appears as a dense patch of shadow, unaffected by ambient light around it.
_System_: The vampire spends a blood point, but no roll is necessary to create the Oubliette. To actually create the Oubliette around someone requires a contested ^Wits + Larceny^ roll against the target’s Dexterity + Occult (difficulty 7 for both rolls). Mortals suffocate within a number of minutes equal to their Stamina (though the Lasombra may choose to leave their heads exposed or trap a quantity of air inside as well), while vampires are simply suspended impotently in darkness and may not use Disciplines or take other actions. The Oubliette vanishes instantly when touched by sunlight - which has left more than one vampire exposed to the sun’s unforgiving rays - or when the Kindred chooses to relax it. A vampire may maintain only one Oubliette at a time (which can only contain one target at a time), which leads some Cainite philosophers to argue that it is a prison created from the vampire’s very soul."""
      ),
      Power(
        name='Ahriman’s Demesne',
        discipline='obtenebration',
        level=9,
        description="""This power allows the vampire to summon a darkness so oppressive that it extinguishes the light of life - or unlife - of any victim trapped within it. Ahriman’s Demesne creates a 50-foot (or 15-meter) radius of void that issues from the Cainite’s hand and takes away the bodies of those it claims when it vanishes. The overwhelming darkness destroys friend and foe alike, claiming anyone unfortunate enough to be within its circumference.
_System_: The player spends two points of Willpower and concentrates for three turns. During this time, the blackness billows out of the character’s hand, growing to fill the area. At the end of the third turn, the player rolls ^Manipulation + Occult^ (difficulty 6). Everyone in the darkness’ area suffers that many health levels of damage (aggravated, if the victims are vampires) outright - six successes yield six levels of damage, not six dice of damage. After Ahriman’s Demesne does its damage, it collapses, taking with it the bodies of any who died when they came in contact with the dreadful shadow."""
      )
    ],
    description="""
The signature power of the Lasombra, Obtenebration grants the vampire power over darkness itself. The nature of the darkness invoked by Obtenebration is a matter of intense debate among Kindred. Some believe it to be merely shadows, while others feel that the power gives control over the stuff of the vampire’s soul, coaxing it tangibly outward.

Regardless, the effects of Obtenebration are terrifying, as waves of darkness roil out from the Cainite, enveloping those in their path like an infernal wave. As Obtenebration is mostly known as a Sabbat Discipline, any Camarilla vampire caught using the power had better have a damned good explanation.

_Note:_ Vampires using Obtenebration can see through the darkness they control, though other vampires (even those that also have Obtenebration) cannot. Dreadful tales of rival Lasombra struggling to blind and smother each other with the same wisps of darkness circulate among young members of the Clan, though no elders have come forth to substantiate these claims.
"""
  ),
  Discipline(
    name='Obfuscate',
    sorcery=False,
    powers= [
      Power(
        name='Cloak of Shadows',
        discipline='obfuscate',
        level=1,
        description="""At this level, the vampire must rely on nearby shadows and cover to assist in hiding his presence. He steps into an out-of-the-way, shadowed place and eases himself from normal sight. The vampire remains unnoticed as long as he stays silent, still, under some degree of cover (such as a curtain, bush, door frame, lamppost, or alley), and out of direct lighting. The immortal’s concealment vanishes if he moves, attacks, or falls under direct light. Furthermore, the vampire’s deception cannot stand up to concentrated observation without fading.
_System_: No roll is required as long as the character fulfills the criteria described above. So long as he remains quiet and motionless, virtually no one but another Kindred with a high enough Auspex rating will see him."""
      ),
      Power(
        name='Unseen Presence',
        discipline='obfuscate',
        level=2,
        description="""With experience, the vampire can move around without being seen. Shadows seem to shift to cover him, and people automatically avert their gazes as he passes by. Others move unconsciously to avoid contact with the cloaked creature; those with weak wills may even scurry away from the area in unacknowledged fear. The vampire remains ignored indefinitely unless someone deliberately seeks him out or he inadvertently reveals himself. Since the vampire fully retains his physical substance, he must be careful to avoid contact with anything that may disclose his presence (knocking over a vase, bumping into someone). Even a whispered word or the scuffing of a shoe against the floor can be enough to disrupt the power.
_System_: No roll is necessary to use this power unless the character speaks, attacks, or otherwise draws attention to himself. The Storyteller should call for a ^Wits + Stealth^ roll under any circumstances that might cause the character to reveal himself. The difficulty of the roll depends on the situation; stepping on a squeaky foorboard might be a 5, while walking through a pool of water may require a 9. Other acts may require a certain number of successes; speaking quietly without giving away one’s position, for instance, demands at least three successes. Upon success, the vampire, all her clothing, and objects that could fit into a pocket are concealed. Some things are beyond the power of Unseen Presence to conceal. Although the character is cloaked from view while he smashes through a window, yells out, or throws someone across the room, the vampire becomes visible to all in the aftermath. Bystanders snapout of the subtle fugue in which Obfuscate put them. Worse still, each viewer can make a Wits + Awareness roll (difficulty 7); if successful, the mental haze clears completely, so those individuals recall every move the character made up until then as if he had been visible the entire time."""
      ),
      Power(
        name='Mask of a Thousand Faces',
        discipline='obfuscate',
        level=3,
        description="""The vampire can infuence the perception of others, causing them to see a face different from his. Although the Kindred’s physical form does not change, any observer who cannot sense the truth sees whomever the vampire wishes her to see. The vampire must have a firm idea of the visage he wishes to project. The primary decision is whether to create an imaginary face or to superimpose the features of another person. Manufactured features are often more difficult to compose in believable proportions, but such a disguise is easier to maintain than having to impersonate someone else. Of course, things get simpler if the Kindred borrows the face but doesn’t bother with the personality.
_System_: The player rolls ^Manipulation + Performance^ (difficulty 7) to determine how well the disguise works. If the character tries to impersonate someone, he must get a good look at the subject before putting on the mask. The Storyteller may raise the difficulty if the character catches only a glimpse. The chart below lists the degrees of success in manufacturing another appearance. Vampires wishing to mask themselves as a person more attractive than they are must pay additional blood points equal to the difference between the vampire’s Appearance rating and the Appearance of the mask (which means that younger vampires may need to take longer in order to spend the blood necessary).
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>The vampire retains the same height and build, with a few slight alterations to his basic features. Nosferatu can appear as normal, albeit ugly, mortals.</td></tr><tr><td>2 successes</td><td>He looks unlike himself; people don’t easily recognize him or agree about his appearance.</td></tr><tr><td>3 successes</td><td>He looks the way he wants to appear.</td></tr><tr><td>4 successes</td><td>Complete transformation, including gestures, mannerisms, appearance,and voice.</td></tr><tr><td>5 successes</td><td>Profound alteration (appear as the opposite sex, a vastly different age, or an extreme change of size). Actually posing as someone else carries its own problems. The character should know at least basic information about the individual; especially difficult deceptions (fooling a lover or close friend) require at least some familiarity with the target in order to succeed.</td></tr></table>"""
      ),
      Power(
        name='Vanish from the Mind’s Eye',
        discipline='obfuscate',
        level=4,
        description="""This potent expression of Obfuscate enables the vampire to disappear from plain view. So profound is this vanishing that the immortal can fade away even if he stands directly in front of someone. While the disappearance itself is quietly subtle, its impact on those who see it is anything but. Most kine panic and flee in the aftermath. Especially weak-willed individuals wipe the memory of the Kindred from their minds. Although vampires are not shaken so easily, even Kindred may be momentarily surprised by a sudden vanishing.
_System_: The player rolls ^Charisma + Stealth^; the difficulty equals the target’s Wits + Alertness (use the highest total in the group if the character disappears in front of a crowd). With three or fewer successes, the character fades but does not vanish, becoming an indistinct, ghostlike figure. With more than three, he disappears completely. If the player scores more successes than an observer’s Willpower rating, that person forgets that the vampire was there in the first place. Tracking the character accurately while he appears ghostlike requires a Perception + Alertness roll (difficulty 8). A successful roll means the individual can interact normally with the vampire (although the Kindred looks like a profoundly disturbing ghostly shape). A failed roll results in a +2 difficulty modifier (maximum 10) when attempting to act upon, or interact with, the vampire. The Storyteller may call for new observation checks if the vampire moves to an environment in which he’s difficult to see (heads into shadows, crosses behind an obstacle, proceeds through a crowd). When fully invisible, the vampire is handled as described under Unseen Presence, above. A person subject to the vanishing makes a Wits + Courage roll (mortals at difficulty 9, vampires at difficulty 5). A successful roll means the individual reacts immediately (although after the vampire performs his action for that turn); failure means the person stands uncomprehending for two turns while her mind tries to make sense of what she just experienced."""
      ),
      Power(
        name='Cloak the Gathering',
        discipline='obfuscate',
        level=5,
        description="""At this degree of power, the vampire may extend his concealing abilities to cover an area. The immortal may use any Obfuscate power upon those nearby as well as upon himself, if he wishes. Any protected person who compromises the cloak exposes himself to view. Further, if the one who invokes the power gives himself away, the cloak falls from everyone. This power is particularly useful if the vampire needs to bring his retinue through a secure location without drawing the notice of others.
_System_: The character may conceal one extra individual for each dot of Stealth he possesses. He may bestow any single Obfuscate power at a given time to the group. While the power applies to everyone under the character’s cloak, his player need only make a single roll. Each individual must follow the requirements described under the relevant Obfuscate power to remain under its effect; any person who fails to do so loses the cloak’s protection, but doesn’t expose the others. Only if the vampire himself errs does the power drop for everyone."""
      ),
      Power(
        name='Conceal',
        discipline='obfuscate',
        level=6,
        description="""The vampire may mask an inanimate object up to the size of a house (Obfuscate cannot be used to disguise inanimate objects without the use of this power). If the object is hidden, so are all of its contents. While Conceal is in effect, passersby walk around the concealed object as if it were still visible, but refuse to acknowledge that they are making any kind of detour.
_System_: In order to activate this power, a character must be within about 30 feet (approximately 10 meters) of the object to be concealed and the item must hold some personal significance for him. The Conceal power functions as Unseen Presence for purposes of detection, as well as the duration and durability of the disguise. Conceal can be used on a vehicle in which the character is traveling. In this instance, traffic patterns seem to flow around the vehicle, and accidents are actually less likely as other drivers subconsciously maneuver away from the concealed auto. A police radar gun still registers a speeding car masked in this fashion, but the officer behind the gun is disinclined to make a traffic stop of the phantom blip. Using Conceal on aircraft is problematic, as the power’s range generally doesn’t extend far enough to cover air traffic controllers and the like."""
      ),
      Power(
        name='Mind Blank',
        discipline='obfuscate',
        level=6,
        description="""A vampire with this power is able to shrug off telepathic contact, easily withstanding invasive probes of her mind.
_System_: Any attempt to read or probe the character’s mind first requires a successful ^Perception + Empathy^ roll (difficulty equal to the character’s Wits + Stealth).
Even if a potential intruder does succeed, his dice pool for the attempt is then limited to the number of successes he scored on the initial roll."""
      ),
      Power(
        name='Soul Mask',
        discipline='obfuscate',
        level=6,
        description="""In addition to concealing her form, a vampire who has developed Soul Mask is able to conceal her aura. She may display whatever combination of colors and shades she wishes, or may appear to have no aura whatsoever. This power is of particular use to those of elder Generation who have reached such heights of power through diablerie.
_System_: The use of this power allows the projection of only one aura (or lack thereof) - the vampire chooses the precise colors to be displayed when she first develops Soul Mask. If the character has no experience with the use of Aura Perception, she may not choose an alternate aura, as she has no idea what one would look like, though she can still choose to display no aura whatsoever. Soul Mask can be bought multiple times, if desired, in order to give a vampire multiple alternate auras from which to choose. Unless the player states otherwise, Soul Mask is always in effect. If the character has bought Soul Mask two or more times, her “default” aura displayed is the first one she learned."""
      ),
      Power(
        name='Cache',
        discipline='obfuscate',
        level=7,
        description="""Most Obfuscate powers require the individual using them to be within a short distance of the subjects of the concealment. Cache extends this range considerably, allowing an elder with this power to leave people or objects safely hidden while he goes about his business elsewhere.
_System_: A character must be within the normal required distance to initiate an Obfuscate power. Once this is done, the player spends a Willpower point, which activates Cache on top of the already functioning use of the Discipline. The concealment will now remain in effect as long as the vampire is within a distance equal to his ^Wits + Stealth^ in miles (or one and half times that in kilometers) from the object or person he wishes to conceal. The enhanced concealment fades at the next sunrise, or breaks (as always) if the Obfuscate subject reveals himself."""
      ),
      Power(
        name='Veil of Blissful Ignorance',
        discipline='obfuscate',
        level=7,
        description="""This power’s development is attributed to the Malkavians, but many Nosferatu have also found it to be highly useful. The Veil of Blissful Ignorance allows a vampire to Obfuscate an unwilling victim, removing him from the notice of others. Some Nosferatu use this power to teach a humbling lesson to individuals who take the presence and aid of others for granted, while others utilize it to remove an essential member of a group in the midst of a crisis.
_System_: The character must touch the victim to activate this power. The player spends a blood point and rolls ^Wits + Stealth^ (difficulty equals the victim’s Appearance + 3). If the roll is a success, the victim is subject to the effects of Vanish From the Mind’s Eye for a length of time determined by the number of successes the player rolls.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Three turns</td></tr><tr><td>2 successes</td><td>One minute (20 turns)</td></tr><tr><td>3 successes</td><td>15 minutes</td></tr><tr><td>4 successes</td><td>One hour</td></tr><tr><td>5 successes</td><td>One night</td></tr></table>The victim of Veil of Blissful Ignorance does not necessarily know that he is under the effect of this power. He is only aware that everyone around him has suddenly begun acting as if he were not there. The victim cannot break this effect, even with violence; if he attacks someone, the target ascribes the act to the visible individual nearest to him. More than one fatal brawl has been incited by this side-effect. The Veil persists even if the vampire who activated it leaves the area. Curiously enough, Veil of Blissful Ignorance can never be used on anyone who is ready and willing to accept its effects."""
      ),
      Power(
        name='Old Friend',
        discipline='obfuscate',
        level=8,
        description="""Many elder Nosferatu have made reputations for omniscience with the secrets they learn through creative uses of this power. A variation of Mask of a Thousand Faces, Old Friend allows a vampire to probe a subject’s subconscious and take the semblance of the individual whom that victim trusts over anyone else. Someone using this power does not appear as someone who the victim is frightened of or awed by, but rather someone to whom the victim feels comfortable revealing intimate secrets. Old Friend doesn’t necessarily make its user appear as someone who is still among the living; a long-dead friend or relative is just as likely, and in such cases the subject remembers the encounter as a dream or a ghostly visitation.
_System_: The player rolls ^Manipulation + Subterfuge^ (difficulty equal to the victim’s Perception + Alertness or Awareness, maximum 10). The more successes, the more convincing the impersonation. This power only affects one victim at a time; other observers see the vampire as she truly is, unless she also establishes a Mask of a Thousand Faces in addition to using Old Friend."""
      ),
      Power(
        name='Create Name',
        discipline='obfuscate',
        level=9,
        description="""Some Toreador call this power the ultimate development of method acting. Create Name allows a character to create a completely new identity; face, speech pattern, aura, even thought processes are constructed according to the vampire’s desired identity. The power can be used to impersonate an existing individual, or it can project the semblance of a completely fictional identity with perfect accuracy.
_System_: A vampire working with Create Name must spend three hours a night in relatively uninterrupted quiet to establish a new personality by means of this power. The player makes an extended roll of ^Intelligence + Subterfuge^ (difficulty 8), one roll per night. A total of 20 successes are necessary to construct a new identity, while a botch removes five successes from the vampire’s total. Once a new identity has been successfully created, however, the character can step into it at any time without any sort of roll. Any outside observer without Auspex 9 or the equivalent sees the artificial identity. The character’s face, aura, Nature, Demeanor, even thoughts and Psychological Merits and Flaws all appear to be those of the persona selected and crafted by the character. The only way to pierce this disguise, other than Auspex 9, is to notice any discrepancies between the assumed identity and the Abilities it logically ought to possess. A character with no dots in Medicine should have a hard time pulling off a created identity as a neurosurgeon, for example. The Storyteller should make a secret roll of Perception + Alertness (difficulty 9) for each character who should catch a slip made by the impostor."""
      )
    ],
    description="""
Obfuscate is the uncanny ability for Kindred to conceal themselves from sight, sometimes even in full view of a crowd. An Obfuscated vampire doesn’t actually become invisible, however - rather, he is able to delude observers into believing that he has vanished. Obfuscate also allows Kindred to change their features and conceal other people or objects. Typically vampires using Obfuscate must be within a short range of their witnesses (approximately five yards or meters per dot of Wits + Stealth) for their power to be effective.

Unless the Kindred chooses to make herself seen, she can remain obscured for as long as she wills it. At higher levels, the vampire can actually fade from sight so subtly that those nearby can’t actually recall the moment at which she left.

Usually, few mortals or supernaturals (even those trained in Awareness) can pierce through the fog of Obfuscate. Animals, who rely more on their instincts than their normal senses, can sometime perceive (and be frightened by) the vampire’s presence. Children and those to whom deception is foreign may also be able to pierce the illusion, at the Storyteller’s discretion. Finally, the Auspex Discipline enables Kindred to see through Obfuscate. Even that is not guaranteed, however; refer to “Seeing the Unseen,” p. 142, for more details. (Storytellers needing a die roll for animals or children can use this quick and dirty guideline: treat them as if they had Auspex 1 in terms of contesting Obfuscate. They do not have the Auspex 1 power, but are considered to have it when determining whether a vampire is noticed.)

Since Obfuscate clouds the mind of the viewer, vampires can’t use it to hide their presence from electronic or mechanical devices. Video and photo cameras, for example, capture the vampire’s image accurately. Even so, the person using, say, her cell phone to record an Obfuscated vampire will still have her mind impacted by the power, and she won’t see the Kindred’s image until she views the video at a later date (if even then).

Several Clans cultivate this power - the Assamites, Followers of Set, and Malkavians, for example - but the Nosferatu are particularly known for this Discipline. Some elder Kindred believe that Caine, or perhaps Lilith, bestowed the Clan with this Discipline to compensate for the hideous physical deformities its members suffer.

Most Obfuscate powers last for a scene, or until the vampire ceases maintaining them. Once evoked, they require very little mental effort to keep in place.
"""
  ),
  Discipline(
    name='Protean',
    sorcery=False,
    powers= [
      Power(
        name='Eyes of the Beast',
        discipline='protean',
        level=1,
        description="""The vampire sees perfectly well in pitch darkness, not requiring a light source to notice details in even the darkest basement or cave. The vampire’s Beast is evident in his red glowing eyes, a sight sure to disturb most mortals.
_System_: The character must declare his desire to call forth the Eyes. No roll is necessary, but the change requires a full turn to complete. While manifesting the Eyes, the character suffers a +1 difficulty to all Social rolls with mortals unless he takes steps to shield his eyes (sunglasses are the simplest solution). (A vampire without this power who is immersed in total darkness suffers blind-fighting penalties as per p.274)."""
      ),
      Power(
        name='Feral Claws',
        discipline='protean',
        level=2,
        description="""The vampire’s nails transform into long, bestial claws. These talons are wickedly sharp, able to rend flesh with ease and even carve stone and metal with little trouble. The Beast is prominent in the claws as well, making them fearsome weapons against other immortals. It’s rumored that some Gangrel have modified this power to change their vampiric fangs into vicious tusks.
_System_: The claws grow automatically in response to the character’s desire, and can grow from both hands and feet. The transformation requires the expenditure of a blood point, takes a single turn to complete, and lasts for a scene. The character attacks normally in combat, but the claws inflict Strength + 1 aggravated damage. Other supernaturals cannot normally soak this damage, although a power such as Fortitude may be used. Additionally, the difficulties of all climbing rolls are reduced by two."""
      ),
      Power(
        name='Earth Meld',
        discipline='protean',
        level=3,
        description="""One of the most prized powers within Protean, Earth Meld enables the vampire to become one with the earth. The immortal literally sinks into the bare ground, transmuting his substance to bond with the earth. Though a vampire can immerse himself fully into the ground, he cannot move around within it. Further, it is impossible to meld into earth through another substance. Wood slats, blacktop, even artificial turf blocks Earth Meld’s effectiveness - then again, it’s a relatively simple matter for a vampire at this level of power to grow claws and rip apart enough of the fooring to expose the raw soil beneath. By interring himself in the ground, the vampire gains full protection from daylight when outdoors. It is also the method of choice for those Kindred who wish to sleep away the centuries; these vampires lock themselves in the earth’s embrace, gaining strength and power as they rest. Superstitious and paranoid Kindred whisper that thousands of Ancients sleep within theground and will awaken when Gehenna arrives. While so interred, the vampire is in a transitional state between flesh and earth. His physical presence exists between the physical world and the astral plane. As such, the vampire is difficult to sense, even through supernatural means. However, a disruption to the soil that the immortal occupies, or to his presence on the astral realm, returns him immediately to the physical world (and to full wakefulness), showering dirt outward as his body displaces the soil.
_System_: No roll is necessary, although the character must spend a blood point. Sinking into the earth is automatic and takes a turn to complete. The character falls into a state one step above torpor during this time, sensing his surroundings only distantly. The player must make a ^Humanity or Path^ roll (difficulty 6) for the character to rouse himself in response to danger prior to his desired time of emergence. Since the character is in an inbetween state, any attempts to locate him (catching his scent, scanning for his aura, traveling astrally, and so on) are made at +2 difficulty. Astral individuals cannot affect the vampire directly, instead meeting with a kind of spongy resistance as their hands pass through him. Similarly, digging in the material world encounters incredibly hard-packed earth, virtually as dense as stone. Attempts at violence upon the submerged vampire from either side return him to his physical nature, expelling the soil with which he bonded in a blinding spray (all Perception-based rolls are at +2 difficulty for the turn). The character himself subtracts two from his initiative for the first turn after his restoration, due to momentary disorientation. Once expelled from the earth, the vampire may act normally."""
      ),
      Power(
        name='Shape of the Beast',
        discipline='protean',
        level=4,
        description="""This endows the vampire with the legendary ability to transform into a wolf or bat. A Kindred changed in this way is a particularly imposing representative of the animal kingdom. Indeed, he is far superior to normal animals, even ones possessed by Subsume the Spirit. He retains his own psyche and temperament, but can still call upon the abilities of the beast form - increased senses for the wolf and flight for the bat. Gangrel are reputed to change to other animal forms better suited to their environment - jackals in Africa, dholes in Asia, and even enormous rats in urban environments - a feat that other Clans learning Protean cannot seem to duplicate.
_System_: The character spends one blood point to assume the desired shape. The transformation requires three turns to complete (spending additional blood points reduces the time of transformation by one turn per point spent, to a minimum of one). The vampire remains in his beast form until the next dawn, unless he wishes to change back sooner. While in the animal’s shape, the vampire can use any Discipline he possesses except Necromancy, Serpentis, Thaumaturgy, or Vicissitude (as well as any others the Storyteller deems unavailable). Furthermore, each form gives the character the abilities of that creature. In wolf form, the vampire’s teeth and claws inflict Strength + 1 aggravated damage, he can run at double speed, and the difficulties of all Perception rolls are reduced by two. In bat form, the vampire’s Strength is reduced to 1, but he can fy at speeds of up to 20 miles per hour, difficulties for all hearing-based Perception rolls are reduced by three, and attacks made against him are at +2 difficulty due to his small size. The Storyteller may allow Gangrel to assume a different animal shape, but should establish the natural abilities it grants the character."""
      ),
      Power(
        name='Mist Form',
        discipline='protean',
        level=5,
        description="""This truly unsettling power enables the vampire to turn into mist. His physical shape disperses into a hazy cloud, but one still subject entirely to the immortal’s will. He foats at a brisk pace and may slip under doors, through screens, down pipes, and through other tiny openings. Although strong winds can blow the vampire from his chosen course, even hurricane-force winds cannot disperse his mist shape. Some Kindred feel that this power is an expression of the vampire’s ultimate control over the material world, while others believe that it is the immortal’s soul made manifest (damned though it may be).
_System_: No roll is required, although a blood point must be spent. The transformation takes three turns to complete, although the character may reduce this time by one turn for each additional blood point spent (to a minimum of one turn). Strong winds may buffet the character, although Disciplines such as Potence may be used to resist them. Vampires in Mist Form can perceive their surroundings normally, although they cannot use powers that require eye contact. The vampire is immune to all mundane physical attacks while in mist form, although supernatural attacks affect him normally. Also, the vampire takes one fewer die of damage from fire and sunlight. The character may not attack others physically while in this state - this includes encountering another vampire in mist form. He may use Disciplines that do not require physical substance, however."""
      ),
      Power(
        name='Earth Control',
        discipline='protean',
        level=6,
        description="""An Earth Melded character with this power is no longer confined to the resting place she selected the night before. She can pass through the ground as if it were water, “swimming” through the earth itself. Some elders use this as a means of unobstructed and unobtrusive travel, while others find it a highly effective means of maneuvering in combat.
_System_: This power is in effect whenever a character is Earth Melded, with no additional roll or expenditure necessary. While in the ground, a vampire can propel herself at half of her normal walking speed. She cannot see, but gains a supernatural awareness of her underground surroundings out to a range of 50 yards or meters. Water, rock, tree roots, and cement all effectively block her progress; she can only move through earth and substances of similar consistency, such as sand or fine gravel. If two or more vampires attempt to interact underground, only direct physical contact is possible. All damage dice pools in this case are halved, and dodge and parry attempts are at -2 difficulty. If an underground chase takes place, it is resolved with an extended, contested ^Strength + Athletics^ roll (see p.261)."""
      ),
      Power(
        name='Flesh of Marble',
        discipline='protean',
        level=6,
        description="""Tales have long spoken of the combat prowess of Gangrel elders and of their inhuman resilience. Poorly informed individuals believe the stories of swords shattering and bullets flattening against immortal skin to be exaggerated reports of the effects of Fortitude. Those with more reliable information know that such tales result from encounters with vampires who have developed Flesh of Marble. The skin of an elder with Flesh of Marble becomes in essence a sort of flexible stone, although it appears (and feels) no different than normal skin and muscle.
_System_: The player spends three blood points to activate Flesh of Marble, which goes into effect instantly. The effects of the power last for the remainder of the scene. While the power is functioning, the damage dice pools of all physical attacks made against the character are halved (round down). That includes assaults made with fists, claws, swords, firearms, and explosions, but not fire, sunlight, or supernatural powers (unless the effect in question is a direct physical attack, such as a rock hurled by means of Movement of the Mind). Additionally, while this power is in effect, a character can attempt to parry melee attacks with his bare hands as if he were holding some form of weapon."""
      ),
      Power(
        name='Restore the Mortal Visage',
        discipline='protean',
        level=7,
        description="""Cainites are of two opinions regarding this power. Those who are politically active, or who associate extensively with mortals, view it as both necessary and acceptable. Those Kindred who embrace their more feral sides, however, see it as a disgusting defiance of the very nature of vampirism. The schism comes because the power allows the elder who possesses it to temporarily return his appearance to what it was before the Embrace, removing the bestial features he has accumulated over the centuries. Restore the Mortal Visage has only been displayed by Gangrel; several Nosferatu elders have attempted to develop it, and it is whispered that they met spontaneous, grotesque Final Deaths when they attempted to take their mortal forms.
_System_: The player spends three blood points and a Willpower point and rolls ^Willpower^ (difficulty 8). Success restores the character’s appearance to what it was just before he was first Embraced, erasing all physical or social animalistic features gained from frenzies (see p.55). The power also affects any of the character’s affected Traits relating to social interaction, returning them to their original values (for example, lost Appearance dots return, but Humanity points removed due to frenzy are not). A botched Willpower roll earns the character another feature, as per the Gangrel Clan weakness. Once activated, Restore the Mortal Visage lasts for the remainder of the scene."""
      ),
      Power(
        name='Shape of the Beast’s Wrath',
        discipline='protean',
        level=7,
        description="""Users of this power are often mistaken for Tzimisce employing the Vicissitude power Horrid Form. A vampire employing this power shifts into a huge, monstrous form, gaining half her height again and tripling her weight. Her overall shape flows into an unholy amalgamation of her own form and that of the animal she feels the closest kinship to (wolves, rats, and great cats are the most common manifestations, though ravens, serpents, bats, and stranger beasts have been reported). The vampire’s new shape does bear some vague resemblance to the war-forms of the werecreatures, but the difference quickly becomes apparent.
_System_: The player spends three blood points, the expenditure of which triggers the change. The character’s transformation takes three turns (the player may spend additional blood points to reduce this time at a cost of one point per turn of reduction). Once transformed, the character remains in this form until sunrise or until she shifts back voluntarily. The precise Traits of this form are determined when the character first learns this power, as is the animal whose appearance the character takes on. The vampire’s new form adds a total of seven dots to the character’s Physical Attributes. At least one dot must go into each Physical Attribute, meaning that no more than five can go into any one (so a character could have +5 Strength, +1 Dexterity, and +1 Stamina, but not +2 Strength and +5 Dexterity). These bonuses are always the same once they are selected; a different allocation requires that the character buy this power a second time and thus purchase another alternate form. Additionally, the character inflicts Strength + 2 dice of aggravated damage with both bite and claw attacks when in monstrous form. She also gains an extra Hurt health level, and doubles her normal running speed. Finally, the character’s perceptions are also heightened. She is assumed to have both the Auspex power Heightened Senses and the Protean power Eyes of the Beast after transformation, with all of the benefits and drawbacks of each. This form does carry two additional drawbacks. The first is a lack of communication ability. The character’s Social Attributes all drop to 1, or to 0 if they already were 1 (except when making Intimidation rolls) when the transformation occurs. The second problem that a character in this form encounters is the suddenly heightened power of her Beast. All difficulties of rolls to resist frenzy are increased by two for the duration of the power’s effect, and the player may not spend Willpower points on such rolls."""
      ),
      Power(
        name='Spectral Body',
        discipline='protean',
        level=7,
        description="""This powerful variation on Mist Form allows a vampire to take a shape with most of the advantages of the lesser power but fewer of the disadvantages. A vampire who assumes Spectral Form retains his normal appearance, but becomes completely insubstantial. He walks through walls and bullets with equal ease, and can pass through the foor on which he stands if he chooses to. Although his lungs are no longer solid, the vampire can still speak, a fact in which some elders of the Daughters of Cacophony bloodline have expressed great interest.
_System_: The player spends three blood points. The transformation takes one turn to complete, and lasts for the rest of the night unless the character decides to reverse it. When the power takes hold, the character becomes completely insubstantial, but remains fully visible. Henceforth, he is unaffected by any physical attacks, and he doubles his dice pool to soak damage from fire and sunlight. The vampire may even ignore gravity if he chooses to do so, rising and sinking through solid objects if he does not wish to stand on them (although he may move no faster than his normal walking speed while “flying” in this manner). While in this form, the character may also use any Disciplines that do not require physical contact or a physical body. On the downside, while in Spectral Form, a vampire can physically manipulate his environment only through the use of powers such as Movement of the Mind."""
      ),
      Power(
        name='Purify the Impaled Beast',
        discipline='protean',
        level=8,
        description="""Camarilla records indicate that a disproportionately small number of Gangrel elders were killed by mortals and Anarchs during the Inquisition and the Anarch Revolt. This power is one of the primary reasons for the survival of these Kindred. An elder with this Protean power can expel foreign objects from her body with great force, even excising stakes that transfix her heart.
_System_: The player spends three blood points and rolls ^Willpower^ (difficulty 6, or 8 if the vampire is paralyzed by an object impaling her heart). One success is sufficient to remove all foreign objects and substances from the character’s body. Dirt, bullets, and even stakes through the heart are instantly and violently removed. The larger the object, the farther away it is hurled by this power. Objects expelled thus are considered to have an attack dice pool of three for any bystanders, and to have a dice pool of one to four (depending on size) for damage. If the character wishes to leave an object in his body (such as a prosthetic limb) or partially in (expelling a stake from his heart but leaving it sticking out of his breastbone as a ruse), the player must also spend a Willpower point when activating this power."""
      ),
      Power(
        name='Inward Focus',
        discipline='protean',
        level=9,
        description="""This power has no outwardly visible effects whatsoever. Indeed, its very existence is unknown outside those Gangrel Methuselahs who have developed it. The internal effects of this razor-sharp honing of Protean, however, are in some ways more dramatic than any external manifestation. A vampire with this power can heighten the efficiency of his undead body’s internal workings to levels undreamed of by lesser Kindred, withstanding inconceivable amounts of injury and moving with blinding speed and shattering strength.
_System_: The player spends four blood points to activate this power and an additional two blood points for every turn past the first that Inward Focus is maintained. There are three effects of this power: First, the character gains a number of extra actions during each turn equal to his unmodified Dexterity score. Second, the damage of his physical attacks is increased by three dice per dice pool. Finally, all damage inflicted on the character is halved and rounded down after the soak roll is made (so an attack that inflicts five health levels after soak is reduced to two health levels). This power may be used in conjunction with other Protean powers that modify the character’s combat abilities, such as Shape of the Beast’s Wrath (above). It may also be used in conjunction with Celerity, Fortitude, and Potence, turning a vampire who has mastered this power into a truly terrifying opponent."""
      )
    ],
    description="""
Protean allows the Kindred the mystical ability to manipulate his physical form. Some vampires believe the power stems from a heightened connection to the natural world, while others consider it to be a magnification of the mark of Caine. Whatever its basis may be, those that develop this Discipline can grow bestial claws, take on the forms of bats and wolves, turn themselves into mist, and even meld into the very earth itself.

Transformed Kindred can generally use other Disciplines - vampires in wolf form can still read auras and communicate with other animals, for example. However, the Storyteller may rule that certain Disciplines may not be used in specific situations. The Kindred’s clothes and personal possessions also change when he transforms (presumably absorbed within his very substance), although armor and the like do not provide any benefit while transformed.

Vampires cannot change or transform large objects or other beings; Protean is a personal expression of power. A Kindred who has been staked (thereby trapping his soul within his body) cannot transform. Some vampires believe that those who have mastered the highest levels of Protean can deny this limitation, however.

The Gangrel Clan is well known for their mastery of Protean, although other Kindred have learned some of this Discipline’s secrets from these bestial Cainites.
"""
  ),
  Discipline(
    name='Thaumaturgy',
    sorcery=False,
    powers= [
      Power(
        name='Thaumaturgy 1',
        discipline='thaumaturgy',
        level=1,
        description="""Thaumaturgy 1"""
      ),
      Power(
        name='Thaumaturgy 2',
        discipline='thaumaturgy',
        level=2,
        description="""Thaumaturgy 2"""
      ),
      Power(
        name='Thaumaturgy 3',
        discipline='thaumaturgy',
        level=3,
        description="""Thaumaturgy 3"""
      ),
      Power(
        name='Thaumaturgy 4',
        discipline='thaumaturgy',
        level=4,
        description="""Thaumaturgy 4"""
      ),
      Power(
        name='Thaumaturgy 5',
        discipline='thaumaturgy',
        level=5,
        description="""Thaumaturgy 5"""
      ),
      Power(
        name='Thaumaturgy 6',
        discipline='thaumaturgy',
        level=6,
        description="""Thaumaturgy 6"""
      ),
      Power(
        name='Thaumaturgy 7',
        discipline='thaumaturgy',
        level=7,
        description="""Thaumaturgy 7"""
      ),
      Power(
        name='Thaumaturgy 8',
        discipline='thaumaturgy',
        level=8,
        description="""Thaumaturgy 8"""
      ),
      Power(
        name='Thaumaturgy 9',
        discipline='thaumaturgy',
        level=9,
        description="""Thaumaturgy 9"""
      )
    ],
    description="""
Thaumaturgy encompasses blood magic and other sorcerous arts available to Kindred. The Tremere Clan is best known for their possession (and jealous hoarding) of this Discipline. The Tremere created Thaumaturgy by combining mortal wizardry with the power of vampiric vitae, and as a result it is a versatile and powerful Discipline. Although there are whispers of the existence of Tremere <i>antitribu</i> in the Sabbat, other Clans in the Sword of Caine have also researched and developed access to such mystical might. Nevertheless, the Tremere of the Camarilla remain this Discipline’s masters.

Like Necromancy, the practice of Thaumaturgy is divided into paths and rituals. Thaumaturgical paths are applications of the vampire’s knowledge of blood magic, allowing her to create effects on a whim. Rituals are more formulaic in nature, most akin to ancient magical “spells.” Because so many different paths and rituals are available to the arcane Tremere, one never knows what to expect when confronted with a practitioner of this Discipline.

When a character first learns Thaumaturgy, the player selects a path for the character. That path is considered the character’s primary path, and she automatically receives one dot in it, as well as one Level One ritual. Thereafter, whenever the character increases her level in Thaumaturgy, her rating in the primary path increases by one as well. Additional rituals are learned separately, as part of a story; players need not pay experience points for their characters to learn rituals up to the level equal to their overall rating in Thaumaturgy, though they must find someone to teach the rituals in question. Path ratings never exceed 5, though the overall Thaumaturgy score may. If a character reaches a rating of 5 in her primary path and increases her Thaumaturgy score afterward, she may allocate her “free” path dot to a different path. (Experience costs are covered on p. 124.)

Many Kindred fear crossing the practitioners of Thaumaturgy. It is a very potent and mutable Discipline, and almost anything the Kindred wishes may be accomplished through its magic.
"""
  ),
  Discipline(
    name='Bardo',
    sorcery=False,
    powers= [
      Power(
        name='Restore Humanitas',
        discipline='bardo',
        level=1,
        description="""The first thing that the Children of Osiris are taught is that Humanity does not have to be an inexorable slide into depravity. Instead, it is more akin to a climb up an extremely steep hill. The vampire is going to lose some ground, but with perseverance and strength, he can regain it.
_System_: When the vampire loses a dot of Humanity, he can attempt to regain it without spending experience points by using this power. The Child must use this power within a week of losing the Humanity, and must not have lost any more Humanity since the initial loss (that is, if the character falls from Humanity 8 to Humanity 7, and then falls to Humanity 6 before using this power, Restore Humanitas can only be used to recover Humanity 7). The character meditates for several hours, and spends all of the blood points currently in his body. The player then rolls ^Conscience^ (difficulty equal to the level of Humanity being regained). If the roll succeeds, the character regains the dot of Humanity and (if applicable) the dot of Conscience lost to a botched degeneration roll. If the character gained a derangement, it fades within a week of using Restore Humanitas."""
      ),
      Power(
        name='Banishing Sign of Thoth',
        discipline='bardo',
        level=2,
        description="""The character gestures, turning aside any supernatural effect aimed at her. The source of the effect does not matter. She can thwart, or at least blunt, the strength of any mystical attack. This sign was supposedly taught to Osiris by Thoth, the Egyptian god of wisdom and magic. What Thoth actually was - vampire, mortal,or spellcaster - is lost to time.
_System_: The player spends a blood point and rolls ^Dexterity + Occult^ (difficulty 7). This power can be used to “dodge” any incoming attack of a mystical nature, including any Disciplines that target the character (whether or not they actually inflict damage). Any successes the player rolls are subtracted from the successes on the attacker’s roll. The sign does not serve to turn aside magically enhanced physical attacks; a punch from a vampire with the Potence Discipline still has the full effect."""
      ),
      Power(
        name='Gift of Apis',
        discipline='bardo',
        level=3,
        description="""All vampires must consume blood, no matter how good their intentions. While this basic fact of undeath cannot be circumvented, the Children of Osiris can at least avoid drinking human blood.
_System_: Animal blood is just as nourishing to the character as human blood. An animal is considered to have a blood pool equal to the number of health levels it has, rather than the lesser value usually assigned to represent the creature’s less-than-filling fluids (see p.270 for more on drinking from animals). This ability is always active."""
      ),
      Power(
        name='Pillar of Osiris',
        discipline='bardo',
        level=4,
        description="""In the center of every temple is a Pillar of Osiris, a place of meditation and power in which the Children’s magic is greatly increased. At this level of Bardo, the character learns to create such a Pillar, meaning that he can create his own temple.
_System_: Creating the Pillar of Osiris requires a night-long ritual, with the difficulty determined by the location. The more remote and free from violence the location is, the lower the difficulty. A cave far from human populations that has never seen violence might be difficulty 5, whereas the site of a grisly murder-suicide in a downtown area would be difficulty 9. The player spends a Willpower point and rolls ^Willpower^. Success creates the Pillar, which does not require a physical pillar - the Pillar of Osiris is conceptual, not literal. Once the Pillar is created, any vampire with at least one dot of Bardo receives a -3 to the difficulties of any Discipline or other mystical activity (including blood magic) performed at the Pillar. However, this requires regular trips to the Pillar. Once the vampire has created a Pillar, he must visit it at least once a month, or it ceases to function. In addition, for every week he is away from a Pillar (not necessarily the one he created), the difficulties of all rolls to avoid frenzy increase by one. The Beast, long denied by the Child’s ascetic practices, grows in strength while away from the Pillar, and eventually pushes the vampire to frenzy and (likely) Humanity loss. The Children of Osiris, for this and other reasons, do not leave their temples for long."""
      ),
      Power(
        name='Paradox',
        discipline='bardo',
        level=5,
        description="""The Child utters a phrase or a riddle that lays bare the truth of the universe to a listener. That truth - the perspective of that one listener’s importance weighed against the whole of creation - is enough to immobilize the target for a  short while. Although this experience would seem to be disheartening, after the fact the targets are loath to harm the Child. Whether that’s because of a new-found appreciation for one’s place in the world, or out of fear that the vampire will reveal the paradox again, no one really knows.
_System_: The vampire speaks the phrase, and the player spends a point of Willpower and rolls ^Manipulation + Occult^ (difficulty equal to the listener’s current Willpower). If multiple listeners are present, the player rolls against the highest difficulty. If the roll is successful, the listener(s) is immobilized for the scene as he contemplates what he has heard. Striking the victim snaps him out of it. At the end of the scene, the paradox is gone, and the target can’t ever quite explain it. He does, however, suffer a permanent +1 difficulty to harm or act against the Child of Osiris."""
      ),
      Power(
        name='Boon of Anubis',
        discipline='bardo',
        level=6,
        description="""The vampire can protect a mortal from Embrace, leaving instructions for Anubis, the judge of the dead, not to take this particular mortal to his scales. If the mortal is Embraced while under the power of this Discipline, she simply sleeps for a full night and day, and awakens aching and sick, but unharmed. In order to enact this power, the Child of Osiris must kiss the mortal, usually on the forehead.
_System_: The vampire spends a point of Willpower and rolls ^Humanity^ (difficulty 6). If the roll succeeds, the target is immune to the Embrace for a number of months equal to the successes rolled. The player can spend a dot of Willpower to make the effect permanent. Note that this Discipline does not protect against any other form of death than the Embrace. If a vampire drains the unfortunate victim dry and then shoots her in the head, she dies just the same. However, the difficulty to avoid degeneration when killing or harming someone under protection of this power is increased by three."""
      ),
      Power(
        name='Bring Forth the Dawn',
        discipline='bardo',
        level=7,
        description="""This power does not actually cause the sun to rise, but rather triggers the daysleep in Kindred. The Child simply gestures, and the target’s Beast responds as though the sun had just risen outside. The Child can then beat a hasty retreat - or stake and behead the vampire now lying helpless before him.
_System_: The player spends a blood point for each vampire to be affected and rolls ^Manipulation + Occult^ in a contested roll against each target’s Humanity or Path (both rolls at difficulty 7). If the target wins, the power fails. If the Child wins, however, all affected vampires fall asleep for a number of hours equal to the Child’s net successes. Followers of Set and other blood-lines that share their weakness suffer a -2 to their dice pool for this roll. Any Disciplines or Thaumaturgy rituals which protect the Kindred during their sleep also work in defending against this level of Bardo."""
      ),
      Power(
        name='Mummification',
        discipline='bardo',
        level=8,
        description="""The Children of Osiris have an uneasy relationship with destroying other vampires. They would prefer not to do so, but some Kindred are too evil to be allowed to exist. For the vampires that straddle the line - that are wicked, but retain a spark of Humanity - the Children sometimes use Mummification. This long ritual allows a vampire to be put into torpor for as long as the Child wishes. The target can attempt to struggle free, but only once per century. Once the vampire is mummified, the Children usually seal her up in a deep tomb, where (hopefully) she will remain undisturbed.
_System_: The target must be immobilized, ritually bound in strips of fabric, and prepared with incense and special herbs. The player then rolls ^Willpower^ in a contested action against the target’s Willpower (both difficulty 8). If the Child wins, the target enters torpor. If the victim wins, he remains awake and the ritual cannot be completed for another night (meaning that resistance is usually temporary). The target can also attempt to shake the spell free once per century, with a Willpower roll (difficulty 9). Ghouls can also be mummified, but they get no chance to escape."""
      ),
      Power(
        name='Ra’s Blessing',
        discipline='bardo',
        level=9,
        description="""This ritual is difficult, but allows the vampire to accomplish the impossible - walking in sunlight, fully experiencing the day once more. Gaining Ra’s Blessing requires a month-long period of fasting and meditation, at the end of which the character might be granted the chance to spend a few precious hours in sunlight. Even this brief period, however, can bolster the character’s Humanity.
_System_: After completing the month of contemplation, the character ritually washes herself and prepares to greet the dawn. The player spends 10 blood points and rolls ^Humanity^ (difficulty 9). Every success allows the character to withstand the sunlight as if she were mortal for a single hour. If the roll fails or botches, the character cannot attempt Ra’s Blessing for a decade. If the roll succeeds, though, the character can use the reaffirmation of seeing sunlight as a way to boost her Humanity and Virtues. For every hour spent under the sun, the Child can roll his ^Humanity^, or one of his Virtues, against a difficulty of 9. Success means that trait is raised by one, while failure or botching this roll means no gain."""
      )
    ],
    description="""
This Discipline has been handed down since Osiris himself first discovered this path. It involves attainment of a constant state of mystical consciousness, only achieved by the rigid, ascetic unlife of the Children. This Discipline is not the same state as Golconda. Golconda is a realization and acceptance of the way things are, while the Children’s Disciplines are based on denial. They deny the Beast within them by intensely concentrating on their Humanity and their state of death.

If a Child was to give up his meditations and discipline, he would be assailed by his Beast. The Child must maintain Humanity equal to their highest level of ability, or else lose that ability. For example, a Child must have a Humanity of 9 to gain the ninth level of attainment. If the Child’s Humanity ever drops below the required level, then the ability of that level is lost and must be bought all over again with experience points. The Child can counteract this with Restore Humanitas (below).

A Child of Osiris cannot follow any type of moral code other than Humanity.
"""
  ),
  Discipline(
    name='Sanguinus',
    sorcery=False,
    powers= [
      Power(
        name='Brother’s Blood',
        discipline='sanguinus',
        level=1,
        description="""A circle of Blood Brothers is closer than any Sabbat pack, any blood-bound pair of vampiric lovers, any ghoul family. The circle shares flesh, mind, and, of course, blood. The members of the circle can spend blood to heal each other’s bodies, no matter how far apart they are.
_System_: The player spends a blood point, which may be used to heal any member of the circle, regardless of distance from the character. The Blood Brother may also “bank” blood, spending five points to heal another’s aggravated wound over the course of several turns. This power takes effect automatically; no roll is necessary. Blood spent by another Frankenstein does not count against the maximum amount of vitae the target character can spend per turn."""
      ),
      Power(
        name='Octopod',
        discipline='sanguinus',
        level=2,
        description="""The Blood Brother circle can donate limbs and organs to one another. This isn’t meant for healing after the battle, but for use during the battle. An opponent facing down the Blood Brothers might see one of his opponents grow a second set of legs (making him nearly impossible to knock down), another pair of arms (meaning he can block or parry almost any incoming attack), extra eyes for 360 degree vision, or an extra mouth for a greater blood consumption. Of course, the Frankenstein that gives up the organ might be left a limbless, eyeless, mouthless lump of flesh on the side of the battlefield, but the Blood Brothers never seem to mind that.
_System_: The “donor” player spends a blood point for each limb or organ he wishes to loan to the other circle member. (Only the donor needs to have this level of mastery of Sanguinus; the recipient may be any other member of the donor’s circle). The loaned organs appear at the end of that turn, in whatever location the recipient wishes - eyes on the back of heads or on the ends of hands have been seen, as have entire heads located between a Blood Brother’s legs. Use of this power does not impart any extra attacks, but it may allow for additional sensory input, more blood to be consumed in a single turn, or extra hands to hold weapons or pin down foes. Only external organs may be loaned in this manner - hearts, stomachs, and brains cannot."""
      ),
      Power(
        name='Gestalt',
        discipline='sanguinus',
        level=3,
        description="""Blood Brothers share a hive-mind; this ability was one of the guiding principles behind their creation. The Gestalt power is that hive-mind, the ability of the Frankensteins to coordinate silently and perfectly in battle, to avoid mind-controlling powers, and to act in unison.
_System_: This power confers several benefits on the Blood Brothers. For this power to work, however, every Blood Brother in the circle must spend a blood point. If even one member cannot or will not spend a blood point, this power fails. Once a Blood Brother has met the Final Death, he is no longer a part of the circle, so the power continues to function among the still-undead members of the group. Gestalt lasts for one scene. While this power is active:
Dominate, Presence, and the like take effect against the highest Willpower rating in the circle. For example, if a vampire attempts to Dominate a Blood Brother under the influence of Gestalt, she must roll against the highest Willpower rating any of the vampires in the circle possesses, even if her subject has the lowest Willpower rating in the circle. Additionally, a Blood Brother affected by powers in this manner drops out of the Gestalt, though Gestalt remains active for others. This mental “fuse” was supposedly created to prevent the entire circle from being Dominated by a vampire looking into the eyes of one Blood Brother.
Perception difficulties for all Blood Brothers in the circle decrease by three, as they share the sensory input of other vampires in the circle.
By taking no action other than concentrating, a Blood Brother may “loan” an Ability to another brother. For example, a wounded vampire with Melee 4 may step out of combat and loan a circle-mate with Melee 2 his mastery of that Skill. The “borrowing” vampire makes Ability checks against the loaned Trait as if it were his own.
The Blood Brothers in the Gestalt may communicate through telepathy, allowing them to coordinate actions. In game terms, only one initiative roll is made for the circle, based on the character with the highest initiative rating (see p.271). Not all Blood Brothers in the circle need to have this level of Sanguinus to benefit from the Gestalt. If a given character does not know this power, though, the player rolls ^Wits + Occult^ (difficulty 7) when the power is enacted. If this roll fails, the character can still receive loaned Abilities, but gains no other benefits from the Gestalt."""
      ),
      Power(
        name='Walk of Caine',
        discipline='sanguinus',
        level=4,
        description="""The sorcerous theory behind the Blood Brothers reads like a philosophical treatise on the nature of individuality, free will, and hematology. The Frankensteins are not a group of vampires but are one vampire in several bodies, or so goes the theory. As such, any of their characteristics must be viewed as a continuum - they are not individually Twelfth, Eleventh, and Thirteenth Generation, for example, but they are collectively Ninth Generation at any given time. While the metaphysics of this kind of thinking makes most vampires’ heads ache, there seems to be something to it. A Blood Brother can draw strength from his circle, lowering his Generation to allow for greater feats of vitae expenditure.
_System_: Each member of the circle can “donate” one step in Generation. In the example listed above, the vampire of Eleventh Generation could take one step from his two circle-mates and drop to Ninth, but the vampire of Thirteenth Generation couldn’t drop lower than Eleventh. No matter how big the circle, no Blood Brother can drop to an effective Generation lower than Fourth. Likewise, a Thirteenth Generation Blood Brother can drop to an effective Generation of Fourteenth, which carries with it the penalties listed for the Fourteenth Generation Flaw (p.481) (He cannot go to Fifteenth Generation, however). As with Gestalt, only one Blood Brother needs to know this power in order to begin the process. Any that don’t have Walk of Caine need to make a Stamina + Awareness roll (difficulty 7). If this roll fails, they may not participate in the action."""
      ),
      Power(
        name='Coagulated Entity',
        discipline='sanguinus',
        level=5,
        description="""The Blood Brothers merge into a fleshy, bleeding mound of horror. This juggernaut surges forward, crushing and consuming anything in its path. The Sabbat has learned to its chagrin that if the Blood Brothers are not explicitly told to separate after using this power, they won’t. This merger is, apparently, what the Blood Brothers truly want.
_System_: Every vampire in the circle who wishes to become part of the Coagulated Entity spends three blood points. Three turns after the process begins, the monster is complete and able to act. The vampire of the lowest Generation who is part of the construct guides the creature’s actions. The actual Generation of the creature itself, however, is the highest Generation of any vampire present in the construct, less one for each additional vampire present in the construct. (Using the previous example, the Eleventh-Generation vampire would be the guide but the highest Generation is 13, so the overall Entity would be 13 minus 2, or Eleventh Generation). The creature’s Strength, Stamina, and Perception are equal to the guide’s, with a +1 for every additional vampire contained within. (Generational limits do not apply to this creature - through sheer size, a Coagulated Entity may have a Strength of 7 or more). All physical actions undertaken by the monstrosity gain one extra die to the pool for each vampire beyond the first present in the construct (before splitting dice pools). Only one vampire in the circle needs to possess Sanguinus at Level Five for this power to work. Body parts tend to shift during the creation of a Coagulated Entity - fanged maws at the ends of hands and eyes atop fleshy stalks have been reported by terrified survivors. Storytellers should feel free to give any bonuses (or penalties) to the construct as they see fit. A Coagulated Entity may not be staked, as it has too many hearts in unconventional places for any but the blindest luck to impale. It has a vampire’s normal seven health levels, plus two for each additional vampire who becomes part of the entity (treat these extra health levels as Bruised). The entity remains congealed for one scene, unless the Storyteller wishes to rule that no one told the Blood Brothers to separate."""
      )
    ],
    description="""
Sanguinus is the unwholesome Discipline granted to the Blood Brothers by the Tzimisce who created them. A curious relative of Vicissitude, Sanguinus allows vampires who practice it to combine parts of their bodies, loan them out to others, and coordinate their minds and appendages. Even low levels of it are unsettling to watch. Use of the higher levels is disgusting, indeed, as flesh parts and exposed organs, atrophied by the Blood Brothers’ state of undeath, merge and pulse. Mortals observing the spectacle of this Discipline’s more obvious powers must make Courage rolls (difficulty 4), spend a point of Willpower, or flee the area in nausea.
"""
  ),
  Discipline(
    name='Valeren',
    sorcery=False,
    powers= [
      Power(
        name='Sense Vitality (Valeren)',
        discipline='valeren',
        level=1,
        description="""A healer learns a subject’s illnesses to cure them. The Salubri <i>antitribu</i>, however, learn how close to death a target is so that they may hasten the process.
_System_: This power works identically to the Obeah power of the same name (p.457).
_System_: The Salubri must touch the target to see how close to death she is. He must then make a ^Perception + Empathy^ roll (difficulty 7). One success on this roll identifies a subject as a mortal, vampire, ghoul, or other creature. Two successes reveal how many health levels of damage the subject has suffered. Three successes tell how full the subject’s blood pool is (if a vampire) or how many blood points she has left in her system (if a mortal or other blood-bearing form of life). Four successes reveal any diseases in the subject’s bloodstream. A player may opt to learn the information yielded by a lesser degree of success - for example, a player who accumulates three successes may learn whether or not a subject is a vampire as well as the contents of his blood pool. Alternately, each success on this roll allows the player to ask the Storyteller one question about the subject’s health or health levels. “Was he drugged?” or “Are his wounds aggravated?” are valid questions, but “Did the Sabbat do this?” or “What did the Lupine who attacked him look like?” are not. The Salubri may use this power on herself if she has injuries but has somehow lost the memory of how the wounds were received. Additionally, at the cost of one blood point, the Salubri may use Empathy for a roll instead of Medicine."""
      ),
      Power(
        name='Anesthetic Touch (Valeren)',
        discipline='valeren',
        level=2,
        description="""The Salubri <i>antitribu</i> can ameliorate a subject’s pain, allowing him to bolster a ghoul’s effectiveness in combat. This power can also put a mortal to sleep, which has obvious applications for escaping human scrutiny (though the Fury is probably just as likely to kill the mortal in question).
_System_: This power works identically to the Obeah power of the same name (p.458).
_System_: If the subject is willing to undergo this process, the player spends a blood point and makes a ^Willpower^ roll (difficulty 6) to block the subject’s pain. This allows the subject to ignore all wound penalties for one turn per success. A second application of this power may be made once the first one has expired, at the cost of another blood point and another Willpower roll. If the subject is unwilling for some reason, the player must make a contested ^Willpower^ roll against the subject (difficulty 8). To put a mortal to sleep, the same system applies. The mortal sleeps for five to 10 hours - whatever his normal sleep cycle is - and regains one temporary Willpower point upon awakening. He sleeps peacefully and does not suffer nightmares or the effects of any derangements while asleep. He may be awakened normally (or violently). Kindred, including the Salubri herself, are unaffected by this power - their corpse-like bodies are too tied to death."""
      ),
      Power(
        name='Burning Touch',
        discipline='valeren',
        level=3,
        description="""The character’s hands bring searing pain, as though the target is being burnt with red-hot metal. Although the power does not inflict actual damage, prolonged or repeated exposure can be enough to traumatize a victim. This power works extremely well as a torture method.
_System_: The vampire must touch his subject for this power to take effect, and the effects diminish rapidly after he removes his hand. The player spends at least one blood point to activate this power, and each blood point spent reduces the victim’s dice pools by two while the Fury is in contact with the victim. This power is often used for interrogation or torture, wearing down the subject’s resistance and rendering him much more tractable."""
      ),
      Power(
        name='Armor of Caine’s Fury',
        discipline='valeren',
        level=4,
        description="""The Salubri <i>antitribu</i> is surrounded by a shining, crimson halo. This phantom armor protects the vampire against most physical injury, as well as against Rötschreck.
_System_: The player spends one blood point and rolls ^Stamina + Melee^ (difficulty 7). For each success, the character gains one point of armor protection against bashing and lethal damage, to a maximum of five points of protection. Additionally, for every two successes rolled, she gains an additional die to resist Rötschreck from the effects of battle (but not fire or sunlight). This power works for one scene."""
      ),
      Power(
        name='Vengeance of Samiel',
        discipline='valeren',
        level=5,
        description="""The Salubri <i>antitribu</i> strikes his foe with superhuman accuracy and strength, as his third eye opens and changes to a furious, icy blue. Some Furies invoke the names of ancient Salubri warriors, while others simply close their normal eyes and let Samiel guide their hands.
_System_: This power costs three blood points. Any single attack made by the vampire automatically hits the target as mystic forces guide the blow. Attacks made in this manner may not be dodged, though they may be blocked, parried, and soaked as normal. The blow strikes as if the Salubri <i>antitribu</i> had succeeded with all of his Dexterity + Melee or Brawling dice pool (which makes for significant damage). This power may be used only once per turn, and only then the Salubri <i>antitribu</i>’s sole action is the attack. Additionally, this power does not work for ranged weapons; only bare hands or melee weapons."""
      ),
      Power(
        name='Blissful Agony',
        discipline='valeren',
        level=6,
        description="""The vampire may cause pain with a mere touch, as per Burning Touch, but this pain lingers and swells even after the Fury has removed her hand. It is believed that this power was originally used to acclimate warrior Salubri to the pain they would experience in battle, but among the Sabbat Salubri, Blissful Agony has been turned to more brutal uses. If applied with enough intensity, Blissful Agony can drive vampires to the point of frenzy, incapacitate Lupines, and even kill mortals outright.
_System_: The player makes a ^Willpower^ roll (difficulty 8) and spends a blood point. The power lasts for one scene, though this duration may be prolonged if the Salubri <i>antitribu</i> wishes by making a subsequent ^Willpower^ roll (though no additional blood points need be spent). The character must touch her subject for the power to take effect initially. At the vampire’s option, she may cause actual physical damage to the victim at the rate of one health level per blood point spent, though touch must be maintained for this to happen. Damage to vampires and other supernatural creatures in this fashion vanishes at the next sunset, but mortals must heal the damage normally. This damage is considered lethal damage, and mortals may not soak it (though vampires and other supernatural entities may). To induce frenzy in a victim, the Fury must cause damage in excess of the subject’s Willpower. At that point, the subject must make a Willpower roll (difficulty 6) or succumb to frenzy."""
      )
    ],
    description="""
Valeren is a warrior’s Discipline, a holdover from the nights when warrior Salubri acted as noble fighters and Kindred knights. The Discipline is still applicable to the modern nights, but the Salubri <i>antitribu</i> put it to decidedly more vicious ends.

Like Obeah, Valeren imparts its practitioners with the fabled third eye of Saulot. The third eye appears at the time the vampire masters the second level of Valeren. The precise nature and purpose of the eye are all but unknown to vampires outside the Salubri <i>antitribu</i>. Some suspect the eye grants them sight beyond sight, while others venture that the eye allows them to see the infernal taint in the non-Sabbat Salubri themselves.
"""
  ),
  Discipline(
    name='Any',
    sorcery=False,
    powers= [
      
    ],
    description=""" """
  ),
  Discipline(
    name='Necromancy',
    sorcery=False,
    powers= [
      Power(
        name='Necromancy 1',
        discipline='necromancy',
        level=1,
        description="""Necromancy 1"""
      ),
      Power(
        name='Necromancy 2',
        discipline='necromancy',
        level=2,
        description="""Necromancy 2"""
      ),
      Power(
        name='Necromancy 3',
        discipline='necromancy',
        level=3,
        description="""Necromancy 3"""
      ),
      Power(
        name='Necromancy 4',
        discipline='necromancy',
        level=4,
        description="""Necromancy 4"""
      ),
      Power(
        name='Necromancy 5',
        discipline='necromancy',
        level=5,
        description="""Necromancy 5"""
      ),
      Power(
        name='Necromancy 6',
        discipline='necromancy',
        level=6,
        description="""Necromancy 6"""
      ),
      Power(
        name='Necromancy 7',
        discipline='necromancy',
        level=7,
        description="""Necromancy 7"""
      ),
      Power(
        name='Necromancy 8',
        discipline='necromancy',
        level=8,
        description="""Necromancy 8"""
      ),
      Power(
        name='Necromancy 9',
        discipline='necromancy',
        level=9,
        description="""Necromancy 9"""
      )
    ],
    description="""
Necromancy is both a Discipline and a school of blood magic devoted to the command of the souls of the dead. It’s similar to Thaumaturgy in that it has several “paths” and accompanying “rituals” rather than a strict linear progression of powers. The study of Necromancy is not widespread among the Kindred, and its practitioners - primarily the Giovanni - are shunned and despised for their foul practices (until those practices become useful, of course).

Over the centuries, the various schools of vampiric Necromancy have evolved and diversified from an earlier form of death magic, leaving several distinct paths of necromantic magic available to Cainites. Nearly all modern necromancers learn the Sepulchre Path first before extending their studies to other paths. The primary Necromancy path increases automatically as the character increases her overall Necromancy rating. Other paths must be bought separately, using the experience costs for secondary paths.

Like Thaumaturgy, Necromancy has also spawned a series of rituals. While not nearly so immediate in effect as the basic powers of Necromancy, Necromantic rituals can have impressive long-term effects. Unsurprisingly, the elements of Necromantic ritual are things like long-buried corpses and hands from the cadavers of hanged men, so obtaining suitable materials can be quite difficult.

_System:_ A Cainite necromancer must learn at least three levels in his primary path before learning his first level in a secondary Necromancy path. He must then master the primary path (all five levels) before acquiring any knowledge of a third path.

As with Thaumaturgy, advancement in the primary path costs the normal experience amount, while study of additional Necromantic paths incurs an additional experience-point cost (see p. 124). Because Necromancy is not quite so rigid a study as Thaumaturgy is, the rolls required to use Necromantic powers can vary from path to path and even within individual paths. The commonly-learned Sepulchre Path is presented first, with the remaining paths presented in alphabetical order. Statistics for ghosts may be found in Chapter Nine, p. 385.
"""
  ),
  Discipline(
    name='Flight',
    sorcery=False,
    powers= [
      Power(
        name='Flight 1',
        discipline='flight',
        level=1,
        description="""The character cannot actually fly, but can soar like a hang-glider. He also cannot carry anything (he needs his hands to help steer). Maximum speed is equal to prevailing winds, or 15 miles/25 kilometers per hour in calm air."""
      ),
      Power(
        name='Flight 2',
        discipline='flight',
        level=2,
        description="""The character can make a running take-off and carry 20 pounds/10 kilograms while flying. Maximum speed is 30 miles/50 kilometers per hour."""
      ),
      Power(
        name='Flight 3',
        discipline='flight',
        level=3,
        description="""The character can make a straight, vertical take-off if unencumbered, or can make a running take-off carrying up to 50 pounds/25 kg. Maximum air speed is 45 miles/70 kilometers per hour."""
      ),
      Power(
        name='Flight 4',
        discipline='flight',
        level=4,
        description="""The character can now make a vertical take-off with up to 50 pounds/25 kg of baggage, but can carry up to 100 pounds/45 kg while flying. Maximum speed is 60 miles/95 kilometers per hour."""
      ),
      Power(
        name='Flight 5',
        discipline='flight',
        level=5,
        description="""The character can now carry up to 200 pounds/90 kg, easily enough to carry away an adult person (or vampire). Maximum speed is 75 miles/120 kilometers per hour."""
      ),
      Power(
        name='Flight 6',
        discipline='flight',
        level=6,
        description="""The character can now carry up to 300 pounds/135 kg, easily enough to carry away an adult person (or vampire). Maximum speed is 95 miles/150 kilometers per hour."""
      ),
      Power(
        name='Flight 7',
        discipline='flight',
        level=7,
        description="""The character can now carry up to 400 pounds/180 kg, easily enough to carry away an adult person (or vampire). Maximum speed is 115 miles/180 kilometers per hour."""
      ),
      Power(
        name='Flight 8',
        discipline='flight',
        level=8,
        description="""The character can now carry up to 500 pounds/225 kg, easily enough to carry away an adult person (or vampire). Maximum speed is 135 miles/210 kilometers per hour."""
      ),
      Power(
        name='Flight 9',
        discipline='flight',
        level=9,
        description="""The character can now carry up to 600 pounds/270 kg, easily enough to carry away an adult person (or vampire). Maximum speed is 155 miles/240 kilometers per hour."""
      )
    ],
    description="""
Gargoyles possess a fourth in-clan Discipline, called Flight. All Gargoyles start with a free dot, and it can be increased like any other Discipline. As the Gargoyle gains dots of Flight, he becomes capable of flying faster.
"""
  ),
  Discipline(
    name='Ogham',
    sorcery=False,
    powers= [
      Power(
        name='Consecrate the Grove',
        discipline='ogham',
        level=1,
        description="""The Lhiannan with this ability can use the power of her blood to awaken the spirits of plant life in her territory; they will act in her defense against any unwelcome intruder. Roots tangle feet, grass grasps at boots, trees sway unnaturally in foes’ way, and so on. Typically the Lhiannan slits a wrist and whirls in place, or stabs a palm and walks a spiral pattern through the foliage that she wishes to awaken.
_System_: The player spends from one to three blood points, and the character must undertake the process described above. One blood point rouses the plant life in a 10-foot (3-meter) diameter; two blood points doubles that to 20 feet (6 meters); three makes it 40 feet (12 meters). Tracing the desired area takes one turn per blood point spent. When the blood has been sown, the player rolls ^Charisma + Survival^ (difficulty 6). If the roll garners even one success, the plant life animates as the local spirit world is roused to action. Enemies in the area suffer a -2 to all dice pools from distraction and physical interference. Additionally, interlopers must make a Stamina + Athletics roll to avoid three dice of bashing damage from the local flora (provided the local plant life is capable of such damage; trees and brambles probably are, but a grassy meadow doesn’t contain the kind of flora necessary for such an assault). Botching this roll causes the plants to turn on the Lhiannan instead. This power lasts for one scene."""
      ),
      Power(
        name='Crimson Woad',
        discipline='ogham',
        level=2,
        description="""The Lhiannan traces mystical runes or script on her own body in vitae, inviting spirits of war to infuse her and gird her for battle. While so imbued, she ignores many wounds and retains greater control of her mind as the spirits direct her Beast. The Lhiannan can also lash out at her enemies with a fierce, blood-borne attack.
_System_: The character spends one scene tracing the woad on her body; this costs one blood point. The player then rolls ^Intelligence + Occult^ (difficulty 7). Each success enables the character to ignore one die of wound penalties from injury. It also subtracts one from the difficulty to avoid frenzy or Rötschreck. This ability lasts through one scene. Additionally, if the character receives more than four health levels of damage, the mystic inscriptions are ruined, and the spirits flee her body. The Lhiannan may also lash out at her enemies, adding the fury of the woad to her attack. The player may add the number of successes achieved on the above roll to the number of dice rolled for damage for a single close-combat attack (this ability can only be used once per application of Crimson Woad)."""
      ),
      Power(
        name='Inscribe the Curse',
        discipline='ogham',
        level=3,
        description="""The Lhiannan inscribes the name of an enemy on her body in vitae, in whatever language or set of symbols she likes. When the name is so inscribed and the Lhiannan’s enemy can see it, baleful spirits become bound to the name and enact a curse upon that enemy. The curse takes effect the moment the victim sees his name scrawled in blood.
_System_: The player spends three blood points. The Lhiannan must write the foe’s name in blood, and it must be displayed on a part of her body visible to the intended target in order for Inscribe the Curse to take effect. The player chooses which curse to enact on the target from the list below; the curse takes effect as soon as the target sees his name. He does not need to understand the language used, but if he can comprehend it, he may resist the curse with a Wits + Occult roll (difficulty 8). The curses described below expire when the glyph is erased, worn off, or defaced by the Lhiannan taking four or more health levels of damage. The curse works differently depending on where the Lhiannan inscribes the target’s name.
_Body_: Inscribe the name on arms, legs, or belly. The victim’s body becomes ill and weak (+2 to all difficulties on Physical rolls, and all wound penalties are increased by one die) or, in the case of Cainites, the victim cannot use blood other than the one point per day necessary to remain active.
_Mind_: Inscribe the name across the forehead. The foe becomes confused as parts of his mind become disconnected from one another; he must spend one Willpower point in order to attempt any Knowledge roll or use any magical ability or Discipline (other than Celerity, Fortitude, or Potence). This Willpower doesn’t buy him a success on that roll; it simply allows him to make it.
_Voice_: Inscribe the name on the throat. The victim loses the power of speech; he can grunt or moan, but cannot say any words.
_Soul_: Inscribe the name down the sternum and over the heart. The subject loses his will to resist the Beast: difficulties to avoid frenzy are increased by two. Non-vampires are overcome by fear. The target must flee the Lhiannan’s territory unless he succeeds in a Courage roll (difficulty 8)."""
      ),
      Power(
        name='Moon and Sun',
        discipline='ogham',
        level=4,
        description="""The life of a Cainite is dominated by two celestial bodies: the sun, which she must fear and hate; and the moon, her only safe source of light. A Lhiannan can trace ancient sigils of those two orbs on her body to gain gifts - the spirit of the moon, ever the vampire’s friend, blesses her by its current phase, while the sun’s spirit wards off some of that orb’s fiery curse.
_System_: The player spends three blood points. The Lhiannan inscribes the desired sigil on her body over the course of 15 minutes. The sigil can be inscribed anywhere, but must be exposed. The character may choose to inscribe both the moon and the sun, but each symbol requires the blood expenditure and 15 minutes to trace it. She can also inscribe these sigils on any voluntary subject. The sun emblem protects a vampire from the worst effects of fire and sunlight. So long as the symbol remains on the character’s body, the player makes a Stamina roll (difficulty 8) when afflicted by fire or sunlight. If the roll is successful, the damage is considered lethal and the player may roll to soak it normally. This roll must be made every time the character faces such damage.
The moon emblem adds one to the difficulties of Self-Control/Instinct rolls to avoid frenzy (but not Courage rolls to avoid Rötschreck). Other effects of the moon emblem depend on the current phase of the moon:
_New Moon_: Add one die to Dexterity and Stealth dice pools.
_Crescent Moon_: Add one die to Wits and Occult dice pools.
_Half Moon_: Add one die to Perception and Subterfuge dice pools.
_Gibbous Moon_: Add one die to Charisma and Expression dice pools.
_Full Moon_: Add one die to Strength and Brawl dice pools."""
      ),
      Power(
        name='Drink Dry the Earth',
        discipline='ogham',
        level=5,
        description="""The spirit within every Lhiannan is drawn to sites of mystical energy, whether ancient stone circles, faerie rings, or dragon tracks. That spirit-shard can wrest spiritual energy out of those places of power and use it to aid the Lhiannan. A word of caution, however: stealing too much power from any mystical site renders it barren and lifeless, much as if the Cainite had consumed the very blood of the Earth. Also, wizards and werewolves frequent these same sites, and destroying these places can rouse their ire.
_System_: The player rolls ^Perception + Occult^ (difficulty 8). One success determines if a given location is a suitable site (a decision generally left in the Storyteller’s hands, though a Lhiannan with a high Domain Background may have such a site within her holdings). Two or more successes on this roll grants a rough idea of the site’s power on a scale of 1 to 5. If the character wishes to tap the power of that location, she must spend a scene and one blood point marking various parts of the site with sigils of power, keys for her spirit-shard to unlock the location’s energies. Once the site is prepared, the player makes a second, reflexive ^Perception + Occult^ roll (difficulty 7). Any successes beyond the site’s power rating are ignored. For each success, the player gains two dice, which she may add to any dice pools (except those to avoid frenzy or Rötschreck) for the remainder of the scene. These dice are gone when used, but the character may tap the same location again from turn to turn. The player must make the ^Perception + Occult^ roll each time. Each “drink” of the site’s energies depletes it, however, as described below. The Lhiannan’s spirit-shard is a greedy thing, wearing as it does the garb of a Cainite’s Beast, and drinks the site’s energies recklessly. A Lhiannan can only garner a number of successes equal to 10 times the site’s power rating, after which point the area turns into a barren wasteland, incapable of sustaining life. This sort of activity in particular is certain to attract the attention of Lupines or wizards. A site may replenish itself over a period of years. However, a site that is tapped with Drink Dry the Earth at any point during the year is unable to replenish lost dice at all that year, and if the site is completely drained, it is irrevocably dead."""
      ),
      Power(
        name='Inscribe the Forgotten Names',
        discipline='ogham',
        level=6,
        description="""When the Lhiannan reaches this level of Ogham, she reverses the relationship between herself and her spirit-shard and can dominate and extract information from it. The Lhiannan’s ancient spirit knows the names of many mythical beings, and it can be bludgeoned into giving the Lhiannan one of those names so that she may invoke such a creature. These beings are dangerous, and not to be trifed with. Many are on a par with Methuselahs. Inscribe the Forgotten Names allows its wielder to communicate with the being she summons, but it does not give her domination or control over that creature. She must appease it in whatever manner she can, and hope that it does not take offense at being called up.
_System_: The player spends three blood points. The Lhiannan must spend one half hour undisturbed as blood oozes from her skin to sate the spirit-shard’s hunger. At the end of this time, the player rolls ^Intelligence + Occult^ (difficulty 9, or 8 if the character has summoned this particular being before). If the roll succeeds, a powerful creature arrives in the immediate vicinity before the end of the current scene. The Storyteller is free to assign game statistics to any creature summoned. Such creatures have their own desires and demands, and many do not take kindly to being called."""
      )
    ],
    description="""
The Ogham Discipline is only found among the Lhiannan bloodline; they do not (some say cannot) share its secrets with those who do not suffer from their line’s curse. All Lhiannan share a splinter of a dark, once-vast, and powerful forest spirit. Ogham allows them to tap into that spirit’s power, and into its communion with free spirits of its ilk.

Ogham is a limited form of blood magic; it is neither as flexible nor as powerful as Tremere Thaumaturgy, nor other Clans’ blood sorcery, but within the bounds set by the Lhiannan’s territorial nature it is quite powerful. Ogham is strongest within a Lhiannan’s home territory. More than 50 miles (80 km) from her home territory, the difficulty of using Ogham increases by one across the board, as the Lhiannan’s own spirit-shard comes into conflict with unfamiliar local spirit life.
"""
  ),
  Discipline(
    name='Auspex',
    sorcery=False,
    powers= [
      Power(
        name='Heightened Senses',
        discipline='auspex',
        level=1,
        description="""This power increases the acuity of all of the vampire’s senses, effectively doubling the clarity and range of sight, hearing, and smell. While her senses of taste and touch extend no farther than normal, they likewise become far more distinct; the vampire could taste the hint of liquor in a victim’s blood or feel the give of the board concealing a hollow space in the foor. The Kindred may magnify her senses at will, sustaining this heightened focus for as long as she desires. At the Storyteller’s option, this may make hunting easier. Occasionally, this talent provides extrasensory or even precognitive insights. These brief, unfocused glimpses may be odd premonitions, flashes of empathy, or eerie feelings of foreboding. The vampire has no control over these perceptions, but with practice can learn to interpret them with a fair degree of accuracy. Expanded senses come at a price, however. Bright lights, loud noises and strong smells present a hazard while the vampire uses this power. In addition to the possibility for distraction, an especially sudden or potent stimulus (like the glare of a spotlight or a clap of thunder) can blind or deafen the Kindred for an hour or more.
_System_: It takes a refexive action to activate this ability, but no roll or other cost is required. In certain circumstances, dice rolls associated with using the character’s sense (such as ^Perception + Alertness^) decrease in difficulty by a number equal to the character’s Auspex rating when the power is engaged. The Storyteller may also use this power to see if the character perceives a threat. In this case, the Storyteller privately rolls the character’s unmodified Auspex rating, applying whatever difficulty he feels best suits the circumstances. For example, sensing that a pistol is pointed at the back of the character’s head may require a roll of difficulty 5, while the sudden realization that a rival for Primogen is planning her assassination may require a 9. Note that even this “precognition” comes only as a result of interpreting details the Kindred is able to notice. It’s not an all-purpose insight or miraculous revelation. At the character’s discretion, she may selectively heighten one specific sense, rather than leaving them all on. In these cases, the difficulty to perceive stimuli using that sense drops by one, but the difficulty to avoid distraction or temporary bedazzlement increases by one. This power does not let characters see in pitch darkness, as does Eyes of the Beast (p.199), but it does reduce difficulty penalties to act in such darkness from +2 to +1, and the character may make ranged attacks in pitch darkness if she can hear, smell, or otherwise detect her foe."""
      ),
      Power(
        name='Aura Perception',
        discipline='auspex',
        level=2,
        description="""Using this power, the vampire can perceive the psychic “auras” that radiate from mortals and supernatural beings alike. These halos comprise a shifting series of colors that take practice to discern with clarity. Even the simplest individual has many shifting hues within his aura; strong emotions predominate, while momentary impressions or deep secrets flash through in streaks and swirls. The colors change in sympathy with the subject’s emotional state, blending into new tones in a constantly dancing pattern. The stronger the emotions involved, the more intense the hues become. A skilled vampire can learn much from her subject by reading the nuances of color and brilliance in the aura’s flow. Aside from perceiving emotional states, vampires use Aura Perception to detect supernatural beings. The colors in Kindred auras, while intense, are quite pale; mage halos often flare and crackle with arcane power; the race of shapeshifters has strikingly bright, almost frantic, auras; ghosts have weak auras that ficker fitfully like a dying flame; and faerie creatures’ radiance is shot through with capricious rainbow hues.
_System_: After the character stares at the subject for at least a few seconds, the player rolls ^Perception + Empathy^ (difficulty 8); each success indicates how much of the subject’s aura the character sees and understands (see the table below). A failure indicates that the play of colors and patterns yields no prevailing impression. A botch indicates a false or erroneous interpretation. The Storyteller may wish to make this roll, thus keeping the player in the dark as to the veracity of the character’s interpretation.
<table><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Can distinguish only the shade (pale or bright).</td></tr><tr><td>2 successes</td><td>Can distinguish the main color.</td></tr><tr><td>3 successes</td><td>Can recognize the color patterns.</td></tr><tr><td>4 successes</td><td>Can detect subtle shifts.</td></tr><tr><td>5 successes</td><td>Can identify mixtures of color and pattern.</td></tr></table>The Aura Colors chart offers some example ideas of common colors and the emotions they refect that Storytellers can use. Note that it is nearly impossible to determine with certainty if a particular character is lying or not with this power - vampires are inherently deceitful by nature, but even mortals might react with anxiety to questions while still being truthful. It is, however, helpful in determine the target’s emotional state, which might lead the vampire to decide that a particular target is suspicious. A character may choose to perform a very cursory aura scan of a large area like a nightclub’s dance floor or the audience in a gallery. In this case, the player decides which characteristic of auras she’s looking for, and that’s the only information she’s able to glean if the roll is successful. (At the Storyteller’s discretion, on this general scan roll, more successes on the roll may more quickly yield what the character seeks). For example, the player may specify, “Who’s the most nervous person in attendance?” or “Are there any vampirically pale auras among the CEO’s entourage?” Thereafter, the player may narrow down her scrutiny of a single individual, with an additional roll as normal. The character may focus in on a particular subject’s aura only once per scene with any degree of clarity. Any subsequent attempts that result in failure should be considered botches. It is very easy for the character to imagine seeing what she wants to see when judging someone’s intentions. After 24 hours, the character may try again at no penalty. It is possible, though difficult, to sense the aura of a being who is otherwise invisible to normal sight. Refer to “Seeing the Unseen”, p.142, for more information."""
      ),
      Power(
        name='The Spirit’s Touch',
        discipline='auspex',
        level=3,
        description="""When someone handles an object for any length of time, he leaves a psychic impression on the item. A vampire with this level of Auspex can “read” these sensations, learning who handled the object, when he last held it, and what was done with it recently (For these purposes, a corpse counts as an “object” and can be read accordingly). These visions are seldom clear and detailed, registering more like a kind of “psychic snapshot”. Still, the Kindred can learn much even from such a glimpse. Although most visions concern the last person to handle the item, a long-time owner leaves a stronger impression than someone who held the object briefy. Gleaning information from the spiritual residue requires the vampire to hold the object and enter a shallow trance. She is only marginally aware of her surroundings while using The Spirit’s Touch, but a loud noise or jarring physical sensation breaks the trance instantly.
_System_: The player rolls ^Perception + Empathy^. The difficulty is determined by the age of the impressions and the mental and spiritual strength of the person or event that left them. Sensing information from a pistol used for a murder hours ago may require a 4, while learning who owned a blood-stained puppet fashioned a century ago might be a 9. The greater the individual’s emotional connection to the object, the stronger the impression he leaves on it - and the more information the Kindred can glean from it. Events involving strong emotions (a gift-giving, a torture, a long family history) likewise leave stronger impressions than short or casual contact do. Assume that each success offers one piece of informa-tion, as per the chart below.
<table><tr><th>Successes</th><th>Information</th></tr><tr><td>Botch</td><td>The character is overwhelmed by psychic impressions for the next 30 minutes and unable to act.</td></tr><tr><td>Failure</td><td>No information of value.</td></tr><tr><td>1 success</td><td>Very basic information: the last owner’s gender or hair color, for instance.</td></tr><tr><td>2 successes</td><td>A second piece of basic information.</td></tr><tr><td>3 successes</td><td>More useful information about the last owner, such as age and state of mind the last time he used the item.</td></tr><tr><td>4 successes</td><td>The person’s name.</td></tr><tr><td>5+ successes</td><td>A wealth of information: nearly anything you want to know about the person’s relationship with that object is available.</td></tr></table>At the Storyteller’s discretion, some impressions on objects may be so strong - a knife plunged into Caesar’s breast, the tip of the Spear of Destiny, a fang pulled from the maw of Dracula - that any use of this power may be deemed a success."""
      ),
      Power(
        name='Telepathy',
        discipline='auspex',
        level=4,
        description="""The vampire projects a portion of her consciousness into a nearby mortal’s mind, creating a mental link through which she can communicate wordlessly or even read the target’s deepest thoughts. The Kindred “hears” in her own mind the thoughts plucked from a subject as if they were spoken to her. This is one of the most potent vampiric abilities, since, given time, a Kindred can learn virtually anything from a subject without him ever knowing. The Tremere and Tzimisce in particular find this power especially useful in gleaning secrets from others, or for directing their mortal followers with silent precision.
_System_: The player rolls ^Intelligence + Subterfuge^ (difficulty of the subject’s current Willpower points). Projecting thoughts into the target’s mind requires one success. The subject recognizes that the thoughts come from somewhere other than his own consciousness, though he cannot discern their actual origin without a successful Perception + Awareness roll (difficulty equalto the vampire’s ^Manipulation + Subterfuge^). To read minds, one success must be rolled for each item of information plucked or each layer of thought pierced. Deep secrets or buried memories are harder to obtain than surface emotions or unspoken comments, requiring five or more successes to access. Reading thoughts with Telepathy does not commonly work upon the undead mind. A character may expend a Willpower point to make the effort, making the roll normally afterward. Likewise, it is equally difficult to read the thoughts of other supernatural creatures. However, the character may project her thoughts without expending a Willpower point. These thoughts, however, are still obviously intrusions into the target’s mind, but the character may attempt to disguise her mental “voice” with a roll of ^Manipulation + Subterfuge^ (difficulty equals the target’s Perception + Awareness) so the target doesn’t recognize her as the “speaker”. Storytellers are encouraged to describe thoughts as flowing streams of impressions and images, rather than as a sequence of prose (powers such as Telepathic Communication are of more use for that). Instead of making flat statements like “He’s planning on killing his former lover’s new boyfriend”, say “You see a fleeting series of visions: A couple kissing passionately in a doorway, then the man walking alone at night; you suddenly see your hands, knuckles white, wrapped around a steering wheel, with a figure crossing the street ahead; your heart, mortal now and hammering with panic as you hear the engine rev wildly; and above all, a blazing anger coupled with emotional agony and a panicked fear of loss”. Such descriptions not only add to the story, but they also force the player to interpret for herself what her character gleans. After all, understanding minds - especially highly emotional or deranged minds - is a difficult and often puzzling task."""
      ),
      Power(
        name='Psychic Projection',
        discipline='auspex',
        level=5,
        description="""The Kindred with this awesome ability projects her senses out of her physical shell, stepping from her body as an entity of pure thought. The vampire’s astral form is immune to physical damage or fatigue, and can “fly” with blinding speed anywhere across the earth - or even underground - so long as she remains below the moon’s orbit.
The Kindred’s material form lies in a torpid state while her astral self is active, and the vampire isn’t aware of anything that befalls her body until she returns to it. An ephemeral silver cord connects the Kindred’s psyche to her body. If this cord is severed, her consciousness becomes stranded in the astral plane (the realm of ghosts, spirits and shades). Attempting to return to the vampire’s physical shell is a long and terrifying ordeal, especially since there is no guarantee that she will accomplish the journey successfully. This significant danger keeps many Kindred from leaving their bodies for long, but those who dare can learn much.
_System_: Journeying in astral form requires the player to expend a point of Willpower and make a ^Perception + Awareness^ roll. Difficulty varies depending on the distance and complexity of the intended trip; 5 is within sight, 7 is nearby or to a familiar location, and 9 reflects a trip far from familiar territory (a first journey from North America to the Far East; trying to shortcut through the earth). The greater the number of successes rolled, the more focused the character’s astral presence is and the easier it is for her to reach her desired destination.
Failure means the character is unable to separate her consciousness from her body, while a botch can have nasty consequences - flinging her astral form to a random destination on Earth or in the spirit realm, arriving in a place where the sun is active (necessitating a frenzy roll, although the sunlight doesn’t do any damage), or hurtling toward the desired destination so forcefully that the silver cord snaps.
The player may spend a point of Willpower to activate this power, and an additional point of Willpower to gain the success necessary to perform the jaunt. This is an exception to the normal rule where a player may not spend more than a single point of Willpower per turn.
Each scene in Psychic Projection requires another point of Willpower and a new roll. Failure indicates that the vampire has lost her way and must retrace the path of her silver cord. A botch at this stage means the cord snaps, stranding the character’s psychic form in the mysterious astral plane. An astral form may travel at great speeds (the Storyteller can use roughly 1000 miles per hour or 1500 kilometers per hour as a general guide) and carries no clothing or material objects of any kind. Some artifacts are said to exist in the spirit world, and the character can try to use one of these tools if she finds one. The character cannot bring such relics to the physical world when she returns to her body, however. Interaction with the physical world is impossible while using Psychic Projection. At best, the character may spend a Willpower point to manifest as a ghost-like shape. This apparition lasts one turn before fading away; while she can’t affect anything physically during this time, the character can speak. Despite lacking physical substance, an astral character can use Auspex normally. At the Storyteller’s discretion, such a character may employ some or all Animalism, Dementation, Dominate, Necromancy, Obtenebration, Presence, Thaumaturgy, and similar non-corporeal powers she has, though this typically requires a minimum of three successes on the initial Psychic Projection roll. If two astral shapes encounter one another, they interact as if they were solid. They may talk, touch,and even fight as if both were in the material world. Since they have no physical bodies, astral characters seeking to interact “physically” substitute Mental and Social Traits for Physical ones (Wits replaces Dexterity, Manipulation supplants Strength, and Intelligence replaces Stamina). Due to the lack of a material form, the only real way to damage another psychic entity is to cut its silver cord. When fighting this way, consider Willpower points to be health levels; when a combatant loses all of her Willpower, the cord is severed. Although an astrally projected character remains in the reflection of the mortal world, she may venture further into the spirit realms, especially if she becomes lost. Other beings with particular sensitivity to psychic activity, such as ghosts, werewolves, and even some magi, travel the astral plane as well, and can interact with a vampire’s psychic presence normally (although the astrally projected character is not considered a “ghost” for powers such as Necromancy). The observing character notices the astrally projecting vampire with a Perception + Awareness roll (difficulty 8), requiring more successes than the Psychic Projection activation roll. Even those who do notice you won’t be able to identify you; you are merely an immaterial shade hovering in the general area. Storytellers are encouraged to make trips into the spirit world as bizarre, mysterious and dream-like as possible. The world beyond is a vivid and fantastic place, where the true nature of things is stronger and often strikingly different from their earthly appearances."""
      ),
      Power(
        name='Clairvoyance',
        discipline='auspex',
        level=6,
        description="""By using Clairvoyance, a vampire can perceive distant events without using Psychic Projection. By concentrating on a familiar person, place, or object, a character can observe the subject’s immediate vicinity while staying aware of her own surroundings.
_System_: The player rolls ^Perception + Empathy^ (difficulty 6) and describes the target she’s trying to look in on. If the roll is successful, the character can then perceive the events and environment surrounding the desired target for one turn per success. Other Auspex powers may be used on the scene being viewed; these are rolled normally. Clairvoyance does split the vampire’s perceptions between what she is viewing at a distance and what is taking place around her. As a result, while using this power, a character is at +3 difficulty on all rolls relating to actions that affect her physical surroundings."""
      ),
      Power(
        name='Prediction',
        discipline='auspex',
        level=6,
        description="""Some people are capable of finishing their friends’ sentences. Elder vampires with Prediction sometimes begin their friends’ sentences. Prediction is a constant low-level telepathic scan of the minds of everyone the character is in proximity to. While this power does not give the vampire the details of his neighbors’ conscious thoughts, it does provide a wealth of cues as to the subjects’ moods, suppressed refexes, and attitudes toward the topic of conversation.
_System_: Whenever the character is in conversation and either participant in the discussion makes a Social roll, the player may pre-empt the roll to spend a blood point and make a ^Perception + Empathy^ roll (difficulty of the target’s Manipulation + Subterfuge). Each success is an additional die that can be applied to the player’s Social roll or subtracted from the dice pool of the Social roll being made against the character."""
      ),
      Power(
        name='Telepathic Communication',
        discipline='auspex',
        level=6,
        description="""Telepathy (p.137) allows a character to pick up only the surface thoughts of other individuals, and to speak to one at a time. With Telepathic Communication, a character can form a more powerful link between his mind and that of other subjects, allowing them to converse in words, concepts, and sensory images at the speed of thought (and without the need for Willpower expenditure, unlike with Telepathy). Vampires with this level of Auspex can act as “switchboard operators”, creating a telepathic web that allows all participants to share thoughts with some or all other members of the network as they choose.
_System_: The player rolls ^Charisma + Empathy^ (difficulty equals the target’s current Willpower points) to establish contact, although a willing subject may allow the vampire access and thus obviate the need for a roll. The maximum range at which a subject may be contacted and the maximum number of individuals who may be linked simultaneously with this power depends on the Auspex rating of the vampire who initiates contact.
<table><tr><th>Auspex Rating</th><th>No. of Targets</th><th>Approximate Range</th></tr><tr><td>Auspex 6</td><td>3 subjects</td><td>500 miles/800 kilometers</td></tr><tr><td>Auspex 7</td><td>Perception rating</td><td>1000 miles/1500 kilometers</td></tr><tr><td>Auspex 8</td><td>^Perception + Empathy^</td><td>500 miles/800 kilometers per point of Intelligence</td></tr><tr><td>Auspex 9</td><td>2x (^Perception + Empathy^)</td><td>1000 miles/1500 kilometers per point of Intelligence</td></tr></table>"""
      ),
      Power(
        name='Karmic Sight',
        discipline='auspex',
        level=7,
        description="""The power of Aura Perception (Auspex 2) allows a vampire to take a brief glimpse at the soul of a subject. This power takes Aura Perception several steps forward, allowing a vampire who has mastered Auspex2 to probe the inner workings of a subject’s mind and soul.
_System_: The player rolls ^Perception + Empathy^ (difficulty equals the subject’s current Willpower). The degree of success determines the information gained.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>Botch</td><td>The character gains a Derangement or Psychological/Mental/Supernatural Flaw similar to one of the target’s for one night, at Storyteller discretion.</td></tr><tr><td>1 success</td><td>As per five successes on an Aura Perception roll.</td></tr><tr><td>2 successes</td><td>Subject’s Nature, Demeanor and Humanity or Path can be determined.</td></tr><tr><td>3 successes</td><td>Any outside infuences on the subject’s mind or soul, such as Dominate or a demonic pact, can be detected.</td></tr><tr><td>4 successes</td><td>Subject’s Willpower, Humanity or Path, and Virtue ratings can be determined.</td></tr><tr><td>5 successes</td><td>The state of the subject’s karma may be determined. This is a highly abstract piece of information best left to Storyteller discretion, but should reveal the general balance between “good” and “bad” actions the subject has performed, both recently and over the course of his existence. If the plot merits it, the character may receive visions of one or more incidents in the subject’s past that radically altered his destiny. With this degree of success, some fate-related Merits and Flaws (e.g. Dark Fate) can be identified as well.</td></tr></table>"""
      ),
      Power(
        name='Mirror Reflex',
        discipline='auspex',
        level=7,
        description="""This power was developed by a Toreador elder who made a fearsome reputation through her fencing prowess, acting as a hired champion in dozens of Ventrue duels. Mirror Reflex is similar to Prediction in that it is in essence a low-level telepathic scan of an opponent, but this power taps into physical (rather than social) reflexes, allowing the character to anticipate an enemy’s moves in personal combat.
_System_: The player spends a blood point and rolls Perception + the combat skill the opponent is using (difficulty of the subject’s Manipulation + combat skill in use). Each success is an additional die that can be applied to the character’s dice pools during the next turn of combat for any actions taken against the scanned opponent. The use of Mirror Reflex does take one combat action, and the power has a maximum range in yards or meters equal to the character’s Willpower rating."""
      ),
      Power(
        name='Psychic Assault',
        discipline='auspex',
        level=8,
        description="""Psychic Assault is nothing less than a direct mind-to-mind attack which uses the sheer force of an elder’s will to overpower his target. Victims of Psychic Assault show little outward sign of the attack, save for nose-bleeds and expressions of intense agony; all injuries by means of this psychic pressure inflicted are internal. A medical examination of a mortal victim of a Psychic Assault invariably shows the cause of death to be a heart attack or aneurysm, while vampires killed with this power decay to dust instantly, regardless of age.
_System_: The character must touch or make eye contact with his target. The player spends three blood points (and a Willpower point, if assaulting a vampire or other supernatural being) and rolls ^Manipulation + Intimidation^ in a contested roll against the victim’s Willpower. The result depends on the number of net successes the attacker rolls.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>Botch</td><td>The target becomes immune to the attacker’s Psychic Assault for one night per each “1” rolled.</td></tr><tr><td>Failure</td><td>The target is unharmed and may determine that a psychic assault is taking place by succeeding on a Perception + Awareness roll (difficulty 6).</td></tr><tr><td>1 success</td><td>The target is shaken but unharmed. He loses a temporary Willpower point.</td></tr><tr><td>2 successes</td><td>The target is badly frightened. He loses three temporary Willpower points and, if a vampire, must roll Courage (difficulty of the attacker’s Auspex rating) to avoid Rötschreck.</td></tr><tr><td>3 successes</td><td>The target loses six temporary Willpower points and, if a vampire, must roll Courage as above. If this causes him to lose his last temporary Willpower point, he loses a permanent Willpower point and receives three health levels of bashing damage (soaked normally).</td></tr><tr><td>4 successes</td><td>The target loses all temporary Willpower points and half of his permanent Willpower points (round down) and suffers three health levels of lethal damage (soaked normally).</td></tr><tr><td>5 successes</td><td>The target must roll his permanent Willpower (difficulty 7). If he succeeds, apply the effect of four successes, and is also rendered unconscious for the rest of the night. If he fails, the Psychic Assault kills him instantly.</td></tr></table>"""
      ),
      Power(
        name='False Slumber',
        discipline='auspex',
        level=9,
        description="""Possibly the source of many Malkavians’ conviction that their sire is alive and well on the astral plane, this power allows a Methuselah’s spirit to leave his body while in torpor. While seemingly asleep, the vampire is able to project astrally, think, and perceive events normally.
_System_: No roll is needed. This power is considered to be active whenever the vampire’s body is in torpor, and astral travels are handled as per the rules for Psychic Projection. The vampire is not able to awaken physically at will, however - waking from torpor is handled per the normal rules for such an action (see p.283).
A vampire with this power whose silver cord is severed in astral combat loses all Willpower points, as per the rules for astral combat under Psychic Projection, but is not killed. Instead, he loses the use of this Auspex power and half of his permanent Willpower points. Both the Auspex 9 power and the Willpower must be bought back with experience points. The vampire’s soul slowly returns to his body over the course of a year and a day, during which time he may not be awakened from torpor by any means."""
      )
    ],
    description="""
Auspex gives the vampire uncanny sensory abilities. She starts with the capacity to heighten her natural senses significantly, but as she grows in power, she can perceive psychic auras and read the thoughts of another being. Auspex can also pierce through mental illusions such as those created by Obfuscate - see the sidebar “Seeing the Unseen” on p. 142 for more.

However, a vampire with Auspex needs to be careful. Her increased sensory sensitivity can cause her to be drawn in by beautiful things or stunned by loud noises or pungent smells. Sudden or dynamic events can disorient an Auspex-using character unless her player makes a Willpower roll to block them out (difficulty of at least 4, although the more potent the source of distraction, the higher the difficulty). Failure overwhelms the character’s senses, making her oblivious to her surroundings for a turn or two. While the Malkavians and Toreador are more prone to these kinds of distractions, the Tremere and Tzimisce aren’t immune.

Dots in Perception are very useful for using Auspex powers, as more successes help the character gain more sensory information.
"""
  ),
  Discipline(
    name='Spiritus',
    sorcery=False,
    powers= [
      Power(
        name='Aid from Spirits',
        discipline='spiritus',
        level=1,
        description="""Spirits are everywhere, but invisible to most living (and unliving) beings. This power allows the vampire to briefy rouse the spirit of an object, making that object perform its intended function better and more efficiently. It in no way makes the spirit well-disposed toward the vampire - not that this usually matters to the Ahrimane.
_System_: The character touches the object, and the player spends a blood point and rolls ^Manipulation + Occult^ (difficulty 6). If the roll succeeds, the player receives a bonus to her dice pool using that item, equal to the number of successes rolled. For example, if the character uses this power on a gun and the player rolls three successes, she then receives a +3 to her next Firearms roll made with that gun. Unused bonuses fade at the end of the scene, and multiple uses of this power do not combine (the most recent use trumps any previous uses). The character can, however, use the power on multiple objects she uses in the same scene, so long as she has the blood for it."""
      ),
      Power(
        name='Summon Spirit Beasts',
        discipline='spiritus',
        level=2,
        description="""The vampire might not fully understand the link between “animal” and “animal-spirit”, but spirits of aggressive animals are usually more than willing to take on a physical body and fight for the vampire. Spirits of curious animals, meanwhile, seem to enjoy unlocking doors or following people. With this power, the Ahrimane can summon up the spirit of an animal indigenous to the area and send it to do what comes naturally. The spirit assumes the corporeal form of the appropriate animal, and is capable of whatever the animal would normally be able to do. The animal can follow simple telepathic commands, and is slightly more intelligent than a normal animal would be (but still not as intelligent as a person).
_System_: The animal summoned must be native to the area - just because the local zoo hosts a tiger doesn’t mean there are tiger-spirits running about. The player must spend one blood point and roll ^Charisma + Animal Ken^ (difficulty 7). The number of successes indicates how long the spirit remains material. The spirits have the same number of health levels their physical counterparts would normally have (see p.388 for some sample animals’ traits). If they are reduced to Incapacitated, they discorporate.
<table><tr><th>Successes</th><th>Duration</th></tr><tr><td>1 Success</td><td>One Turn</td></tr><tr><td>2 Successes</td><td>Five Turns</td></tr><tr><td>3 Successes</td><td>One Hour</td></tr><tr><td>4 Successes</td><td>One Night</td></tr><tr><td>5 Successes</td><td>One Week</td></tr></table>"""
      ),
      Power(
        name='Aspect of the Beast',
        discipline='spiritus',
        level=3,
        description="""Instead of calling up animal spirits, the vampire learns to emulate aspects of those spirits herself. In this way, she can become faster, stronger, tougher, or gain the special powers of nearly any animals, provided that the spirit is local to the area.
_System_: The player spends a blood point and rolls ^Manipulation + Occult^ (difficulty 7). The power lasts for one turn per success, unless otherwise noted. Some examples of aspects are given below, though the player and Storyteller are welcome to make up others:
_Beaver’s Bite_ - This makes the Ahrimane’s bite strong and sharp enough to cut through almost any substance (though it does no additional damage to living or unliving targets).
_Chameleon’s Colors_ - The Ahrimane becomes capable of changing color to suit the environment (-2 difficulties to all Stealth rolls involving hiding).
_Ears of the Hare_ - The Ahrimane can hear as well as a rabbit, reducing the difficulty of Perception rolls involving hearing by two.
_Falcon’s Eye_ - The Ahrimane can see great distances as if she had the eyes of a falcon (-3 to all Perception rolls involving vision).
_Ferocity of the Cougar_ - All Courage rolls are made at -2 difficulty.
_Leapfrog_ - This grants the Ahrimane the ability to leap three times the normal height and distance. (See p.260 for jumping rules).
_Nose of the Hound_ - The Ahrimane’s sense of smell is far greater than that of a mortal. She can even track by scent on a ^Perception + Survival^ roll (difficulty set by Storyteller).
_Serpent’s Venom_ - The Ahrimane’s bite transmits a venomous toxin that causes two health levels of damage in living victims per turn (see “Poisons and Drugs”, p.301). The damage continues until the toxin is removed or nullified, or until the Ahrimane’s spirit power ends.
_Sound of the Cricket_ - This grants the power to produce an annoying, grating sound loud enough to deafen those nearby. The target suffers a +4 to all Perception rolls related to hearing for the next scene unless he succeeds on a Willpower roll (difficulty 7).
_Squirrel’s Balance_ - The Ahrimane can move about in the branches and limbs of trees or across tightropes with little fear of falling. All such Athletics rolls have their difficulties decreased by two.
_Strength of the Bear_ - This gives the Ahrimane two extra dots of Strength.
_Swiftness of the Stag_ - The Ahrimane can move at twice her normal running speed."""
      ),
      Power(
        name='Engling Fury',
        discipline='spiritus',
        level=4,
        description="""Spirits abound - supposedly everything, from one’s shirt to the very air, has one. The Ahrimane can take those spirits into herself, break them down, and refresh her own mental reserves. This destroys the spirit, but no repercussions have been reported.
_System_: The player rolls ^Manipulation + Intimidation^ (difficulty 8). Every success allows her to regain a point of Willpower, but each use of this power destroys another spirit."""
      ),
      Power(
        name='The Wild Beast',
        discipline='spiritus',
        level=5,
        description="""The Ahrimane grows leaner, lithe, and strong. She hunches over slightly, her eyes become slitted and cat-like, and she grows vicious claws on her hands. Her features become slightly feline, and in this form she is an even more formidable predator than usual. Animals react with fear to the Wild Beast, and mortals see her as a monster - if they see her at all.
_System_: The change does not require a roll, but the player must spend two blood points. The change raises the vampire’s Strength by three, and Dexterity and Stamina each by two. Appearance falls to 0 and Manipulation is reduced by three. The vampire’s fangs inflict an extra die of damage, and she grows claws that inflict aggravated damage. The character can see in the dark, and all difficulties involving scent, hearing, and vision fall by two. The character can retain the Wild Beast form for a number of hours every night equal to her Willpower rating."""
      )
    ],
    description="""
The Discipline of Spiritus opens the vampire up to worlds and vistas - and methods of feeding - that most Kindred can never touch. Vampires are spiritually dead, unable to create life. The shamanic ritual that created the Ahrimanes, though, allowed a spiritual connection between the undead and the vast, living world all around them. While the vampire can barely scratch the surface of what living shamans can accomplish, the Discipline of Spiritus is still formidable.
"""
  ),
  Discipline(
    name='Daimoinon',
    sorcery=False,
    powers= [
      Power(
        name='Sense the Sin',
        discipline='daimoinon',
        level=1,
        description="""A real mark always convinces himself. The most dangerous Baali aren’t the ones that use extortion, threats, or overt displays of power; the most dangerous Demons simply know how to talk their victims into cutting their own throats. This power allows the Baali to find a target’s particular vice.
_System_: The player rolls ^Perception + Empathy^ against living or undead beings; the difficulty is equal to the subject’s Self-Control or Instincts +4. If successful, the Baali can sense the subject’s greatest weakness. The significance of this information is dictated by the degree of success: One success might determine a low Virtue, weak Willpower, or a poorly defended avenue of approach, while two might yield a closely guarded secret or conversational misstep. Three or more yields a central derangement or formative trauma from the subject’s past."""
      ),
      Power(
        name='Fear of the Void Below',
        discipline='daimoinon',
        level=2,
        description="""Once the Baali has mastered reading a subject’s darkest secrets, he can reach into the victim’s mind and twist what he finds there. The shock of feeling one’s most deeply held beliefs and darkest fears manipulated can send the victim into catatonia or fits of panic.
_System_: The Baali must first employ Sense the Sin (above) or use some other method to discern the tragic flaw of the target. She must then speak to the target, playing upon his inadequacies and the inescapable consequences of his shortcomings. A successful ^Wits + Intimidation^ roll (difficulty of the subject’s Courage + 4) drives the victim into fits of terror (one success), mindless panic-borne flight similar to Rötschreck (two successes), or even unconsciousness (three or more successes). All effects last for the remainder of the scene. Kindred targets may resist with a Courage roll (difficulty equal to the Baali’s ^Willpower^) - they are accustomed to dealing with their Beasts. If the Kindred target garners more successes than the Baali did on her original roll, he resists the power completely."""
      ),
      Power(
        name='Conflagration',
        discipline='daimoinon',
        level=3,
        description="""Not all of the Baali’s powers are designed for manipulation and subtlety. The Demons can also call up the fire from the realms of their infernal patrons, hurling it at their enemies in exultation of the Outer Dark. This fire spreads and burns normally, but at the moment of creation it is black and cold, as though drawn from a place where terrestrial physics do not apply.
_System_: The player spends a blood point. This creates a bolt of black flame that inflicts one die of aggravated damage; more blood points may be spent to increase the size and damage of the flame. Such fires are fleeting and dissipate at the end of the turn, unless the Baali continues to spend blood points on Conflagration over several turns, gradually creating a larger flame. The player also rolls ^Dexterity + Occult^ (difficulty 6) to hit his target, who may dodge as normal. Vampires confronted with this black fire make Rötschreck tests as if confronted with a similar quantity of normal flame."""
      ),
      Power(
        name='Psychomachia',
        discipline='daimoinon',
        level=4,
        description="""With this power, the Baali combines his ability to read the psyche of a victim with the ability to summon up matter from the Outer Dark. Psychomachia pits a victim against the most dangerous, shameful parts of her own subconscious.
_System_: The vampire, after learning the targets tragic flaw (such as after using Sense the Sin, above), forces the subject’s player to roll her lowest Virtue (difficulty 6). Failing this roll pits the target against an apparition summoned from her darker self, perceptible to the subject only. The target may see or feel his abusive father, a long-dead lover, a childhood bogeyman, or (for Kindred victims) even the Beast itself. A botch indicates the target has been overwhelmed and frenzies - or, worse, becomes possessed by his inner demons. This imaginary antagonist may be wholly narrated, or assigned Traits equivalent or slightly inferior to the victim’s, at the Storyteller’s option. All injuries sustained by the target in such an encounter are illusory (substitute catatonia or torpor for death as appropriate) and vanish upon the phantasm’s defeat or the Baali’s loss of concentration."""
      ),
      Power(
        name='Condemnation',
        discipline='daimoinon',
        level=5,
        description="""The Baali levies a curse upon the victim. The more skillful in her dark studies the Baali has become, the more dire the curse is likely to be. Legend states that some Baali can wield curses so foul that the victims attempt suicide after a single night - only to find that they can no longer die.
_System_: An ^Intelligence + Occult^ roll (difficulty equal to the subject’s Willpower) dictates the length and severity of the curse. Successes must be split between both these effects, as per the sidebar below. The player must split successes between effect and duration - curses with zero successes allotted to duration last for one night. For example, if the Baali’s player rolls four successes, she can inflict a two-success curse for one month, a three-success curse for up to week, or a four-success curse for one night. At any time, the Baali may choose to end the curse. Storytellers should feel free to invent creative or story-appropriate curses.
<table><tr><th>Successes</th><th>Duration</th><th>Example</th></tr><tr><td>1 success</td><td>Up to one week</td><td>“No voice shall be lent your lying tongue” - All Subterfuge rolls suffer a +3 difficulty.</td></tr><tr><td>2 successes</td><td>One month</td><td>“Sicken and wither, infidel... a babe’s weakness upon you” - All Strength rolls suffer a +2 difficulty, or vampire cannot use blood to boost Strength.</td></tr><tr><td>3 successes</td><td>One year</td><td>“Reap this bitter harvest - may your closest friends turn foe” - The character’s friends do not trust him. This can have any number of mechanical effects (higher difficulty on Social rolls, friends might be more prone to frenzy around the character) at the Storyteller’s discretion.</td></tr><tr><td>4 successes</td><td>Ten years</td><td>“Barren be thy seed and the loins of all your line” - The character becomes sterile or barren, or (if Kindred) cannot Embrace childer or create ghouls.</td></tr><tr><td>5 successes</td><td>Permanent</td><td>“The mark of doom - all you touch must fail” - Simple failures are considered botches while the curse is in effect.</td></tr></table>"""
      ),
      Power(
        name='Concordance',
        discipline='daimoinon',
        level=6,
        description="""The Baali makes a Devil’s bargain and takes the unholy nature of his masters into his own being. This warps his body both to his detriment and benefit. A truly dedicated Demon might make numerous such pacts, growing more grotesque and more powerful each time.
_System_: The most typical manifestation of this power incorporates immunity to the damaging effects of fire, though other equivalently-powered assets may be available at the Storyteller’s option. Most of these tributes take the form of left-handed “gifts” with unforeseen consequences (a tell-tale bronze tint to flame-resistant flesh, a vestigial set of wings, visible talons or horns that cannot be concealed, etc.). This Discipline may be purchased more than once at greater cost to body and soul. (The current shaitan is said to have been so gnarled and twisted by the Masters as to be no longer even remotely mistakable for human). Note that three of the banes particular to the Baali - piety, vulnerability to sunlight, and dependency on blood for sustenance - may not be overcome by this Discipline under any circumstances. In the end, it is up to the Storyteller’s discretion what the Baali can or cannot withstand."""
      ),
      Power(
        name='Summon the Herald of Topheth',
        discipline='daimoinon',
        level=7,
        description="""Using the same skill that allows for calling up demon-fire, the Baali can call a minion of his masters to Earth. Although the names assigned them differ (angel, demon, daeva, djinn, efreet, malakim, shedim, and countless others), the end results are the same. This being is under the Baali’s control, at least for a short time after being summoned. Yet scholars who have studied the blasphemous rite by which this Discipline is enacted note that no provision is made for banishing the Herald.
_System_: To summon a Herald of Topheth, the Demon must spend at least three blood points and perform an infernal ceremony. Heralds of Topheth have the following stats: Attributes 10/7/3, Abilities (15 points worth), Willpower 8, Disciplines (10 points worth), Fortitude of at least 3, and the capacity to heal one health level at least every other round. Storytellers should feel free to alter these guidelines based on the power level of the troupe and the form the Herald takes. Though most celestial beings chafe at the notion of wearing a single shape, many adopt those common to myth and legend; preternatural succubi or angels, reptilian horrors, and bat-winged monsters are among the most often seen."""
      ),
      Power(
        name='Contagion',
        discipline='daimoinon',
        level=8,
        description="""The most damaging disease is human sin. Pandora learned it to her detriment, as did the ungrateful and impolite denizens of Sodom. The Baali, of course, revel in the slow decay of human settlements, and Methuselahs of the bloodline learn to infect a mortal community with jealousy, slander, hate, and bigotry. Crime and violence soar, petty angers give rise to seething hatreds, and local economies take a downward spiral. Marriages end over trivial quarrels and the world becomes a nastier place in general. In the history of the Baali, entire towns and villages have been temporarily enslaved to an infernal master’s will.
_System_: Successes garnered on an ^Intelligence + Occult^ roll (difficulty 9) must be divided between the intensity and the area of the desired effect - at least two successes are needed to cover both area and effect. Sufficiently high degrees of Auspex or powers that detect demons may be able to pick up on this vague, malevolent aura; otherwise they will simply assume that times have taken a dire change for the worse.
<table><tr><th>Successes</th><th>Area</th><th>Effect</th></tr><tr><td>1 success</td><td>Immediate vicinity</td><td>Ill-tempered/out-of-sorts behavior</td></tr><tr><td>2 successes</td><td>An office complex</td><td>Civil/domestic unrest, prejudice</td></tr><tr><td>3 successes</td><td>A city block</td><td>Angry (even riotous) dissent</td></tr><tr><td>4 successes</td><td>A stadium or apartment complex</td><td>Bar-brawls, hate crimes, blood in the streets</td></tr><tr><td>5+ successes</td><td>An entire city</td><td>A throng of bloodthirsty single-minded Philistines</td></tr></table>"""
      ),
      Power(
        name='Call the Great Beast',
        discipline='daimoinon',
        level=9,
        description="""This Discipline is largely theoretical. Baali have, in the past, boasted that their most powerful elders know a ritual that can tear a rift to the Outer Dark and allow the creatures that dwell there into our world. Occasionally, a vampire destroys a Baali and sees the beginnings of such a ritual carved on a wall or tattooed onto a minion’s flesh. But even among the Kindred who know of the Baali and what they are capable of, the ability to Call the Great Beast doesn’t meet with much credence. This isn’t because the Kindred don’t think it’s possible, but because they realize that if a Demon ever succeeded in using it, there wouldn’t be much to be done anyway.
_System_: The preparatory ritual requires a tremendous investment of time and sacrifice; veiled allusions such as “fivescore souls, plucked clean and whole” and “when three times sets the hooded sun” indicate a selective sacrificial rite spanning days, nights, and dozens of victims (Deviation or imperfection in this litany may well have unforeseen consequences, ranging from simple failure to unwelcome demonic attention). At this point, the high priest expends all of his permanent Willpower and releases his consciousness in a desperate attempt to breach the gulf Beyond, becoming an empty vessel for whatever will most effectively end the world as your chronicle knows it. You’re the Storyteller - what would the Devil do to your world? (Call the Great Beast has two main functions in the chronicle. It’s either a plot device that the characters must work to prevent, or a means to change the world of Vampire into a demon-infested apocalypse. Either is useful, but it’s not the sort of power that a vampire just pulls out casually)."""
      )
    ],
    description="""
These are the mysteries of the Baali, black arts torn whole and beating from the sorcerer-kings of ancient cultures and prehistoric civilizations, incoherent memories passed from tome to tongue, hearkening to times of oblivion. They are sibilant secrets in which all begins to end and begin again. With every new night and novice brought into the circle, the telling grows shorter.
"""
  ),
  Discipline(
    name='Serpentis',
    sorcery=False,
    powers= [
      Power(
        name='The Eyes of the Serpent',
        discipline='serpentis',
        level=1,
        description="""This power grants the vampire the legendary hypnotic gaze of the serpent. The Kindred’s eyes become gold with large black irises, and mortals in the character’s vicinity find themselves strangely attracted to him. A mortal who meets the vampire’s beguiling gaze is immobilized. Until the character takes his eyes off his victim, the person is frozen in place.
_System_:  No roll is required, but this power can be avoided if the mortal takes care not to look into the vampire’s eyes. Vampires and other supernatural creatures can also be affected by this power if the Cainite’s player succeeds on a ^Willpower^ roll (difficulty 9). If attacked or otherwise harmed, supernatural creatures can spend a point of Willpower to break the spell.
Note: This is different than normal eye contact detailed on p.152. The target must be able to see the vampire’s eyes for Eyes of the Serpent to work."""
      ),
      Power(
        name='The Tongue of the Asp',
        discipline='serpentis',
        level=2,
        description="""The vampire may lengthen her tongue at will, splitting it into a fork like that of a serpent. The tongue may reach 18 inches or half a meter, and makes a terrifyingly effective weapon in close combat.
_System_: The lash of the tongue’s razor fork causes aggravated wounds (difficulty 6, Strength damage). If the Kindred wounds her enemy, she may drink blood from the target on the next turn as though she had sunk her fangs into the victim’s neck. Horrifying though it is, the tongue’s caress is very like the Kiss, and strikes mortal victims helpless with fear and ecstasy. Additionally, the tongue is highly sensitive to vibrations, enabling the vampire to function effectively in the darkness the Clan prefers. By flicking his tongue in and out of his mouth, the vampire can halve any penalties relating to darkness (p.274)."""
      ),
      Power(
        name='The Skin of the Adder',
        discipline='serpentis',
        level=3,
        description="""By calling upon her Blood, the vampire may transform her skin into a mottled, scaly hide. A vampire in this form becomes more supple and fexible.
_System_: The vampire spends one blood point and one Willpower point. Her skin becomes scaly and mottled; this, combined with the character’s increased flexibility, reduces soak difficulties to 5. The vampire may use her Stamina to soak aggravated damage from claws and fangs, but not from fire, sunlight, or other supernatural energies. The vampire’s mouth widens and fangs lengthen, enabling her bite to inflict an extra die of damage. Finally, the vampire may slip through any opening wide enough to fit her head through. The vampire’s Appearance drops to 1, and she is obviously inhuman if observed with any degree of care, though casual passers-by might not notice, if the vampire is in darkness or wearing heavy clothing."""
      ),
      Power(
        name='The Form of the Cobra',
        discipline='serpentis',
        level=4,
        description="""The Cainite may change his form into that of a huge black cobra. The serpent weighs as much as the vampire’s human form, stretches over 10 feet or three meters long, and is about 20 inches (50 cm) around. The Form of the Cobra grants several advantages, including a venomous bite, the ability to slither through small spaces, and a greatly enhanced sense of smell. The character may use any Disciplines while in this form save those that require hands (such as Feral Claws).
_System_: The vampire spends one blood point; the change is automatic, but takes three turns. Clothing and small personal possessions transform with the vampire. The vampire remains in serpent form until the next dawn, unless he desires to change back sooner. The Storyteller may allow the Setite bonus dice on all Perception rolls related to smell, but the difficulties for all hearing rolls are increased by two. The cobra’s bite inflicts damage equal to the vampire’s, but the vampire does not need to grapple his victim; furthermore, the poison delivered is fatal to mortals."""
      ),
      Power(
        name='The Heart of Darkness',
        discipline='serpentis',
        level=5,
        description="""A Kindred with mastery of Serpentis may pull her heart from her body. She can even use this ability on other Cainites, although this requires several hours of gruesome surgery. This power can only be invoked during a new moon. If performed under any other moon, the rite fails. Upon removing her heart, the vampire places it in a small clay urn, and then carefully hides or buries the urn. While her heart is hidden, she cannot be staked by any wood that pierces her breast. Moreover, because the heart is the seat of emotion, the difficulties of all her rolls to resist frenzy are two lower while this power is in effect. Cainites are careful to keep their hearts safe from danger. If someone seizes her heart, the vampire is completely at that person’s mercy. The heart can be destroyed only by casting it into a fire or exposing it to sunlight. If this happens, the Kindred dies where she stands, boiling away into a blistering heap of ash and blackened bone. Plunging a wooden stake into an exposed heart drives the vampire into instant torpor. A vampire may carry her heart with her, or have several false hearts buried in different places. A smart Kindred often avoids her heart’s hiding place, to deter discovery. Those wise in Setite lore whisper that the corrupt elders of the Clan often hold their underlings’ hearts as yet another method of control.
_System_: This power requires no roll. Those who witness a vampire pull his heart from his breast (or cut the heart from another vampire) must make Courage rolls. Failure indicates anything from strong uneasiness to complete revulsion, possibly even Rötschreck."""
      ),
      Power(
        name='Cobra Fangs',
        discipline='serpentis',
        level=6,
        description="""A character using Form of the Cobra gains a venomous bite along with his serpentine form. Unfortunately, huge black cobras tend to make people run away as fast as they can. This Serpentis power enables a vampire to gain the deadly bite without the full-body transformation, making it more useful for taking victims by surprise. The police do ask questions when someone dies from a cobra bite under unlikely circumstances, so Cobra Fangs still requires some discretion in its use.
_System_: The Kindred expends one blood point, and in one turn his fangs become hollow, more slender and venomous. The vampire injects venom when he bites. He must still grapple with the victim to deliver a bite attack, and the bite does the usual amount of damage; the venom, however, kills mortals within one minute. Bitten vampires or other supernaturally resilient creatures suffer (10 - victim’s Stamina and Fortitude) levels of aggravated damage over the course of five minutes."""
      ),
      Power(
        name='Divine Image',
        discipline='serpentis',
        level=7,
        description="""Many of the low Generation Setite elders no longer need the illusions of Obfuscate to appear as a god. Through this Serpentis power, a vampire can physically metamorphose into the form of a god. Male Kindred generally take the form of Set himself: a muscular man with the head of the “Typhonic Beast”, an animal with a long, narrow snout and upstanding, square-topped ears. Less often, they take the form of the crocodile-headed god Sobek, whom the Egyptians often linked to Set, or the wolf-headed war-god Wepwawet, often identified with Set’s son Anubis. Female vampires generally assume the form of the cobra-headed goddess Renenet, wife of Sobek, or the hippopotamus-goddess Taweret, sometimes considered a consort of Set. Both were goddesses of pregnancy and childbirth. Setite doctrine labels all four deities as Set’s eldest childer. While assuming the Divine Image, the vampire becomes stronger, tougher, and more impressive. More importantly, perhaps, the vampire’s will becomes more powerful as he identifies with a divine forebear.
_System_: The character expends three blood points and transforms into the Divine Image in one turn. In the Divine Image, the vampire gains two dots each of Strength and Stamina and a dot each of Charisma and Manipulation, but her Appearance drops to 1. These enhancements can push the vampire over his generational limit. The character also gains two full dots of Willpower (to a maximum of 10). The Cainite can stay in the Divine Image for a full scene. A vampire has only one Divine Image form (unless the player buys this power twice). The character does not know what Divine Image he will manifest until he invokes the power the first time, although the player can freely choose the preferred form."""
      ),
      Power(
        name='Heart Thief',
        discipline='serpentis',
        level=8,
        description="""The Serpentis power Heart of Darkness normally takes hours to perform upon other vampires, and only works at the dark of the moon. Some elders, however, can pull the heart from another vampire’s chest with a quick snatch. This does not destroy the victim, unless the attacker then destroys the stolen heart. Heart Thief is not an easy power to use despite its speed, but few Discipline effects can place one vampire in another’s power so suddenly and completely.
_System_: The character must expend one Willpower point. Removing the heart of a reluctant vampire is a difficult feat, comparable to staking: the attacker must garner at least three successes on a ^Dexterity + Brawl^ attack (difficulty 9). The victim may use Fortitude to “soak” the attacker’s successes, but mundane Stamina has no effect against this magical attack. A vampire who loses his heart this way takes one unsoakable level of aggravated damage, and receives all the benefits and drawbacks of the Heart of Darkness power. Resisting frenzy becomes easier (-2 difficulty) and he cannot be staked by wood that impales his breast. On the other hand, thrusting a stake through the removed heart will instantly force the vampire into torpor and exposing the heart to fire or sunlight will burn the vampire to ash; even biting into the heart will cause aggravated wounds to the vampire in question."""
      ),
      Power(
        name='Shadow of Apep',
        discipline='serpentis',
        level=9,
        description="""Only Set and Set’s own childer can perform this terrifying power. These ancient monsters can take the form of Set’s defeated enemy, Apep. The vampire becomes a giant serpent of fluid, glittering Darkness - not mere shadow, but anti-light, like the black force commanded by Obtenebration. In this form, physical force cannot harm the vampire: not claws or fangs, not bullets, not explosions, nothing but fire, sunlight, or mystical powers. Physical barriers cannot easily stop the vampire, whose shadowy form can seep through even the tiniest crack. The vampire, however, can still exert physical and supernatural force quite freely.
_System_: Taking the form of Apep costs a Willpower point. The transformation takes three turns to complete; once the vampire has transformed, her body remains changed for one scene. In this form, the vampire takes no damage from any physical attack: fists, weapons, or falling buildings pass through the vampire as if she were a shadow. Fire and sunlight inflict the normal aggravated damage, however, and mystical powers (such as Thaumaturgy) still affect the transformed vampire. The vampire’s new body gains three dots in each Physical Attribute. Ignore generational limits for this purpose. The transformed vampire can use her Strength to make normal close combat attacks and can bite for Strength + 2 dice of damage. The vampire can also employ any Discipline that does not require hands."""
      )
    ],
    description="""
Serpentis is believed to be the legacy of Set himself, a gift to his children. The Followers of Set are very careful to guard this Discipline’s secrets, only teaching the art to those who they deem worthy. Most vampires fear the Setites because of the powers of Serpentis and its connection to snakes and reptiles; this Discipline can evoke a primordial fear in others, particularly those who recall the tale of Eden.
"""
  ),
  Discipline(
    name='Countermagic',
    sorcery=False,
    powers= [
      Power(
        name='Thaumaturgical Countermagic 1',
        discipline='countermagic',
        level=1,
        description="""The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes.
Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.
Thaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.
_Two dice of countermagic._ The character can attempt to cancel only those powers and rituals that directly affect him, his garments, and objects on his person."""
      ),
      Power(
        name='Thaumaturgical Countermagic 2',
        discipline='countermagic',
        level=2,
        description="""The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes.
Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.
Thaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.
_Four dice of countermagic._"""
      ),
      Power(
        name='Thaumaturgical Countermagic 3',
        discipline='countermagic',
        level=3,
        description="""The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes.
Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.
Thaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.
_Six dice of countermagic._ The character can attempt to cancel a Thaumaturgy power that affects anyone or anything in physical contact with him."""
      ),
      Power(
        name='Thaumaturgical Countermagic 4',
        discipline='countermagic',
        level=4,
        description="""The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes.
Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.
Thaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.
_Eight dice of countermagic._"""
      ),
      Power(
        name='Thaumaturgical Countermagic 5',
        discipline='countermagic',
        level=5,
        description="""The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes.
Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.
Thaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.
_Ten dice of countermagic._ The character can now attempt to cancel a power or ritual that targets anything within a radius equal to his Willpower in yards or meters, or one that is being used or performed within that same radius."""
      )
    ],
    description="""
This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are not officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.

_System:_ Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals.

The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes.

Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.

Thaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.
"""
  ),
  Discipline(
    name='Obeah',
    sorcery=False,
    powers= [
      Power(
        name='Sense Vitality (Obeah)',
        discipline='obeah',
        level=1,
        description="""With a touch, the Salubri can instantaneously read a target’s injuries. She may learn how much damage a target has incurred, and therefore make a guess at what must be done to save him. This power can also be used for diagnostic purposes - useful for a victim who can no longer speak.
_System_: The Salubri must touch the target to see how close to death she is. He must then make a ^Perception + Empathy^ roll (difficulty 7). One success on this roll identifies a subject as a mortal, vampire, ghoul, or other creature. Two successes reveal how many health levels of damage the subject has suffered. Three successes tell how full the subject’s blood pool is (if a vampire) or how many blood points she has left in her system (if a mortal or other blood-bearing form of life). Four successes reveal any diseases in the subject’s bloodstream. A player may opt to learn the information yielded by a lesser degree of success - for example, a player who accumulates three successes may learn whether or not a subject is a vampire as well as the contents of his blood pool. Alternately, each success on this roll allows the player to ask the Storyteller one question about the subject’s health or health levels. “Was he drugged?” or “Are his wounds aggravated?” are valid questions, but “Did the Sabbat do this?” or “What did the Lupine who attacked him look like?” are not. The Salubri may use this power on herself if she has injuries but has somehow lost the memory of how the wounds were received. Additionally, at the cost of one blood point, the Salubri may use Empathy for a roll instead of Medicine."""
      ),
      Power(
        name='Anesthetic Touch (Obeah)',
        discipline='obeah',
        level=2,
        description="""The vampire can ease a target’s pain or place him into a deep, soothing sleep with nothing but a touch. This power is intended to heal the pain or succor the mind of willing targets, but the character can, with some effort, employ the power against someone who does not wish it.
_System_: If the subject is willing to undergo this process, the player spends a blood point and makes a ^Willpower^ roll (difficulty 6) to block the subject’s pain. This allows the subject to ignore all wound penalties for one turn per success. A second application of this power may be made once the first one has expired, at the cost of another blood point and another Willpower roll. If the subject is unwilling for some reason, the player must make a contested ^Willpower^ roll against the subject (difficulty 8). To put a mortal to sleep, the same system applies. The mortal sleeps for five to 10 hours - whatever his normal sleep cycle is - and regains one temporary Willpower point upon awakening. He sleeps peacefully and does not suffer nightmares or the effects of any derangements while asleep. He may be awakened normally (or violently). Kindred, including the Salubri herself, are unaffected by this power - their corpse-like bodies are too tied to death."""
      ),
      Power(
        name='Corpore Sano',
        discipline='obeah',
        level=3,
        description="""The Salubri can heal wounds with a laying-on of hands. The subject feels a warm, tingling sensation over the affected areas as pain leaves the body and flesh knits. The vampire’s third eye opens during this process.
_System_: This power works on any living or undead creature, but the character must touch the actual injury (or the closest part of the victim’s body, in the case of internal injuries). Each health level to be healed requires the expenditure of one blood point and one turn of contact. Aggravated wounds may also be healed in this manner, but the vampire must spend two blood points instead of one for each aggravated health level."""
      ),
      Power(
        name='Shepherd’s Watch',
        discipline='obeah',
        level=4,
        description="""The Salubri with this level of mastery of Obeah can create an invisible barrier between those under his care and those who would do them harm. The Salubri himself must stand among his charges as he generates this barrier; he cannot defend them from afar. Enemies armed with guns or other ranged weapons can still attack, but none may approach closer than a few paces.
_System_: The player spends two Willpower points. Erecting this barrier is a standard action, but maintaining it from turn to turn or dropping it is a reflexive action. The invisible barrier extends to about a 3 yard/1 meter radius from the character, and no one outside that barrier may cross it while she maintains the power. Those within it at its creation may leave and return, however. The barrier moves with the Salubri. It cannot be maintained at a distance. Those who wish to cross the barrier from the outside, whether friendly or hostile, must best the character in an extended, resisted ^Willpower^ roll (difficulty equals the opponent’s current Willpower for the Salubri, and the Salubri’s current Willpower for the opponent). The opponent may cross the barrier as soon as he accumulates three more net successes than the Salubri."""
      ),
      Power(
        name='Mens Sana',
        discipline='obeah',
        level=5,
        description="""With this power, the Salubri can heal madness, quieting inner demons and bringing a soul to peace. Indeed, ancient stories of the Salubri state that Saulot used this power to bring sweet, if temporary, relief to his “brother” Malkav. Other, more recent stories claim that Saulot caused Malkav’s madness in the first place.
_System_: The player spends two blood points and rolls ^Intelligence + Empathy^ (difficulty 8). The use of Mens Sana takes at least 10 minutes of relatively uninterrupted conversation. Success cures the subject of one derangement of the Salubri player’s choice. This power cannot cure a Malkavian of his core derangement, though it alleviates its effects for the rest of the scene. A botch inflicts the same derangement on the Salubri for the rest of the scene. This power may not be used by the Salubri to cure her own derangements."""
      ),
      Power(
        name='Unburdening the Bestial Soul',
        discipline='obeah',
        level=6,
        description="""This power is the leverage that the Tremere have used for years to tarnish the Salubri’s name. The Warlocks claim that the Salubri use this power to remove the souls of their victims, alter them in horrible ways, or simply consume them and then make mindless slaves from the blasted husks. The truth is that the Cyclops use this power to rebuild a target’s tattered soul, at the expense of their own mental fortitude. The Salubri draws the subject’s soul out of his body, and into the vampire’s third eye. There, the vampire repairs the soul. During this time, the target’s body is vacant, but alive. It obeys the Salubri’s commands (and the vampire must command it to eat and drink, or else it will starve - repairing the soul is not a quick undertaking). By a similar process, the character can cleanse a person, place, or object of demonic or evil infuence. This isn’t a simple banishment, however. It is a battle, pitting the Salubri’s moral and spiritual purity against whatever malign entity is present. If the Salubri loses the contest, she might lose her own soul in the process.
_System_: This power may be used to draw out the soul of any character except those with Humanity or Path ratings of 1 or 0 or those who follow particularly inhuman Paths of Enlightenment - some souls are beyond redemption. The player rolls ^Stamina + Empathy^ (difficulty of 12 minus the subject’s Humanity or Path rating). A botch gives the Salubri the subject’s derangement for the remainder of the scene. The Salubri must make eye contact with the subject and the subject must be willing to be subjected to this power. A soul drawn out in this manner becomes part of the Salubri’s soul while the healing process takes place. She may return it to its proper body at any time. While the soul is within the Salubri, she may spend a permanent Willpower point to restore a point to the subject’s Humanity or Path rating. The Salubri may restore a maximum number of points equal to her Empathy rating, and may not raise the subject’s Humanity or Path higher than the sum of his relevant Virtues (for example, a character subscribing to Humanity with Conscience 3 and Self-Control 3 could not have his Humanity raised above 6 in this manner). While a soul is being held by the Salubri, its body is an empty husk, comatose or in torpor, with no motivating force within it. A soul whose body is killed immediately vanishes, its disposition unknown to any (although the Salubri strongly suspect that souls that vanish in this manner are completely and irreversibly destroyed). Killing the body of a drawn-out soul may warrant a Conscience or Conviction roll if the killer knows of the soul’s absence, at the Storyteller’s discretion. If used to draw out a demon, the player spends a Willpower point if the subject is willing and the corrupting agent does not resist (a rare occurrence). If the subject is possessed by a conscious entity, the demon (or other foreign consciousness) fights the Salubri for dominance. This takes place via an extended, contested roll of the Salubri’s ^Humanity or Path^ versus the opponent’s Willpower (each party’s difficulty is equal to the other’s current Willpower). The winner is the first one to achieve three net successes more than the other. If the player fails, the attempt at purification also fails. If the player botches, the demon takes over the Salubri’s body. This purification cannot be used on oneself and has no effect on the Beast or an alternate personality. Once the initial removal has been successfully performed, the player spends a second Willpower point. The Salubri thrusts the demon into a nearby item, animal, or person, trapping the demon in the selected vessel. This must be accomplished within two turns of the Purification and the target must be within physical reach. If this cannot be accomplished, the demon is likely to go free... or find another suitable vessel (such as the Salubri). If the vampire places the demon in a being who is likely to suffer from its presence, the player must make an immediate Conscience or Conviction roll (difficulty 8) if the Storyteller believes that the character’s morality would object. A botch, in addition to the normal consequences, releases the demon into the world."""
      ),
      Power(
        name='Renewed Vigor',
        discipline='obeah',
        level=7,
        description="""At this level of power, the Salubri no longer has to repair a target’s body wound by wound. With a touch and a moment’s concentration, she can restore the body to full health.
_System_: The Salubri touches the target and spends a full turn concentrating. The player spends a point of Willpower. At the end of the turn, the target is healed of all damage, including aggravated damage. If the character attempts any other action but the laying of hands during this turn, the Willpower point is lost and no healing occurs. The Salubri can use this power on herself."""
      ),
      Power(
        name='Safe Passage',
        discipline='obeah',
        level=8,
        description="""The Salubri radiates a non-threatening aura, altering the minds of those around her to seem safe, pleasant, and harmless. Crowds unconsciously part for her, pursuers lose interest, and passers-by are willing to provide assistance. In the event that someone does attempt to do her harm, the rest of the crowd may even protect her.
_System_: This power is always activate, though the Salubri can turn it off if she so desires. While Safe Passage is active, anyone in a crowd (defined as more than 10 people in close proximity) who wants to harm the Salubri must engage in a contested ^Willpower^ roll with the vampire’s player (difficulty 6). If the pursuer wins, he may do as he wishes. If the vampire wins, her net successes act as a dice pool penalty on any hostile action the pursuer chooses to take. This manifests as lost interest in the vampire (the pursuers wonders why he is chasing this person rather than doing something more interesting). Safe Passage can also assist a Salubri in finding help or shelter. The player rolls ^Charisma + Expression^ (difficulty 7). Each success reduces the difficulty of a subsequent, appropriate Social roll by one. This affects only attempts to gain seemingly harmless or innocent assistance, such as a place to stay or advice on the bad parts of town - a Salubri won’t be able to get automatic weapons or low-grade heroin more easily with this power. The effects of this power last until the next sunrise. Safe Passage affects only those who know the Salubri casually or not at all. Anyone who has known her long enough to form an opinion of her cannot be touched by this power."""
      ),
      Power(
        name='Unburden the Flesh-Clad Soul',
        discipline='obeah',
        level=9,
        description="""Some few Salubri elders can (or could, at least) achieve an understanding of the soul that allowed them to free it from its fleshly confines. The character allows a willing subject’s soul to fy free, able to explore the world as an astral projection and transcend that existence whenever it wishes.
_System_: The vampire and a willing subject must both enter a deep meditative trance for a minimum of one uninterrupted hour as the Salubri performs the ritual necessary to separate soul from flesh without damaging either. During this period, the player spends a number of blood points equal to twice the permanent Willpower of the subject. At the end of the ritual, the subject’s body slips into a coma and dies by the end of the night. Many Tremere and other cautious Kindred warn that the Salubri may misrepresent themselves and convince others to volunteer for a “release” from mortal concerns, when in truth they wish to trap the soul in another plane of existence. The subject’s soul is released from her body and enters the astral plane (such as the Auspex power Psychic Projection on p.138). This separation is permanent and irreversible. The subject is treated as an astrally-projecting character in terms of rules mechanics. However, she no longer has a silver cord and no longer needs one, as she exists independently of her body. If she is reduced to zero Willpower through astral combat, she loses one point of permanent Willpower and reforms after a year and a day at the place where this power was used upon her. A character reduced to zero permanent Willpower is destroyed forever. This power may only be used upon mortals (excluding mages) and vampires who are in Golconda, and the subject must have a full understanding of what this ritual entails - including its permanence and the impossibility of a reversal. The body of a vampire who is Unbound decays at sunrise. It is possible to drink the blood remaining in the vampire’s body, but no benefits are gained from an attempt at diablerie. Any attempt to Embrace the body of an Unbound mortal automatically fails. The free-flying soul may choose to dissipate, moving on to whatever awaits beyond death, at any time (and is therefore not a ghost). The Salubri may use this power on herself, provided she is in Golconda."""
      )
    ],
    description="""
The bloodline known in modern nights simply as the Salubri is actually descendant of one half of the ancient Clan. In bygone nights, one might have spoken of “healer” and “warrior” Salubri. In the modern nights, the last vestiges of the warrior Salubri are the <i>antitribu</i> of the Clan, and practice their Discipline of Valeren (see p. 474). The rest of the bloodline know the Discipline of Obeah. This Discipline allows the Salubri to judge and even improve a subject’s health. As the vampire grows more powerful, Obeah lets her heal a target’s soul directly. It is this power that forms the basis of the “soulsucker“ charge that dogs the bloodline these nights.

This Discipline gives its practitioners a third eye in the center of the vampire’s forehead when the Kindred masters the second level of Obeah.
"""
  ),
  Discipline(
    name='Vicissitude',
    sorcery=False,
    powers= [
      Power(
        name='Malleable Visage',
        discipline='vicissitude',
        level=1,
        description="""A vampire with this power may alter her own bodily parameters: height, build, voice, facial features, and skin tone, among other things. Such changes are cosmetic and minor in scope - no more than a foot (30cm) of height gained or lost, for example. She must physically mold the alteration, literally shaping her flesh into the desired result.
_System_: The player must spend a blood point for each body part to be changed, then roll ^Intelligence + Medicine^ (difficulty 6). To duplicate another person or voice requires a ^Perception + Medicine^ roll (difficulty 8), and five successes are required for a flawless copy; fewer successes leave minute (or not-so-minute) flaws. Increasing one’s Appearance Trait has a difficulty of 9, and the vampire must spend an additional blood point for each dot of Appearance increased beyond their natural total. A botch permanently reduces the Attribute by one."""
      ),
      Power(
        name='Fleshcraft',
        discipline='vicissitude',
        level=2,
        description="""This power is similar to Malleable Visage, above, but allows the vampire to perform drastic, grotesque alterations on other creatures. Tzimisce often use this power to transform their servitors into monstrous guards, the better to frighten foes. Only flesh (skin, muscle, fat, and cartilage, but not bone) may be transformed.
_System_: After spending a blood point, the vampire must grapple the intended victim. The player of the Fleshcrafting vampire makes a successful ^Dexterity + Medicine^ roll (difficulty variable: 5 for a crude yank-and-tuck, up to 9 for precise transformations). A vampire who wishes to increase another’s Appearance Trait does so as described under Malleable Visage; reducing the Attribute is considerably easier (difficulty 5), though truly inspired disfigurement may dictate a higher difficulty. In either case, each success increases or reduces the Attribute by one. A vampire may use this power to move clumps of skin, fat, and muscle tissue, thus providing additional padding where needed. For each success scored on a ^Dexterity + Medicine^ roll (difficulty 8), the vampire may increase the subject’s soak dice pool by one, at the expense of either a point of Strength or a health level (vampire’s choice)."""
      ),
      Power(
        name='Bonecraft',
        discipline='vicissitude',
        level=3,
        description="""This terrible power allows a vampire to manipulate bone in the same manner that flesh is shaped. In conjunction with Fleshcraft, above, this power enables a Vicissitude practitioner to deform a victim (or herself) beyond recognition. This power should be used in conjunction with the flesh-shaping arts, unless the vampire wants to inflict injury on the victim (see below).
_System_: The vampire’s player must spend a blood point and make a ^Strength + Medicine^ roll (difficulties as above). Bonecraft may be used without the flesh-shaping arts, as an offensive weapon. Each success scored on the ^Strength + Medicine^ roll (difficulty 7) inflicts one health level of lethal damage on the victim, as his bones rip, puncture, and slice their way out of his skin. The vampire may utilize this power (on herself or others) to form spikes or talons of bone, either on the knuckles as an offensive weapon or all over the body as defensive “quills”. If bone spikes are used, the vampire or victim takes one health level of lethal damage (the vampire’s comes from having the very sharp bone pierce through his skin - this weaponry doesn’t come cheaply). In the case of quills, the subject takes a number of health levels equal to five minus the number of successes (a botch kills the subject or sends the vampire into torpor). These health levels may be healed normally. Knuckle spikes inflict Strength +1 lethal damage. Defensive quills inflict a hand-to-hand attacker’s Strength in lethal damage unless the attacker scores three or more successes on the attack roll (in which case the attacker takes no damage); the defender still takes damage normally. Quills also enable the vampire or altered subject to add two to all damage inflicted via holds, clinches, or tackles. A vampire who scores five or more successes on the ^Strength + Medicine^ roll may cause a rival vampire’s rib cage to curve inward and pierce the heart. While this does not send a vampire into torpor, it does cause the affected vampire to lose half his blood points, as the seat of his vitae ruptures in a shower of gore."""
      ),
      Power(
        name='Horrid Form',
        discipline='vicissitude',
        level=4,
        description="""Kindred use this power to become hideous and deadly monsters. The vampire’s stature increases to a full eight feet (two and a half meters), the skin becomes a sickly greenish-gray or grayish-black chitin, the arms become apelike and ropy with ragged black nails, and the face warps into something out of a nightmare. A row of spines sprouts from the vertebrae, and the external carapace exudes a foul-smelling grease.
_System_: The Horrid Form costs two blood points to awaken. All Physical Attributes increase by three, but all Social Attributes drop to zero, except when dealing with others also in Horrid Form. However, a vampire in Horrid Form who is trying to intimidate someone may substitute Strength for a Social Attribute. Damage inflicted in brawling combat increases by one due to the jagged ridges and bony knobs creasing the creature’s hands."""
      ),
      Power(
        name='Bloodform',
        discipline='vicissitude',
        level=5,
        description="""A vampire with this power can physically transform all or part of her body into sentient vitae. This blood is in all respects identical to the vampire’s normal vitae; she can use it to nourish herself or others, create ghouls, or establish blood bonds. If all this blood is imbibed or otherwise destroyed, the vampire meets Final Death.
_System_: The vampire may transform all or part of herself as she deems fit. Each leg can turn into two blood points worth of vitae, as can the torso; each arm, the head, and the abdomen convert to one blood point each. The blood can be reconverted to the body part, provided it is in contact with the vampire. If the blood has been utilized or destroyed, the vampire must spend a number of blood points equal to what was originally created to regrow the missing body part. A vampire entirely in this form may not be staked, cut, bludgeoned, or pierced, but can be burned or exposed to the sun. The vampire may ooze along, drip up walls, and flow through the narrowest cracks, as though she were in Tenebrous Form (p.190). Mental Disciplines may be used, provided no eye contact or vocal utterance is necessary, although the vampire can perceive her surroundings just fine (but the perceptions are always centered on the largest pool of blood). If a vampire in this form “washes” over amortal or animal, that mortal must make a Courage roll (difficulty 8) or fly into a panic."""
      ),
      Power(
        name='Chiropteran Marauder',
        discipline='vicissitude',
        level=6,
        description="""Similar to Horrid Form, the Chiropteran Marauder is a terrifying, bipedal bat, bearing a wickedly fanged maw and veined, leathery wings. This power confers all of the benefits of the Horrid Form, in addition to a few others. The mere sight of the marauder is enough to make mortals or weak-willed vampires flee in horror.
_System_: The vampire gains all the effects of the Horrid Form. Further, the Marauder’s fluted wings allow flight at 25 mph (40 kph), during which the vampire may carry, but not manipulate, objects no larger than it can hold in its hands. If the player chooses to, she may make a ^Strength + Medicine^ roll (difficulty 6) to extend bony claws at the ends of the vampire’s wings. These claws inflict Strength + 2 aggravated damage. Also, the vampire subtracts two from all hearing-based Perception rolls (though he adds one to vision- based Wits and Perception rolls). Assuming the mantle of the Chiropteran Marauder costs three blood points."""
      ),
      Power(
        name='Blood of Acid',
        discipline='vicissitude',
        level=6,
        description="""At this level of mastery, the vampire has converted his blood to a viscous acid. Any blood he consumes likewise becomes acid, which is corrosive enough to burn human (and vampiric flesh) as well as wood. This effect is particularly potent when the vampire assumes the Bloodform. One of the side effects of this power is the complete inability to create new vampires and ghouls, or give blood to another vampire - the acid would corrode them as they drank it. The obvious benefit, however, is that would-be diablerists are likewise unable to devour the Cainite’s blood.
_System_: Each acidified blood point that comes in contact with something other than the vampire himself does five dice worth of aggravated damage. If the vampire is injured in combat, his blood may splatter on an opponent - foes must make Dexterity + Athletics rolls to avoid the blood, which must be accomplished by splitting their dice pools. (Unless an opponent knows the vampire has this power, she’s unlikely to split her dice pool on her first attack, which causes many Tzimisce to cackle with glee)."""
      ),
      Power(
        name='Cocoon',
        discipline='vicissitude',
        level=7,
        description="""The Cainite can form an opaque cocoon from blood and other fluids excreted from her body. The cocoon hardens after a few moments, turning into a tough, white shell. This cocoon provides considerable protection to the vampire, even shielding her from sunlight and, to a limited degree, fire.
_System_: A vampire may only cocoon herself, and the process takes 10 minutes. Additionally, creating a cocoon costs three blood points. The cocoon offers complete protection from sunlight, and provides a number of dice of soak equal to twice the vampire’s unmodified Stamina against all damage, aggravated or otherwise. It lasts as long as the Cainite wishes, and she may dissolve it at her whim, emerging from a pulpy, bloody paste. A vampire contained within a cocoon may still use mental Disciplines that do not require eye contact or other conditions to be met."""
      ),
      Power(
        name='Breath of the Dragon',
        discipline='vicissitude',
        level=8,
        description="""The vampire becomes like one of the terrible draculs of the Old World, able to exhale a deadly gout of flame. This flame does not hurt the vampire himself, though he may become trapped in flames if it engulfs flammable objects.
_System_: The flaming cloud affects a six-foot area, doing two dice of aggravated damage to anyone in the flames’ circumference. This fire may cause combustible items to ignite, and it may ignite victims who suffer fire damage as per the fire rules on page 297."""
      ),
      Power(
        name='Earth’s Vast Haven',
        discipline='vicissitude',
        level=9,
        description="""This power, developed in the nights when the Tzimisce were the terrible masters of Eastern Europe, allows the vampire to sink into and disperse himself through the ground. Unlike the Protean power of EarthMeld, however, the vampire actually dissolves his body into the ground; nothing short of a wide-area explosion can affect him, and he may not be dug up bodily. In addition, from sunset to sunrise, the vampire may see and hear everything happening in his environment through his mystical connection to the land. The mere fact that this power exists terrifies many Tzimisce, who are secretly unsure of whether or not the diablerie of their Antediluvian was successful.
_System_: This power costs six blood points to activate, and it lasts as long as the vampire wishes to remain contained within the soil. As per the Cocoon, the vampire may use mental Disciplines that do not require physical solvency or eye contact. He may communicate mentally with anyone who wanders into the area under which he rests."""
      )
    ],
    description="""
Vicissitude is the signature power of the Tzimisce, and is rarely shared outside the Clan (though it is known to some other Cainites of the Sabbat). Similar to Protean in some ways, Vicissitude allows vampires to shape and sculpt flesh and bone. When a Kindred uses Vicissitude to alter mortals, ghouls, and vampires of higher Generation, the effects of the power are permanent; vampires of equal or lower Generation can choose to heal the effects of Vicissitude as though they were aggravated wounds. A wielder of Vicissitude can always reshape her own flesh.

The wielder must establish skin-to-skin contact and must often manually sculpt the desired result for these powers to take effect. This also applies to the use of the power on oneself. Tzimisce skilled in Vicissitude are often inhumanly beautiful; those less skilled are simply inhuman.

There are rumors that Vicissitude is a disease rather than a “normal” Discipline, but only the Fiends know for sure, and they aren’t talking.

_Note:_ Nosferatu <i>always</i> “heal” Vicissitude alterations, at least the ones that make them better-looking. The ancient curse of the Clan may not be circumvented through Vicissitude. The same applies to physical deformities from the Gangrel Clan weakness.



_Body Crafts_

Vampires who wish to use Vicissitude well often specialize their knowledge of Medicine in an art known as Body Crafts. This specialization enables its possessor to make all manner of alterations to living and dead flesh and bone. It also gives insight into more mundane techniques; many Tzimisce are skilled at flaying, bone-carving, embalming, taxidermy, tattooing, and piercing.
"""
  ),
  Discipline(
    name='Potence',
    sorcery=False,
    powers= [
      Power(
        name='Potence 1',
        discipline='potence',
        level=1,
        description="""Add 1 die to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Potence 2',
        discipline='potence',
        level=2,
        description="""Add 2 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Potence 3',
        discipline='potence',
        level=3,
        description="""Add 3 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Potence 4',
        discipline='potence',
        level=4,
        description="""Add 4 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Potence 5',
        discipline='potence',
        level=5,
        description="""Add 5 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Potence 6',
        discipline='potence',
        level=6,
        description="""Add 6 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Imprint',
        discipline='potence',
        level=6,
        description="""A vampire with extensive knowledge of Potence can squeeze very, very hard. As a matter of fact, she can squeeze (or press, or push) so hard that she can leave an imprint of her fingers or hand in any hard surface up to and including solid steel. A use of Imprint can simply serve as a threat, or it can be used, for example, to dig handholds into sheer surfaces for purposes of climbing.
_System_: Imprint requires a point of blood to activate. The power remains active for the duration of a scene. The depth of the imprint the vampire creates with Imprint is up to the Storyteller - decisions should take into account how much force the vampire can bring to bear, the toughness of the material, and its thickness. If the object the vampire grasps is thin enough, at the Storyteller’s discretion, the vampire might simply be able to push through it (in the case of a wall) or tear it off (in the case of a spear or pipe)."""
      ),
      Power(
        name='Potence 7',
        discipline='potence',
        level=7,
        description="""Add 7 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Earthshock',
        discipline='potence',
        level=7,
        description="""According to some pundits, Potence is merely the art of hitting something very hard. But what do you do when your target is too far away to hit directly? The answer is, if you’re sufficiently talented with the Discipline, to employ Earthshock. On its simplest level, Earthshock is the ability to hit the ground at point A, and subsequently have the force of the blow emerge from the ground at point B.
_System_: The use of Earthshock requires the expenditure of two blood points, as well as a normal ^Dexterity + Brawl^ roll. The vampire punches or stamps on the ground, and, if the attack is a success, the force of the blow emerges from the ground as a geyser of stone and earth directly underneath the target. The attack can be dodged at a +2 difficulty. Earthshock’s range is 10 feet or three meters for every level of Potence the vampire has, up to the limits of visibility. A failure on the attack roll means that the strike goes errant and is liable to explode anywhere within range; a botch means that the vampire pulverizes the ground beneath him and may well bury himself in the process."""
      ),
      Power(
        name='Potence 8',
        discipline='potence',
        level=8,
        description="""Add 8 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      ),
      Power(
        name='Flick',
        discipline='potence',
        level=8,
        description="""It is a truism that “the great ones always make it look easy”. In the case of Flick, that saying stops being a truism and becomes literal truth. With this power, a master of Potence can make the slightest gesture - a wave, a snap of the fingers, the toss of a ball - and have it unleash the full, devastating impact of a dead-on strike. The attack can come without warning, limiting the target’s ability to dodge or anticipate; this makes Flick one of the most feared applications of Potence.
_System_: Flick costs a point of blood, and requires a ^Dexterity + Brawl^ roll (difficulty 6). The vampire must also make some sort of gesture directing the blow. What the gesture is remains up to the player - anything from a snap of the fingers to a blown kiss has worked in the past. Flick’s range is equal to the limit of the Kindred’s perception, and the blow struck does damage equal to a normal punch (including all bonuses)."""
      ),
      Power(
        name='Potence 9',
        discipline='potence',
        level=9,
        description="""Add 9 dice to all Strength-related rolls. Spend blood to turn into automatic successes to all Strength-related rolls for a turn"""
      )
    ],
    description="""
Kindred endowed with Potence possess unnatural strength. This Discipline enables vampire to leap massive distances, lift tremendous weights, and strike opponents with brutal force. Even low ranks of this power can give Kindred physical power beyond mortal bounds. More powerful Kindred can leap so far that they appear to be flying, toss cars like soda cans, and punch through walls like cardboard. While the more subtle mental Disciplines can be awe-inspiring, the brutal effectiveness of Potence is formidable in its own right.

The Brujah, Giovanni, Lasombra, and Nosferatu are naturally gifted with this Discipline, but members of other Clans often make a point to find someone who can teach them the awesome power of Potence.

_System:_ Each dot that the vampire has in Potence adds one die to all Strength-related dice rolls. Further, the player can spend one blood point and change his Potence dice into an equal number of automatic successes to all Strength-related rolls for the turn. In melee and brawling combat, successes from Potence (either rolled or automatic) are applied to the damage roll results.
"""
  ),
  Discipline(
    name='Mytherceria',
    sorcery=False,
    powers= [
      Power(
        name='Folderol',
        discipline='mytherceria',
        level=1,
        description="""The Kiasyd can cleave truth from lies. The exact effect varies from vampire to vampire. Some Kiasyd experience bleeding from the eyes or ears when they hear a lie, while some Weirdlings’ eyes glow when told a falsehood. Whatever the effect, this power detects lies, not mistakes, meaning that a target has to know he is lying in order for this power to work.
_System_: The character knows when a target is deliberately lying. No roll or expenditure is necessary for this power to work, but the character must deliberately activate it. Note that this power does not provide any insight into what the truth might be, nor does it enable the vampire to tell if a target is simply stating something false that he believes to be true."""
      ),
      Power(
        name='Fae Sight',
        discipline='mytherceria',
        level=2,
        description="""The Kiasyd’s knowledge of magic isn’t just theoretical. Their strangely-colored eyes are capable of detecting the arcane energies of the fae, as well as magic from other, more esoteric sources. They are not, however, capable of using this power to detect the residue of ghosts or vampiric magic.
_System_: The Kiasyd sees faeries and other fae-touched mortals for what they really are, with no roll required. Additionally, the player can detect any form of magic that does not stem from ghosts or the undead, including magic from mages, werewolves, and other such odd sources. The character can recognize these for what they truly are, provided he has seen similar effects before."""
      ),
      Power(
        name='Aura Absorption',
        discipline='mytherceria',
        level=3,
        description="""The Kiasyd is capable of seeing images of events and emotions past by touching an object or an area. However, unlike the Auspex Power The Spirit’s Touch, this power absorbs the images, making them harder for other beings with similar powers to access. Anyone attempting to use this power, Spirit’s Touch, or a similar ability to see what the Kiasyd has seen finds that the images are hard to hold, slipping through his mind’s eye like minnows through a stream.
_System_: The player must make a ^Perception + Empathy^ roll. The difficulty is determined by the Storyteller based on the age of the impressions and the mental and spiritual strength of the person who left them. The number of successes determines the amount of information gained, both in terms of images of the scene when the object was being held or touched, and the nature of the person who was holding the object. One scene-type image and one aspect of the person’s identity (Nature, Demeanor, aura, name, sex, or age) becomes clear for each success the player garners on the roll. Anyone attempting to use this power or The Spirit’s Touch on the same object subsequently must accumulate more successes than the Kiasyd did to get any impression at all. The first Kiasyd’s successes subtract from the number of successes scored by anyone trying to read the object thereafter."""
      ),
      Power(
        name='Chanjelin Ward',
        discipline='mytherceria',
        level=4,
        description="""The vampire inscribes a ward on an object, a location, or a person. That ward disorients and befuddles anyone that sees it, meaning that even if an intruder can penetrate a Weirdling’s security and steal an object of value, he’s unlikely to be able to find his way to the exit. Spiteful Kiasyd use these wards as punishment - one story tells of a Weirdling that drew a ward on an enemy’s shirt as dawn approached, and then watched (from safety) as the unfortunate vampire burned in the sun, unable to remember which way to run.
_System_: The vampire creating the ward inscribes the symbol in a visible location - on a library door, book-shelf, or an individual’s clothing - and the player rolls ^Intelligence + Larceny^ (difficulty 7 for inanimate objects, or the subject’s current Willpower +2). Anyone entering the warded area or touching the warded object loses two dice from her Intelligence dice pools as long as she maintains contact with or proximity to the ward. Additionally, anyone seeing the ward becomes addled and lost unless she succeeds on a Wits + Investigation roll (difficulty 8). The Kiasyd is immune to his own wards. The glyphs last for a duration indicated by the number of successes on the ^Intelligence + Larceny^ roll:
<table><tr><th>Successes</th><th>Duration</th></tr><tr><td>1 success</td><td>One hour</td></tr><tr><td>2 successes</td><td>One night</td></tr><tr><td>3 successes</td><td>One week</td></tr><tr><td>4 successes</td><td>One month</td></tr><tr><td>5 successes</td><td>One year</td></tr></table>"""
      ),
      Power(
        name='The Riddle Phantastique',
        discipline='mytherceria',
        level=5,
        description="""The Kiasyd whispers a riddle to an opponent, and the riddle consumes his mind. The target can do nothing until he solves the riddle, and no one can help him - answers provided by others, even correct answers, fail to counteract this affiction.
_System_: The player rolls ^Manipulation + Occult^ (difficulty of the victim’s current Willpower). After a successful roll, the victim can do nothing but sit and ponder the Riddle until she accumulates three times the riddler’s successes. The subject rolls Wits + Occult (difficulty 8, plus or minus the number of derangements the victim has, at the Storyteller’s discretion). She makes this roll as soon as she is told the Riddle, and then once per hour until she has gathered enough successes. Should the victim botch on a roll to solve the Riddle, she takes one level of lethal damage as the mystical enigma racks her body, and she loses all successes from the accumulated total. This damage cannot be healed until the Riddle has been solved. The riddler can end this trance by telling the victim the answer, but no-one else can."""
      ),
      Power(
        name='Steal the Mind',
        discipline='mytherceria',
        level=6,
        description="""Legends tell of the Fair Folk taking the memories and faculties of their victims, leaving these hapless people drooling idiots for the rest of their lives. While modern thinking is that these stories actually referred to stroke victims, elder Kiasyd display a power with a similar effect. The victim of Steal the Mind loses his memories and all knowledge he has accumulated. The Kiasyd gains these memories for a short time, and generally uses this time to inscribe them before they revert to the original owner... assuming the Weirdling lets that happen.
_System_: The player selects a mortal or supernatural target and rolls ^Perception + Subterfuge^ (difficulty equal to the target’s current Willpower). While the Kiasyd has “stolen” her subject’s mind, she retains her own consciousness, but has complete access to all of the subject’s thoughts and memories. Subjects have no knowledge that they have been affected in this manner, though any attempts to harm them - by the Kiasyd or anyone else - return their wits to them immediately. Subjects have no access to their Knowledges while this power is active, but Talents and most Skills (those that work on muscle memory) are still present. The Storyteller might need to exercise discretion as to which Abilities are lost. Those who are victims of this power for long periods of time may starve, though they will eat food presented to them. The number of successes determines the duration of the effect, though the Kiasyd may return the subject’s mind at any time before this period ends. If the victim dies before the memories return, the Weirdling keeps them. If the Kiasyd kills the target to keep his memory, the character may need to roll for degeneration (see p.309) depending on what Path they follow - Kiasyd on Humanity must always roll.
<table><tr><th>Successes</th><th>Duration</th></tr><tr><td>1 Success</td><td>10 minutes</td></tr><tr><td>2 Successes</td><td>One hour</td></tr><tr><td>3 Successes</td><td>One night</td></tr><tr><td>4 Successes</td><td>One week</td></tr><tr><td>5 Successes</td><td>One month</td></tr></table>"""
      ),
      Power(
        name='Absorb the Mind',
        discipline='mytherceria',
        level=7,
        description="""This power, similar to Steal the Mind, allows the vampire to absorb Abilities from her victim. These traits are transferred permanently; the victim loses the knowledge, and the Kindred gains it. Absorb the Mind is an extremely invasive and insidious power, and fortunately only a bare handful of Kindred in the world know of it.
_System_: The player rolls ^Perception + Empathy^ (difficulty equal to the target’s current Willpower). The target may resist with a Willpower roll (difficulty equal to the Kiasyd’s current Willpower). The difference between the two determines the effect. If the target gets more successes, he resists completely and the Kiasyd may never use Absorb the Mind on this target again. The Kiasyd, if successful, may select a combination of Abilities to her satisfaction. Taking some of a victim’s Ability dots may leave a remainder - the Kiasyd need not take all of a subject’s dots in a given Ability. For example, a character with three dots in Occult, from whom a Kiasyd steals one, retains an Occult of 2. If a Kiasyd takes fewer dots than she already has in a given Ability, these points do not serve to raise her own rating (In the previous example,the Kiasyd would not increase his Occult rating if he already had a rating of one or more, as he took only one dot). If the Kiasyd fails in an attempt to use this power on a target, no subsequent attempt can be made on that target for a year and a day. In all cases, the maximum to which the Kiasyd can raise an Ability is the level the target has in that Ability, so if a victim has only one dot in Law and the Kiasyd gets 2 successes, she can’t gain 2 dots in Law. Generational restrictions do apply: a Sixth-Generation Kiasyd can have a maximum of seven dots in an Ability, for example. All losses of Abilities on the part of the victim are permanent, though they may be returned to their original levels via experience point expenditure.
<table><tr><th>Successes</th><th>Effect</th></tr><tr><td>1 Success</td><td>Steal 1 dot</td></tr><tr><td>2 Successes</td><td>Steal 2 dots in one Ability</td></tr><tr><td>3 Successes</td><td>Steal 3 dots in up to two Abilities</td></tr><tr><td>4 Successes</td><td>Steal 4 dots in up to three Abilities</td></tr><tr><td>5 Successes</td><td>Steal 5 dots in up to four Abilities</td></tr></table>"""
      ),
      Power(
        name='The Grandest Trick',
        discipline='mytherceria',
        level=8,
        description="""The Kiasyd can fool himself into believing that he is not, and has never been, a vampire. This trick lasts for a short time, during which the character gives up all blessings (but loses all drawbacks) of being Kindred. He retains all of his other knowledge, but the magic of the Grandest Trick deftly prevents him from figuring out the truth (notes that explain the truth vanish, knowledge of clues that would lead him to it don’t make sense, etc.). The Grandest Trick is useful for throwing vampire hunters off a character’s scent, but also for gathering information that can only be obtained during the day. Rumors among younger Kiasyd also persist that some elders of the bloodline use the Grandest Trick to meet during the day once every 50 years, exchanging documents and letters that, for that day, make no sense to any of them. It is only after the Trick wears off that they remember who they are and can read what their Clanmates wrote.
_System_: The player spends eight blood points and makes a ^Willpower^ roll (difficulty 9). If this roll is successful, the character becomes mortal at the next sunrise for a duration determined by the number of successes on the roll. The Kiasyd knows, however subliminally, the duration of the power, and he automatically attempts to return to safety, should daylight be a problem at the power’s end. After this power ends, the Kiasyd retains all memories of his brief return to the world of mortals. During his time as a mortal, the character’s Traits are limited to ratings of 5 (which return to their original levels when the character becomes a vampire again), and the character has no access to her Disciplines. Likewise, the character may not use blood points for any vampiric benefits while mortal.
<table><tr><th>Successes</th><th>Duration</th></tr><tr><td>1 success</td><td>10 minutes</td></tr><tr><td>2 successes</td><td>One hour</td></tr><tr><td>3 successes</td><td>Four hours</td></tr><tr><td>4 successes</td><td>12 hours</td></tr><tr><td>5 successes</td><td>24 hours</td></tr></table>"""
      )
    ],
    description="""
Whatever odd commingling of blood which produced the Kiasyd has led to a number of weird effects, not least of which is the Mytherceria Discipline. This collection of powers mimics the abilities of faeries - or at least, that’s the best guess of the Kindred who are familiar with it. The Kiasyd use this power to alter and beguile the minds of their foes, as well as to force others to tell the truth. The Kiasyd do not, in general, teach this Discipline to those outside the bloodline, and supposedly it would require oaths sworn on the lifeblood of the student to learn.
"""
  ),
  Discipline(
    name='Assamite Sorcery',
    sorcery=False,
    powers= [
      Power(
        name='Assamite Sorcery 1',
        discipline='assamite sorcery',
        level=1,
        description="""Assamite Sorcery 1"""
      ),
      Power(
        name='Assamite Sorcery 2',
        discipline='assamite sorcery',
        level=2,
        description="""Assamite Sorcery 2"""
      ),
      Power(
        name='Assamite Sorcery 3',
        discipline='assamite sorcery',
        level=3,
        description="""Assamite Sorcery 3"""
      ),
      Power(
        name='Assamite Sorcery 4',
        discipline='assamite sorcery',
        level=4,
        description="""Assamite Sorcery 4"""
      ),
      Power(
        name='Assamite Sorcery 5',
        discipline='assamite sorcery',
        level=5,
        description="""Assamite Sorcery 5"""
      ),
      Power(
        name='Assamite Sorcery 6',
        discipline='assamite sorcery',
        level=6,
        description="""Assamite Sorcery 6"""
      ),
      Power(
        name='Assamite Sorcery 7',
        discipline='assamite sorcery',
        level=7,
        description="""Assamite Sorcery 7"""
      ),
      Power(
        name='Assamite Sorcery 8',
        discipline='assamite sorcery',
        level=8,
        description="""Assamite Sorcery 8"""
      ),
      Power(
        name='Assamite Sorcery 9',
        discipline='assamite sorcery',
        level=9,
        description="""Assamite Sorcery 9"""
      )
    ],
    description="""
From a purely functional standpoint, the blood magic that the Assamite sorcerer caste practices differs little from that wielded by the Tremere. From a philosophical perspective, however, worlds of difference separate the two. The Tremere force every piece of knowledge they incorporate into the structured, rigid framework of high Hermetic invocation. By contrast, the sorcerer caste’s practices are the result of millennia of adaptation and melding, and are too disparate to be considered “structured” in any real sense. The modern body of knowledge that is Assamite Sorcery draws its content from a wide array of magical traditions, from the ecstatic rites of Kali and Shiva’s followers to the subtle precision of feng shui to the elegant symbolic and mathematical transformations of Islamic alchemists and astronomers.

Assamite Sorcery is mechanically identical to the more common Thaumaturgy that appears on pp. 212-240. However, though they work on similar principles (the use of vampiric vitae to fuel exertions of conscious will in order to effect change upon the physical or spiritual world), the two are not cross-compatible. A Tremere strives to perform his magic the same way, all the time, every time. An Assamite might never enact the same ritual the same exact way twice in a millennium.

As may be expected, students of Assamite Sorcery have great difficulty learning the practices of other blood magic traditions. All experience points costs to learn other blood magic paths and rituals are increased by half (round up) for Assamite sorcerers. In addition, even once the sorcerer has incorporated these lessons into her repertoire, they are still alien to her. All invocations of a “foreign” path require one extra blood point and all rituals take triple the normal time and require one extra success for any desired result.
"""
  ),
  Discipline(
    name='Chimerstry',
    sorcery=False,
    powers= [
      Power(
        name='Ignis Fatuus',
        discipline='chimerstry',
        level=1,
        description="""The vampire may conjure a minor, static mirage that confounds one sense. For instance, he may evoke a sulfurous stench, the appearance of stigmata, or the shatter of broken glass. Note that though tactile illusions can be felt, they have no real substance; an invisible but tactile wall cannot confine anyone, and invisible razor-wire causes no real damage. Similarly, the vampire must know the characteristics of what he’s creating. While it’s easy enough to estimate what a knife wound might look like, falsifying a person’s voice or a photograph of a childhood home requires knowledge of the details.
_System_: The player spends a point of Willpower for the vampire to create this illusion. The volume of smells, ambient lighting, smoke clouds, and the like are limited to roughly 20 cubic feet (half a cubic meter) per dot the vampire has in Chimerstry. The illusion lasts until the vampire leaves its vicinity (such as stepping out of the room) or until another person sees through it somehow. The Cainite may also end the illusion at any time with no effort."""
      ),
      Power(
        name='Fata Morgana',
        discipline='chimerstry',
        level=2,
        description="""The Cainite can now create illusions that appeal to all the senses, though they remain static. For example, the vampire could make a filthy cellar appear as an opulent ballroom, though she could not create a glittering chandelier or a score of graceful dancers. Again, the illusion has no solid presence, though it’s easy enough to fool an enraptured visitor with suggestions of what she might expect. A bucket of brackish water is as cool as chilled champagne, after all.
_System_: The player spends a Willpower point and a blood point to create the illusion. These static images remain until dispelled, in much the same way that an Ignis Fatuus illusion does."""
      ),
      Power(
        name='Apparition',
        discipline='chimerstry',
        level=3,
        description="""Not really a power unto itself, Apparition allows a vampire to give motion to an illusion created with Ignis Fatuus or Fata Morgana. Thus, the Cainite could create the illusion of a living being, running water, futtering drapes, or a roaring fire.
_System_: The creator spends one blood point to make the illusion move in one significant way, or in any number of subtle ways. For example, the vampire could create the illusion of a lurking mugger lurching at her victim, or she could create the illusion of a desolate street, down which a chill wind blows trash while a streetlamp fickers and hums. Taking complicated actions besides maintaining the illusion - that is, anything that would require a dice roll - first requires success on a ^Willpower^ roll, resulting in the dissolution of the false construct if the roll fails. Once the creator stops concentrating on the illusion, it can continue in simple, repetitive motions - roughly speaking, anything that can be described in a simple sentence, such as a guard walking back and forth in front of a steel door. After that, the vampire cannot regain control over the illusion - she can either allow it to continue moving as ordered, or let it fade as described under Ignis Fatuus."""
      ),
      Power(
        name='Permanency',
        discipline='chimerstry',
        level=4,
        description="""This power, also used in conjunction with Ignis Fatuus or Fata Morgana, allows a mirage to persist even when the vampire cannot see it. In this way, Ravnos often cloak their temporary havens in false trappings of luxury, or ward off trespassers with illusory guard dogs.
_System_: The vampire need only spend a blood point, and the illusion becomes permanent until dissolved (including “programmed” illusions like those created by Apparition)."""
      ),
      Power(
        name='Horrid Reality',
        discipline='chimerstry',
        level=5,
        description="""Rather than create simple illusions, the vampire can now project hallucinations directly into a victim’s mind. The target of these illusions believes completely that the images are real; a hallucinatory fire can burn him, an imaginary noose can strangle him, and an illusory wall can block him. This power affects only one person at a time; though others can see the illusion, it doesn’t impact them in the same way. Other people can try to convince the victim that his terrors are not real, but he won’t believe them. Note that targets with enough dots in Auspex can still attempt to roll for Seeing the Unseen (p.142).
_System_: A Horrid Realty illusion costs two Willpower points to set in motion and lasts for an entire scene (though its effects may last longer; see below). If the vampire is trying to injure his victim, his player must roll ^Manipulation + Subterfuge^ (difficulty of the victim’s Perception + Self-Control/Instinct). Each success inflicts one health level of lethal damage on the victim that cannot be soaked - the Cainite assaults the victim’s mind and perceptions, not his body. If the player wishes to inflict less damage or change it to bashing, he may announce a maximum amount of damage before rolling the dice. Secondary effects (such as frenzy rolls for illusory fire) may also occur. The victim heals all his damage instantaneously if he can be convinced that the damage he took was illusory, but convincing him may take some doing, such as with at least two successes on a Charisma + Empathy roll (difficulty equal to the ^Manipulation + Subterfuge^ of the Cainite using Horrid Reality). The target must be convinced of the attack’s illusory nature within 24 hours of its taking place, or it becomes too well established in his memory, and he will have to heal the damage using blood (if a vampire) or over time (if mortal). This power cannot actually kill its victims (though a target with a heart condition may well die from fright). A victim “killed” by an illusory attack loses consciousness or enters torpor."""
      ),
      Power(
        name='False Resonance',
        discipline='chimerstry',
        level=6,
        description="""Illusions of living or unliving beings are all well and good until someone decides to read the illusion’s mind or its aura. The automatic failure to perceive any sense of the target’s thoughts or emotions will usually be passed off as bad luck, lack of concentration, or whatever reason any Kindred might construct to explain why he didn’t succeed in gleaning information through supernatural means. A vampire can use False Resonance to overlay auras and thoughts on illusions, as well as leave a trace that other emotionally resonant powers can detect later.
_System_: This power automatically applies to any other use of Chimerstry as the user wishes. In effect, any attempt to use Auspex, the Dementation power Eyes of Chaos, or similar sensory powers that generates five or fewer successes will detect an aura, thoughts, Demeanor or whatever the power would normally detect. Thoughts won’t be exceptionally complex, and will relate to whatever is going on around the illusion in a mundane and simplistic way. Auras will consist of colors related to specific emotions (anger, sadness, hatred, love, and happiness) and will not show much complexity beyond that. Spirit’s Touch can pick up the same emotional resonance until the next sunrise."""
      ),
      Power(
        name='Fatuus Mastery',
        discipline='chimerstry',
        level=6,
        description="""A Ravnos with Fatuus Mastery has no restriction on how often she may use the first three levels (Ignis Fatuus, Fata Morgana, and Apparition) and can maintain or control illusions with minimal concentration or fatigue. Kindred who rely on the high cost of Chimerstry to limit a vampire’s ability to use illusions are in for a very rude surprise when they encounter a Cainite with this power.
_System_: Fatuus Mastery negates the Willpower and blood cost for using the first three levels of Chimerstry. In addition, the Kindred may direct movement for a number of illusions equal to his Intelligence without intense concentration. Furthermore, the character can maintain the illusion as long as it remains within his Willpower rating in miles (or about one and a half times that in kilometers), although he may not make it react to events around it if he has no way to perceive those events."""
      ),
      Power(
        name='Shared Nightmare',
        discipline='chimerstry',
        level=6,
        description="""Even though Horrid Reality is visible to all onlookers, it can only inflict “damage” on one victim. With Shared Nightmare, a vampire can inflict her tormented visions on a crowd.
_System_: To use this power, the player must spend two Willpower points, plus one blood point per target. The player rolls ^Manipulation + Subterfuge^ once, but compares the results against each target individually. The difficulty is still each victim’s Perception + Self-Control/Instinct."""
      ),
      Power(
        name='Far Fatuus',
        discipline='chimerstry',
        level=7,
        description="""This power allows a Kindred to project illusions to any area he can see or visualize. Under most circumstances, accomplishing this requires him to have visited the location in question before he can project illusions there. Although more difficult, a vampire may project illusions on the basis of a description, a photo, or a video clip.
_System_: The difficulty for using Far Fatuus depends on the user’s familiarity with the location. The player must roll ^Perception + Subterfuge^ to affect the location. Once this roll is successful, the vampire may then use any other Chimerstry power on that location.
<table><tr><th>Diffculty</th><th>Familiarity</th></tr><tr><td>6</td><td>As familiar as one’s haven; currently viewing with Clairvoyance or Psychic Projection</td></tr><tr><td>7</td><td>Visited three or more times</td></tr><tr><td>8</td><td>Visited once; viewing on a live feed</td></tr><tr><td>9</td><td>Described in detail; seen it in a video or have a undoctored photo</td></tr></table>"""
      ),
      Power(
        name='Suspension of Disbelief',
        discipline='chimerstry',
        level=7,
        description="""A Ravnos with this power can imbue her Chimerstry with a sense of reality that makes it easier for viewers to believe in the illusion. No matter how strange or surreal the illusion is, an onlooker will accept it as real. If the illusion is wildly unrealistic (fire-breathing dragons, a pack of aliens), once it is no longer in his sight, the observer will question what he saw and eventually deny the event ever happened. A vampire can also use this power to make something appear unbelievable, whether it’s real or not. In this case, observers will write off what they’re seeing as some kind of trick or hallucination.
_System_: The player rolls ^Manipulation + Subterfuge^ (difficulty 7). The number of successes determines how many witnesses are affected. If the player uses the power to make something look unbelievable, Auspex will show the thing in question to be an illusion unless the Auspex rating is not high enough to penetrate the Kindred’s Chimerstry.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Five people</td></tr><tr><td>2 successes</td><td>10 people</td></tr><tr><td>3 successes</td><td>25 people</td></tr><tr><td>4 successes</td><td>50 people</td></tr><tr><td>5 successes</td><td>Everyone who can see it</td></tr></table>"""
      ),
      Power(
        name='Synesthesia',
        discipline='chimerstry',
        level=8,
        description="""A Cainite who masters this power can shuffe others’ senses around to suit his preferences. He can select one target and inflict a serious, disorienting, and all-encompassing case of synesthesia upon her, making it impossible for her to interact meaningfully with the real world for the power’s duration. The vampire has complete control over how the target’s senses work and can manipulate them to suit. For example, he may decide that she smells all sounds as varieties of nauseating stenches, or more subtly, he may exchange pain for pleasure. Used against a crowd, sensations are randomly shuffed, so one man will see what the woman next to him sees, but hears what the man 15 feet behind him hears and feels what the child a block away feels. The end result is extremely disorienting for all victims.
_System_: When used against a single victim, the player must spend one Willpower point and roll ^Manipulation + Intimidation^ (difficulty is victim’s current Willpower points). For use against crowds, the difficulty is 7, and the power affects everyone within the vampire’s line of sight and subtracts one point from Perception per success rolled. Victims whose Perception has been reduced to zero can only sit down and wait for the disorientation to end. Duration against a single victim is determined below. Against a crowd, the power persists until sunrise.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>One week</td></tr><tr><td>2 successes</td><td>One month</td></tr><tr><td>3 successes</td><td>Six months</td></tr><tr><td>4 successes</td><td>One year</td></tr><tr><td>5 successes</td><td>Permanent</td></tr></table>"""
      ),
      Power(
        name='Mayaparisatya',
        discipline='chimerstry',
        level=9,
        description="""This expression of Chimerstry allows the Cainite to directly alter or create real objects or creatures, although such changes are of finite duration. A vampire with this power can transform the air around a rival Kindred into fire or render a locked door insubstantial. A more harrowing use of this power enables the vampire to force an object out of existence by transforming it into nothing more than a wisp of its former reality.
_System_: To use this power, the player must spend 10 blood points and one permanent Willpower point and roll ^Manipulation + Subterfuge^. Difficulty for the roll is 6 for affecting inanimate objects, and the victim’s Willpower rating for affecting characters. This power can affect anything within miles (kilometers) of the vampire, as long as the character is aware of the target in some way. If used with Far Fatuus, the effects are centered on the chosen location. This power can affect a number of conscious targets equal to the Kindred’s ^Willpower^ per use. When dealing with inanimate objects, the number of successes determines how drastic the alteration may be. No matter how many successes the player rolls, the duration is always a scene. This power can affect any objects of a type within the vampire’s targeted area.
<table><tr><th>Successes</th><th>Result</th></tr><tr><td>1 success</td><td>Render an object harmless (swords won’t cut, firearms won’t shoot), create a large volume of obscuring smoke</td></tr><tr><td>2 successes</td><td>Change an object into another object (turn candles into tarantulas, etc.)</td></tr><tr><td>3 successes</td><td>Render the object insubstantial, make smoke solid</td></tr><tr><td>4 successes</td><td>Cause drastic changes (stone becomes highly flammable)</td></tr><tr><td>5 successes</td><td>Cause the environment to behave illogically (gravity twists sideways, rivers stand still as hills flow upward)</td></tr><tr><td>6+ successes</td><td>Delete any offending material objects from existence. This effect is permanent (to use this on conscious targets, follow the system described below). When using the power on conscious targets, consult the table above for alterations (such as forcing the victim into another form or transforming her into a different substance). If using the power to negate the victim’s existence, the power inflicts two levels of unsoakable aggravated damage per success. If the power doesn’t kill the victim, subtract one dot of Strength and Stamina per success. The damage must be healed normally, but the lost Attributes return at the end of the scene. Victims of this power look hazy and insubstantial. Victims destroyed with this power simply vanish.</td></tr></table>"""
      )
    ],
    description="""
The Ravnos are known as masters of illusion, although the reason why is lost to history. Rumors abound of Ravnos ghûls, rakshasas, and shapeshifters, but whatever its origins, Chimerstry remains a potent and powerful weapon for the Deceivers. The Discipline is, fundamentally, an art of conjuration that converts the vampire’s will into phantoms that confound the senses and technology alike. Even vampires fall under the sway of the Ravnos’ illusory world, unless they have a strong enough grasp of Auspex (see p. 142). The Ravnos often use this power to swindle and seduce their victims into acts that work out badly for the victim (but great for the Ravnos).

Illusions created by Chimerstry can be seen for what they are by a victim who “proves” the illusion’s falsehood (e.g., a person who walks up to an illusory wall, expresses his disbelief in it, and puts his hand through it effectively banishes the illusion), and explicitly incredible illusions are seen as false immediately (e.g., dragons breathing fire or gravity working in reverse). Sometimes, frequent targets of Chimerstry end up attempting to disbelieve everything around them, leading to derangements (and, quite often, to the amusement of the Ravnos).
"""
  )
]

disciplines = dict((discipline.name, discipline) for discipline in disciplines)
