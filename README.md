🌱 AgroAura — AI-Powered Personal Farming Assistant

<p align="center"> <b>The Aura of Digital Farming</b> </p>

<p align="center"> An intelligent, accessible and end-to-end digital farming companion for small and marginal farmers. </p>

🚜 About AgroAura

AgroAura is an AI-powered personal farming assistant developed by Team SYNAPSE for the Smart India Hackathon 2026.

It provides personalized agricultural support throughout the crop lifecycle by combining:

🌱 Farmer and farm information
🧪 Soil sensor data
📸 Crop images
🌦️ Weather information
📊 Market information
🤖 AI-powered recommendations
🗣️ Voice and multilingual interaction

The goal is to help farmers make better decisions about crop selection, irrigation, fertilizers, disease management, market access and farm documentation.

🎯 Problem

Small and marginal farmers face several challenges:

Difficulty selecting suitable crops
High input costs
Limited access to reliable agricultural information
Crop diseases and pest-related losses
Rain-fed farming and unpredictable weather
Lack of reliable market and buyer information
Limited connectivity and digital accessibility
Difficulty maintaining records for loans, subsidies and insurance

AgroAura addresses these challenges through an integrated digital farming platform.

💡 Our Solution

AgroAura works as a continuous digital companion throughout the farming lifecycle.

🌱 DECIDE — Crop Planner

Recommends suitable crops based on:

Soil parameters
Farmer inputs
Farm conditions
Estimated cost
ROI
Market information
Government subsidies
🌾 MONITOR — Virtual BioTwin

Maintains a digital representation of the crop and farm using:

Soil conditions
Crop stage
Weather
Irrigation information
Growth history

This enables continuous crop monitoring and farm insights.

🛡️ PROTECT — AI Disease Detection

Farmers can upload crop images to identify potential diseases.

The system provides:

Disease identification
Severity information
Possible causes
Organic treatment options
Chemical treatment options
Preventive guidance
🛒 SOURCE & SELL — Resource & Vendor Agents

Helps farmers:

Find agricultural resources
Compare input prices
Explore seeds, fertilizers and pesticides
Identify alternative buyers
Explore different selling routes
🗣️ ASSIST — Voice & Multimodal Support

AgroAura supports:

Text interaction
Voice interaction
Image-based interaction
Native-language assistance
Read-aloud guidance
SMS alerts
📄 DOCUMENT — Farm Evidence Report

Creates structured farm records containing information such as:

Crop journey
Farm activities
Yield
Income
Photos

These records can support:

Loans
Government subsidies
Insurance claims
✨ Key Features
Feature	Description
🌱 AI Crop Recommendation	Suggests suitable crops using farm and soil information
🧪 Soil Intelligence	Uses soil parameters for agricultural decisions
🌾 Virtual BioTwin	Digital representation of crop and field conditions
📸 Disease Detection	Detects potential crop diseases from images
📊 Market Analysis	Provides market and price-related insights
🛒 Resource Agent	Helps compare agricultural input resources
🤝 Vendor Agent	Provides alternative routes for selling produce
🗣️ Voice Assistant	Voice-based agricultural assistance
🌐 Multilingual Support	Designed for local-language accessibility
📢 Weather Alerts	Weather and disaster-related notifications
📱 Offline-First	Supports operation during limited connectivity
💬 SMS Support	Important alerts through SMS
📄 Farm Reports	Generates structured farm records
🏛️ Scheme Guidance	Helps farmers discover relevant government schemes
🏗️ System Architecture
                    ┌─────────────────────┐
                    │       FARMER        │
                    └──────────┬──────────┘
                               │
                    Voice / Text / Image
                               │
                               ▼
                 ┌─────────────────────────┐
                 │       AGROAURA           │
                 │   Farmer AI Assistant    │
                 └────────────┬────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
 ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
 │ Crop Planner │      │ Disease AI   │      │ Market Agent │
 └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   AI / ML Layer  │
                    └────────┬─────────┘
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
        Soil Sensors      Weather Data     Market Data
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                    ┌──────────────────┐
                    │ Farmer Insights  │
                    │ & Recommendations│
                    └──────────────────┘
🔧 Technology Stack
Frontend / Interface
HTML5
CSS3
Streamlit
AI / Machine Learning
Python
PyTorch
Scikit-learn
TensorFlow Lite
MobileNetV2
Machine Learning based crop and market analysis
IoT
ESP32
Soil Moisture Sensor
pH Sensor
NPK Sensor
EC Sensor
Data & Storage
SQLite
Local offline storage
Cloud synchronization
Communication
SMS Alerts
Voice Interaction
Multilingual Text Interaction
Security
OTP Authentication
HTTPS/TLS Encryption
🧠 AI & Intelligent Modules
Crop Recommendation

Uses farmer inputs and soil information to recommend suitable crops while considering cost, ROI and market factors.

Disease Detection

A lightweight MobileNetV2-based approach is intended for crop disease detection, including offline/edge execution using TensorFlow Lite.

Market Intelligence

Machine learning techniques can be used for agricultural commodity price forecasting using market and government data.

Virtual BioTwin

Combines:

Soil Data
    +
Weather Data
    +
Crop Stage
    +
Irrigation
    +
Disease Events
    ↓
Virtual BioTwin
    ↓
Farm Insights
📡 Offline-First Approach

AgroAura is designed for farmers operating in areas with limited connectivity.

                 INTERNET AVAILABLE
                        │
                        ▼
              ┌──────────────────┐
              │ Cloud Synchronize│
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Local Farm Data  │
              └──────────────────┘
                       ▲
                       │
              INTERNET UNAVAILABLE
                       │
              ┌────────┴─────────┐
              │                  │
              ▼                  ▼
        Local Database        SMS Alerts

The platform can store farmer, crop and field information locally and synchronize when connectivity becomes available.

👨‍🌾 Target Users

AgroAura is primarily designed for:

Smallholder farmers
Marginal farmers
Rain-fed farmers
Fruit and vegetable growers
Resource-constrained farmers
🌍 Expected Impact
For Farmers
Better crop selection
Reduced crop losses
Improved farm productivity
Better access to market information
Easier access to agricultural resources
Improved access to government schemes
For Insurance
Structured farm records
Easier crop-loss documentation
Digital evidence through photos and farm history
For Consumers
Improved agricultural productivity
Better supply-chain efficiency
More stable access to agricultural products
Environmental Benefits
Optimized water usage
Optimized fertilizer usage
Reduced unnecessary pesticide usage
Early disease detection
💰 Sustainability & Business Model
Freemium Model

Basic agricultural assistance can remain free while advanced AI features can be offered as premium services.

Government / PPP Model

Potential collaboration with:

Government agricultural departments
AgriTech organizations
Rural development programs
B2B Model

Potential partnerships with:

Agricultural banks
Input suppliers
Insurance companies
Agricultural service providers
⚠️ Current Challenges
Data Quality

Incomplete or inaccurate farm information can affect recommendations.

Language Diversity

Different dialects and accents can affect voice recognition.

Expert Validation

AI-generated agricultural recommendations require appropriate agricultural expert validation.

System Integration

Integration with external government and agricultural systems can be complex.

Sensor Reliability

Sensor calibration errors can affect soil and crop analysis.

🔮 Future Improvements
Advanced agricultural expert validation
More regional languages and dialects
More crop-specific AI models
Improved disease severity estimation
More accurate price forecasting
Wider government-system integration
Affordable IoT sensor kits
Expanded offline capabilities
Advanced farmer analytics
Large-scale regional deployment
📚 Research & References

The project research includes work related to:

IoT-based automated irrigation
Plant disease detection using deep learning
Agricultural commodity price prediction
Smart agriculture using soil and climate sensors
Digital twins in agriculture
Offline-first agricultural advisory systems
Agriculture 4.0 decision-support systems
Weather-based crop yield prediction
👥 Team SYNAPSE

Team: SYNAPSE

Problem Statement: SIH26193
Problem Statement: AI-Powered Personal Farming Assistant for Farmers
Theme: Agriculture, FoodTech & Rural Development
Category: Software
Event: Smart India Hackathon 2026

🚀 Project Status

Current Status: In Progress

The product is currently under development. The present focus is on completing the remaining modules, improving the farmer-friendly interface, integrating intelligent agricultural services and developing a sustainable deployment model.

📜 License

This project is licensed under the MIT License.

See LICENSE for details.

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

<p align="center"> 🌱 <b>AgroAura — Empowering Farmers Through Intelligent Digital Agriculture</b> 🌱 </p>
