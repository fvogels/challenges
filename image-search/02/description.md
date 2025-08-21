# Image Search

This machine was used by the Germans during World War 2 to encrypt their communication.

![Picture](./picture.jpg)

Knowing your enemy's intentions is crucial in a war, so the Allies invested a lot of resources in finding ways for cracking the coded messages.
This was not an easy task: every day, the Germans would initialize the machine with a different key, which could take on many values (158,962,555,217,826,360,000 to be exact).
So, every day, the allies had to start over and find the right key: none of the cracking achievements could be carried over to the next day.

To beat the German's machine, the Allies (among which Alan Turing) developed a computer specialized in finding the key.
In order to help reduce the search space (i.e., the number of possible keys to be considered), all kinds of clever trickery had to be employed:

* The Germans would (foolishly) start each message with three letters repeated, e.g., `AJFAJF`.
* They would also have many standard messages, such as "nothing to report" or "weather forecast".
  Knowing which words to expect helps cut down the number of possibilities drastically.
* The Allies would sometimes trick the Germans into sending specific messages,
  such as performing an attack and then waiting for the report about it.

The Allies could not always afford acting on decrypted messages and had to deliberately undergo German attacks at times, lest
the Germans grow suspicious and upgrade their encoding machine.

## Question

What was the name of this encrypting contraption?
