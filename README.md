# Calculator

Simple calculator simulator that contains good vs bad programming methods.

Principles: <br>
KISS - Keep it simple, stupid <br>
DRY - Don’t repeat Yourself. <br>
Document - Leave comments to methods that need it <br>
YAGTNI - You aren’t going to need it, meaning don’t code for stuff you aren’t going to need or use. <br>
Code Implementation: ErrorCalculator.py <br>
Violations: <br>
KISS - The calculator class not only deals with all the methods but it also deals with the “main menu” and user input. <br>
DRY - There is a lot of repeated code under the “main menu” comment such as the “menu” options and the if-else loops such as the print statements. <br>
Documentation - There are comments for almost every piece of code which is unnecessary as some of the code is self explanatory.<br>
YAGTNI - All other methods are used except print_result which is never referenced or used in any way. This would be an example of a method that is unnecessary. <br>
