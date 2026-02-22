class CorrectiveRAG:

    def __init__(self, retriever, grader, generator, transformer):
        self.retriever = retriever
        self.grader = grader
        self.generator = generator
        self.transformer = transformer

    def run(self, query):
        docs = self.retriever(query)
        filtered_docs = self.grader(query, docs)

        if not filtered_docs:
            query = self.transformer(query)
            docs = self.retriever(query)
            filtered_docs = self.grader(query, docs)

        return self.generator(query, filtered_docs)