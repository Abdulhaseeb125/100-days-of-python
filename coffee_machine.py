from list import Menu, resources
import prettytable


class Coffee:
    def __init__(self):
        self.profit = 0

    def refill(self):
        """
        Refills the resources by +500
        """
        for resource in resources:
            resources[resource] += 500

    def resources_details(self):
        re_table = prettytable.PrettyTable()
        resource = []
        amount = []

        for key in resources:
            resource.append(key)
            amount.append(resources[key])
        re_table.add_column("Resource", resource)
        re_table.add_column("Amount(ml)", amount)
        return re_table

    def resource_checker(self, selection):
        count = 0
        for key1 in Menu[selection]["ingredients"]:
            if resources[key1] >= Menu[selection]["ingredients"][key1]:
                  count +=1
        if count == 3:
            for key1 in Menu[selection]["ingredients"]:
                resources[key1] -= Menu[selection]["ingredients"][key1]
                self.profit += Menu[selection]["cost"]
                return True
            else:
                return False


    def MENU(self):
        table = prettytable.PrettyTable()
        cost = []
        names = []
        for i in Menu:
            cost.append(Menu[i]["cost"])
            names.append(i)
        table.add_column("Name", names)
        table.add_column("Price", cost)
        return table
