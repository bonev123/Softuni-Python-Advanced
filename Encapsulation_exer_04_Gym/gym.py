from typing import Dict, List

from Encapsulation_exer_04_Gym.customer import Customer
from Encapsulation_exer_04_Gym.equipment import Equipment
from Encapsulation_exer_04_Gym.exercise_plan import ExercisePlan
from Encapsulation_exer_04_Gym.subscription import Subscription
from Encapsulation_exer_04_Gym.trainer import Trainer


class Gym:
    #     def __init__(self):
    #         self.customers = []
    #         self.trainers = []
    #         self.equipment = []
    #         self.plans = []
    #         self.subscriptions = []
    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

        self._customer_by_id: Dict[int, Customer] = {}
        self._trainer_by_id: Dict[int, Trainer] = {}
        self._equipment_by_id: Dict[int, Equipment] = {}
        self._plan_by_id: Dict[int, ExercisePlan] = {}
        self._subscription_by_id: Dict[int, Subscription] = {}

    #     def add_customer(self, customer):
    #         if customer not in self.customers:
    #             self.customers.append(customer)
    #
    #     def add_trainer(self, trainer):
    #         if trainer not in self.trainers:
    #             self.trainers.append(trainer)
    #
    #     def add_equipment(self, equipment):
    #         if equipment not in self.equipment:
    #             self.equipment.append(equipment)
    #
    #     def add_plan(self, plan):
    #         if plan not in self.plans:
    #             self.plans.append(plan)
    #
    #     def add_subscription(self, subscription):
    #         if subscription not in self.subscriptions:
    #             self.subscriptions.append(subscription)

    # @staticmethod
    #     def get_object(object_id, class_iterable):
    #         return list(filter(lambda _: _.id == object_id, class_iterable))

    #     def subscription_info(self, subscription_id):
    #         csubscription = self.get_object(subscription_id, self.subscriptions)
    #         customer_id = csubscription.customer_id
    #         ccustomer = self.get_object(customer_id, self.customers)
    #         trainer_id = csubscription.trainer_id
    #         ctrainer = self.get_object(trainer_id, self.trainers)
    #         cplan = self.get_object(trainer_id, self.plans)
    #         cequipment = self.get_object(cplan.equipment_id, self.equipments)
    #         return f"{csubscription}\n{ccustomer}\n{ctrainer}\n{cplan}\n{cequipment}"
    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)
        self._customer_by_id[customer.id] = customer

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)
        self._trainer_by_id[trainer.id] = trainer

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)
        self._equipment_by_id[equipment.id] = equipment

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)
        self._plan_by_id[plan.id] = plan

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)
        self._subscription_by_id[subscription.id] = subscription

    def subscription_info(self, subscription_id: int):
        subscription = self._subscription_by_id[subscription_id]
        customer = self._customer_by_id[subscription.customer_id]
        trainer = self._trainer_by_id[subscription.trainer_id]
        plan = self._plan_by_id[subscription.exercise_id]
        equipment = self._equipment_by_id[plan.equipment_id]

        return '\n'.join([
            repr(subscription),
            repr(customer),
            repr(trainer),
            repr(equipment),
            repr(plan)
        ])