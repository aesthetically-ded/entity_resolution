# Entity Resolution Framework (November 2023)

**Mentor:** Ajit Kumar Pasayat, KIIT University  

## 📌 Project Overview
This project develops a **framework for entity resolution** — cleaning and matching dirty raw data to identify duplicate or related records.  
It processes data through **data preparation, attribute analysis, binning, blocking, and pairwise matching** to produce clean, consistent data.  

## ⚙️ Technologies Used
- Python  
- Jupyter Notebook / Anaconda  
- Jellyfish (Soundex, NYSIIS, Jaro-Winkler algorithms)  
- pandas, numpy  

## 📊 Features
- Data cleaning (remove duplicates, handle missing values)  
- Attribute analysis for name/address fields  
- **Blocking** to group similar entities and reduce comparison space  
- **Pairwise Matching** with:  
  - NYSIIS  
  - Jaro-Winkler similarity  
  - Soundex  

✅ Reduced execution time from **days to minutes** using blocking.  

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/entity-resolution
   cd entity-resolution
