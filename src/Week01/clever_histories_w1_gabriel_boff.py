print('Welcome to clever histories!\n')
print("""
-------------------------> MENU <---------------------------
		-> Select a text complexity:
		1. Low
		2. Normal
		3. Realistic  
------------------------------------------------------------
""")
menu = int(input('Type here: '))
print('Please enter the following:\n')


if (menu == 3):

    adjective = str(input('adjective: '))
    plural_noun = str(input('plural noun: '))
    noun = str(input('noun: '))
    adverb = str(input('adverb: '))
    number = str(input('number: '))
    past_tense_verb = str(input('past tense verb:'))
    est_adjective = str(input('-est adjective: '))

    print(f"""
	The fun park
		
	Today, my fabulous camp group went to a (an)
	{adjective} amusement park. It was a
	fun park with lots of cool {plural_noun}
	and enjoyable play structures. When we got there, my
	kind counselor shouted loudly, "Everybody off the
	{noun}." We all pushed out in a terrible
	hurry. My counselor handed out yellow tickets, and
	we scurried in. I was so excited! I couldn't figure out
	what exciting thing to do first. I saw a scary roller
	coaster I really liked so, I {adverb} ran
	over to get in the long line that had about
	{number} people in it. When I finally
	got on the roller coaster I was {past_tense_verb}. In fact I was so nervous my two knees
	were knocking together. This was the 
	{est_adjective} ride I had ever been on! In about two
	minutes I heard the crank and grinding of the gears.
	That’s when the ride began! When I got to the bottom,
	I was a little {past_tense_verb} but I
	was proud of myself. The rest of the day went
	{adverb}. It was a(n) {adjective} day at the fun park.		
	""")
else:

    adjective = str(input('adjective: '))
    animal = str(input('animal: '))
    verb1 = str(input('verb: '))
    exclamation = str(input('exclamation: '))
    verb2 = str(input('verb: '))
    verb3 = str(input('verb: '))
    print('Your history is:\n')

    if (menu == 1):
        print(f"""
        {exclamation}! My {animal} is {verb1} while I\'m {verb2}. 
		This sentences don\'t make sense, this makes me remember how {adjective} is 
		my {animal} when It is {verb3}.	
		""")
    if(menu == 2):
        print(f"""
		The other day, I was really in trouble. It all started when I saw a very
		{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
		I could think to do was to {verb2} over and over. Miraculously,
		that caused it to stop, but not before it tried to {verb3}
		right in front of my family.
		""")
