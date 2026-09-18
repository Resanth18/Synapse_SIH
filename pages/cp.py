
import streamlit as st
import pandas as pd
from crop_database import get_crop_database
from recommendation_engine import CropRecommendationEngine
from image_analyzer import ImageAnalyzer
from voice_processor import VoiceProcessor
from economic_advisor import EconomicAdvisor
import base64
import time
import webbrowser
from PIL import Image
import io
import streamlit as st
from weather_alerts import run_weather_alerts


st.set_page_config(
    page_title="Farmer Planner App",
    page_icon="🌱",
    layout="wide"   # 👈 this makes app wide screen
)


st.title("🌱 Welcome to the Farmer Planner App!")
st.write("You’re logged in successfully 🎉")


# Initialize the recommendation engine and other modules
@st.cache_resource
def load_recommendation_engine():
    return CropRecommendationEngine()

@st.cache_resource
def load_image_analyzer():
    return ImageAnalyzer()

@st.cache_resource
def load_voice_processor():
    return VoiceProcessor()

@st.cache_resource
def load_economic_advisor():
    return EconomicAdvisor()

# Language translations
def get_translations():
    return {
        'English': {
            'title': '🌾 Farmer Planner AI',
            'subtitle': 'Get personalized crop recommendations for your farm',
            'language_prompt': 'Hello! Which language would you like to continue in?',
            'land_size': 'What is the size of your land?',
            'land_size_help': 'Enter your farmland size in acres (e.g., 1.5 acres)',
            'soil_type': 'What type of soil do you have?',
            'soil_help': 'Choose your soil type. If not sure, Loamy is good for most crops.',
            'season': 'When do you want to plant?',
            'season_help': 'Choose your planting season',
            'budget': 'How much money can you spend?',
            'budget_help': 'Enter your budget in dollars for seeds, fertilizer, and supplies',
            'get_recommendations': 'Get My Crop Suggestions',
            'recommendations_title': 'Best Crops for Your Farm',
            'farm_summary': 'Your Farm',
            'acres': 'acres',
            'soil': 'soil',
            'planting': 'planting',
            'budget_text': 'budget',
            'economics': 'Money Details',
            'growing_info': 'Growing Details',
            'cost_per_acre': 'Cost per acre',
            'expected_yield': 'Expected harvest',
            'profit_potential': 'Profit potential',
            'growing_time': 'Growing time',
            'difficulty': 'Difficulty',
            'water_needs': 'Water needs',
            'why_crop': 'Why this crop?',
            'growing_tips': 'Growing Tips',
            'budget_breakdown': 'Budget Breakdown',
            'total_cost': 'Total cost for top 3 crops',
            'your_budget': 'Your budget',
            'can_afford': 'You can afford these crops!',
            'budget_warning': 'Consider fewer crops or cheaper options.',
            'no_crops': 'No suitable crops found. Try different inputs.',
            'general_tips': 'General Tips',
            'about_tool': 'About This Tool',
            'tool_description': 'This AI helper suggests the best crops for your specific farm by considering your land size, soil type, planting season, and budget.',
            'get_started': 'Fill in your farm details above to get started!'
        },
        'Hindi': {
            'title': '🌾 किसान योजना AI',
            'subtitle': 'अपने खेत के लिए व्यक्तिगत फसल सुझाव पाएं',
            'language_prompt': 'नमस्ते! आप किस भाषा में जारी रखना चाहते हैं?',
            'land_size': 'आपकी जमीन का आकार क्या है?',
            'land_size_help': 'अपनी खेती की जमीन एकड़ में लिखें (जैसे 1.5 एकड़)',
            'soil_type': 'आपकी मिट्टी किस प्रकार की है?',
            'soil_help': 'अपनी मिट्टी का प्रकार चुनें। अगर पता नहीं है, तो दोमट अच्छी है।',
            'season': 'आप कब बोना चाहते हैं?',
            'season_help': 'अपना बुवाई का मौसम चुनें',
            'budget': 'आप कितना पैसा खर्च कर सकते हैं?',
            'budget_help': 'बीज, खाद और सामान के लिए अपना बजट रुपयों में लिखें',
            'get_recommendations': 'मेरी फसल सुझाव पाएं',
            'recommendations_title': 'आपके खेत के लिए सबसे अच्छी फसलें',
            'farm_summary': 'आपका खेत',
            'acres': 'एकड़',
            'soil': 'मिट्टी',
            'planting': 'बुवाई',
            'budget_text': 'बजट',
            'economics': 'पैसे की जानकारी',
            'growing_info': 'उगाने की जानकारी',
            'cost_per_acre': 'प्रति एकड़ लागत',
            'expected_yield': 'अपेक्षित फसल',
            'profit_potential': 'लाभ की संभावना',
            'growing_time': 'उगने का समय',
            'difficulty': 'कठिनाई',
            'water_needs': 'पानी की जरूरत',
            'why_crop': 'यह फसल क्यों?',
            'growing_tips': 'उगाने की सलाह',
            'budget_breakdown': 'बजट विवरण',
            'total_cost': 'टॉप 3 फसलों की कुल लागत',
            'your_budget': 'आपका बजट',
            'can_afford': 'आप इन फसलों को उगा सकते हैं!',
            'budget_warning': 'कम फसलें या सस्ते विकल्प चुनें।',
            'no_crops': 'कोई उपयुक्त फसल नहीं मिली। अलग जानकारी दें।',
            'general_tips': 'सामान्य सलाह',
            'about_tool': 'इस टूल के बारे में',
            'tool_description': 'यह AI सहायक आपकी जमीन, मिट्टी, मौसम और बजट के अनुसार सबसे अच्छी फसलों का सुझाव देता है।',
            'get_started': 'शुरू करने के लिए ऊपर अपने खेत की जानकारी भरें!'
        },
        'Tamil': {
            'title': '🌾 விவசாயி திட்ட AI',
            'subtitle': 'உங்கள் பண்ணைக்கான தனிப்பட்ட பயிர் பரிந்துரைகளைப் பெறுங்கள்',
            'language_prompt': 'வணக்கம்! நீங்கள் எந்த மொழியில் தொடர விரும்புகிறீர்கள்?',
            'land_size': 'உங்கள் நிலத்தின் அளவு என்ன?',
            'land_size_help': 'உங்கள் விவசாய நிலத்தின் அளவை ஏக்கரில் உள்ளிடுங்கள் (எ.கா. 1.5 ஏக்கர்)',
            'soil_type': 'உங்களிடம் எந்த வகை மண் உள்ளது?',
            'soil_help': 'உங்கள் மண் வகையைத் தேர்ந்தெடுங்கள். தெரியவில்லை என்றால், களிமண் நல்லது.',
            'season': 'எப்போது விதைக்க விரும்புகிறீர்கள்?',
            'season_help': 'உங்கள் விதைப்பு பருவத்தைத் தேர்ந்தெடுங்கள்',
            'budget': 'நீங்கள் எவ்வளவு பணம் செலவழிக்க முடியும்?',
            'budget_help': 'விதைகள், உரம் மற்றும் பொருட்களுக்கான உங்கள் பட்ஜெட்டை ரூபாயில் உள்ளிடுங்கள்',
            'get_recommendations': 'எனது பயிர் பரிந்துரைகளைப் பெறுங்கள்',
            'recommendations_title': 'உங்கள் பண்ணைக்கான சிறந்த பயிர்கள்',
            'farm_summary': 'உங்கள் பண்ணை',
            'acres': 'ஏக்கர்',
            'soil': 'மண்',
            'planting': 'விதைப்பு',
            'budget_text': 'பட்ஜெட்',
            'economics': 'பணம் விவரங்கள்',
            'growing_info': 'வளர்ப்பு விவரங்கள்',
            'cost_per_acre': 'ஏக்கருக்கான செலவு',
            'expected_yield': 'எதிர்பார்க்கப்படும் அறுவடை',
            'profit_potential': 'லாப சாத்தியம்',
            'growing_time': 'வளரும் நேரம்',
            'difficulty': 'சிரமம்',
            'water_needs': 'நீர் தேவை',
            'why_crop': 'இந்த பயிர் ஏன்?',
            'growing_tips': 'வளர்ப்பு குறிப்புகள்',
            'budget_breakdown': 'பட்ஜெட் விவரம்',
            'total_cost': 'முதல் 3 பயிர்களின் மொத்த செலவு',
            'your_budget': 'உங்கள் பட்ஜெட்',
            'can_afford': 'நீங்கள் இந்த பயிர்களை வளர்க்க முடியும்!',
            'budget_warning': 'குறைவான பயிர்கள் அல்லது மலிவான விருப்பங்களைக் கருத்தில் கொள்ளுங்கள்.',
            'no_crops': 'பொருத்தமான பயிர்கள் கிடைக்கவில்லை. வெவ்வேறு உள்ளீடுகளை முயற்சிக்கவும்.',
            'general_tips': 'பொதுவான குறிப்புகள்',
            'about_tool': 'இந்த கருவி பற்றி',
            'tool_description': 'இந்த AI உதவியாளர் உங்கள் நிலம், மண், பருவம் மற்றும் பட்ஜெட்டைக் கருத்தில் கொண்டு சிறந்த பயிர்களை பரிந்துரைக்கிறது.',
            'get_started': 'தொடங்க மேலே உங்கள் பண்ணை விவரங்களை நிரப்பவும்!'
        },
        'Telugu': {
            'title': '🌾 రైతు ప్రణాళిక AI',
            'subtitle': 'మీ పొలానికి వ్యక్తిగత పంట సిఫార్సులను పొందండి',
            'language_prompt': 'నమస్కారం! మీరు ఏ భాషలో కొనసాగించాలని అనుకుంటున్నారు?',
            'land_size': 'మీ భూమి పరిమాణం ఎంత?',
            'land_size_help': 'మీ వ్యవసాయ భూమి పరిమాణాన్ని ఎకరాల్లో నమోదు చేయండి (ఉదా. 1.5 ఎకరాలు)',
            'soil_type': 'మీకు ఏ రకమైన నేల ఉంది?',
            'soil_help': 'మీ నేల రకాన్ని ఎంచుకోండి. తెలియకపోతే, లోమీ మంచిది.',
            'season': 'మీరు ఎప్పుడు విత్తాలని అనుకుంటున్నారు?',
            'season_help': 'మీ విత్తన సీజన్‌ను ఎంచుకోండి',
            'budget': 'మీరు ఎంత డబ్బు ఖర్చు పెట్టగలరు?',
            'budget_help': 'విత్తనాలు, ఎరువులు మరియు సామాగ్రి కోసం మీ బడ్జెట్‌ను రూపాయల్లో నమోదు చేయండి',
            'get_recommendations': 'నా పంట సిఫార్సులను పొందండి',
            'recommendations_title': 'మీ పొలానికి అత్యుత్తమ పంటలు',
            'farm_summary': 'మీ పొలం',
            'acres': 'ఎకరాలు',
            'soil': 'నేల',
            'planting': 'విత్తనం',
            'budget_text': 'బడ్జెట్',
            'economics': 'డబ్బు వివరాలు',
            'growing_info': 'పెరుగుదల వివరాలు',
            'cost_per_acre': 'ఎకరాకు ఖర్చు',
            'expected_yield': 'ఆశించిన దిగుబడి',
            'profit_potential': 'లాభ సంభావ్యత',
            'growing_time': 'పెరుగుదల సమయం',
            'difficulty': 'కష్టం',
            'water_needs': 'నీటి అవసరం',
            'why_crop': 'ఈ పంట ఎందుకు?',
            'growing_tips': 'పెరుగుదల చిట్కాలు',
            'budget_breakdown': 'బడ్జెట్ వివరణ',
            'total_cost': 'టాప్ 3 పంటల మొత్తం ఖర్చు',
            'your_budget': 'మీ బడ్జెట్',
            'can_afford': 'మీరు ఈ పంటలను పెంచగలరు!',
            'budget_warning': 'తక్కువ పంటలు లేదా తక్కువ ఖర్చైన ఎంపికలను పరిగణించండి.',
            'no_crops': 'తగిన పంటలు దొరకలేదు. వేరే ఇన్‌పుట్‌లను ప్రయత్నించండి.',
            'general_tips': 'సాధారణ చిట్కాలు',
            'about_tool': 'ఈ సాధనం గురించి',
            'tool_description': 'ఈ AI సహాయకుడు మీ భూమి, నేల, సీజన్ మరియు బడ్జెట్‌ను పరిగణనలోకి తీసుకుని అత్యుత్తమ పంటలను సిఫార్సు చేస్తుంది.',
            'get_started': 'ప్రారంభించడానికి పైన మీ పొలం వివరాలను నింపండి!'
        },
        'Odia': {
            'title': '🌾 କୃଷକ ପ୍ରଣାଳୀ AI',
            'subtitle': 'ଆପଣଙ୍କ ଖେତ ପାଇଁ ବ୍ୟକ୍ତିଗତ ଫସଲ ସୁପାରିଶ ପାଇନ୍ତୁ',
            'language_prompt': 'ନମସ୍କାର! ଆପଣ କେମିତି ଭାଷାରେ ଚାଲୁ ରଖିବାକୁ ଚାହୁଁଛନ୍ତି?',
            'land_size': 'ଆପଣଙ୍କ ଜମିର ଆକାर କେତେ?',
            'land_size_help': 'ଆପଣଙ୍କ ଚାଷଜମିର ଆକାର ଏକରରେ ଲେଖନ୍ତୁ (ଉଦାହରଣ: 1.5 ଏକର)',
            'soil_type': 'ଆପଣଙ୍କ ମାଟି କେମିତି ପ୍ରକାରର?',
            'soil_help': 'ଆପଣଙ୍କ ମାଟି ପ୍ରକାର ବାଛନ୍ତୁ। ଯଦି ନିଶ୍ଚିତ ନୁହେଁ, ଲୋମି ଅଧିକାଂଶ ଫସଲ ପାଇଁ ଭଲ।',
            'season': 'ଆପଣ କେବେ ଚାଷ କରିବାକୁ ଚାହୁଁଛନ୍ତି?',
            'season_help': 'ଆପଣଙ୍କ ଚାଷ ଋତୁ ବାଛନ୍ତୁ',
            'budget': 'ଆପଣ କେତେ ଟଙ୍କା ଖର୍ଚ୍ଚ କରିପାରିବେ?',
            'budget_help': 'ବିଆ, ଇରିଗେସନ୍ ଏବଂ ସାମଗ୍ରୀ ପାଇଁ ଆପଣଙ୍କ ବଜେଟ୍ ଟଙ୍କାରେ ଲେଖନ୍ତୁ',
            'get_recommendations': 'ମୋର ଫସଲ ସୁପାରିଶ ପାଇନ୍ତୁ',
            'recommendations_title': 'ଆପଣଙ୍କ ଖେତ ପାଇଁ ସର୍ବୋତ୍ତମ ଫସଲ',
            'farm_summary': 'ଆପଣଙ୍କ ଖେତ',
            'acres': 'ଏକର',
            'soil': 'ମାଟି',
            'planting': 'ବୋଆ',
            'budget_text': 'ବଜେଟ୍',
            'economics': 'ଟଙ୍କା ବିବରଣୀ',
            'growing_info': 'ଚାଷ ବିବରଣୀ',
            'cost_per_acre': 'ପ୍ରତି ଏକର ଖର୍ଚ୍ଚ',
            'expected_yield': 'ଆଶାକରା ଫସଲ',
            'profit_potential': 'ଲାଭ ସମ୍ଭାବନା',
            'growing_time': 'ଚାଷ ସମୟ',
            'difficulty': 'କଷ୍ଟସାଧ୍ୟତା',
            'water_needs': 'ପାଣିର ଆବଶ୍ୟକତା',
            'why_crop': 'ଏହି ଫସଲ କାହିଁକି?',
            'growing_tips': 'ଚାଷ ସୁପାରିଶ',
            'budget_breakdown': 'ବଜେଟ୍ ବିବରଣୀ',
            'total_cost': 'ଶୀର୍ଷ 3 ଫସଲର ମୋଟ ଖର୍ଚ୍ଚ',
            'your_budget': 'ଆପଣଙ୍କ ବଜେଟ୍',
            'can_afford': 'ଆପଣ ଏହି ଫସଲ ଚାଷ କରିପାରିବେ!',
            'budget_warning': 'କମ୍ ଫସଲ କିମ୍ବା ସସ୍ତା ବିକଳ୍ପ ବିଚାର କରନ୍ତୁ।',
            'no_crops': 'କୌଣସି ଉଚିତ ଫସଲ ମିଳିଲା ନାହିଁ। ଅନ୍ୟାନ୍ୟ ତଥ୍ୟ ପରିକ୍ଷା କରନ୍ତୁ।',
            'general_tips': 'ସାଧାରଣ ସୁପାରିଶ',
            'about_tool': 'ଏହି ଟୁଲ ବିଷୟରେ',
            'tool_description': 'ଏହି AI ସହାୟକ ଆପଣଙ୍କ ଜମିର ଆକାର, ମାଟି ପ୍ରକାର, ଋତୁ ଏବଂ ବଜେଟ୍ ଧ୍ୟାନରେ ରଖି ସର୍ବୋତ୍ତମ ଫସଲ ସୁପାରିଶ କରିଥାଏ।',
            'get_started': 'ଆରମ୍ଭ କରିବା ପାଇଁ ଉପରେ ଆପଣଙ୍କ ଖେତର ବିବରଣୀ ଭରନ୍ତୁ!'
        }
    }


def main():
    # Initialize session state
    if 'selected_language' not in st.session_state:
        st.session_state.selected_language = None
    if 'step' not in st.session_state:
        st.session_state.step = 'language_selection'
    if 'input_method' not in st.session_state:
        st.session_state.input_method = 'form'  # 'form', 'image', 'voice'
    
    translations = get_translations()
    
    # Language selection step
    if st.session_state.step == 'language_selection':
        st.title("🌾 Farmer Planner AI")
        st.markdown("**Get personalized crop recommendations for your farm**")
        
        st.subheader("🌍 Language Selection / भाषा चयन / மொழி தேர்வு / భాష ఎంపిక / ଭାଷା ପସନ୍ଦ")
        
        languages = ['English', 'Hindi', 'Tamil', 'Telugu', 'Odia']
        selected_lang = st.selectbox(
            "Hello! Which language would you like to continue in? / नमस्ते! आप किस भाषा में जारी रखना चाहते हैं? / வணக்கம்! எந்த மொழியில் தொடர விரும்புகிறீர்கள்? / నమస్కారం! మీరు ఏ భాషలో కొనసాగించాలని అనుకుంటున్నారు? / ନମସ୍କାର! ଆପଣ କେଉଁ ଭାଷା ଚାହାଁତେ?",
            languages,
            index=0
        )
        
        if st.button("Continue / जारी रखें / தொடர் / కొనసాగించండి / ଚାଲନ୍ତୁ", type="primary"):
            st.session_state.selected_language = selected_lang
            st.session_state.step = 'input_method_selection'
            st.rerun()
    
    # Input method selection step
    elif st.session_state.step == 'input_method_selection':
        lang = st.session_state.selected_language
        t = get_translations()[lang]
        
        st.title(t['title'])
        st.markdown(f"**{t['subtitle']}**")
        
        # Input method selection
        input_methods = {
            'English': {
                'form': '📝 Fill Form - Enter farm details step by step',
                'image': '📸 Upload Photo - Analyze your land from image',
                'voice': '🎤 Voice/Text Input - Describe your farm in your language'
            },
            'Hindi': {
                'form': '📝 फॉर्म भरें - खेत की जानकारी चरणबद्ध तरीके से दें',
                'image': '📸 फोटो अपलोड करें - तस्वीर से अपनी जमीन का विश्लेषण करें',
                'voice': '🎤 आवाज/लिखित - अपनी भाषा में खेत का विवरण दें'
            },
            'Tamil': {
                'form': '📝 படிவம் நிரப்பு - பண்ணை விவரங்களை படிப்படியாக உள்ளிடவும்',
                'image': '📸 புகைப்படம் பதிவேற்று - உங்கள் நிலத்தை படத்தில் இருந்து பகுப்பாய்வு செய்யவும்',
                'voice': '🎤 குரல்/உரை உள்ளீடு - உங்கள் மொழியில் பண்ணையை விவரிக்கவும்'
            },
            'Telugu': {
                'form': '📝 ఫారం నింపండి - పొలం వివరాలను దశల వారీగా నమోదు చేయండి',
                'image': '📸 ఫోటో అప్‌లోడ్ - మీ భూమిని చిత్రం నుండి విశ్లేషించండి',
                'voice': '🎤 వాయిస్/టెక్స్ట్ ఇన్‌పుట్ - మీ భాషలో పొలం వివరించండి'
            },
            'Odia': {
                'form': '📝 ଫର୍ମ ପୂରଣ କରନ୍ତୁ - ପ୍ରତ୍ୟେକ ଧାପରେ ଖେତ ବିବରଣୀ ଦିଅନ୍ତୁ',
                'image': '📸 ଫଟୋ ଅପଲୋଡ୍ କରନ୍ତୁ - ଚିତ୍ରରୁ ଆପଣଙ୍କ ଜମିର ବିଶ୍ଲେଷଣ କରନ୍ତୁ',
                'voice': '🎤 ଉଚ୍ଚାରଣ/ଲେଖନ - ଆପଣଙ୍କ ଭାଷାରେ ଖେତ ବର୍ଣ୍ଣନା କରନ୍ତୁ'
            }
        }

        # (rest of the code continues...)


        
        method_options = input_methods.get(lang, input_methods['English'])
        
        st.subheader("🎯 How would you like to provide your farm information?")
        
        # Create columns for input method selection
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(method_options['form'], key="form_method"):
                st.session_state.input_method = 'form'
                st.session_state.step = 'farm_details'
                st.rerun()
        
        with col2:
            if st.button(method_options['image'], key="image_method"):
                st.session_state.input_method = 'image'
                st.session_state.step = 'image_analysis'
                st.rerun()
        
        with col3:
            if st.button(method_options['voice'], key="voice_method"):
                st.session_state.input_method = 'voice'
                st.session_state.step = 'voice_input'
                st.rerun()
        
    
    # Farm details and recommendations step
    elif st.session_state.step == 'farm_details':
        lang = st.session_state.selected_language
        t = translations[lang]
        
        st.title(t['title'])
        st.markdown(f"**{t['subtitle']}**")
        
        # Create two columns for layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📋 " + t['farm_summary'])
            
            # Land size input
            land_size = st.number_input(
                t['land_size'],
                min_value=0.1,
                max_value=1000.0,
                value=1.0,
                step=0.1,
                help=t['land_size_help']
            )
            
            # Soil type selection with multilingual options
            if lang == 'Hindi':
                soil_options = [
                    "Clay / चिकनी मिट्टी", "Sandy / रेतीली मिट्टी", "Loamy / दोमट मिट्टी", 
                    "Silty / गाद मिट्टी", "Peaty / पीट मिट्टी", "Chalky / चूना मिट्टी"
                ]
            elif lang == 'Tamil':
                soil_options = [
                    "Clay / களி மண்", "Sandy / மணல் மண்", "Loamy / வண்டல் மண்", 
                    "Silty / கனிம மண்", "Peaty / கரி மண்", "Chalky / சுண்ணாம்பு மண்"
                ]
            elif lang == 'Telugu':
                soil_options = [
                    "Clay / బంకమట్టి", "Sandy / ఇసుక మట్టి", "Loamy / లోమి మట్టి", 
                    "Silty / సిల్టీ మట్టి", "Peaty / పీట్ మట్టి", "Chalky / సుణ్ణం మట్టి"
                ]
            else:
                soil_options = [
                    "Clay", "Sandy", "Loamy", "Silty", "Peaty", "Chalky"
                ]
            
            soil_selection = st.selectbox(
                t['soil_type'],
                soil_options,
                help=t['soil_help']
            )
            
            # Extract English soil type for processing
            soil_type = soil_selection.split(' / ')[0] if ' / ' in soil_selection else soil_selection
            
            # Season selection with multilingual options
            if lang == 'Hindi':
                season_options = [
                    "Spring / वसंत", "Summer / गर्मी", "Fall / शरद", "Winter / सर्दी"
                ]
            elif lang == 'Tamil':
                season_options = [
                    "Spring / வசந்த காலம்", "Summer / கோடை காலம்", "Fall / இலையுதிர் காலம்", "Winter / குளிர் காலம்"
                ]
            elif lang == 'Telugu':
                season_options = [
                    "Spring / వసంత ఋతువు", "Summer / వేసవి ఋతువు", "Fall / శరదృతువు", "Winter / శీతాకాలం"
                ]
            else:
                season_options = [
                    "Spring", "Summer", "Fall", "Winter"
                ]
            
            season_selection = st.selectbox(
                t['season'],
                season_options,
                help=t['season_help']
            )
            
            # Extract English season for processing
            season = season_selection.split(' / ')[0] if ' / ' in season_selection else season_selection
            
            # Budget input with currency context
            budget_label = t['budget']
            if lang in ['Hindi', 'Tamil', 'Telugu']:
                budget_label += " (₹)"
            else:
                budget_label += " (₹)"
                
            budget = st.number_input(
                budget_label,
                min_value=50,
                max_value=100000,
                value=5000 if lang in ['Hindi', 'Tamil', 'Telugu'] else 500,
                step=50,
                help=t['budget_help']
            )
            
            # Get recommendations button
            if st.button(f"🌱 {t['get_recommendations']}", type="primary"):
                engine = load_recommendation_engine()
                recommendations = engine.get_recommendations(
                    land_size=land_size,
                    soil_type=soil_type,
                    season=season,
                    budget=budget
                )
                
                # Store recommendations in session state
                st.session_state.recommendations = recommendations
                st.session_state.farm_details = {
                    'land_size': land_size,
                    'soil_type': soil_type,
                    'season': season,
                    'budget': budget
                }
        
        with col2:
            st.subheader("🎯 " + t['recommendations_title'])
            
            # Display recommendations if available
            if hasattr(st.session_state, 'recommendations') and st.session_state.recommendations:
                recommendations = st.session_state.recommendations
                farm_details = st.session_state.farm_details
                
                # Summary box
                currency_symbol = "₹" if lang in ['Hindi', 'Tamil', 'Telugu'] else "₹"
                st.info(f"**{t['farm_summary']}:** {farm_details['land_size']} {t['acres']} • {farm_details['soil_type']} {t['soil']} • {farm_details['season']} {t['planting']} • {currency_symbol}{farm_details['budget']} {t['budget_text']}")
                
                if recommendations['suitable_crops']:
                    st.success(f"Found {len(recommendations['suitable_crops'])} suitable crops for your farm!")
                    
                    # Display each recommended crop
                    for i, crop in enumerate(recommendations['suitable_crops'], 1):
                        with st.expander(f"#{i} {crop['name']} - {crop['category']}", expanded=i<=2):
                            
                            # Crop details in columns
                            detail_col1, detail_col2 = st.columns(2)
                            
                            with detail_col1:
                                st.write(f"**💰 {t['economics']}:**")
                                st.write(f"• {t['cost_per_acre']}: {currency_symbol}{crop['cost_per_acre']}")
                                st.write(f"• {t['expected_yield']}: {crop['yield_per_acre']}")
                                st.write(f"• {t['profit_potential']}: {currency_symbol}{crop['profit_potential']}")
                                
                            with detail_col2:
                                st.write(f"**🌱 {t['growing_info']}:**")
                                st.write(f"• {t['growing_time']}: {crop['growing_time']}")
                                st.write(f"• {t['difficulty']}: {crop['difficulty']}")
                                st.write(f"• {t['water_needs']}: {crop['water_needs']}")
                            
                            # Why this crop section
                            st.write(f"**🤔 {t['why_crop']}**")
                            st.write(crop['recommendation_reason'])
                            
                            # Growing tips
                            if crop['growing_tips']:
                                st.write(f"**💡 {t['growing_tips']}:**")
                                for tip in crop['growing_tips']:
                                    st.write(f"• {tip}")
                            
                            # Economic analysis button
                            if st.button(f"📊 Get Economic Analysis for {crop['name']}", key=f"economic_{i}"):
                                st.session_state.selected_crop = crop
                                st.session_state.step = 'economic_input'
                                st.rerun()
                    
                    # Budget breakdown
                    st.subheader(f"💵 {t['budget_breakdown']}")
                    total_cost = sum(crop['cost_per_acre'] for crop in recommendations['suitable_crops'][:3])
                    st.write(f"**{t['total_cost']}:** {currency_symbol}{total_cost:.2f}")
                    st.write(f"**{t['your_budget']}:** {currency_symbol}{farm_details['budget']}")
                    
                    if total_cost <= farm_details['budget']:
                        st.success(f"✅ {t['can_afford']}")
                    else:
                        st.warning(f"⚠️ {t['budget_warning']}")
                        
                else:
                    st.warning(t['no_crops'])
                    
                # Additional tips
                st.subheader(f"🌟 {t['general_tips']}")
                for tip in recommendations['general_tips']:
                    st.write(f"• {tip}")
                    
            else:
                st.info(f"👈 {t['get_started']}")
                
                # Show some general information while waiting
                st.markdown(f"### 🌾 {t['about_tool']}")
                st.write(t['tool_description'])
        
        # Language change button
        if st.button("🌍 Change Language / भाषा बदलें / மொழியை மாற்று / భాష మార్చు"):
            st.session_state.step = 'language_selection'
            st.rerun()
    
    # Image analysis step
    elif st.session_state.step == 'image_analysis':
        lang = st.session_state.selected_language
        t = get_translations()[lang]
        
        st.title(t['title'])
        st.markdown(f"**📸 Image Analysis Mode**")
        
        # Image upload
        uploaded_file = st.file_uploader(
            "Upload a photo of your land/farm:",
            type=['jpg', 'jpeg', 'png', 'bmp'],
            help="Upload a clear photo of your farmland, garden, or growing area"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Your uploaded land photo", use_container_width=True)
            
            # Analyze image
            if st.button("🔍 Analyze Land & Get Recommendations", type="primary"):
                analyzer = load_image_analyzer()
                
                with st.spinner("Analyzing your land photo..."):
                    analysis_result = analyzer.analyze_land_image(image, lang)
                    visual_assessment = analyzer.get_visual_assessment(image, lang)
                
                # Display analysis results
                st.success("Analysis Complete!")
                
                # Visual assessment
                st.subheader("🔍 Visual Assessment")
                for key, value in visual_assessment.items():
                    st.write(f"**{key.replace('_', ' ').title()}:** {value}")
                
                # Land analysis
                st.subheader("📊 Land Analysis")
                land_analysis = analysis_result['land_analysis']
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Land Type:** {land_analysis['land_type']}")
                    st.write(f"**Estimated Size:** {land_analysis['land_size']}")
                    st.write(f"**Soil Condition:** {land_analysis['soil_condition']}")
                
                with col2:
                    st.write(f"**Drainage:** {land_analysis['drainage']}")
                    st.write(f"**Sunlight:** {land_analysis['sunlight']}")
                    st.write(f"**Suitability Score:** {land_analysis['suitability_score']}/10")
                
                # Recommendations
                st.subheader("🌱 Crop Recommendations")
                recommendations = analysis_result['recommendations']
                
                # Suitable crops
                st.write("**Recommended Crops:**")
                for crop in recommendations['suitable_crops']:
                    st.write(f"• {crop}")
                
                # Daily care schedule
                st.subheader("📅 Daily Care Schedule")
                for care in recommendations['daily_care']:
                    st.write(f"• {care}")
                
                # Water and fertilizer info
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("💧 Water Schedule")
                    st.write(recommendations['water_schedule'])
                
                with col2:
                    st.subheader("🌾 Fertilizer Tips")
                    for tip in recommendations['fertilizer_tips']:
                        st.write(f"• {tip}")
                
                # Expected yield and improvement tips
                st.subheader("📈 Expected Yield")
                st.write(recommendations['expected_yield'])
                
                st.subheader("💡 Improvement Tips")
                for tip in recommendations['improvement_tips']:
                    st.write(f"• {tip}")
        
        # Back button
        if st.button("← Back to Input Method Selection"):
            st.session_state.step = 'input_method_selection'
            st.rerun()
    
       # Voice input step
    elif st.session_state.step == 'voice_input':
        js = "window.open('https://34149a8d-3589-4ed5-9f35-c3a5e7ba2e77-00-1dgt8y5974alw.spock.replit.dev/', '_blank')"
        st.components.v1.html(f"<script>{js}</script>", height=0)


    
    # Economic input step - simplified farmer-friendly interface
    elif st.session_state.step == 'economic_input':
        lang = st.session_state.selected_language
        t = get_translations()[lang]
        
        if hasattr(st.session_state, 'selected_crop'):
            crop = st.session_state.selected_crop
            
            # Language-specific titles
            economic_titles = {
                'English': f"💰 Economic Planning for {crop['name']}",
                'Hindi': f"💰 {crop['name']} के लिए आर्थिक योजना",
                'Tamil': f"💰 {crop['name']} பயிருக்கான பொருளாதார திட्பீட்டம்",
                'malayalam': f"💰 {crop['name']} కోసం ఆర్థిక ప్రణాళిక"
            }
            
            st.title(economic_titles.get(lang, economic_titles['English']))
            
            # Simple input questions in user's language
            input_labels = {
                'English': {
                    'budget': "How much money do you have for cultivation? (₹)",
                    'turnover': "What price do you expect to sell at? (₹)",
                    'location': "Where is your farm? (District/State)",
                    'land_size': "How much land do you have? (Acres)"
                },
                'Hindi': {
                    'budget': "खेती के लिए आपके पास कितना पैसा है? (₹)",
                    'turnover': "आप कितनी कीमत पर बेचने की उम्मीद करते हैं? (₹)",
                    'location': "आपका खेत कहाँ है? (जिला/राज्य)",
                    'land_size': "आपके पास कितनी जमीन है? (एकड़)"
                },
                'Tamil': {
                    'budget': "விவசாயத்திற்கு உங்களிடம் எவ்வளவு பணம் உள்ளது? (₹)",
                    'turnover': "எந்த விலையில் விற்க எதிर்பார்க்கிறீர்கள்? (₹)",
                    'location': "உங்கள் பண்ணை எங்கே உள்ளது? (மாவட்டம்/மாநிலம்)",
                    'land_size': "உங்களிடம் எவ்வளவு நிலம் உள்ளது? (ஏக்கர்)"
                },
                'Malayalam': {
                    'budget': "వ్యవసాయం కోసం మీ దగ్గర ఎంత డబ్బు ఉంది? (₹)",
                    'turnover': "మీరు ఎంత ధరకు అమ్మాలని అనుకుంటున్నారు? (₹)",
                    'location': "మీ పొలం ఎక్కడ ఉంది? (జిల్లా/రాష్ట్రం)",
                    'land_size': "మీ దగ్గర ఎంత భూమి ఉంది? (ఎకరాలు)"
                }
            }
            
            labels = input_labels.get(lang, input_labels['English'])
            
            # Simple form layout
            st.subheader("📝 Tell me about your farming plan:")
            
            cultivation_budget = st.number_input(
                labels['budget'],
                min_value=1000,
                max_value=10000000,
                value=max(1000, int(crop['cost_per_acre'] * 1.2)),
                step=1000
            )
            
            expected_turnover = st.number_input(
                labels['turnover'],
                min_value=1000,
                max_value=20000000,
                value=max(1000, int(crop['profit_potential'] * 1.5)),
                step=1000
            )
            
            location = st.text_input(
                labels['location'],
                value="Erode, Tamil Nadu"
            )
            
            land_size_economic = st.number_input(
                labels['land_size'],
                min_value=0.1,
                max_value=1000.0,
                value=1.0,
                step=0.1
            )
            
            # Calculate economics button
            if st.button("🔍 Get Economic Analysis & Market Recommendations", type="primary"):
                advisor = load_economic_advisor()
                
                with st.spinner("Analyzing economics and market opportunities..."):
                    # Calculate total budget based on land size
                    total_budget = cultivation_budget * land_size_economic
                    total_turnover = expected_turnover * land_size_economic
                    
                    # Get economic analysis
                    economic_analysis = advisor.calculate_profit_loss(
                        crop_name=crop['name'],
                        budget=total_budget,
                        expected_turnover=total_turnover,
                        location=location,
                        language=lang
                    )
                
                # Display results
                st.success("Economic Analysis Complete!")
                
                # Profit/Loss summary
                st.subheader("📈 Profit/Loss Analysis")
                profit_loss = economic_analysis['profit_loss']
                profit_percentage = economic_analysis['profit_percentage']
                
                # Create metrics display
                metric_col1, metric_col2, metric_col3 = st.columns(3)
                
                with metric_col1:
                    st.metric("Total Investment", f"₹{total_budget:,}")
                
                with metric_col2:
                    st.metric("Expected Revenue", f"₹{total_turnover:,}")
                
                with metric_col3:
                    color = "normal" if profit_loss >= 0 else "inverse"
                    st.metric("Profit/Loss", f"₹{profit_loss:,}", f"{profit_percentage:.1f}%")
                
                # Profit/Loss indicator
                if profit_loss >= 0:
                    st.success(f"✅ Expected Profit: ₹{profit_loss:,} ({profit_percentage:.1f}%)")
                else:
                    st.error(f"⚠️ Expected Loss: ₹{abs(profit_loss):,} ({abs(profit_percentage):.1f}%)")
                
                # Cost breakdown
                st.subheader("💸 Cost Breakdown")
                cost_breakdown = economic_analysis['cost_breakdown']
                
                breakdown_col1, breakdown_col2 = st.columns(2)
                
                with breakdown_col1:
                    st.write(f"**Seeds:** ₹{cost_breakdown['seeds']:,.0f}")
                    st.write(f"**Fertilizers:** ₹{cost_breakdown['fertilizers']:,.0f}")
                    st.write(f"**Irrigation:** ₹{cost_breakdown['irrigation']:,.0f}")
                
                with breakdown_col2:
                    st.write(f"**Labor:** ₹{cost_breakdown['labor']:,.0f}")
                    st.write(f"**Miscellaneous:** ₹{cost_breakdown['miscellaneous']:,.0f}")
                    st.write(f"**Total:** ₹{sum(cost_breakdown.values()):,.0f}")
                
                # Market information
                st.subheader("🏪 Market Opportunities")
                market_info = economic_analysis['market_info']
                
                market_col1, market_col2, market_col3 = st.columns(3)
                
                with market_col1:
                    st.write(f"**{market_info['local_markets']['title']}:**")
                    for market in market_info['local_markets']['options']:
                        st.write(f"• {market}")
                
                with market_col2:
                    st.write(f"**{market_info['export_destinations']['title']}:**")
                    for dest in market_info['export_destinations']['options']:
                        st.write(f"• {dest}")
                
                with market_col3:
                    st.write(f"**{market_info['processing_centers']['title']}:**")
                    for center in market_info['processing_centers']['options']:
                        st.write(f"• {center}")
                
                # Government schemes
                st.subheader("🏛️ Government Schemes & Subsidies")
                schemes = economic_analysis['government_schemes']
                
                scheme_col1, scheme_col2 = st.columns(2)
                
                with scheme_col1:
                    st.write(f"**Crop-Specific Schemes:**")
                    for scheme in schemes['crop_specific']:
                        st.write(f"• {scheme}")
                
                with scheme_col2:
                    st.write(f"**General Agricultural Schemes:**")
                    for scheme in schemes['general']:
                        st.write(f"• {scheme}")
                
                # Recommendations
                st.subheader("💡 Profit Maximization Tips")
                recommendations = economic_analysis['recommendations']
                
                for rec in recommendations:
                    st.write(f"• {rec}")
                
                # Alternative crops if profit is low
                if profit_percentage < 20:
                    st.subheader("🌿 Alternative Crop Suggestions")
                    alternatives = advisor.get_alternative_crops(crop['name'], location, lang)
                    
                    alt_col1, alt_col2, alt_col3 = st.columns(3)
                    
                    with alt_col1:
                        st.write("**High-Value Crops:**")
                        for alt in alternatives['high_value']:
                            st.write(f"• {alt}")
                    
                    with alt_col2:
                        st.write("**Medium-Value Crops:**")
                        for alt in alternatives['medium_value']:
                            st.write(f"• {alt}")
                    
                    with alt_col3:
                        st.write("**Safe Options:**")
                        for alt in alternatives['safe_options']:
                            st.write(f"• {alt}")
                
                # Contact information
                st.subheader("📞 Need More Help?")
                
                help_messages = {
                    'English': "Ask me about marketing strategies, storage solutions, or transportation options!",
                    'Hindi': "मार्केटिंग रणनीति, भंडारण समाधान, या परिवहन विकल्पों के बारे में पूछें!",
                    'Tamil': "சந்தைப்படுத்தல் உத்திகள், சேமிப்பு தீர்வுகள் அல்லது போக்குவரத்து விருப்பங்களைப் பற்றி கேளுங்கள்!",
                    'Malayalam': "మార్కెటింగ్ వ్యూహాలు, నిల్వ పరిష్కారాలు లేదా రవాణా ఎంపికల గురించి అడగండి!"
                }
                
                st.info(help_messages.get(lang, help_messages['English']))
                
                # Additional questions input
                follow_up_question = st.text_area(
                    "Ask any questions about marketing, storage, or transport:",
                    height=100,
                    placeholder="e.g., How to store turmeric properly? Best transport methods for my location?"
                )
                
                if follow_up_question:
                    st.success("Thank you for your question! Here are some general tips:")
                    
                    # Simple response based on keywords
                    if 'storage' in follow_up_question.lower() or 'store' in follow_up_question.lower():
                        st.write("• Use proper ventilation and moisture control")
                        st.write("• Consider cold storage for perishables")
                        st.write("• Implement pest control measures")
                        st.write("• Use proper packaging materials")
                    
                    elif 'transport' in follow_up_question.lower() or 'shipping' in follow_up_question.lower():
                        st.write("• Choose appropriate vehicle size for your quantity")
                        st.write("• Consider refrigerated transport for perishables")
                        st.write("• Plan route optimization to reduce costs")
                        st.write("• Use proper loading and unloading techniques")
                    
                    elif 'marketing' in follow_up_question.lower() or 'sell' in follow_up_question.lower():
                        st.write("• Research current market prices regularly")
                        st.write("• Build relationships with multiple buyers")
                        st.write("• Consider direct-to-consumer sales")
                        st.write("• Explore online marketing platforms")
                    
                    else:
                        st.write("• Focus on quality production")
                        st.write("• Keep detailed records of costs and income")
                        st.write("• Network with other successful farmers")
                        st.write("• Stay updated on government schemes")
            
            
            # Back button
            if st.button("← Back to Crop Recommendations"):
                st.session_state.step = 'farm_details'
                st.rerun()
        
        else:
            st.error("No crop selected. Please go back and select a crop first.")
            if st.button("← Back to Crop Recommendations"):
                st.session_state.step = 'farm_details'
                st.rerun()
        


if __name__ == "__main__":
    main()

import streamlit as st


st.markdown("---")
st.title("🤖 Try out our other tools here:")

# Embed the site using iframe (height can be adjusted)
if st.button("SMART GARDEN AI"):
    js = f"window.open('https://a4c98246-619f-45ee-a4ab-44cc4c29de31-00-2hyvpf9a964fl.spock.replit.dev/', '_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)

if st.button("Open Crop Disease Detection Tool"):
    js = f"window.open('https://9b92e64a-f831-478e-a942-edbba1efde3d-00-15x9xbrb9ax8f.worf.replit.dev/', '_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)

if st.button("Bio digital twin"):
    js = f"window.open('https://4ac95776-94ba-4d62-b233-cb20fb4be147-00-op2yb3e3ib10.kirk.replit.dev/', '_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)

if st.button("Weather Prediction"):
    js = f"window.open('https://afb6a5401a8dbfe5d4.gradio.live/', '_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)

if st.button("PRICE TREND PREDICTOR"):
    js = f"window.open('https://496f97d3-e21c-450a-b867-7ca3d211e8a1-00-t6ypczltxvsg.janeway.replit.dev/', '_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)

if st.button("🌦 Weather Alerts"):
    run_weather_alerts()

if st.button("Report Genreator"):
    js = f"window.open('https://b5a5dd3b-3b47-4618-b02c-8356ef39d0f7-00-39fje3kemj5o6.spock.replit.dev/', '_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)

if st.button("Voice-based AI"):
    js = f"window.open('https://3ef815aa958da4aee0.gradio.live', '_blank')"
    st.components.v1.html(f"<script>{js}</script>", height=0)