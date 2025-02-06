def physicalAttack(target, attacker):
    # 取自明日方舟 https://prts.wiki/w/%E6%B8%B8%E6%88%8F%E6%95%B0%E6%8D%AE%E5%9F%BA%E7%A1%80

    dmg = max(0.05 * attacker.atk, attacker.atk - max(0, target.dp))
    target.changeHealth(-dmg)
    print(f"{attacker.name} attacked {target.name}, dealing {dmg} damage\n"
          f"{target.name} is now at {target.hp} HP\n")
