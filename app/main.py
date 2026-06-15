import gradio as gr
from dotenv import load_dotenv
from core.research_manager import ResearchManager

load_dotenv()


async def run(query: str):

    output = ""

    async for chunk in ResearchManager().run(query):
        output += f"\n{chunk}\n"
        yield output


with gr.Blocks() as ui:

    gr.Markdown("# Deep Research Agent")

    query_textbox = gr.Textbox(
        label="Research Topic",
        placeholder="Enter a topic..."
    )

    output_box = gr.Textbox(
        label="Output",
        lines=25
    )

    run_button = gr.Button("Run Research")

    run_button.click(
        fn=run,
        inputs=query_textbox,
        outputs=output_box
    )

    query_textbox.submit(
        fn=run,
        inputs=query_textbox,
        outputs=output_box
    )


ui.launch(
    server_name="127.0.0.1",
    server_port=7860,
    share=True,
    inbrowser=True
)