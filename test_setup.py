#!/usr/bin/env python3
"""Test script to verify API key and available Gemini models"""

import os
import sys

# Try to load environment
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️ python-dotenv not installed, using system environment variables")

# Check API key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key or api_key == "your-gemini-api-key-here":
    print("❌ GEMINI_API_KEY not set properly in .env file!")
    print("\nPlease edit .env file and add your API key:")
    print("  GEMINI_API_KEY=AIzaSy... (your actual key)")
    print("\nGet your key from: https://aistudio.google.com/app/apikey")
    sys.exit(1)

print(f"✅ API Key found: {api_key[:20]}...")

# Try to import and configure
try:
    import google.generativeai as genai
    print("✅ google-generativeai library imported")
except ImportError as e:
    print(f"❌ Failed to import google-generativeai: {e}")
    print("Run: pip install google-generativeai")
    sys.exit(1)

# Configure API
try:
    genai.configure(api_key=api_key)
    print("✅ API configured successfully")
except Exception as e:
    print(f"❌ Failed to configure API: {e}")
    sys.exit(1)

# List available models
print("\n📋 Listing available models...")
print("=" * 60)

try:
    models = genai.list_models()
    found_compatible = False
    
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            found_compatible = True
            print(f"  ✓ {m.name}")
    
    if not found_compatible:
        print("  ⚠️ No compatible models found for generateContent")
    else:
        print("\n✅ Compatible models found! The app should work.")
        
except Exception as e:
    print(f"❌ Error listing models: {e}")
    sys.exit(1)

# Test creating a model instance
print("\n🧪 Testing model initialization...")
print("=" * 60)

test_models = ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-1.5-pro"]

for model_name in test_models:
    try:
        test_model = genai.GenerativeModel(model_name)
        print(f"  ✅ Successfully initialized: {model_name}")
        break
    except Exception as e:
        print(f"  ❌ Failed to initialize {model_name}: {str(e)[:50]}...")

print("\n" + "=" * 60)
print("✅ Setup verification complete!")
print("\nYou can now run: streamlit run app.py")
