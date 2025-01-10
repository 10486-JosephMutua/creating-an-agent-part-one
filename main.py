from src.helper import load_pdf, text_split, HuggingFaceInferenceAPIEmbeddings

from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os
load_dotenv()
inference_api_key=os.getenv("inference_api_key")

notes="The maintenance stage of opioid pharmacotherapy begins when a patient is responding optimally to medication treatment and routine dosage adjustments are no longer needed. Patients at this stage have stopped abusing opioids and other substances and have resumed productive lifestyles away from the people, places, and things associated with their addictions. These patients typically receive scheduled take-home medication privileges. Patients who continue to abuse substances, do not seek employment, or remain connected to their drugusing social networks have not reached this stage. Along with continued observed medication treatment, these latter patients are candidates for intensified counseling and other services to help them reach the maintenance stage.During the maintenance stage, many patients remain on the same dosage of treatment medication for many months, whereas others require frequent or occasional adjustments. Periods of increased stress, strenuous physical labor, negative environmental factors, greater drug availability, pregnancy, or increased drug hunger can reawaken the need for increased dosages over short or extended periods. Serious emotional crises may require long-term or temporary dosage adjustments. Although the counseling relationship and patient interview are paramount, drug test reports and medication blood levels are useful for dosage determination and adjustment during and after transition from stabilization to the maintenance stageMedically Supervised Withdraw alWhen stable patients in the maintenance stage ask for dosage reductions, it is important to explore their reasons. They might believe that they can get by on less medication, or they might be responding to external pressures. Patients often perceive that those on lower dosages are ìbetter patients.î These situations require physicians or other staff members to educate patients and their significant others about the importance of adequate dosage and how individual differences in absorption, body weight, metabolism, and tolerance can affect the dosage necessary to achieve stability (Leavitt et al. 2000).Voluntary Tapering and Dosag e ReductionFor various reasons, some patients attempt reduction or cessation of maintenance medication. Some studies indicate high relapse rates, often 80 percent or more, for this group, including patients judged to be rehabilitated before tapering (e.g., Magura and Rosenblum 2001). However, the likelihood of successful dose tapering also depends on individual factors such as motivation and family support. The possibility of relapse should be explained to patients who want to dose taper, especially those who are not stable on their current dosage, as part of the informed-consent process. Patients who choose tapering should be monitored closely and taught relapse prevention strategies. They and their families should be aware of risk factors for relapse during and after tapering. If relapse occurs or is likely, additional therapeutic measures can be taken, including rapid resumption of MAT when appropriate (American Society of Addiction Medicine 1997).Ideally, withdrawal should be attempted when it is desired strongly by a stable patient who has a record of abstinence and has adjusted positively on MAT. However, sometimes dose tapering is necessary for administrative reasons, such as a response to extreme antisocial behavior, noncompliance with minimal program standards, or a move to a location where MAT is unavailable. In such cases, providers should refer patients to other programs that are more reasonable and practical in terms of the patientsí overall situation (e.g., motivation, resource availability, ability to pay).In a review of research on withdrawal from MAT, Magura and Rosenblum (2001) noted that many treatment providers lacked effective ways to improve outcomes for patients who undertook planned withdrawal and that opioid craving remained prevalent in this group, even after successful physiological withdrawal. They concluded, therefore, that planned withdrawal from opioid pharmacotherapy should be undertaken conservatively.Relapse prevention techniques should be incorporated into counseling and other support services both before and during dosage reduction. Such structured techniques can be useful safeguards in preventing and preparing for relapse. Use of mutual-help techniques (see chapter 8) is recommended highly, especially during dosage reduction.Although most data about outcomes after tapering from opioid medication come from studies of methadone maintenance, the consensus panel believes that success rates are likely to be similar for patients who taper from buprenorphine or LAAM, and similar cautions and monitoring processes should be in place.Methadone dosage reductionThe techniques and rates of graded methadone reduction vary widely among patients. One common practice is to reduce daily doses in roughly 5- to 10-percent increments with 1 to 2 weeks between reductions, adjusting as needed for patient conditions. Because reductions become smaller but intervals remain about the same, many months may be spent in such graded reductions. The rate of withdrawal can be increased or decreased based on individual patient response. A slow withdrawal gives patients and staff time to stop the tapering or resume maintenance if tapering is not working and relapse seems likely.Regardless of the rate of withdrawal from methadone, a point usually is reached at which steady-state occupancy of opiate receptors is no longer complete and discomfort, often with drug hunger and craving, emerges. This point may occur at any dosage but is more common with methadone when the dosage is below 40 mg per day. Highly motivated patients with good support systems can continue withdrawal despite these symptoms. Some patients appear to have specific thresholds at which further dosage reductions become difficult.Physicians and other st"




PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

print(PINECONE_API_KEY)
print(PINECONE_API_ENV)



text_chunks = text_split(notes)
embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)


index_name="agent"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=Pinecone.from_texts(embeddings, index_name=index_name)


























