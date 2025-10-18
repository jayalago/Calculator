# Calculator

Simple calculator simulator that contains good vs bad programming methods.

Principles:
KISS - Keep it simple, stupid
DRY - Don’t repeat Yourself.
Document - Leave comments to methods that need it 
YAGTNI - You aren’t going to need it, meaning don’t code for stuff you aren’t going to need or use. 
Code Implementation: ErrorCalculator.py
Violations: 
KISS - The calculator class not only deals with all the methods but it also deals with the “main menu” and user input. 
DRY - There is a lot of repeated code under the “main menu” comment such as the “menu” options and the if-else loops such as the print statements. 
Documentation - There are comments for almost every piece of code which is unnecessary as some of the code is self explanatory.
YAGTNI - All other methods are used except print_result which is never referenced or used in any way. This would be an example of a method that is unnecessary. 
