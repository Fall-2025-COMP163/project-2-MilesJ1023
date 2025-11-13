"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Miles Johnson]
Date: [2025 - 11 - 13]

AI Usage: [CHAT OPENAI and Githubs Copilot]
 AI helped with inheritance structure and method overriding concepts and catering code towards the project requirements and Test cases.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================
import random
class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables
        
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        damage = self.strength * 2 # Basic attack damage calculation
        target.take_damage(damage) # Applies damage to targets
        print(f"{target} took {damage} pts of damage!") #displays damage dealt
        
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        self.health = self.health - damage #reduces health by damage amount

        if self.health < 0:
            self.health = 0
        
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0
        
        
    def display_stats(self): #Initisl display stats method
        """
        Prints the character's current stats in a nice format.
        """
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")

        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic, level = 1): #Initializes player method
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        super().__init__(name, health, strength, magic) #calls parent init method with basic charachter info using super()
        self.character_class = character_class #stores character class
        self.level = level #stores player level
        
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        super().display_stats() #calls parent display stats method using super()
        print(f"Character Class: {self.character_class}") #prints additional player info character class

        

class Warrior(Player): #Warrior class inherits from Player
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        super().__init__(name, "Warrior", 120, 15, 5, 1) #calls parent init method with warrior specific stats using super()
        
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        damage = self.strength + 5 #warrior attack damage calculation with +5 bonus
        target.take_damage(damage) #applies damage to target
        print(f"{target} took {damage} pts of damage!") #print damage dealt
        
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = (self.strength + 5) * 2 #power strike damage calculation with double damage
        target.take_damage(damage)
        print(f"{target} took {damage} pts of damage from Power Strike!")
        

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        super().__init__(name, "Mage", 80, 8, 20, 1) #calls parent init method with mage specific stats using super()
        
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        damage = self.magic
        target.take_damage(damage)
        print(f"{target} took {damage} pts of magical damage!")
        
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = self.magic * 2
        target.take_damage(damage)
        print(f"{target} took {damage} pts of damage from Fireball!")

        

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        super().__init__(name, "Rogue", 90, 12, 10, 1)
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        result = random.randint(1, 10) #generates random number between 1 and 10
        if result <= 3: #30% chance for critical hit
            damage = self.strength * 2 #critical hit damage calculation
            target.take_damage(damage)
            print(f"Critical Hit! {target} took {damage} pts of damage!")
        else:
            damage = self.strength
            target.take_damage(damage)
            print(f"{target} took {damage} pts of damage!")
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        damage = self.strength * 2 #sneak attack damage calculation with guaranteed critical hit
        target.take_damage(damage)
        print(f"Sneak Attack! {target} took {damage} pts of damage!")

        

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name #stores weapon name
        self.damage_bonus = damage_bonus #stores damage bonus
        
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        print(f"Weapon Name: {self.name}")
        print(f"Damage Bonus: {self.damage_bonus}")
        # TODO: Print weapon name and damage bonus
        

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
