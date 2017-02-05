
INSERT INTO VtM20_Users (ID,Name,Pass,FullName,IsRevoked) VALUES
(1,'Admin','AdminPa$$w0rd',  'Admin',  0);

INSERT INTO VtM20_Games (ID,Name,StoryTellerID,Logo,Abilities,Attributes,Backgrounds,Disciplines,Virtues,FreebiePoints,BaseGeneration,MaxBackgrounds,YBEarly,YBLate,YEEarly,YELate,ICDate,ICStart,Started,Finished,IsActive,Display) VALUES
(1,'Chronicle of Ages',1,'CoA.png','13/9/5','7/5/3',5,4,7,15,12,5,1167,1168,1183,1193,'1198-04-15','1198-04-15','2014-04-18',NULL,1,1);

INSERT INTO VtM20_Chars (ID,Name,IsApproved,UserID,GameID,ClanID,NatureID,DemeanorID,MoralityID,Morality,Willpower,Generation,CurrWillpower,CurrBloodPool,
               XPTotal,XPAvail,WeaknessNotes,Health0,Health1,Health2,Health3,Health4,Health5,Health6,Health7,IsUgly,IsHuge,IsSorc,IsStarting,IsDead) VALUES
(01,'Laszlo',1,1,1,08,08,11,1,6,6,7,6,20, 0, 0,'',0,0,0,0,0,0,0,0,1,0,0,1,0); -- First Character

INSERT INTO VtM20_Games_Users (GameID,UserID,IsPlayer,DefaultCharID,DefaultHomepage,IsMBoardIC) VALUES
-- Game 1 - Chronicle of Ages
(01,01,0,04,'charSheet.php', 0);  -- Admin [StoryTeller]

INSERT INTO VtM20_Games_Advancement (GameID,NewAbil,NewDisc,NewPath,AdvAttr,AdvAbil,AdvAbilOther,AdvDiscClan,AdvDiscCaitiff,AdvDiscNonClan,AdvPath,AdvVirtues,AdvMorality,AdvWillpower,Ritual1,Ritual2,Ritual3,Ritual4,Ritual5,Ritual6,Ritual7,Ritual8,Ritual9) VALUES
(01,3,10,7,4,2,2,5,6,7,4,2,2,1,'1 week','1 month','3 months','6 months','1 year','2 years','4 years','8 years','16 years'); -- Game 1 - Chronicle of Ages (all default values)

--      VtM20_Games_Alerts (ID,GameID,FromUserID,ToUserID,DTStamp,IsRead,Message)

INSERT INTO VtM20_Games_Chars (GameID,CharID,IsPC,InParty) VALUES
-- Game 1 - Chronicle of Ages
(01,01,0,0); -- First Character

INSERT INTO VtM20_Games_Messageboard (GameID,Name,IsIC,DTStamp,Message,PrivUserID) VALUES
(1,'Lawson',0,'2006-09-12 12:01:07','<b>A few notes about the website.</b><br>This website contains the following pages, all accessible from the navigation panel running across the top of every page.<br><br>&nbsp;&nbsp;&nbsp;<b>1. Character Sheets : </b>Displays a Character Sheet in the same format as the paper version.  All players sheets can be seen by all players.  I will be writing a page that allows you to spend XP and update your character sheet with those spends, but it is not complete yet.  For now, if you spot any mistakes or wish to make any changes to your character, you will have to let me know.<br>You can also view the Character History (a link in the top left of the character sheet).  Again, at this time there is no way that you can edit this history.  If you wish for me to add your characters history to this page, please email/give it to me (any format will do : text, Word doc, written on toilet paper with crayon) and I will sort it out for you.<br><br>&nbsp;&nbsp;&nbsp;<b>2. Character Journal : </b>This allows you to maintain a character journal or diary.  All players can read your characters journal, but you can only update your own.  Entries do not have to be made in chronological order, but they are sorted into this order and displayed \\"oldest at the top\\" like a paper diary.  You are not limited to creating journal entries on game date (6th August 1999).  Your journal can be used to flesh out your characted histories before the game starts by writing older entries.  If you Delete an entry, particularly by mistake it can be recovered if you ask me.  No entries are actually permanently deleted, I just set a \\"Deleted\\" flag next to that entry and it is no longer displayed or available for editing.<br><br>&nbsp;&nbsp;&nbsp;<b>3. Character Gallery : </b>A summary of the current party.  If you click on a Character Portrait (all produced by Wanju) it will take you to their character sheet. Primarily I used this as a quick navigation tool to move about the Character Sheets.  Ive left it in the final version cos I think its pretty and shows me a Coterie Portrait.<br><br>&nbsp;&nbsp;&nbsp;<b>4. Character Summaries : </b>This is a tool I put in, primarily for me but I left it in the generally available pages.  It represents the Characters in a standard stat block, as used by all of the Vampire books. It is a concise way of representing the characters in a format I am used to reading quickly.<br><br>&nbsp;&nbsp;&nbsp;<b>5. Picture Viewer : </b>A chance for Wanju to show off her Character sketches even more.  Again, this is more useful to me as it also holds NPC portraits, which I will use during game sessions to give faces to names of certain people you will meet.  Under a Players login, it will only present the Coteries portraits for display.<br><br>&nbsp;&nbsp;&nbsp;<b>6. Message Board : </b>This is it. Here we are.  A simple thread-less message board in the old-school style of the LT Boards.  Please note that you can post either In-Character or Out Of Character posts (the radio buttons to the right of the message entry box). The website will automatically label your posts with your real name for OOC posts and your Character name for IC posts.  There is a drop-down box just below the text-entry box to filter and display IC or OOC posts if you prefer to read them seperately.  At the moment, the default is to post In-Character.  Dont forget to change this to OOC when posting website comments or suchlike.  I nearly did just now.<br><br>&nbsp;&nbsp;&nbsp;<b>7. Sun and Moon : </b>A basic Sunrise, Sunset and Moon Phase calculator.  You can quickly tell what times your character can be up and about for planning or journal writing purposes.  You can also predict when the full moons are going to happen, but this is for no real game reason. Honestly, its just for extra detailing to the game. No, really.  Stop looking at me like that.<br><br>I would also like to know if you have any ideas for new pages, or any comments on how any existing pages work or operate.  I would prefer to spend my spare time on plot-development rather than web-development, but if anyone has a good suggestion that meets with majority approval, then I am happy to implement it if it aids the game and the game experience (oooh, do I sound like a Hasbro PR suit?).<br>However, I am not going to get into a discussion about which shade of blue you think the background colour should be.  Black text on a white background is about the only thing I am going to be inflexible on.<br><br>After writing this large chunk of text, I think my first web-improvement will be a preview button for this page.<br><br>Finally, I have just noticed that the server time is set to GMT (I think).  This means that the post time on the message board is an hour out (I really posted this at 11:01am).  Unfortunately, I dont think I can change that on the server. Ill have to have a word with DK and see what he says.  For now, just notice it and allow for it.<br><br>See you Thursday.',1),
(1,'Lawson',0,'2006-09-12 12:58:46','I have now added <br>1. a \\"Preview\\" button - press this to preview your post before \\"Send\\"ing it.  It makes it easier to check for spelling and formatting mistakes.  It is also a handy check on whether the post is IC or OOC.<br><br>2. a \\"Refresh page\\" button.  Use this to refresh the page, instead of your browsers F5/Refresh button.  It causes a page refresh without the browser attempting to re-send any previous messages you may have entered earlier.  This is useful when you are trying to have an almost real-time conversation on the board - not recommended, but it may happen from time to time.',1);

INSERT INTO VtM20_Games_Prohibit (GameID,LookupTable,ProhibitID) VALUES
-- Game 1 - Chronicle of Ages
-- Game 1 Archetypes
(1,'Archetypes',28), -- Monster
-- Game 1 Clans
(1,'Clans',15), -- Baali
(1,'Clans',16), -- Blood Brothers
(1,'Clans',27), -- Cappadocians
(1,'Clans',28), -- Children of Osiris
(1,'Clans',30), -- Lhiannan
(1,'Clans',31), -- Noiad
(1,'Clans',52), -- Angellis Ater (Potence)
(1,'Clans',53), -- Angellis Ater (Presence)
(1,'Clans',54), -- Angellis Ater (Obtenebration)
(1,'Clans',57), -- Brahman
(1,'Clans',58), -- Wu Zao (Obeah)
(1,'Clans',59), -- Wu Zao (Valeren)
-- Game 1 Disciplines
(1,'Disciplines',19), -- Bardo
(1,'Disciplines',20), -- Daimoinon
(1,'Disciplines',27), -- Sanguinus
-- Game 1 Morality
(1,'Morality',11); -- Path of Paradox

INSERT INTO VtM20_Chars_Abilities (CharID,Alertness,AlertnessNotes,Athletics,AthleticsNotes,Awareness,AwarenessNotes,Brawl,BrawlNotes,Empathy,EmpathyNotes,Expression,ExpressionNotes,Intimidation,IntimidationNotes,Leadership,LeadershipNotes,Streetwise,StreetwiseNotes,Subterfuge,SubterfugeNotes,Animal_Ken,Animal_KenNotes,Crafts,CraftsNotes,Drive,DriveNotes,Etiquette,EtiquetteNotes,Firearms,FirearmsNotes,Larceny,LarcenyNotes,Melee,MeleeNotes,Performance,PerformanceNotes,Stealth,StealthNotes,Survival,SurvivalNotes,Academics,AcademicsNotes,Computers,ComputersNotes,Finance,FinanceNotes,Investigation,InvestigationNotes,Law,LawNotes,Medicine,MedicineNotes,Occult,OccultNotes,Politics,PoliticsNotes,Science,ScienceNotes,Technology,TechnologyNotes) VALUES
-- 01 Laszlo
(01,2,'',1,'',1,'',0,'',2,'',1,'',2,'',1,'',2,'',2,'',1,'',0,'',0,'',1,'',0,'',0,'',1,'',2,'',2,'',1,'',1,'',0,'',0,'',2,'',0,'',0,'',1,'',1,'',0,'',0,'');

INSERT INTO VtM20_Chars_Abilities_Other (CharID,AbilityID,Value,Notes) VALUES
-- 01 Laszlo
(01,02,1,'');  -- Prof Skill (Riding) 1

INSERT INTO VtM20_Chars_Attributes (CharID,Strength,StrengthNotes,Dexterity,DexterityNotes,Stamina,StaminaNotes,Charisma,CharismaNotes,Manipulation,ManipulationNotes,Appearance,AppearanceNotes,Perception,PerceptionNotes,Intelligence,IntelligenceNotes,Wits,WitsNotes) VALUES
-- 01 Laszlo
(01,3,'',2,'',3,'',3,'',3,'',0,'',3,'',3,'',4,'Quick Thinker');

INSERT INTO VtM20_Chars_Backgrounds (CharID,BackgID,Value,Notes) VALUES
-- 01 Laszlo
(01,07,5,''), -- Generation 5
(01,04,2,'Inkeeper, Guard Cpt'), -- Contacts 2
(01,11,2,''); -- Resources 2

-- VtM20_Chars_ComboDisciplines (CharID,ComboID)

INSERT INTO VtM20_Chars_Creation (CharID,PriorityAttr,PriorityAbil,AttrSpend,AbilSpend,DiscSpend,BackSpend,MeriSpend,VirtSpend,FreeSpend) VALUES
(01,'231','123',15,27,4,5,0,7,15); -- 01 Laszlo

-- VtM20_Chars_Derangements (ID,CharID,Derangement,IsPermanent,WillCost,WillSpend)

INSERT INTO VtM20_Chars_Disciplines (CharID,DiscID,Value,IsClan) VALUES
-- 01 Laszlo
(01,01,1,1), -- Animalism 1
(01,09,2,1), -- Obfuscate 2
(01,11,1,1); -- Potence 1

INSERT INTO VtM20_Chars_Disciplines_Powers (CharID,DiscID,Notes) VALUES
-- 01 Laszlo
(01,001,''), -- Animalism 1 - Feral Whispers
(01,091,''), -- Obfuscate 1 - Cloak of Shadows
(01,092,''), -- Obfuscate 2 - Unseen Presence
(01,113,''); -- Potence 1   - Potence 1

-- VtM20_Chars_Journals (IsDeleted,GameID,CharID,DTStamp,ICDate,Title,Entry)

INSERT INTO VtM20_Chars_Merits (CharID,MeritID,Notes) VALUES
-- 01 Laszlo
(01,049,'Romanian, Slavic'), -- Language
(01,049,'German, Latin'), -- Language
(01,049,'two, more'), -- Language
(01,056,''), -- Natural Linguist
(01,060,''), -- Deep Sleeper
(01,148,''), -- Deceptive Aura
(01,150,''), -- Inoffensive to Animals
(01,162,''), -- Cast No Reflection
(01,066,''); -- Speech Impediment


INSERT INTO VtM20_Chars_Notes (CharID,Haven,Concept,Sire,Birth,Embrace,Image,Notes,History,WishList,STNotes) VALUES
(01,'','ex-Noble Son','Dondinni','1168-04-13','1190-05-31','Laszlo.png',   '','','',''); -- 01 Laszlo

-- VtM20_Chars_Sorcery_Paths (CharID,PathID,PathOrder,Value)
-- INSERT INTO VtM20_Chars_Sorcery_Paths (CharID,PathID,PathOrder,Value) VALUES ()

-- VtM20_Chars_Sorcery_Rituals (CharID,RitualID,Notes)
-- INSERT INTO VtM20_Chars_Sorcery_Rituals (CharID,RitualID,Notes) VALUES ()

-- VtM20_Chars_Vinculum (FromCharID,ToCharID,Rating)

INSERT INTO VtM20_Chars_Virtues (CharID,VirtueID,Value) VALUES
-- 01 Laszlo
(01,1,3), -- Conscience 3
(01,2,3), -- Self-Control 3
(01,3,4); -- Courage 4

