**📘 Generation Augmentée par Récupération (RAG Correctif)**

Implémentation complète d’un RAG (Retrieval-Augmented Generation) avec une boucle corrective (CRAG) permettant d’améliorer la pertinence des réponses générées par un modèle de langage.


Ce projet démontre comment :

->Indexer un corpus

->Effectuer une recherche sémantique vectorielle

->Filtrer les documents non pertinents

->Reformuler automatiquement la requête si nécessaire

->Générer une réponse finale basée uniquement sur un contexte fiable

**Qu'est-ce que le RAG Correctif ?**

Le RAG Correctif (CRAG) améliore le RAG en vérifiant et corrigeant l’étape de récupération avant la génération.

Le process :

Récupérer les documents → Récupérer les chunks candidats.

Noter la pertinence → Évaluer si chaque document est vraiment lié à la question de l’utilisateur.

Filtrer → Garder uniquement les documents pertinents, éliminer les non pertinents.

Corriger la query → Si aucun bon document n’est trouvé, réécrire la query et réessayer la récupération.

Générer la réponse → Utiliser uniquement les documents fiables et pertinents pour la réponse finale.

**Analogie:**
RAG classique : Vous posez une question à un ami, il vous apporte une pile de livres qui pourraient aider, et il essaie de répondre immédiatement.

RAG Correctif : L’ami parcourt les livres, élimine ceux qui ne sont pas pertinents, et si aucun n’est utile, il reformule votre question et cherche à nouveau. Ce n’est qu’ensuite qu’il répond.

**Avantages**

Réduit les hallucinations en éliminant le contexte non pertinent.

Produit des réponses plus précises et dignes de confiance.

Ajoute de la robustesse car il peut réessayer si la première tentative de récupération échoue.

**Point clé**

RAG Correctif = RAG + une boucle de filtrage et de correction.
Il rend la récupération plus intelligente et plus fiable en validant les documents et en affinant les queries avant de générer la réponse finale.



Generation-augmente-par-recuperation/
│
├──Diagrammes/
│   ├── DIAGRAMME_SEQUENCE.png
│   ├── RAG correctif – diagramme d'activité.png
├──Fichiers pdf/
│   ├── atos-retrieval-augmented-generation-ai-whitepaper.pdf
│   ├── Corrective_Retrieval_Augm.pdf
│   ├── IA_et_Transformation digitale.pdf
│   ├── Tabular_list_of_deseases.py
├── src/
│   ├── data_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── grader.py
│   ├── query_transform.py
│   └── pipeline.py
│
├── models/
│   ├── generation_model.py
│   └── model_config.py
│
├── Test/
│   └── Test_rag_correctif.py
│
└── requirements.txt



⚙️ Fonctionnement du pipeline

1️⃣ Chargement des documents
2️⃣ Découpage en chunks
3️⃣ Génération des embeddings
4️⃣ Indexation dans FAISS
5️⃣ Recherche sémantique
6️⃣ Filtrage des documents non pertinents
7️⃣ Reformulation si aucun bon document
8️⃣ Génération finale via LLM

![alt text](<Diagrammes/RAG correctif – diagramme d'activité.png>)


🚀 Installation

git clone https://github.com/Yobapatrick/Generation-augmente-par-recuperation.git
cd Generation-augmente-par-recuperation

python -m venv venv
source venv/bin/activate   # Windows : venv\Scripts\activate

pip install -r requirements.txt

python TEST/Test_rag_correctif.py


⭐ Auteur
Patrick Yoba
Étudiant ingénieur 3IL INGENIEURS – Data & IA
Passionné par les architectures LLM, RAG et systèmes intelligents.