from Encapsulation_exer_03_Document_management.category import Category
from Encapsulation_exer_03_Document_management.document import Document
from Encapsulation_exer_03_Document_management.storage import Storage
from Encapsulation_exer_03_Document_management.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize Encapsulation_exer_03_Document_management")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
