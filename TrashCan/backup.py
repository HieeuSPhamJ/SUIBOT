with open("./bank.json","r") as f:
          users = json.load(f)
        wallet = users[str(member.id)]['wallet']