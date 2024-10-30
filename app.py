import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="Generate a comprehensive blog relavant to the title  and keywods blockchain  The blog should be (num_words) words in length and ensure to mantain same tone during the entire blog . ensure the content is suitable for online audience and is always academically keyword intensive.\n",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Generate a comprehensive blog relavant to the title Finance and blockchain and keywods blockchain , decentralised ledger Interplanetary Filing system , ethereum , cryptocurrency  The blog should be exactly  500 words in length and ensure to mantain same tone during the entire blog . ensure the content is suitable for online audience and is always academically keyword intensive.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Finance and Blockchain: A Decentralized Revolution\n\nThe intersection of finance and blockchain technology is rapidly reshaping the global economic landscape.  Blockchain, a decentralized ledger technology, offers unprecedented opportunities for innovation in various financial sectors, from payments and remittances to asset management and securities trading.  This distributed ledger system, secured by cryptography, provides transparency, immutability, and security, features highly sought after in the traditional financial world.\n\nOne of the most prominent applications of blockchain in finance is the emergence of cryptocurrencies like Bitcoin and Ethereum. These digital currencies utilize blockchain as their underlying infrastructure, enabling peer-to-peer transactions without intermediaries like banks. Ethereum, in particular, extends beyond simple cryptocurrency functionality.  Its smart contract capabilities facilitate programmable agreements and automated execution, opening doors for decentralized finance (DeFi) applications.  These DeFi platforms leverage smart contracts to offer services traditionally provided by centralized financial institutions, including lending, borrowing, and decentralized exchanges.\n\nThe decentralized nature of blockchain fosters financial inclusion by reducing reliance on traditional banking systems.  Individuals without access to conventional financial services can participate in the global economy through blockchain-based solutions.  This empowerment is particularly significant in developing nations where access to banking infrastructure is limited.  Furthermore, blockchain simplifies cross-border transactions, reducing costs and processing times associated with traditional remittance systems.\n\nThe immutability of the blockchain also enhances security and reduces the risk of fraud.  Once a transaction is recorded on the blockchain, it cannot be altered or deleted, creating a permanent and auditable record.  This characteristic is invaluable in combatting financial crimes and ensuring transparency in financial operations.\n\nAnother crucial aspect of blockchain in finance is its potential to streamline and automate complex processes.  Smart contracts can automate various financial agreements, from insurance claims processing to supply chain finance.  This automation reduces operational costs and increases efficiency, benefiting both businesses and consumers.\n\nMoreover, blockchain's impact extends to areas like asset tokenization and fractional ownership.  Traditional illiquid assets like real estate or art can be represented as digital tokens on a blockchain, facilitating easier trading and fractional ownership. This democratizes investment opportunities, allowing a broader range of investors to participate in previously inaccessible markets.\n\nLooking ahead, the integration of blockchain with other emerging technologies like the InterPlanetary File System (IPFS) holds immense potential. IPFS, a peer-to-peer distributed file system, can enhance the scalability and resilience of blockchain networks.  By storing large datasets and files on IPFS, blockchain applications can overcome storage limitations and improve performance.  This combination creates a powerful synergy, fostering further innovation in decentralized finance and beyond.\n\nHowever, the widespread adoption of blockchain in finance also faces challenges. Regulatory uncertainty, scalability limitations, and interoperability issues are some of the hurdles that need to be addressed.  As regulatory frameworks evolve and technological advancements continue, the integration of blockchain into the financial ecosystem is expected to accelerate, transforming the industry and empowering individuals globally. The future of finance is undeniably intertwined with the decentralized revolution powered by blockchain technology.  From cryptocurrencies and DeFi to asset tokenization and enhanced security, blockchain is poised to redefine the financial landscape, offering a more transparent, efficient, and inclusive future for all.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Generate a comprehensive blog relavant to the title Finance and blockchain and keywods blockchain , decentralised ledger Interplanetary Filing system , ethereum , cryptocurrency  The blog should be exactly  500 words in length and ensure to mantain same tone during the entire blog . ensure the content is suitable for online audience and is always academically keyword intensive.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Finance and Blockchain: A Decentralized Paradigm Shift\n\nThe convergence of finance and blockchain technology is driving a profound transformation within the global financial ecosystem. Blockchain, a decentralized ledger technology, presents unparalleled opportunities for innovation across diverse financial sectors, spanning payments and remittances to complex securities trading and asset management. This distributed ledger system, secured by cryptographic principles, offers transparency, immutability, and enhanced security, attributes highly coveted within the traditionally centralized financial world.\n\nA prominent manifestation of blockchain's influence",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)


blog="Investment banking is a high-pressure, fast-paced industry that offers significant financial rewards and career advancement opportunities, but also comes with long hours and demanding work schedules. Investment bankers are known for their grueling work hours, often exceeding 60-80 hours per week, and during peak times or when working on specific deals, these hours can extend to 100+ hours per week. The work schedule can be highly unpredictable, with late nights and weekend work being common, disrupting work-life balance and requiring significant personal sacrifice. The intensity of the workload varies depending on the level of seniority, with junior bankers tending to have the most demanding schedules, while senior bankers may have more flexibility. Some of the top investment banks globally include Goldman Sachs, Morgan Stanley, JPMorgan Chase, Bank of America Merrill Lynch, Citigroup, Deutsche Bank, and Barclays. Most investment banking careers start with an analyst program, typically a two-year commitment, involving rigorous training and hands-on experience in various aspects of investment banking. After completing the analyst program, successful individuals can progress to the associate level, taking on more responsibility and having greater client interaction. Further career progression leads to the vice president level, where individuals manage teams and oversee complex deals. The highest level of achievement in investment banking is the managing director role, which involves significant leadership responsibilities and strategic decision-making. Investment banking offers competitive compensation packages, especially at the junior levels, but the salary can vary significantly based on factors such as the bank, location, role, and individual performance. A rough estimate of the salary range for different levels in investment banking is as follows: Analyst: $80,000 - $150,000 (base salary) + significant bonuses, Associate: $150,000 - $300,000 (base salary) + bonuses, Vice President: $300,000 - $500,000 (base salary) + bonuses, Managing Director: $500,000+ (base salary) + significant bonuses. It's important to note that these are just estimates, and actual salaries can vary widely. Additionally, investment banking also offers lucrative benefits packages, including stock options, healthcare, and retirement plans."


# Streamlit UI
st.title("📚 BlogMate: AI Blog Buddy")
st.subheader("🤖 Craft your Blog with AI as your buddy")

# Sidebar for user input
with st.sidebar:
    st.title("What do you want to write about?")
    st.subheader("Describe your blog...")

    # Input fields for user data
    blog_title = st.text_input("Blog Title")
    keywords = st.text_input("Keywords (separated by commas)")
    Number_of_words = st.slider("Number of Words", min_value=200, max_value=1000, step=100)
    Number_of_Images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

    # Button to submit inputs
    submit_button = st.button("Generate Blog")

# Generate blog if submit button is clicked
if submit_button:
    

    # Display the response in Streamlit
    st.image("gettyimages-1338523352-612x612.jpg")
    st.write(blog)
    