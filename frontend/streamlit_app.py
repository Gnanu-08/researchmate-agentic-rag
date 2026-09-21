import streamlit as st
from app.agents.controller import run_agent

st.set_page_config(page_title="ResearchMate", page_icon="🤖", layout="wide")
st.title("🤖 ResearchMate")
st.caption("Provider-independent Agentic AI + RAG Research Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("System")
    st.write("Agent workflow: Planner → Retriever → Evaluator → Generator")
    st.write("LLM provider is configured in `.env`.")
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sources"):
            with st.expander("Sources"):
                for s in message["sources"]:
                    st.write(f"**{s['source']}**" + (f" — page {s['page']}" if s["page"] else ""))
                    st.caption(s["content"])

question = st.chat_input("Ask something about the knowledge base...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Agent is working..."):
            result = run_agent(question)
        st.markdown(result.answer)
        with st.expander("Agent trace"):
            for step in result.steps:
                st.write("• " + step)
        if result.sources:
            with st.expander("Sources"):
                for s in result.sources:
                    st.write(f"**{s.source}**" + (f" — page {s.page}" if s.page else ""))
                    st.caption(s.content)

    st.session_state.messages.append({
        "role": "assistant",
        "content": result.answer,
        "sources": [s.model_dump() for s in result.sources]
    })
