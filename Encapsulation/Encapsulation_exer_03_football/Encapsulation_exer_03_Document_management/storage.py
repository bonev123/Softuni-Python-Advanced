class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for c in self.categories:
            if c.id == category_id:
                c.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for t in self.topics:
            if t.id == topic_id:
                t.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        for d in self.documents:
            if d.id == document_id:
                d.edit(new_file_name)

    def delete_category(self, category_id):
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)

    def delete_topic(self, topic_id):
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)

    def delete_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def get_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                return d

    def __repr__(self) -> str:
        message = []
        NL = '\n'
        for d in self.documents:
            message.append(repr(d))

        return NL.join(message)


