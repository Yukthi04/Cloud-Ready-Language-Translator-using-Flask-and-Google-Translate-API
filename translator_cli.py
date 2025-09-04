from googletrans import Translator
from languages import LANGUAGE_CODES, display_languages
import argparse

def translate_text(text, src_lang='auto', dest_lang='en', show_pronunciation=False):
    """Translate text using Google Translate API"""
    translator = Translator()
    
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        
        print("\nTranslation Results:")
        print("=" * 40)
        print(f"Original ({translation.src.upper()}): {text}")
        print(f"Translated ({translation.dest.upper()}): {translation.text}")
        
        if show_pronunciation and translation.pronunciation:
            print(f"Pronunciation: {translation.pronunciation}")
        
        print("=" * 40)
    except Exception as e:
        print(f"\nError occurred: {e}")

def main():
    """Main CLI interface"""
    print("\nLanguage Translator CLI")
    print("=" * 40)
    
    parser = argparse.ArgumentParser(description='Translate text between languages')
    parser.add_argument('--text', help='Text to translate')
    parser.add_argument('--src', default='auto', help='Source language code (default: auto-detect)')
    parser.add_argument('--dest', default='en', help='Destination language code (default: en)')
    parser.add_argument('--pronounce', action='store_true', help='Show pronunciation')
    parser.add_argument('--list', action='store_true', help='List available languages')
    
    args = parser.parse_args()
    
    if args.list:
        display_languages()
        return
    
    if not args.text:
        # Interactive mode
        display_languages()
        text = input("\nEnter text to translate: ")
        src_lang = input(f"Source language code [{args.src}]: ") or args.src
        dest_lang = input(f"Target language code [{args.dest}]: ") or args.dest
        show_pron = input("Show pronunciation? (y/n) [n]: ").lower() == 'y'
    else:
        # Command line mode
        text = args.text
        src_lang = args.src
        dest_lang = args.dest
        show_pron = args.pronounce
    
    translate_text(text, src_lang, dest_lang, show_pron)

if __name__ == "__main__":
    main()