[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mMxhKicI)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21575083&assignment_repo_type=AssignmentRepo)
# COMP 163 Project 2 – Character Abilities Showcase

### **Author:** [Miles Johnson]  
### **Date:** [11-13-25]  
### **Course:** COMP 163 – Introduction to Object-Oriented Programming  
### **AI Usage:** AI assistance was used for inheritance structure explanations and code commenting.

---

##  Overview

This project demonstrates the use of **classes, inheritance, polymorphism, method overriding, and composition** in Python through a fantasy-themed battle system.

You’ll find six main classes (`Character`, `Player`, `Warrior`, `Mage`, `Rogue`, and `Weapon`) and one provided helper class (`SimpleBattle`) that simulates simple fights between characters.

---

##  Class Hierarchy


###  Character
- Base class for all character types.
- **Attributes:** `name`, `health`, `strength`, `magic`
- **Methods:**
  - `attack(target)` — basic attack using strength  
  - `take_damage(amount)` — reduces health but never below 0  
  - `display_stats()` — prints character info

###  Player
- Inherits from `Character`
- Adds player-specific attributes like `character_class` and `level`
- Overrides `display_stats()` to include class and level

###  Warrior
- Physical fighter with **high strength and health**, low magic  
- Overrides `attack()` for extra physical damage  
- **Special ability:** `power_strike(target)` (double damage)

###  Mage
- Magic-based fighter with **high magic**, low health and strength  
- Overrides `attack()` to use magic instead of strength  
- **Special ability:** `fireball(target)` (double magic damage)

###  Rogue
- Balanced stats with a chance for **critical hits**  
- Overrides `attack()` to sometimes deal double damage  
- **Special ability:** `sneak_attack(target)` (guaranteed critical)

###  Weapon
- Demonstrates **composition** — characters *have a* weapon  
- **Attributes:** `name`, `damage_bonus`  
- **Method:** `display_info()` — prints weapon details

---

##  SimpleBattle Class (Provided)

`SimpleBattle` simulates a one-round battle between two characters.  
It displays stats before and after attacks, determines the winner, and shows how polymorphism allows different classes to handle attacks uniquely.

---

## Example Usage

```python
# Create characters
warrior = Warrior("Sir Galahad")
mage = Mage("Merlin")
rogue = Rogue("Robin Hood")

# Display stats
warrior.display_stats()
mage.display_stats()
rogue.display_stats()

# Run a battle
battle = SimpleBattle(warrior, mage)
battle.fight()

Concepts Demonstrated:
Inheritance: sharing attributes and methods from parent classes

Polymorphism: same method (attack) behaves differently per subclass

Method Overriding: subclasses redefine parent behavior

Composition: Character can own a Weapon object

Encapsulation: managing health and damage safely
