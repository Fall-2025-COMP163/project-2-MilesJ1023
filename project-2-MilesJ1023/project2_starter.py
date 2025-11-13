"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

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
        self.name = str(name)
        self.health = float(health)
        self.strength = float(strength)
        self.magic = float(magic)
        self.weapon = None 
        self.charachter_class = "Character"
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
        damage = max(0, int(self.strength)) # basic damage calculation
        if hasattr(target, "take_damage"):
            target.take_damage(damage)
        return damage
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage
        
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        if isinstance(damage, (int, float)) is False:
            damage = 0.0
        if damage < 0:
            damage = 0.0
        if damage > 10000:
            damage = 10000.0
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0.0
        return self.health
        
        
        
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0
        
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"{self.name} ({getattr(self, 'character_class', 'Character')}): "
              f"HP={self.health}, STR={self.strength}, MAG={self.magic}")

        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        super().__init__(name, health, strength, magic)
        self.character_class = str(character_class)
        self.level = 1
        self.experience = 0
        # TODO: Call super().__init__() with the basic character info
        # TODO: Store the character_class (like "Warrior", "Mage", etc.)
        # TODO: Add any other player-specific attributes (level, experience, etc.)
        
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        print(
            f"{self.name} ({self.character_class}) -> "
            f"HP={self.health}, STR={self.strength}, MAG={self.magic}"
        )

        # TODO: Call the parent's display_stats method using super()
        # TODO: Then print additional player info like class and level
        

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        super().__init__(name, "Warrior", 120, 15, 5)
        # TODO: Call super().__init__() with warrior-appropriate stats
        # Suggested stats: health=120, strength=15, magic=5
        
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        damage = max(0, int(self.strength))
        if hasattr(target, "take_damage"):
            target.take_damage(damage)
        return damage
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = self.strength * 2
        if hasattr(target, "take_damage"):
            target.take_damage(damage)
        return damage
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack
        

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
        super().__init__(name, "Mage", 80, 8, 20)
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        damage = max(0, int(self.magic))
        if hasattr(target, "take_damage"):
            target.take_damage(damage)
        return damage
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength
        
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = self.magic * 2
        if hasattr(target, "take_damage"):
            target.take_damage(damage)
        return damage
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus
        

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
        super().__init__(name, "Rogue", 90, 12, 10)
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        damage = max(0, int(self.strength))
        if hasattr(target, "take_damage"):
            target.take_damage(damage)
        return damage
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        damage = self.strength * 2.5
        if hasattr(target, "take_damage"):
            target.take_damage(damage)
        return damage

        # TODO: Implement sneak attack
        # Should always do critical damage
        

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = str(name)
        if isinstance(damage_bonus, (int, float)):
            self.damage_bonus = float(damage_bonus)
        else:
            self.damage_bonus = 0.0
        # TODO: Store weapon name and damage bonus
        
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        return f"Weapon: {self.name}, Damage Bonus: +{self.damage_bonus}"
        # TODO: Print weapon name and damage bonus
        

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
