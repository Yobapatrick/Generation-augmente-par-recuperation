#Executer l'application de type correctif RAG avec une question

input_state={
    "question": "liste quelque maladies infectieuses et les sympotomes?"
}

#Invoquer le graphe
result=app.invoke(input_state)
#afficher la question
print("Question: \n", input_state["question"])

#afficher la reponse finale

print("\n\n--------Execution de l'application terminé----------")
print("\nRéponse finale: \n", result.get("generation","").strip())

#afficher la question éventuellement reformulée
print("\nQuestion reformulée: \n", result.get("question","").strip())


#Collecter les sources (retriever + recher web)
def extract_source(md: dict) -> str:
  if not md:
    return ""
  return md.get("source") or md.get("title") or md.get("url") or ""
  seen= set()
  sources=[]
  for doc in result.get("documents",[]):

    source=extract_source(getattr(doc,"metadata",{}))
    if source not in seen:
      seen.add(source)
      sources.append(source)