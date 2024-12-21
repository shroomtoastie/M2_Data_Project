{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#  1. Project Overview "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " ### Political Donations made by Owners from American Professional Sport Teams\n",
    " \n",
    " ##### Objectives: analyze and show different party donations made from each League in the dataset "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib\n",
    "from pandas import DataFrame\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2. Data Collection and Loading "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>Team</th>\n",
       "      <th>League</th>\n",
       "      <th>Recipient</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Election Year</th>\n",
       "      <th>Party</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>WRIGHT 2016</td>\n",
       "      <td>$4,000</td>\n",
       "      <td>2016</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>BIDEN FOR PRESIDENT</td>\n",
       "      <td>$2,800</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>CORY 2020</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>Kamala Harris for the People</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>Win The Era PAC</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2793</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>ANGIE CRAIG FOR CONGRESS</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2794</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>DEAN PHILLIPS FOR CONGRESS</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2795</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>MENENDEZ FOR SENATE</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2796</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>TINA SMITH FOR MINNESOTA</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2797</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>TOM MALINOWSKI FOR CONGRESS</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2798 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Owner               Team League                     Recipient  \\\n",
       "0     Adam Silver       Commissioner    NBA                   WRIGHT 2016   \n",
       "1     Adam Silver       Commissioner    NBA           BIDEN FOR PRESIDENT   \n",
       "2     Adam Silver       Commissioner    NBA                     CORY 2020   \n",
       "3     Adam Silver       Commissioner    NBA  Kamala Harris for the People   \n",
       "4     Adam Silver       Commissioner    NBA               Win The Era PAC   \n",
       "...           ...                ...    ...                           ...   \n",
       "2793    Zygi Wilf  Minnesota Vikings    NFL      ANGIE CRAIG FOR CONGRESS   \n",
       "2794    Zygi Wilf  Minnesota Vikings    NFL    DEAN PHILLIPS FOR CONGRESS   \n",
       "2795    Zygi Wilf  Minnesota Vikings    NFL           MENENDEZ FOR SENATE   \n",
       "2796    Zygi Wilf  Minnesota Vikings    NFL      TINA SMITH FOR MINNESOTA   \n",
       "2797    Zygi Wilf  Minnesota Vikings    NFL   TOM MALINOWSKI FOR CONGRESS   \n",
       "\n",
       "       Amount  Election Year     Party  \n",
       "0     $4,000            2016  Democrat  \n",
       "1     $2,800            2020  Democrat  \n",
       "2     $2,700            2020  Democrat  \n",
       "3     $2,700            2020  Democrat  \n",
       "4     $2,700            2020  Democrat  \n",
       "...       ...            ...       ...  \n",
       "2793  $2,700            2018  Democrat  \n",
       "2794  $2,700            2018  Democrat  \n",
       "2795  $2,700            2018  Democrat  \n",
       "2796  $2,700            2018  Democrat  \n",
       "2797  $2,700            2018  Democrat  \n",
       "\n",
       "[2798 rows x 7 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_donate = pd.read_csv(\"sports-political-donations.csv\")\n",
    "\n",
    "df_donate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2798 entries, 0 to 2797\n",
      "Data columns (total 7 columns):\n",
      " #   Column         Non-Null Count  Dtype \n",
      "---  ------         --------------  ----- \n",
      " 0   Owner          2798 non-null   object\n",
      " 1   Team           2798 non-null   object\n",
      " 2   League         2798 non-null   object\n",
      " 3   Recipient      2798 non-null   object\n",
      " 4   Amount         2798 non-null   object\n",
      " 5   Election Year  2798 non-null   int64 \n",
      " 6   Party          2789 non-null   object\n",
      "dtypes: int64(1), object(6)\n",
      "memory usage: 153.1+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(df_donate.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The dataframe has 2798 rows and 7 columns!\n",
      "\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2798 entries, 0 to 2797\n",
      "Data columns (total 7 columns):\n",
      " #   Column         Non-Null Count  Dtype \n",
      "---  ------         --------------  ----- \n",
      " 0   Owner          2798 non-null   object\n",
      " 1   Team           2798 non-null   object\n",
      " 2   League         2798 non-null   object\n",
      " 3   Recipient      2798 non-null   object\n",
      " 4   Amount         2798 non-null   object\n",
      " 5   Election Year  2798 non-null   int64 \n",
      " 6   Party          2789 non-null   object\n",
      "dtypes: int64(1), object(6)\n",
      "memory usage: 153.1+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "df_shape = df_donate.shape\n",
    "print(f'The dataframe has {df_shape[0]} rows and {df_shape[1]} columns!\\n')\n",
    "print(df_donate.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>Team</th>\n",
       "      <th>League</th>\n",
       "      <th>Recipient</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Election Year</th>\n",
       "      <th>Party</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>WRIGHT 2016</td>\n",
       "      <td>$4,000</td>\n",
       "      <td>2016</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>BIDEN FOR PRESIDENT</td>\n",
       "      <td>$2,800</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>CORY 2020</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>Kamala Harris for the People</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>Commissioner</td>\n",
       "      <td>NBA</td>\n",
       "      <td>Win The Era PAC</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2020</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Owner          Team League                     Recipient   Amount  \\\n",
       "0  Adam Silver  Commissioner    NBA                   WRIGHT 2016  $4,000    \n",
       "1  Adam Silver  Commissioner    NBA           BIDEN FOR PRESIDENT  $2,800    \n",
       "2  Adam Silver  Commissioner    NBA                     CORY 2020  $2,700    \n",
       "3  Adam Silver  Commissioner    NBA  Kamala Harris for the People  $2,700    \n",
       "4  Adam Silver  Commissioner    NBA               Win The Era PAC  $2,700    \n",
       "\n",
       "   Election Year     Party  \n",
       "0           2016  Democrat  \n",
       "1           2020  Democrat  \n",
       "2           2020  Democrat  \n",
       "3           2020  Democrat  \n",
       "4           2020  Democrat  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_donate.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>Team</th>\n",
       "      <th>League</th>\n",
       "      <th>Recipient</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Election Year</th>\n",
       "      <th>Party</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2793</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>ANGIE CRAIG FOR CONGRESS</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2794</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>DEAN PHILLIPS FOR CONGRESS</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2795</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>MENENDEZ FOR SENATE</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2796</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>TINA SMITH FOR MINNESOTA</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2797</th>\n",
       "      <td>Zygi Wilf</td>\n",
       "      <td>Minnesota Vikings</td>\n",
       "      <td>NFL</td>\n",
       "      <td>TOM MALINOWSKI FOR CONGRESS</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>2018</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Owner               Team League                    Recipient  \\\n",
       "2793  Zygi Wilf  Minnesota Vikings    NFL     ANGIE CRAIG FOR CONGRESS   \n",
       "2794  Zygi Wilf  Minnesota Vikings    NFL   DEAN PHILLIPS FOR CONGRESS   \n",
       "2795  Zygi Wilf  Minnesota Vikings    NFL          MENENDEZ FOR SENATE   \n",
       "2796  Zygi Wilf  Minnesota Vikings    NFL     TINA SMITH FOR MINNESOTA   \n",
       "2797  Zygi Wilf  Minnesota Vikings    NFL  TOM MALINOWSKI FOR CONGRESS   \n",
       "\n",
       "       Amount  Election Year     Party  \n",
       "2793  $2,700            2018  Democrat  \n",
       "2794  $2,700            2018  Democrat  \n",
       "2795  $2,700            2018  Democrat  \n",
       "2796  $2,700            2018  Democrat  \n",
       "2797  $2,700            2018  Democrat  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_donate.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3. Data Cleaning and Preparation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Now that I have deleted some columns, this dataframe has 2798 rows and 4 columns!\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Party</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>$4,000</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>$2,800</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>$2,700</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Owner League   Amount     Party\n",
       "0  Adam Silver    NBA  $4,000   Democrat\n",
       "1  Adam Silver    NBA  $2,800   Democrat\n",
       "2  Adam Silver    NBA  $2,700   Democrat\n",
       "3  Adam Silver    NBA  $2,700   Democrat\n",
       "4  Adam Silver    NBA  $2,700   Democrat"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#im going to get rid of the unwanted columns: \"Team\" and \"Recipient\" to focus only on the party and league \n",
    "\n",
    "df_donate_cols = df_donate.drop(['Recipient', 'Team', 'Election Year'], axis=1)\n",
    "\n",
    "#checking \n",
    "\n",
    "df_donate_cols.head()\n",
    "\n",
    "#changing the name of the variable\n",
    "donation_df = df_donate_cols\n",
    "\n",
    "df_shape = donation_df.shape\n",
    "\n",
    "print(f\"Now that I have deleted some columns, this dataframe has {df_shape[0]} rows and {df_shape[1]} columns!\")\n",
    "\n",
    "#double checking\n",
    "donation_df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "#checking for null values\n",
    "print(donation_df.isnull().any().any())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Owner     0\n",
       "League    0\n",
       "Amount    0\n",
       "Party     9\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#seeing where the null values are located\n",
    "donation_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Owner     0\n",
       "League    0\n",
       "Amount    0\n",
       "Party     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#getting rid of the null values in the Party column and creating a new variable \n",
    "\n",
    "df_dropna = donation_df.dropna()\n",
    "\n",
    "#placing the cleaned variable inside the original df_donate variable\n",
    "\n",
    "donation_df = df_dropna\n",
    "\n",
    "#checking to see if it looks good\n",
    "\n",
    "donation_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Owner', 'League', 'Amount', 'Party'], dtype='object')"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "donation_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Owner\n",
       "Charles Johnson                     213\n",
       "Micky Arison                        178\n",
       "John Rogers                         149\n",
       "Dan DeVos                           116\n",
       "Jody Allen (Paul G. Allen Trust)    108\n",
       "                                   ... \n",
       "Richard Petty                         1\n",
       "Stephen J. Bisciotti                  1\n",
       "Tom Ricketts                          1\n",
       "Troy Stafford                         1\n",
       "Wyc Grousbeck                         1\n",
       "Name: count, Length: 158, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking the different variables of the Owner column using value_counts() method\n",
    "\n",
    "owner_null= donation_df['Owner'].isna().any()\n",
    "print(owner_null)\n",
    "\n",
    "donation_df[\"Owner\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Amount\n",
       "$2,700      436\n",
       "$5,400      384\n",
       "$5,000      263\n",
       "$1,000      245\n",
       "$5,600      226\n",
       "           ... \n",
       "$53,031       1\n",
       "$5,100        1\n",
       "$1,100        1\n",
       "$21,250       1\n",
       "$18,000       1\n",
       "Name: count, Length: 244, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking the different variables of the Amount column using value_counts() method\n",
    "amount_null= donation_df['Amount'].isna().any()\n",
    "print(amount_null)\n",
    "\n",
    "donation_df[\"Amount\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Party\n",
       "Republican                           1625\n",
       "Democrat                              921\n",
       "Bipartisan                            195\n",
       "Bipartisan, but mostly Republican      40\n",
       "Bipartisan, but mostly Democratic       5\n",
       "Independent                             3\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking the Party columns values\n",
    "donation_df.Party.value_counts()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3a. Removing Columns from df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The original DataFrame variables for the 'Party' column are:\n",
      "Party\n",
      "Republican                           1625\n",
      "Democrat                              921\n",
      "Bipartisan                            195\n",
      "Bipartisan, but mostly Republican      40\n",
      "Bipartisan, but mostly Democratic       5\n",
      "Independent                             3\n",
      "Name: count, dtype: int64\n",
      "\n",
      "\n",
      "The new DataFrame variables for the 'Party' column are:\n",
      "Party\n",
      "Republican    1625\n",
      "Democrat       921\n",
      "Bipartisan     195\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#I want to focus only on the top3: Rep, Dem, Bipart so I will remove the other values\n",
    "val_to_remove = [\"Bipartisan, but mostly Republican\", \"Bipartisan, but mostly Democratic\", \"Independent\"]\n",
    "\n",
    "ind_remove = donation_df[donation_df[\"Party\"].isin(val_to_remove)].index\n",
    "\n",
    "donation_df_filtered = donation_df.drop(ind_remove)\n",
    "\n",
    "#checking the Party column for changes\n",
    "print(\"The original DataFrame variables for the 'Party' column are:\")\n",
    "print(donation_df.Party.value_counts())\n",
    "\n",
    "print(\"\\n\\nThe new DataFrame variables for the 'Party' column are:\")\n",
    "print(donation_df_filtered.Party.value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#donation_df_filtered name switch back to donation_df\n",
    "\n",
    "donation_df = donation_df_filtered"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3b. Cleaning the **'Amount'** column\n",
    "##### *I noticed that the values have '$' and ',' so I need to take those out.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#stripping the $ and , symbol from Amount column and converting values to int \n",
    "\n",
    "#df_donate.loc needs to be used to avoid the \"settingwithcopy\" error\n",
    "\n",
    "donation_df.loc[:,'Amount'] = (donation_df['Amount'].str.replace('$', '')\n",
    "                             .str.replace(',', '')\n",
    "                             .astype(int))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Party</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>4000</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>2800</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>2700</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>2700</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Adam Silver</td>\n",
       "      <td>NBA</td>\n",
       "      <td>2700</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Owner League Amount     Party\n",
       "0  Adam Silver    NBA   4000  Democrat\n",
       "1  Adam Silver    NBA   2800  Democrat\n",
       "2  Adam Silver    NBA   2700  Democrat\n",
       "3  Adam Silver    NBA   2700  Democrat\n",
       "4  Adam Silver    NBA   2700  Democrat"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking Amount column for changes \n",
    "donation_df.Amount\n",
    "\n",
    "donation_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 2741 entries, 0 to 2797\n",
      "Data columns (total 4 columns):\n",
      " #   Column  Non-Null Count  Dtype \n",
      "---  ------  --------------  ----- \n",
      " 0   Owner   2741 non-null   object\n",
      " 1   League  2741 non-null   object\n",
      " 2   Amount  2741 non-null   object\n",
      " 3   Party   2741 non-null   object\n",
      "dtypes: object(4)\n",
      "memory usage: 107.1+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(donation_df.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Party</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1083</th>\n",
       "      <td>Jerry Reinsdorf</td>\n",
       "      <td>NBA, MLB</td>\n",
       "      <td>200000</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1085</th>\n",
       "      <td>Jerry Reinsdorf</td>\n",
       "      <td>NBA, MLB</td>\n",
       "      <td>200000</td>\n",
       "      <td>Republican</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1086</th>\n",
       "      <td>Jerry Reinsdorf</td>\n",
       "      <td>NBA, MLB</td>\n",
       "      <td>100000</td>\n",
       "      <td>Democrat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1087</th>\n",
       "      <td>Jerry Reinsdorf</td>\n",
       "      <td>NBA, MLB</td>\n",
       "      <td>100000</td>\n",
       "      <td>Republican</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1088</th>\n",
       "      <td>Jerry Reinsdorf</td>\n",
       "      <td>NBA, MLB</td>\n",
       "      <td>84000</td>\n",
       "      <td>Republican</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Owner    League  Amount       Party\n",
       "1083  Jerry Reinsdorf  NBA, MLB  200000    Democrat\n",
       "1085  Jerry Reinsdorf  NBA, MLB  200000  Republican\n",
       "1086  Jerry Reinsdorf  NBA, MLB  100000    Democrat\n",
       "1087  Jerry Reinsdorf  NBA, MLB  100000  Republican\n",
       "1088  Jerry Reinsdorf  NBA, MLB   84000  Republican"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#looking at the different variables within the League column\n",
    "\n",
    "nba_mlb = [\"NBA, MLB\"]\n",
    "\n",
    "# Create a boolean mask using isin()\n",
    "mask = donation_df['League'].isin(nba_mlb)\n",
    "\n",
    "# Filter the DataFrame\n",
    "result = donation_df[mask]\n",
    "\n",
    "result.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Owner with the most amount donated is \"Charles Johnson\" with $11000700 donated.\n",
      "\n",
      "The Owner with the least amount donated is \"Jerry Bruckheimer\" with $250 donated.\n"
     ]
    }
   ],
   "source": [
    "#find the owners who have donated the most amounts for all parties\n",
    "\n",
    "#group the owners by amount and sum the total amount \n",
    "owner_amount = donation_df.groupby('Owner')['Amount'].sum()\n",
    "\n",
    "#find the owner with the most amount least amount donated\n",
    "most_amount_owner = owner_amount.idxmax()\n",
    "most_amount = owner_amount.max()\n",
    "min_amount_owner = owner_amount.idxmin()\n",
    "min_amount = owner_amount.min()\n",
    "\n",
    "#print the result\n",
    "print(f'The Owner with the most amount donated is \"{most_amount_owner}\" with ${most_amount} donated.')\n",
    "print(f'\\nThe Owner with the least amount donated is \"{min_amount_owner}\" with ${min_amount} donated.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Charles Johnson\n",
      "Jerry Bruckheimer\n"
     ]
    }
   ],
   "source": [
    "#create function to find the owner with the most/least donation amount in complete dataframe\n",
    "\n",
    "def max_donate(donation_df):\n",
    "    owner_donate = donation_df.groupby('Owner')['Amount'].sum()\n",
    "    result = owner_donate.idxmax()\n",
    "    return result\n",
    "\n",
    "print(max_donate(donation_df))\n",
    "\n",
    "def min_donate(donation_df):\n",
    "    owner_donate = donation_df.groupby('Owner')['Amount'].sum()\n",
    "    result = owner_donate.idxmin()\n",
    "    return result\n",
    "\n",
    "print(min_donate(donation_df))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Creating seperate DataFrames for each Party"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4a. Democratic Party"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Democrat' 'Bipartisan' 'Republican']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "League\n",
       "WNBA              210\n",
       "NBA               171\n",
       "MLB               162\n",
       "NFL                92\n",
       "NHL                87\n",
       "NBA, NFL           47\n",
       "NBA, WNBA          47\n",
       "NBA, NHL           38\n",
       "NBA, MLB           29\n",
       "NASCAR             19\n",
       "NBA, NHL, WNBA     15\n",
       "MLB, WNBA           3\n",
       "NBA, NFL, NHL       1\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#checking Party variables\n",
    "print(donation_df.Party.unique())\n",
    "\n",
    "\n",
    "#creating a seperate dataframe for the democratic donations\n",
    "\n",
    "df_dem = donation_df[donation_df[\"Party\"] == \"Democrat\"]\n",
    "\n",
    "df_dem[\"League\"].value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Peter Angelos\n",
      "Dean A. Spanos\n"
     ]
    }
   ],
   "source": [
    "#testing the max/min owner donatin function on the new dataframes\n",
    "\n",
    "#max donation function\n",
    "def dem_max_donate(df_dem):\n",
    "    owner_donate = df_dem.groupby('Owner')['Amount'].sum()\n",
    "    result = owner_donate.idxmax()\n",
    "    return result\n",
    "\n",
    "print(dem_max_donate(df_dem))\n",
    "\n",
    "#min donation function\n",
    "def dem_min_donate(df_dem):\n",
    "    owner_donate = df_dem.groupby('Owner')['Amount'].sum()\n",
    "    result = owner_donate.idxmin()\n",
    "    return result\n",
    "\n",
    "print(dem_min_donate(df_dem))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['NBA', 'MLB', 'NHL', 'NASCAR', 'NFL', 'WNBA', 'NBA, NHL',\n",
       "       'NBA, NFL, NHL', 'NBA, WNBA', 'NBA, MLB', 'NBA, NFL', 'MLB, WNBA',\n",
       "       'NBA, NHL, WNBA'], dtype=object)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_dem.League.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Owner\n",
      "Peter Angelos      2082772\n",
      "Laura Ricketts     1715424\n",
      "John Rogers         661650\n",
      "Ron Burkle          639300\n",
      "Jerry Reinsdorf     410100\n",
      "Name: Amount, dtype: object\n"
     ]
    }
   ],
   "source": [
    "#find the top donors for the Dem party\n",
    "dem_owners = df_dem.groupby('Owner')['Amount'].sum()\n",
    "\n",
    "dem_owners = dem_owners.sort_values(ascending=False)\n",
    "dem_owners.head(5)\n",
    "\n",
    "print(dem_owners.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Owner\n",
      "Andrew Murstein    1000\n",
      "Jeff Dickerson      650\n",
      "Harvey Alter        500\n",
      "Wyc Grousbeck       500\n",
      "Dean A. Spanos      250\n",
      "Name: Amount, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(dem_owners.tail(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\pwurt\\AppData\\Local\\Temp\\ipykernel_31356\\651244572.py:3: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df_dem['index'] = np.arange(len(df_dem))\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "750000"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#sort_value method is combining two seperate rows into one row. I am going to try to seperate\n",
    "\n",
    "df_dem['index'] = np.arange(len(df_dem))\n",
    "    \n",
    "# Sort by 'col1' and then by 'index'\n",
    "df_sorted = df_dem.sort_values(by=['Owner', 'index'])\n",
    "    \n",
    "# Reset index\n",
    "df_sorted = df_sorted.drop(columns=['index']).reset_index(drop=True)\n",
    "\n",
    "df_sorted.Amount.max()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Party</th>\n",
       "      <th>Amount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>Peter Angelos</td>\n",
       "      <td>MLB</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>2082772</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>Laura Ricketts</td>\n",
       "      <td>MLB</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>1715424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>John Rogers</td>\n",
       "      <td>WNBA</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>661650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>Ron Burkle</td>\n",
       "      <td>NHL</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>639300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Jerry Reinsdorf</td>\n",
       "      <td>NBA, MLB</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>410100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Owner    League     Party   Amount\n",
       "70    Peter Angelos       MLB  Democrat  2082772\n",
       "58   Laura Ricketts       MLB  Democrat  1715424\n",
       "53      John Rogers      WNBA  Democrat   661650\n",
       "80       Ron Burkle       NHL  Democrat   639300\n",
       "45  Jerry Reinsdorf  NBA, MLB  Democrat   410100"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_dem = df_sorted\n",
    "\n",
    "# Group by Owner League and Party then sum the specified columns\n",
    "top_five_dem = df_dem.groupby(['Owner','League', 'Party']).sum().reset_index()\n",
    "\n",
    "# Sort the entire DataFrame by 'Amount' in descending order\n",
    "top_five_dem = top_five_dem.sort_values(by='Amount', kind='sort', ascending=False)\n",
    "\n",
    "top_five_dem.head(5)\n",
    "\n",
    "df_dem = top_five_dem\n",
    "\n",
    "df_dem.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Sum, Mean, Median"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total Amount donated (USD) for the Democratic Party is $10113639.\n",
      "The mean amount is $101136.39.\n",
      "The median amount is $17837.5.\n"
     ]
    }
   ],
   "source": [
    "dem_amount_sum = df_dem['Amount'].sum()\n",
    "dem_amount_mean = df_dem['Amount'].mean().round(2)\n",
    "dem_amount_median = df_dem['Amount'].median()\n",
    "\n",
    "print(f'The total Amount donated (USD) for the Democratic Party is ${dem_amount_sum}.\\nThe mean amount is ${dem_amount_mean}.\\nThe median amount is ${dem_amount_median}.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Party</th>\n",
       "      <th>Amount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>Peter Angelos</td>\n",
       "      <td>MLB</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>2082772</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>Laura Ricketts</td>\n",
       "      <td>MLB</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>1715424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>John Rogers</td>\n",
       "      <td>WNBA</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>661650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>Ron Burkle</td>\n",
       "      <td>NHL</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>639300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Jerry Reinsdorf</td>\n",
       "      <td>NBA, MLB</td>\n",
       "      <td>Democrat</td>\n",
       "      <td>410100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Owner    League     Party   Amount\n",
       "70    Peter Angelos       MLB  Democrat  2082772\n",
       "58   Laura Ricketts       MLB  Democrat  1715424\n",
       "53      John Rogers      WNBA  Democrat   661650\n",
       "80       Ron Burkle       NHL  Democrat   639300\n",
       "45  Jerry Reinsdorf  NBA, MLB  Democrat   410100"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create function to sort the top donors to the Democratic party\n",
    "def top_dems(df_dem):\n",
    "    # Group by Category and State and sum the specified columns\n",
    "    top_ten_dem = df_sorted.groupby(['Owner','League', 'Party']).sum().reset_index()\n",
    "    # Sort the entire DataFrame by 'Usd Pledged Real' in descending order\n",
    "    top_ten_dem = top_ten_dem.sort_values(by='Amount', kind='sort', ascending=False)\n",
    "    return top_ten_dem\n",
    "\n",
    "top_dems(df_dem).head()\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Create Bar graph for the democratic donors**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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JRlJ5t1337VpWxj/5T63U1JSjMViMa+++uoV7dfPP/9sTp48aVN37NgxU716dXPzzTfb1E+aNMlIMj/99JO1bvv27aZSpUrmueees9Zt2bLFHD161Gbds2fPmsaNG5trr73Wpn7evHlGklmwYIG17siRIyYoKMj07du3WLzNmjUz/fv3d3xH8T+PpBu4ipSUdOfm5poRI0aYa6+91nh5eZmGDRuaKVOmmIKCApt2hV9GZ8+ebRo2bGi8vb1Nq1atzKpVq+zaduH6p0+fNmfOnLmi+F988UUTHBxszp07Zx5//HHToEGDYm327dtnJJkpU6aYN99809SpU8f4+vqa22+/3aSlpZmCggLzz3/+09SoUcP4+PiY7t27m+PHjxfrZ8mSJeaWW24xfn5+xt/f39x5551my5YtNm0SEhJMlSpVzO7du02XLl2Mv7+/ufvuu63LoqKibNrn5+ebadOmmWbNmhlvb29TrVo1Ex8fb5NsfPjhh6Zjx46mevXqxsvLyzRp0qTEL9+FX9q///57c8MNNxhvb29Tp04d89FHH132OE6YMMFIMvv3779s28J93LNnj+ncubPx8/MzERERZvz48cXGyJWMpejoaFO5cmUzdepUI6lYsTcBL+2L7KxZs0yrVq2Mj4+PCQ4ONr179zZpaWk2bVavXm169eplatasaby8vMy1115rhg8fbk6fPl3isfj9999N165dTZUqVUxkZKR58803jTHGbN682XTs2NH4+fmZWrVqlfijRknKSvR+//13U7lyZXPTTTfZ1GdkZJiHH37YhIaGGm9vb9OiRQszc+ZMmzZF/xbeffddU7duXePl5WXatGlj86W00IoVK6xjPjAw0HTv3t1s27bNps3YsWONJLN161bTt29fExQUZFq2bGmMMebw4cNmwIABpkaNGsbLy8uEh4eb7t27l5lcdOjQodh7npCQYF0+f/586/tXtWpV069fP/PHH3/Y9FHW3+GlCuO/tBTGWPhefPHFF6Zp06bGy8vLREdHm6VLlxbr648//jADBw40oaGh1nYffPBBqftaVGlJtzHGnDx50oSEhJgaNWrY/O3k5+ebqVOnmujoaOPt7W1CQ0PN4MGDTWZmZol9Jycnm9atWxsfHx/TrFkza9L62WefWT+DWrVqZTZs2FAsBnvGQuExePjhh01ERITx8vIytWvXNo899pg1yZsxY4aRZL777jvz+OOPm+rVq5ugoCBjjDH79+83jz/+uGnYsKHx8fExISEhplevXjbjpXD9S0vhvnTo0MF06NDBJqYzZ86YsWPHmgYNGhhvb28THh5u7rnnHrN79+4y35OSkm5jjOnVq5eRZA4ePGhXzGXtd1njr3379qZFixYlxtawYUPTuXPnMuMfM2aM8fLysvvHgVatWplWrVrZ1IWGhpr77ruvxO136tSpxH4ul3T37t3bREREmPz8fFNQUFAsgb5SPXv2NCEhITZ1N9xwg7nhhhuKte3cubOpV6/eZfscMWKEkWRycnKsdffdd58JCwsz+fn5Nm0HDx5s/Pz8zNmzZ23qn376aRMUFFTs/z3gcki6gavIpUl3QUGBue2224zFYjGPPPKIefPNN023bt2MJDN8+HCbdSWZZs2amWrVqpl//vOfZtKkSSYqKsr4+vqaX3/99bLblmSqVKliLBaLkWSaNGlid1JSqHHjxiYxMdEYczFRuvQXbWP+L9Fo2bKliY6ONq+++qr5xz/+Yby8vMyNN95onn/+eXPTTTeZ119/3QwbNsxYLBYzcOBAmz4+/vhjY7FYzB133GHeeOMNM2nSJFO7dm0TFBRk8+UqISHBeHt7m3r16pmEhAQzffp08/HHH1uXXZp0DxgwwEgyXbp0MdOmTTOvvPKKufvuu80bb7xhbXPDDTeYAQMGmKlTp5o33njDdO7c2UiyJnaFoqKiTKNGjUxYWJh5/vnnzZtvvmlatWplLBZLsR8HLvXJJ58YSeaf//znZb8YJCQkGB8fH9OgQQPTv39/8+abb5q77rrLSDKjR4+2tnN0LDVp0sRUr17djB8/3rz11ltmzZo15p133jGSzD333GNmzZplZs2aZTZt2lRmfIVKSrpfeuklY7FYTO/evc3bb79txo8fb6pVq2Zq165tTpw4YW335JNPmjvvvNO8/PLL5t133zWJiYmmUqVKplevXiUei+joaPPYY4+Zt956y9x0001GkpkxY4aJjIw0zz77rHnjjTdM06ZNTaVKlczevXsvG/vlzq526tTJeHh4WK9AOH36tGnSpInx9PQ0Tz/9tHn99ddNu3btjCQzbdo063qFfwvXX3+9qV+/vpk0aZKZPHmyqVatmrn22mttvpwnJSWZypUrm4YNG5rJkydbj1VwcLDNMS1MGqKjo83dd99t3n77bfPWW28ZY4y56aabTGBgoPnHP/5h/vOf/5iXX37ZdOzYscwf5r799lszePBg63icNWuW+eGHH4wx/5e43HDDDWbq1Knm73//u/H19S32/pX1d3ipTZs2mb59+xpJZurUqdZxVngWUpK57rrrTEREhHnxxRfNtGnTTN26dY2fn585duyYtZ/09HRz7bXXmpo1a5p//vOf5p133jHdu3e39ns5ZSXdxhiTmJhoJNn8LT/yyCOmcuXKZtCgQWb69Olm1KhRpkqVKuaGG26weS8LPxsiIiLMuHHjzNSpU02NGjWMv7+/mT17tqlVq5aZOHGimThxogkMDDT169e3SSjsHQsHDx40kZGRxs/PzwwfPtxMnz7djB492jRp0sT6/hS+h9HR0aZDhw7mjTfeMBMnTjTGXDyDfd1115kxY8aY9957zzz//PMmODjYREVFmVOnThljjNmzZ48ZNmyYkWSef/556/uVnp5ujCmedF+4cMF06tTJSDJ9+vQxb775ppkwYYK57bbbzMKFC8t8T0pLulu1amUqVapkTp06ZVfMZe13WePv/fffN5KK/X/6008/GUmljulCcXFxxZLo0hQUFJgaNWrYJPJ//PGHkWQmTZpUrP2DDz5YLMEtdLmku1q1aqZ79+5m6tSppmrVqkaSCQ8Pt/l/70rcdNNNpmHDhtbX+fn5xtvb2zz++OPF2v7jH/8olkyX5IEHHjB+fn7mwoUL1rr69eubLl26FGv7n//8x0gymzdvtqmfPXt2ie8jcDkk3cBV5NKke+HChUaSeemll2za9erVy1gsFpszA4W/yP/888/Wut9//934+PiYe+6557Lbvummm8y0adPMl19+ad555x3TrFkzhy6h/Pnnn40kk5SUZIy5+KXh2muvNU899ZRNu8JEo3r16iYrK8ta/9xzz1m/UOfl5Vnr+/bta7y8vKy/Vp88edIEBQWZQYMG2fSbnp5uAgMDbeoTEhKMJPP3v/+9WLyXJt0rV640ksywYcOKtS2a+F56dtUYY+Lj403dunVt6qKioowks3r1amvdkSNHjLe3txk5cmSxPoo6ffq0adSokZFkoqKizIABA8wHH3xgMjIyStwPSebJJ5+0ibdr167Gy8vLeomeo2PJw8PDbN261aZteV5evn//flOpUiXzr3/9y6bdr7/+aipXrmxTX9IxnzBhgrFYLDaXWRYei5dfftlad+LECePr62ssFouZO3eutX7Hjh1278vlku6nnnrKSLL+ADFt2jQjycyePdva5vz58yY2Ntb4+/tbv1gW/i1UrVrV5mzol19+aSSZr7/+2lrXsmVLExoaanPVx6ZNm4yHh4d56KGHrHWFSfell1WeOHHCelbdUYUJStErPs6fP29CQ0NNs2bNbK6MWbRokZFkxowZY60r6++wJJe7vNzLy8tmvG7atMlIskkSEhMTTUREhE0ibowxffr0MYGBgSWOqaIul3QXXvnx5ZdfGmOM+f7770u8JWTZsmXF6gs/Gwp/vDDGmG+++cZIKnbp8Lvvvlvs0m17x8JDDz1kPDw8SrwtoPAzrfC9veWWW2wSGWNK/rtLSUkplmCWdXn5pUn3hx9+aCSVeCnz5X5g7NChg2ncuLE5evSoOXr0qNm+fbs14e/WrZtDMZe136WNv6ysLOPj42NGjRplUz9s2DBTpUqVy16Wf+2115p77723zDaFZs2aZSTZXJmxfv36UpP7Z5991kgqdlbXmLI/tzMzM62fQf7+/mbKlClm3rx55o477jCSzPTp0+2K91KrV682FovF5offwjj++c9/Fmv/1ltvGUlmx44dpfa5a9cu4+PjU+zS8CpVqpiHH364WPvFixcbSWbZsmU29T/88IORZObNm+fobuF/HE8vB65iS5YsUaVKlTRs2DCb+pEjR8oYo6VLl9rUx8bGqnXr1tbXtWrV0t13361vvvlG+fn5ZW5r7dq1euqpp9S9e3c99thjSk1NVbNmzfT888/rzJkzl411zpw5CgsLU8eOHSVdfIhL7969NXfu3BK3fd999ykwMND6uvBp5w8++KAqV65sU3/+/HkdPHhQkpSUlKSsrCz17dtXx44ds5ZKlSopJiZGycnJxbb1+OOPXzb+zz77TBaLRWPHji22zGKxWP/t6+tr/Xd2draOHTumDh06aO/evcrOzrZZLzo6Wu3atbO+rl69uho1alTsSa2X8vX11bp16/Tss89KkmbOnKnExERFREToySef1Llz54qtU/RpuIXTKp0/f976tFdHx1KHDh0UHR1dZpx/xueff66CggLdf//9Nu9jeHi4GjRoYPM+Fj3mp06d0rFjx3TTTTfJGKNffvmlWN+PPPKI9d9BQUFq1KiRqlSpovvvv99a36hRIwUFBV32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in0O2RvT5dgbc1kutz/9+/fXiRMn9Oijjyo3N1cPPvigXf3GxsZqy5Ytxf7e8vPz1bt3b6WkpGjBggU29/pf6t5779WiRYt04MABa92KFSv022+/6b777rMrjkv17t1b+fn5+uijj6x1Z8+e1Zw5cxQdHW09UxwXF2dTip75fvLJJzVv3jy9/fbb6tmzZ6nb6tWrl9avX28zJnfu3KmVK1cWi3/KlCl65ZVX9Pzzz+upp54qs8+MjAx9/vnn1rpjx45pwYIF6tatW7Gz/6mpqQoMDLT50QCwB2e6gatYt27d1LFjR73wwgvav3+/rrvuOn377bf68ssvNXz4cJuHCUlSs2bNFB8fr2HDhsnb21tvv/22JJWYSBb11ltvWR+6U6tWLR0+fFgffvih0tLSNGvWLJtfvy/11Vdf6eTJk+revXuJy2+88UZVr15dc+bMUe/evR08AsUFBATonXfeUf/+/dWqVSv16dNH1atXV1pamhYvXqybb765xC90l9OxY0f1799fr7/+unbt2qU77rhDBQUF+v7779WxY0cNHTpUnTt3lpeXl7p162b9wvX+++8rNDS0xMvbrlRSUpLGjh2r7t2768Ybb5S/v7/27t2rDz/8UOfOndO4ceNs2vv4+GjZsmVKSEhQTEyMli5dqsWLF+v555+3nqVwdCyVxNfXV9HR0Zo3b54aNmyokJAQNWvWzO77RouqV6+eXnrpJT333HPav3+/evTooWuuuUb79u3TF198ocGDB+uZZ55R48aNVa9ePT3zzDM6ePCgAgIC9Nlnn5XLvdiO+O233zR79mwZY5STk6NNmzZpwYIFys3N1auvvqo77rjD2nbw4MF69913NWDAAKWmpqp27dr69NNPtXbtWk2bNq3Y2Rx7TJkyRV26dFFsbKwSExN15swZvfHGGwoMDCw2HkqLv1OnTrr//vsVHR2typUr64svvlBGRob69OnjcDyenp6aNGmSBg4cqA4dOqhv377KyMjQa6+9ptq1a+vpp592uM9ChT/yvfDCC+rTp488PT3VrVs3u8/mS9LEiROVnJysmJgYDRo0SNHR0crMzNSGDRu0fPnyy94yI0kHDx60XgGQm5urbdu2acGCBUpPT9fIkSP16KOPWtt26NBBjz76qCZMmKCNGzeqc+fO8vT01K5du7RgwQK99tprNvfM/hn2joWXX35Z3377rTp06KDBgwerSZMmOnz4sBYsWKA1a9YoKCiozO3cddddmjVrlgIDAxUdHa2UlBQtX75cVatWtWnXsmVLVapUSZMmTVJ2dra8vb112223WS9PLuqhhx7Sxx9/rBEjRuinn35Su3btdOrUKS1fvlxPPPGE7r777j91bOyNuSyXG3/XX3+9mjVrpgULFqhJkyZq1aqVXf3efffdevHFF7Vq1Sqb261Gjhypr776St26dVNmZmaxq06KJvXPP/+8FixYoI4dO+qpp55Sbm6upkyZoubNm1ufV1Bo1qxZ+v3333X69GlJ0urVq623JfXv39961cSjjz6q//znPxoyZIh+++031apVy7ru119/fdn9mjZtmt5++23FxsbKz8+vWPz33HOP9dg98cQTev/999W1a1c988wz8vT01KuvvqqwsDCNHDnSus4XX3yhv/3tb2rQoIGaNGlSrM/bb79dYWFhki4m3TfeeKMGDhyobdu2qVq1anr77beVn59f4nefpKQkdevWjXu64bi/5BnpAP4Sl04ZZszFKbKefvppExkZaTw9PU2DBg3MlClTik2vov8/rdHs2bNNgwYNjLe3t7n++utLnMblUt9++625/fbbTXh4uPH09DRBQUGmc+fOZsWKFZddt1u3bsbHx8dmDtRLDRgwwHh6eppjx45Zp0m6dOqi5ORkI8ksWLDApr6k6YoK28fHx5vAwEDj4+Nj6tWrZwYMGGAzZVpCQoKpUqVKiTGVNE/3hQsXzJQpU0zjxo2Nl5eXqV69uunSpYtJTU21tvnqq69MixYtjI+Pj6ldu7aZNGmSdRqcolPMlDbl0KVT6JRk7969ZsyYMebGG280oaGhpnLlyqZ69eqma9euZuXKlcX2o0qVKmbPnj2mc+fOxs/Pz4SFhZmxY8fazO1rjONjqSQ//PCDad26tfHy8nJo+rDSpuH57LPPzC233GKqVKliqlSpYho3bmyGDBlidu7caW2zbds2ExcXZ/z9/U21atXMoEGDrNNEzZgxo9ixuFRp8/teblqoQvr/0/Hp/0+lFhQUZK6//nrz1FNPFZtWrVBGRoYZOHCgqVatmvHy8jLNmze3idUYU+rfQuE2Lz22y5cvNzfffLPx9fU1AQEBplu3bmbbtm02bQqnDCucKq7QsWPHzJAhQ0zjxo1NlSpVTGBgoImJiTHz58+/7P6X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RxEREZKk1q1by9PTUytWrLC22blzp9LS0hQbG1tiH3Xq1FF4eLjNOjk5OVq3bp11ndjYWGVlZSk1NdXaZuXKlSooKFBMTIy1zerVq5WXl2dtk5SUpEaNGik4OLjEbXt7eysgIMCmAAAAAADcQ4Um3bm5udq4caP1SeP79u3Txo0bbR58VpIPPvhAMTExatasWbFlzzzzjFatWqX9+/frhx9+0D333KNKlSqpb9++ki4+AC0xMVEjRoxQcnKyUlNTNXDgQMXGxpb45HLp4pPVhw8frpdeeklfffWVfv31Vz300EOKjIy0Xt7epEkT3XHHHRo0aJB++uknrV27VkOHDlWfPn0UGRkpSXrggQfk5eWlxMREbd26VfPmzdNrr72mESNGXOERBAAAAAC4NFOBkpOTjaRiJSEhwRhjzNixY01UVJTNOllZWcbX19e89957JfbZu3dvExERYby8vEyNGjVM7969ze7du23anDlzxjzxxBMmODjY+Pn5mXvuucccPnzYpk1UVJQZO3as9XVBQYEZPXq0CQsLM97e3qZTp05m586dNuscP37c9O3b1/j7+5uAgAAzcOBAc/LkSZs2mzZtMrfccovx9vY2NWrUMBMnTnTgiBmTnZ1tJJns7GyH1vsrXZwkikK5WAAAAICrkb25mcvM012ShIQEWSwWzZw58y/d7unTp1W1alUtXbpUt95661+67cthnm64G9f9hAEAAACunL25mcs+vdwYo++++05r1qz5y7ednJys2267zeUSbgBXhh+CUBQ/BAEAgL+SS5/pRnGc6Ya7cYVPGMYkinKFMQkAANyfvbmZWz69HAAAAAAAd0DSDQAAAACAk1zRPd1paWn6/fffdfr0aVWvXl1NmzaVt7d3eccGAAAAAIBbszvp3r9/v9555x3NnTtXf/zxh4reCu7l5aV27dpp8ODBuvfee+XhwQl0AAAAAADsyo6HDRum6667Tvv27dNLL72kbdu2KTs7W+fPn1d6erqWLFmiW265RWPGjFGLFi20fv16Z8cNAAAAAIDLs+tMd5UqVbR3715VrVq12LLQ0FDddtttuu222zR27FgtW7ZMBw4c0A033FDuwQIAAAAA4E6YMszNMGUY3I0rfMIwJlGUK4xJAADg/uzNza7oQWrHjh3T/v37ZbFYVLt27RLPgAMAAAAA8L/OoSeebd26Ve3b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t6hZs2Z69dVXdfToUWfECQAAAACA27niB6lVrlxZPXv21IIFCzRp0iTt3r1bzzzzjGrWrKmHHnpIhw8fLs84AQAAAABwO1ecdP/888964oknFBERoVdffVXPPPOM9uzZo6SkJB06dEh33313ecYJAAAAAIDbqezoCq+++qpmzJihnTt36s4779THH3+sO++8Ux4eF/P3OnXqaObMmapdu3Z5xwoAAAAAgFtxOOl+55139PDDD2vAgAGKiIgosU1oaKg++OCDPx0cAAAAAADuzGKMMRUdBOyXk5OjwMBAZWdnKyAgoKLDKZHFUtERwJW4wicMYxJFucKYBAAA7s/e3OyK7un+/vvv9eCDDyo2NlYHDx6UJM2aNUtr1qy5smgBAAAAALgKOZx0f/bZZ4qPj5evr69++eUXnTt3TpKUnZ2tl19+udwDBAAAAADAXTmcdL/00kuaPn263n//fXl6elrrb775Zm3YsKFcgwMAAAAAwJ05nHTv3LlT7du3L1YfGBiorKys8ogJAAAAAICrgsNJd3h4uHbv3l2sfs2aNapbt265BAUAAAAAwNXA4aR70KBBeuqpp7Ru3TpZLBYdOnRIc+bM0TPPPKPHH3/cGTECAAAAAOCWHJ6n++9//7sKCgrUqVMnnT59Wu3bt5e3t7eeeeYZPfnkk86IEQAAAAAAt3TF83SfP39eu3fvVm5urqKjo+Xv71/esaEEzNMNd+MKcyIzJlGUK4xJAADg/uzNzRw+013Iy8tL0dHRV7o6AAAAAABXPYeT7lOnTmnixIlasWKFjhw5ooKCApvle/fuLbfgAAAAAABwZw4n3Y888ohWrVql/v37KyIiQhau2wQAAAAAoEQOP7186dKlWrBggSZNmqThw4frqaeesimOWL16tbp166bIyEhZLBYtXLjwsut89913atWqlby9vVW/fn3NnDmzWJu33npLtWvXlo+Pj2JiYvTTTz/ZLD979qyGDBmiqlWryt/fX/fee68yMjLK3K4xRmPGjFFERIR8fX0VFxenXbt22bTJzMxUv379FBAQoKCgICUmJio3N9emzebNm9WuXTv5+PioZs2amjx58mX3GQAAAADgnhxOuoODgxUSElIuGz916pSuu+46vfXWW3a137dvn7p27aqOHTtq48aNGj58uB555BF988031jbz5s3TiBEjNHbsWG3YsEHX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+dL7MpkMPXv2xJkzZ5Cfn4/ExERMnToVJSUlSEpKQlRUFP7xj3/AyMhI9THW1taqghsAGjZsiJycHADA7du3UVRUBDc3N9SpU0f1Cg0NRWpqqtq/7ezsrHY9e/Zs+Pj4wNXVFQEBAVXeT0REJAqLbiIiIlJjZ2cHmUyGmzdvvvD+zZs3YW5uDktLS/Tu3RtnzpzBuXPn4OTkBFNTU1UhHhUVpTY7DaDKkm+ZTIbKykoAQGFhIQDg8OHDuHbtmuqVmJiotq8bAIyNjdWulyxZghs3bmDIkCE4deoU2rRpg3379lXr80BERKQJLLqJiIhIzRtvvAE3Nzd8/fXXKC4uVruXnZ2Nb7/9Fh4eHpDJZKp93T/88INq73bv3r1x4sQJREdHq+3n/itt2rSBgYEBMjIyYGdnp/Zq0qTJX358y5YtMWvWLERGRsLd3R3BwcH/zX82ERFRjWDRTURERFVs3LgRJSUlGDBgAM6ePYvMzEwcO3YMbm5uaNy4MVasWAEAaNeuHczNzfHdd9+pFd379+9HSUkJXFxc/va/aWJiAj8/P8yaNQshISFITU1FbGwsvvzyS4SEhPzpxxUXF2P69Ok4c+YM7t69i+joaFy+fPlP96QTERFpExupERERURUtWrRATEwMFi9ejHfeeQd5eXlo0KABRowYgcWLF8PCwgLA8+XhPXr0wOHDh9G9e3cAzwtxU1NTtGrVqsoy8L/y73//G5aWlli1ahXS0tJQt25ddOzYEZ988smffoyOjg5yc3Ph5eWF+/fvo169enB3d8fSpUv/908AERGRhsiUf9UlhYiIiIiIiIj+J1xeTkRERERERFRDWHQTERERERER1RAW3UREREREREQ1hEU3ERERERERUQ1h0U1ERERERERUQ1h0ExEREREREdUQFt1ERERERERENYRFNxEREREREVENYdFNREREREREVENYdBMRERERERHVEBbdRERERERERDWERTcRERERERFRDfk/xHPP74AuKxMAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.ticker import FuncFormatter\n",
    "\n",
    "#change type of Amount column\n",
    "df_dem['Amount'] = pd.to_numeric(df_dem['Amount'], errors='coerce')\n",
    "\n",
    "# Step 1: Extract Data\n",
    "# Replace these with your actual DataFrame columns\n",
    "top_5_owners = df_dem.groupby('Owner')['Amount'].sum().nlargest(5)\n",
    "\n",
    "# Step 2: Create the Plot\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(top_5_owners.index, top_5_owners.values, color='blue')\n",
    "\n",
    "#add text to amount donated by the highest donor\n",
    "plt.text(0, top_5_owners.values[0], f'{top_5_owners.values[0]:,.0f}', \n",
    "         ha='center', va='bottom', fontsize=12, color='black')\n",
    "\n",
    "\n",
    "\n",
    "# Step 3: Rotate x-axis labels\n",
    "plt.xticks(rotation=90)\n",
    "\n",
    "# Step 4: Add Title and Labels\n",
    "plt.title('Top 5 American Sport Team Donors for the Democratic Party (2016-2020)')  # Title of the plot\n",
    "plt.xlabel('Owners')  # Label for x-axis\n",
    "plt.ylabel('Amount of Money Donated (USD)')  # Label for y-axis\n",
    "\n",
    "# Step 5: Optional - Add Gridlines\n",
    "# Uncomment the following line if you want to add gridlines\n",
    "# plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7)\n",
    "\n",
    "# Step 6: Adjust Layout\n",
    "plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))\n",
    "plt.tight_layout()  # Adjust layout to avoid overlap\n",
    "\n",
    "# Step 7: Show the Plot\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4b. Republican Party"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                       Owner  League Amount       Party\n",
      "2757            Tony Ressler     NBA   2000  Republican\n",
      "2758           Troy Stafford  NASCAR    250  Republican\n",
      "2767  W. Joseph Williams Jr.     MLB   5400  Republican\n",
      "2768  W. Joseph Williams Jr.     MLB   5100  Republican\n",
      "2769  W. Joseph Williams Jr.     MLB   5000  Republican\n",
      "2770  W. Joseph Williams Jr.     MLB   2500  Republican\n",
      "2771  W. Joseph Williams Jr.     MLB   2000  Republican\n",
      "2772  W. Joseph Williams Jr.     MLB   1500  Republican\n",
      "2774  W. Joseph Williams Jr.     MLB   1000  Republican\n",
      "2776  W. Joseph Williams Jr.     MLB    400  Republican\n"
     ]
    }
   ],
   "source": [
    "#creating a seperate df for the republican donations \n",
    "\n",
    "df_rep = donation_df[donation_df[\"Party\"] == \"Republican\"]\n",
    "\n",
    "df_rep.head(20)\n",
    "print(df_rep.tail(10))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Owner\n",
      "Charles Johnson           10995500\n",
      "Dan DeVos                  2280400\n",
      "Philip F. Anschutz         1776700\n",
      "Jimmy and Susan Haslam     1596900\n",
      "Dan Gilbert                1479700\n",
      "Name: Amount, dtype: object\n"
     ]
    }
   ],
   "source": [
    "#find the top donors for the Rep party\n",
    "rep_owners = df_rep.groupby('Owner')['Amount'].sum()\n",
    "\n",
    "rep_owners = rep_owners.sort_values(ascending=False)\n",
    "rep_owners.head(5)\n",
    "\n",
    "print(rep_owners.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Party</th>\n",
       "      <th>Amount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Charles Johnson</td>\n",
       "      <td>MLB</td>\n",
       "      <td>Republican</td>\n",
       "      <td>10995500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Dan DeVos</td>\n",
       "      <td>NBA</td>\n",
       "      <td>Republican</td>\n",
       "      <td>2280400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>74</th>\n",
       "      <td>Philip F. Anschutz</td>\n",
       "      <td>NHL</td>\n",
       "      <td>Republican</td>\n",
       "      <td>1776700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Jimmy and Susan Haslam</td>\n",
       "      <td>NFL</td>\n",
       "      <td>Republican</td>\n",
       "      <td>1596900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Dan Gilbert</td>\n",
       "      <td>NBA</td>\n",
       "      <td>Republican</td>\n",
       "      <td>1479700</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Owner League       Party    Amount\n",
       "11         Charles Johnson    MLB  Republican  10995500\n",
       "20               Dan DeVos    NBA  Republican   2280400\n",
       "74      Philip F. Anschutz    NHL  Republican   1776700\n",
       "49  Jimmy and Susan Haslam    NFL  Republican   1596900\n",
       "21             Dan Gilbert    NBA  Republican   1479700"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Group by Owner League and Party then sum the specified columns\n",
    "top_five_rep = df_rep.groupby(['Owner','League', 'Party']).sum().reset_index()\n",
    "\n",
    "# Sort the entire DataFrame by 'Amount' in descending order\n",
    "top_five_rep = top_five_rep.sort_values(by='Amount', kind='sort', ascending=False)\n",
    "\n",
    "top_five_rep.head(5)\n",
    "\n",
    "df_rep = top_five_rep\n",
    "\n",
    "df_rep.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Party</th>\n",
       "      <th>Amount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Andrew Murstein</td>\n",
       "      <td>NASCAR</td>\n",
       "      <td>Republican</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>54</th>\n",
       "      <td>John Mara</td>\n",
       "      <td>NFL</td>\n",
       "      <td>Republican</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>78</th>\n",
       "      <td>Richard Petty</td>\n",
       "      <td>NASCAR</td>\n",
       "      <td>Republican</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>Jerry Bruckheimer</td>\n",
       "      <td>NHL</td>\n",
       "      <td>Republican</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>102</th>\n",
       "      <td>Troy Stafford</td>\n",
       "      <td>NASCAR</td>\n",
       "      <td>Republican</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Owner  League       Party Amount\n",
       "1      Andrew Murstein  NASCAR  Republican   1000\n",
       "54           John Mara     NFL  Republican   1000\n",
       "78       Richard Petty  NASCAR  Republican   1000\n",
       "46   Jerry Bruckheimer     NHL  Republican    250\n",
       "102      Troy Stafford  NASCAR  Republican    250"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_rep.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Sum, Mean, Median"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total Amount donated (USD) for the Republican Party is $34246016.\n",
      "The mean amount is $329288.62.\n",
      "The median amount is $41429.0.\n"
     ]
    }
   ],
   "source": [
    "rep_amount_sum = df_rep['Amount'].sum()\n",
    "rep_amount_mean = df_rep['Amount'].mean().round(2)\n",
    "rep_amount_median = df_rep['Amount'].median()\n",
    "\n",
    "print(f'The total Amount donated (USD) for the Republican Party is ${rep_amount_sum}.\\nThe mean amount is ${rep_amount_mean}.\\nThe median amount is ${rep_amount_median}.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "#change type of Amount column\n",
    "df_rep['Amount'] = pd.to_numeric(df_rep['Amount'], errors='coerce')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Create a bar graph for the Republican Party**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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xEQEBgbC3t4ec+bMgbe3N4QQiI2NxdKlS/HBBx/gwoULcHBw0GW+RERERERERGWGxs90jx07Fnv27MGRI0dgamoqW5ednY0mTZogODgY06ZN00mipDk+001lBp/pJiIiIqIyStO6S+Pu5ZGRkRg7dqxawQ0AZmZmGDNmDHbv3v1m2RIRERERERG9hTQuuq9fv4569eoVur5Bgwa4fv16sSRFRERERERE9DbQuOjOyMgo8pZ5hQoVkJmZWSxJEREREREREb0NtJoyLCMjo8Du5cCL/uyc8puIiIiIiIjo/2hcdAshUL169SLXKzhAFhEREREREZFE46J73759usyDiIiIiIiI6K2jcdEdGBioyzyIiIiIiIiI3joaF925ubnIy8uDiYmJ1JaUlIQlS5bgyZMnaNeuHZo0aaKTJImIiIiIiIjKIo2L7gEDBkCpVOLnn38G8GJQtffeew9Pnz6Fs7Mz5s6diz///BOtW7fWWbJEREREREREZYnGU4YdOXIEnTt3ll7/9ttvyMvLw5UrV3D27FmMHDkSs2bN0kmSRERERERERGWRxkX33bt34eXlJb2OiopC586dYW1tDQAICwvDxYsXiz9DIiIiIiIiojJK46Lb1NQU2dnZ0utjx47B399ftj4zM7N4syMiIiIiIiIqwzQuuuvUqYNVq1YBAA4dOoSkpCQ0b95cWn/t2jW4uLgUf4ZEREREREREZZTGA6lNnDgRrVq1wvr163H//n307dsXzs7O0vrNmzejcePGOkmSiIiIiIiIqCzSap7uEydOIDIyEk5OTujatatsfZ06ddCwYcNiT5CIiIiIiIiorFIIIYS+k6DilZ6eDmtra6SlpcHKykrf6ahTKPSdAZUWvPwQERERURmlad2l8Z3uBQsWFNhubW2N6tWrIyAgQPssiYiIiIiIiN5iGhfdc+fOLbA9NTUVaWlpeP/997F161bY2dkVW3JEREREREREZZnGo5ffuHGjwOXx48e4evUqVCoVvvnmG13mSkRERERERFSmaFx0F6VKlSqYPn06/v777+LYHREREREREdFboViKbgBwc3NDYmJice2OiIiIiIiIqMwrtqL7/PnzcHd3L67dEREREREREZV5Gg+klp6eXmB7WloaTp48iVGjRiEsLKzYEiMiIiIiIiIq6zQuum1sbKAoZH5lhUKB/v37Y9y4ccWWGBEREREREVFZp3HRvW/fvgLbrays4OXlBUtLy2JLioiIiIiIiOhtoHHRHRgYqMs8iIiIiIiIiN46Gg2klpCQoNVO7969+0bJEBEREREREb1NNCq633vvPQwcOBDHjx8vNCYtLQ1Lly5FzZo18ccffxRbgkRERERERERllUbdy2NjY/H999/jo48+gqmpKerXrw8XFxeYmpri8ePHiI2NxcWLF1GvXj3MnDkTrVu31nXeRERERERERKWeQgghNA3Ozs7G9u3bcfjwYdy6dQvZ2dmoVKkS6tati5CQENSsWVOXuZKG0tPTYW1tjbS0NFhZWek7HXWFjIJP5ZDmlx8iIiIiolJF07pLq6KbygYW3VRm8PJDRERERGWUpnWXRs90ExEREREREZH2WHQTERERERER6QiLbiIiIiIiIiIdYdFNREREREREpCOluujOy8vDhAkT4OnpCTMzM1StWhXfffcdXjf22/79+1GvXj2YmJigWrVqWLFihVrMjz/+CA8PD5iamsLf3x///POPbP3Tp08xaNAgVKxYEZaWlujcuTOSkpKKPK4QAhMnToSzszPMzMwQFBSEK1euyGJSUlLQq1cvWFlZwcbGBuHh4cjMzJTFnDt3Dh988AFMTU3h6uqKmTNnFnlcIiIiIiIiKp00mqd769atGu+wXbt2b5zMq2bMmIHFixdj5cqV8PX1xYkTJ9CvXz9YW1tj6NChBW5z48YNhIaG4rPPPsPq1asRFRWF/v37w9nZGSEhIQCAdevWYeTIkViyZAn8/f0xb948hISEID4+Hg4ODgCAESNGYPv27diwYQOsra0xePBgdOrUCUeOHCk035kzZ2LBggVYuXIlPD09MWHCBISEhCA2NhampqYAgF69euH+/fuIjIzE8+fP0a9fP0RERGDNmjUAXoyAFxwcjKCgICxZsgTnz5/Hp59+ChsbG0RERBTbZ0tERERERES6p9GUYQYG8hviCoVCdrdZ8dIUUHl5ecWWXJs2beDo6Ihff/1VauvcuTPMzMzw+++/F7jN2LFjsX37dly4cEFq69GjB1JTU7Fr1y4AgL+/P9577z0sWrQIAKBSqeDq6oohQ4Zg3LhxSEtLg729PdasWYMuXboAAC5duoR3330X0dHRaNSokdpxhRBwcXHBqFGjMHr0aABAWloaHB0dsWLFCvTo0QNxcXHw8fHB8ePH0aBBAwDArl270Lp1a9y5cwcuLi5YvHgxxo8fj8TERCiVSgDAuHHjsGXLFly6dEmjz41ThlGZwSnDiIiIiKiMKtYpw1QqlbT8/fffqFOnDnbu3InU1FSkpqZix44dqFevnlTUFpf3338fUVFRuHz5MgDg7NmzOHz4MFq1alXoNtHR0QgKCpK1hYSEIDo6GgCQk5ODkydPymIMDAwQFBQkxZw8eRLPnz+XxXh7e8PNzU2KedWNGzeQmJgo28ba2hr+/v7SNtHR0bCxsZEKbgAICgqCgYEBYmJipJimTZtKBXd+/vHx8Xj8+HGBx3727BnS09NlCxEREREREemfRt3LXzZ8+HAsWbIETZo0kdpCQkJgbm6OiIgIxMXFFVty48aNQ3p6Ory9vWFoaIi8vDx8//336NWrV6HbJCYmwtHRUdbm6OiI9PR0ZGdn4/Hjx8jLyyswJv9Ocv5dZhsbG7WYxMTEQo+bH1PYNomJiVL39XxGRkaws7OTxXh6eqrtI3+dra2t2rGnTZuGyZMnF5gXERERERER6Y/WA6ldu3ZNrRgFXtzVvXnzZjGk9H/Wr1+P1atXY82aNTh16hRWrlyJH374AStXrizW45R1X331FdLS0qTl9u3b+k6JiIiIiIiI8AZF93vvvYeRI0fKRvJOSkrCmDFj0LBhw2JNbsyYMRg3bhx69OgBPz8/9O7dGyNGjMC0adMK3cbJyUltlPGkpCRYWVnBzMwMlSpVgqGhYYExTk5O0j5ycnKQmppaaExBx82PKWq/ycnJsvW5ublISUmRxRS0j5eP8SoTExNYWVnJFiIiIiIiItI/rYvuZcuW4f79+3Bzc0O1atVQrVo1uLm54e7du7IBz4pDVlaW2iBuhoaGUKlUhW4TEBCAqKgoWVtkZCQCAgIAAEqlEvXr15fFqFQqREVFSTH169eHsbGxLCY+Ph4JCQlSzKs8PT3h5OQk2yY9PR0xMTHSNgEBAUhNTcXJkyelmL1790KlUsHf31+KOXjwIJ4/fy7Lv0aNGgV2LSciIiIiIqLSS+tnuqtVq4Zz584hMjJSegb63XffRVBQkGwU8+LQtm1bfP/993Bzc4Ovry9Onz6NOXPm4NNPPy10m88++wyLFi3Cl19+iU8//RR79+7F+vXrsX37dilm5MiRCAsLQ4MGDdCwYUPMmzcPT548Qb9+/QC86CofHh6OkSNHws7ODlZWVhgyZAgCAgIKHLkceDGC+/DhwzFlyhR4eXlJU4a5uLigQ4cOAF58Ti1btsSAAQOwZMkSPH/+HIMHD0aPHj3g4uICAPj4448xefJkhIeHY+zYsbhw4QLmz5+PuXPnFtOnSkRERERERCVG/AvZ2dlCpVL9m10UKT09XQwbNky4ubkJU1NTUaVKFTF+/Hjx7NkzKWbSpEnC3d1dtt2+fftEnTp1hFKpFFWqVBHLly9X2/fChQuFm5ubUCqVomHDhuLYsWOy9dnZ2eKLL74Qtra2wtzcXHTs2FHcv39fFuPu7i4mTZokvVapVGLChAnC0dFRmJiYiBYtWoj4+HjZNo8ePRI9e/YUlpaWwsrKSvTr109kZGTIYs6ePSuaNGkiTExMxDvvvCOmT5+uxacmRFpamgAg0tLStNquxLyYKIoLF32fiUREREREb0zTukujebpfplKp8P3332PJkiVISkrC5cuXUaVKFUyYMAEeHh4IDw/XzbcDhQgLC4NCocCKFStK9LhZWVmoWLEidu7ciQ8//LBEj/06nKebygztLj9ERERERKVGsc7T/bIpU6ZgxYoVmDlzpmwu6Zo1a+K///3vm2X7hoQQ2L9/P7777rsSPS4A7Nu3D82bNy91BTcRERERERGVHlrf6a5WrRp+/vlntGjRAhUqVMDZs2dRpUoVXLp0CQEBAXj8+LGuciUN8U43lRm8001EREREZZTO7nTfvXsX1apVU2tXqVSyEbeJiIiIiIiIyjuti24fHx8cOnRIrX3jxo2oW7dusSRFRERERERE9DbQesqwiRMnIiwsDHfv3oVKpcKmTZsQHx+P3377Ddu2bdNFjkRERERERERlktZ3utu3b4+//voLe/bsgYWFBSZOnIi4uDj89ddf+Oijj3SRIxEREREREVGZpPVAalT6cSA1KjN4+SEiIiKiMkpnA6lVqVIFjx49UmtPTU1FlSpVtN0dERERERER0VtL66L75s2byMvLU2t/9uwZ7t69WyxJEREREREREb0NNB5IbevWrdL/7969G9bW1tLrvLw8REVFwcPDo1iTIyIiIiIiIirLNC66O3ToAABQKBQICwuTrTM2NoaHhwdmz55drMkRERERERERlWUaF90qlQoA4OnpiePHj6NSpUo6S4qIiIiIiIjobaD1PN03btzQRR5EREREREREbx2t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JycHJ0+elMUYGBggKChIijl58iSeP38ui/H29oabm5sU86obN24gMTFRto21tTX8/f2lbaKjo2FjY4MGDRpIMUFBQTAwMEBMTIwU07RpUyiVSln+8fHxePz4cYHHfvbsGdLT02ULERERERER6V+pLrqvX7+OxYsXw8vLC7t378bnn3+OoUOHYuXKlYVuk5iYCEdHR1mbo6Mj0tPTkZ2djYcPHyIvL6/AmMTERGkfSqUSNjY2hcYUdNz8mKL26+DgIFtvZGQEOzs7WUxB+3j5GK+aNm0arK2tpcXV1bXAOCIiIiIiIipZWhfd169f10UeBVKpVKhXrx6mTp2KunXrIiIiAgMGDMCSJUtKLIey4KuvvkJaWpq03L59W98pEREREREREd6g6K5WrRqaNWuG33//XTZAmC44OzvDx8dH1vbuu+8iISGh0G2cnJyQlJQka0tKSoKVlRXMzMxQqVIlGBoaFhjj5OQk7SMnJwepqamFxhR03PyYovb78mBtwIv5zVNSUmQxBe3j5WO8ysTEBFZWVrKFiIiIiIiI9E/rovvUqVOoVasWRo4cCScnJwwcOBD//POPLnJD48aNER8fL2u7fPky3N3dC90mICAAUVFRsrbIyEgEBAQAAJRKJerXry+LUalUiIqKkmLq168PY2NjWUx8fDwSEhKkmFd5enrCyclJtk16ejpiYmKkbQICApCamoqTJ09KMXv37oVKpYK/v78Uc/DgQTx//lyWf40aNYoctZ2IiIiIiIhKoTcdqe358+fijz/+EG3bthXGxsbC19dXzJ49WyQnJ7/pLtX8888/wsjISHz//ffiypUrYvXq1cLc3Fz8/vvvhW5z/fp1YW5uLsaMGSPi4uLEjz/+KAwNDcWuXbukmLVr1woTExOxYsUKERsbKyIiIoSNjY1sHu7PPvtMuLm5ib1794oTJ06IgIAAERAQUGS+06dPFzY2NuLPP/8U586dE+3btxeenp4iOztbimnZsqWoW7euiImJEYcPHxZeXl6iZ8+e0vrU1FTh6OgoevfuLS5cuCDWrl0rzM3Nxc8//6zx58bRy7mUmYWIiIiIqIzStO7613/1Pn36VMyZM0eYmJgIhUIhTExMRO/evcW9e/f+7a6FEEL89ddfombNmsLExER4e3uLX375RbZ+0qRJwt3dXda2b98+UadOHaFUKkWVKlXE8uXL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98aNG6hevTpiY2Ph5eVVosd+Hc7TTWVG2b78EBEREVE5pmndpfXo5aVJWloarl27VuzTlGlix44diIiIKHUFNxEREREREZUeZf5ON6njnW4qM3j5ISIiIqIyStO6S+vRy4mIiIiIiIhIM1oX3QkJCSjo5rgQAgkJCcWSFBEREREREdHbQOui29PTEw8ePFBrT0lJgaenZ7EkRURERERERPQ20LroFkJAUcAzuZmZmTA1NS2WpIiIiIiIiIjeBhqPXj5y5EgAgEKhwIQJE2Bubi6ty8vLQ0xMDOrUqVPsCRIRERERERGVVRoX3adPnwbw4k73+fPnoVQqpXVKpRK1a9fG6NGjiz9DIiIiIiIiojJK46J73759AIB+/fph/vz5pXMqKiIiIiIiIqJSROOiO9/y5ct1kQcRERERERHRW0frovvJkyeYPn06oqKikJycDJVKJVt//fr1YkuOiIiIiIiIqCzTuuju378/Dhw4gN69e8PZ2bnAkcyJiIiIiIiI6A2K7p07d2L79u1o3LixLvIhIiIiIiIiemtoPU+3ra0t7OzsdJELERERERER0VtF66L7u+++w8SJE5GVlaWLfIiIiIiIiIjeGlp3L589ezauXbsGR0dHeHh4wNjYWLb+1KlTxZYcERERERERUVmmddHdoUMHHaRBRERERERE9PZRCCGEvpOg4pWeng5ra2ukpaXByspK3+mo44j3lI+XHyIiIiIqozStu7R+ppuIiIiIiIiINKN193IDA4Mi5+bOy8v7VwkRERERERERvS20Lro3b94se/38+XOcPn0aK1euxOTJk4stMSIiIiIiIqKyrtie6V6zZg3WrVuHP//8szh2R/8Cn+mmMoPPdBMRERFRGVXiz3Q3atQIUVFRxbU7IiIiIiIiojKvWIru7OxsLFiwAO+8805x7I6IiIiIiIjoraD1M922traygdSEEMjIyIC5uTl+//33Yk2OiIiIiIiIqCzTuuieN2+e7LWBgQHs7e3h7+8PW1vb4sqLiIiIiIiIqMzTuugOCwvTRR5EREREREREbx2ti24ASE1Nxa+//oq4uDgAgK+vLz799FNYW1sXa3JEREREREREZZnWA6mdOHECVatWxdy5c5GSkoKUlBTMmTMHVatWxalTp3SRIxEREREREVGZpPU83R988AGqVauGpUuXwsjoxY3y3Nxc9O/f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1q9fH8bGxrL9xsfHIyEhQbbf8+fPywr6yMhIWFlZwcfHR6P8C2JiYgIrKyvZQkRERERERKXAvxmt7dKlS2LMmDHCyclJmJqairZt2/6b3an5/PPPhbW1tdi/f7+4f/++tGRlZRW6zZEjR4SRkZH44YcfRFxcnJg0aZIwNjYW58+fl2KmT58ubGxsxJ9//inOnTsn2rdvLzw9PUV2drYU07JlS1G3bl0RExMjDh8+LLy8vETPnj2LzPezzz4Tbm5uYu/eveLEiRMiICBABAQESOtzc3NFzZo1RXBwsDhz5ozYtWuXsLe3F1999ZUUc/36dWFubi7GjBkj4uLixI8//igMDQ3Frl27NP7cOHo5lzKzlAb6/gy4lI6FiIiISEua1l3F8pdGbm6u2Lx5c7EX3QAKXJYvXy7FhIWFicDAQNl269evF9WrVxdKpVL4+vqK7du3y9arVCoxYcIE4ejoKExMTESLFi1EfHy8LObRo0eiZ8+ewtLSUlhZWYl+/fqJjIwMtfxeziU7O1t88cUXwtbWVpibm4uOHTuK+/fvy7a5efOmaNWqlTAzMxOVKlUSo0aNEs+fP5fF7Nu3T9SpU0colUpRpUoV2TE0waKbS5lZSgN9fwZcSsdCREREpCVN6y6FEELo6SZ7sQgMDESzZs3w7bffluhxb9y4gerVqyM2NlYvA8sVJT09HdbW1khLSyudXc0VCn1nQKVFabj88HwkoHSci0RERFSmaFp3aTx6eWmUlpaGa9euYfv27SV+7B07diAiIqLUFdxERERERERUepT5O92kjne6qcwoDZcfno8E8Fyk0qM0nItERKQRTesujUcvJyIiIiIiIiLtsOgmIiIiIiIi0hEW3UREREREREQ6wqKbiIiIiIiISEfK9OjlRERERFTMOKgf5ePAfkTFgne6iYiIiIiIiHSERTcRERERERGRjrB7ORERERERlT581IHylfFHHXinm4iIiIiIiEhHWHQTERERERER6QiLbiIiIiIiIiIdYdFNREREREREpCMsuomIiIiIiIh0hEU3ERERERERkY6w6CYiIiIiIiLSERbdRERERERERDrCopuIiIiIiIhIR1h0ExEREREREekIi24iIiIiIiIiHWHRTURERERERKQjLLqJiIiIiIiIdIRFNxEREREREZGOsOgmIiIiIiIi0hEW3UREREREREQ6wqKbiIiIiIiISEdYdBMRERERERHpCItuIiIiIiIiIh1h0U1ERERERESkIyy6iYiIiIiIiHSERTcRERERERGRjrDoJiIiIiIiItIRFt1EREREREREOsKim4iIiIiIiEhHWHQTERERERER6QiLbiIiIiIiIiIdYdFNREREREREpCMsuomIiIiIiIh0hEU3ERERERERkY6w6CYiIiIiIiLSERbdRERERERERDrCopuIiIiIiIhIR1h0ExEREREREekIi24iIiIiIiIiHWHRTURERERERKQjLLqJiIiIiIiIdIRFNxEREREREZGOsOgmIiIiIiIi0hEW3aXYjz/+CA8PD5iamsLf3x///POPvlMiIiIiIiIiLbDoLqXWrVuHkSNHYtKkSTh16hRq166NkJAQJCcn6zs1IiIiIiIi0hCL7lJqzpw5GDBgAPr16wcfHx8sWbIE5ubmWLZsmb5TIyIiIiIiIg0Z6TsBUpeTk4OTJ0/iq6++ktoMDAwQFBSE6Ohotfhnz57h2bNn0uu0tDQAQHp6uu6TJfo3eI5SacFzkUoLnotUmvB8pNKilJ6L+fWWEKLIOBbdpdDDhw+Rl5cHR0dHWbujoyMuXbqkFj9t2jRMnjxZrd3V1VVnORIVC2trfWdA9ALPRSoteC5SacLzkUqLUn4uZmRkwLqIHFl0vwW++uorjBw5UnqtUqmQkpKCihUrQqFQ6DEzKkx6ejpcXV1x+/ZtWFlZ6TsdKsd4LlJpwXORSguei1Sa8Hws3YQQyMjIgIuLS5FxLLpLoUqVKsHQ0BBJSUmy9qSkJDg5OanFm5iYwMTERNZmY2OjyxSpmFhZWfECSqUCz0UqLXguUmnBc5FKE56PpVdRd7jzcSC1UkipVKJ+/fqIioqS2lQqFaKiohAQEKDHzIiIiIiIiEgbvNNdSo0cORJhYWFo0KABGjZsiHnz5uHJkyfo16+fvlMjIiIiIiIiDbHoLqW6d++OBw8eYOLEiUhMTESdOnWwa9cutcHVqGwyMTHBpEmT1B4LICppPBeptOC5SKUFz0UqTXg+vh0U4nXjmxMRERERERHRG+Ez3UREREREREQ6wqKbiIiIiIiISEdYdBMRERERERHpCItuIiIiIiKiUuDgwYPIzc1Va8/NzcXBgwf1kBEVBw6kRkRUzqWmpsLGxkbfaVA5c/DgQXh7e8PBwUHW/vz5c0RHR6Np06Z6yozKo3v37uHw4cNITk6GSqWSrRs6dKiesqLyyNDQEPfv31e7Nj569AgODg7Iy8vTU2b0b7DoJioBSUlJGD16NKKiopCcnIxXf+14AaWSMmPGDHh4eKB79+4AgG7duuGPP/6Ak5MTduzYgdq1a+s5QyovDAwM4OjoiM2bN6NRo0ZSe1JSElxcXHhdpBKzYsUKDBw4EEqlEhUrVoRCoZDWKRQKXL9+XY/ZUXljYGCApKQk2Nvby9ovX76MBg0aID09XU+Z0b/BebqJSkDfvn2RkJCACRMmwNnZWfYPOlFJWrJkCVavXg0AiIyMRGRkJHbu3In169djzJgx+Pvvv/WcIZUnPXr0QIsWLfDjjz+ib9++UjvvB1BJmjBhAiZOnIivvvoKBgZ88pL0o1OnTgBefNHTt29f2bzceXl5OHfuHN5//319pUf/EotuohJw+PBhHDp0CHXq1NF3KlTOJSYmwtXVFQCwbds2dOvWDcHBwfDw8IC/v7+es6PyRKFQ4KuvvsIHH3yAPn364Ny5c5g9e7a0jqikZGVloUePHiy4Sa+sra0BvPjSsUKFCjAzM5PWKZVKNGrUCAMGDNBXevQvsegmKgGurq68c0Olgq2tLW7fvg1XV1fs2rULU6ZMAfDiH3l256WSlH9N7NSpEzw9PdG+fXvExsZi/vz5es6Mypvw8HBs2LAB48aN03cqVI4tX75cui4uXLgQlpaWes6IihOf6SYqAX///Tdmz56Nn3/+GR4eHvpOh8qxwYMHY9u2bfDy8sLp06dx8+ZNWFpaYu3atZg5cyZOnTql7xSpnDAwMEBiYqI0WFBiYiI6dOiAO3fu4P79+/wSiEpMXl4e2rRpg+zsbPj5+cHY2Fi2fs6cOXrKjMoblUoFU1NTXLx4EV5eXvpOh4oR73QTlYDu3bsjKysLVatWhbm5udo/6CkpKXrKjMqbuXPnwsPDA7dv38bMmTOlb9Lv37+PL774Qs/ZUXkSFhYm6z7p5OSEAwcOICIigtPiUImaNm0adu/ejRo1agCA2kBqRCXFwMAAXl5eePToEYvutwzvdBOVgJUrVxa5PiwsrIQyISIqHRISEuDq6qpW1AghcPv2bbi5uekpMypvbG1tMXfuXNlgfkT68tdff2HmzJlYvHgxatasqe90qJiw6CYiKmeuXbuGefPmIS4uDgDg4+OD4cOHo0qVKnrOjMoTzkVLpYWTkxMOHTrEO4tUKtja2iIrKwu5ublQKpWyHkEAe0eWVexeTlRC8vLysGXLFqnQ8fX1Rbt27WBoaKjnzKg82b17N9q1a4c6deqgcePGAIAjR47Ax8cHf/31Fz766CM9Z0jlhRCiwK67mZmZMDU11UNGVF4NGzYMCxcuxIIFC/SdChHmzZun7xRIB3inm6gEXL16Fa1bt8bdu3elZ8bi4+Ph6uqK7du3o2rVqnrOkMqLunXrIiQkBNOnT5e1jxs3Dn///TcHUiOdGzlyJABg/vz5GDBgAMzNzaV1eXl5iImJgaGhIY4cOaKvFKmc6dixI/bu3YuKFSvC19dXbdyVTZs26SkzInpbsOgmKgGtW7eGEAKrV6+GnZ0dgBddKD/55BMYGBhg+/btes6QygtTU1OcP39erRvl5cuXUatWLTx9+lRPmVF50axZMwDAgQMHEBAQAKVSKa1TKpXw8PDA6NGj2dWXSky/fv2KXL98+fISyoTohWvXrmH58uW4du0a5s+fDwcHB+zcuRNubm7w9fXVd3r0Blh0E5UACwsLHDt2DH5+frL2s2fPonHjxsjMzNRTZlTeuLq6Ys6cOejatausff369Rg9ejQSEhL0lBmVN/369cP8+fNhZWWl71SIiEqNAwcOoFWrVmjcuDEOHjyIuLg4VKlSBdOnT8eJEyewceNGfadIb4DPdBOVABMTE2RkZKi1Z2Zmyu7yEOnagAEDEBERgevXr+P9998H8OKZ7hkzZkjdfolKAu8eEhGpGzduHKZMmYKRI0eiQoUKUnvz5s2xaNEiPWZG/wbvdBOVgD59+uDUqVP49ddf0bBhQwBATEwMBgwYgPr162PFihX6TZDeenl5eTA0NIQQAvPmzcPs2bNx7949AICLiwvGjBmDoUOHck5aKjHNmzcvcv3evXtLKBMiYOPGjVi/fj0SEhKQk5MjW8exLqgkWVpa4vz58/D09ESFChVw9uxZVKlSBTdv3oS3tzcfAyujDPSdAFF5sGDBAlStWhUBAQEwNTWFqakpGjdujGrVqmH+/Pn6To/KgXfeeQfjxo3D1atXMWLECNy5cwdpaWlIS0vDnTt3MGzYMBbcVKJq164tW3x8fJCTk4NTp06pPYpDpEsLFixAv3794OjoiNOnT6Nhw4aoWLEirl+/jlatWuk7PSpnbGxscP/+fbX206dP45133tFDRlQceKebqARdvXpVmjLs3XffRbVq1fScEZUX3333HVauXIkbN27g/fffR3h4OLp16yYbOZqoNPj222+RmZmJH374Qd+pUDnh7e2NSZMmoWfPnrI7ixMnTkRKSgq79FKJGj16NGJiYrBhwwZUr14dp06dQlJSEvr06YM+ffpg0qRJ+k6R3gCLbiI9yMvLw/nz5+Hu7g5bW1t9p0PlyP79+7F8+XL88ccfMDQ0RLdu3dC/f3/4+/vrOzUiAC++nGzYsCFSUlL0nQqVE+bm5oiLi4O7uzscHBwQGRmJ2rVr48qVK2jUqBEePXqk7xSpHMnJycGgQYOwYsUK5OXlwcjICHl5efj444+xYsUKGBoa6jtFegPsXk5UAoYPH45ff/0VwIuCOzAwEPXq1YOrqyv279+v3+SoXPnwww+xcuVKJCYmYvbs2YiLi0NAQAB8fX0xZ84cfadHhOjoaJiamuo7DSpHnJycpC953NzccOzYMQDAjRs3wHtTVNKUSiWWLl2Ka9euYdu2bfj9999x6dIlrFq1igV3GcY73UQloHLlytiyZQsaNGiALVu24IsvvsD+/fuxatUq7N27F0eOHNF3ilSObd++HX369EFqairy8vL0nQ6VE506dZK9FkLg/v37OHHiBCZMmMAulFRi+vfvD1dXV0yaNAk//vgjxowZg8aNG+PEiRPo1KmT9KU5UUnLL9M45krZx6KbqASYmpri6tWrqFy5MiIiImBubo558+bhxo0bqF27NtLT0/WdIpUzWVlZWL9+PZYvX47Dhw+jatWq+PTTTzFu3Dh9p0blRL9+/WSvDQwMYG9vj+bNmyM4OFhPWVF5pFKpoFKpYGT0YibdtWvX4ujRo/Dy8sLAgQM5tSeVuF9//RVz587FlStXAABeXl4YPnw4+vfvr+fM6E1xnm6iEuDo6IjY2Fg4Oztj165dWLx4MYAXhQ+7ClFJOnr0KJYtW4YNGzYgNzcXXbp0wXfffYemTZvqOzUqZzhPN5UWBgYGMDD4vycue/TogR49eugxIyrPJk6ciDlz5mDIkCEICAgA8OKxmxEjRiAhIQH/+c9/9JwhvQne6SYqAd9++y3mzZsHZ2dnZGVl4fLlyzAxMcGyZcuwdOlSREdH6ztFesvNnDkTy5cvx+XLl9GgQQOEh4dLI/US6VNOTg6Sk5OhUqlk7W5ubnrKiMqDc+fOaRxbq1YtHWZCJGdvb48FCxagZ8+esvb//e9/GDJkCB4+fKinzOjfYNFNVEI2btyI27dvo2vXrqhcuTIAYOXKlbCxsUH79u31nB297ezt7fHJJ58gPDwcNWvW1Hc6RLh8+TLCw8Nx9OhRWbsQAgqFguMLkE4ZGBhAoVC8dqA0notU0mxsbHD8+HF4eXnJ2i9fvoyGDRsiNTVVP4nRv8Kim4ioHHj+/DmMjY1lbU+fPuUo0aQ3jRs3hpGREcaNGwdnZ2e1gYJq166tp8yoPLh165bGse7u7jrMhEhuyJAhMDY2VptRZPTo0cjOzsaPP/6op8zo32DRTVRCoqKiEBUVVWA3ymXLlukpKypvVCoVvv/+eyxZsgRJSUm4fPkyqlSpggkTJsDDwwPh4eH6TpHKCQsLC5w8eRLe3t76ToWISK9Gjhwp/X9ubi5WrFgBNzc3NGrUCAAQExODhIQE9OnTBwsXLtRXmvQvcJ5uohIwefJkBAcHIyoqCg8fPsTjx49lC1FJmTJlClasWIGZM2fKRuStWbMm/vvf/+oxMypvfHx8+GwilQorV67E9u3bpddffvklbGxs8P7772t1R5zoTZ0+fVpazp8/j/r168Pe3h7Xrl3DtWvXUKlSJdSrVw8XL17Ud6r0hninm6gEODs7Y+bMmejdu7e+U6Fyrlq1avj555/RokULVKhQAWfPnkWVKlVw6dIlBAQE8Esg0qmXp0c8ceIEvvnmG0ydOhV+fn5qjz9YWVmVdHpUTtWoUQOLFy9G8+bNER0djRYtWmDevHnYtm0bjIyMsGnTJn2nSERlHKcMIyoBOTk5eP/99/WdBhHu3r2LatWqqbWrVCo8f/5cDxlReWJjYyN7dlsIgRYtWshiOJAalbTbt29L18UtW7agS5cuiIiIQOPGjfHhhx/qNzkieiuw6CYqAf3798eaNWswYcIEfadC5ZyPjw8OHTqkNjDQxo0bUbduXT1lReXFvn379J0CkRpLS0s8evQIbm5u+Pvvv6Xna01NTZGdna3n7Kg86NSpk8ax7HlRNrHoJioBT58+xS+//II9e/agVq1aat0oXx2hkkhXJk6ciLCwMNy9excqlQqbNm1CfHw8fvvtN2zbtk3f6dFbLjAwUN8pEKn56KOP0L9/f9StWxeXL19G69atAQAXL16Eh4eHfpOjcsHa2lrfKZCO8ZluohLQrFmzQtcpFArs3bu3BLOh8u7QoUP4z3/+g7NnzyIzMxP16tXDxIkTERwcrO/UqBxZvnw5LC0t0bVrV1n7hg0bkJWVhbCwMD1lRuVNamoqvvnmG9y+fRuff/45WrZsCQCYNGkSlEolxo8fr+cMiaisY9FNREREJa569er4+eef1b6UPHDgACIiIhAfH6+nzIiIiIoXu5cTEZUjQgicPHkSN2/ehEKhQJUqVVCnTh3Z4FZEJSEhIQGenp5q7e7u7khISNBDRlTeZWVlISEhATk5ObL2WrVq6SkjKi/q1auHqKgo2Nraom7dukX+m3zq1KkSzIyKC4tuohLw5MkTTJ8+HVFRUUhOToZKpZKtv379up4yo/Jk3759CA8Px61bt5DfyUmhUMDT0xPLli1D06ZN9ZwhlScODg44d+6c2jOzZ8+eRcWKFfWTFJVLDx48QN++fbFr164C13MkfdK19u3bw8TEBADQoUMH/SZDOsGim6gE9O/fHwcOHEDv3r3h7OzMu4pU4q5evYo2bdrA398fc+fOhbe3N4QQiI2NxYIFC9C6dWucO3cOVapU0XeqVE707NkTQ4cORYUKFaQvfA4cOIBhw4ahR48ees6OypPhw4cjLS0NMTEx+PDDD7F582YkJSVhypQpmD17tr7To3Jg0qRJBf4/vT34TDdRCbCxscH27dvRuHFjfadC5dTgwYMRFxeHqKgotXVCCAQFBcHHxwcLFy7UQ3ZUHuXk5KB3797YsGEDjIxe3ANQqVTo06cPlixZAqVSqecMqbxwdnbGn3/+iYYNG8LKygonTpxA9erVsXXrVsycOROHDx/Wd4pUDmVkZODlMs3AwACWlpZ6zIj+DQN9J0BUHtja2sLOzk7faVA5tn//fgwfPrzAdQqFAsOHD+ccylSilEol1q1bh/j4eKxevRqbNm3CtWvXsGzZMhbcVKKePHkCBwcHAC/+vX7w4AEAwM/Pj8/PUok5c+aMNF0dALi4uMDW1lZabGxscPz4cT1mSP8Gi26iEvDdd99h4sSJyMrK0ncqVE4lJCTAz8+v0PU1a9bErVu3SjAjohe8vLzQtWtXtGrVCo8fP8bjx4/1nRKVMzVq1JBGy69duzZ+/vln3L17F0uWLIGzs7Oes6PyYuHChWjSpImsbdWqVdi7dy+ioqLw8ccfY8GCBXrKjv4tPtNNpCOvjj559epVODo6wsPDA8bGxrJYfpNOupaZmQlzc/NC15ubm/NLISpRw4cPh5+fH8LDw5GXl4fAwEAcPXoU5ubm2LZtGz788EN9p0jlxLBhw3D//n0AL56nbdmyJVavXg2lUokVK1boNzkqN44ePYrBgwfL2ho1aiSNtWJmZoZu3brpIzUqBiy6iXSEo09SaRMbG4vExMQC1z18+LCEs6HybuPGjfjkk08AAH/99ReuX7+OS5cuYdWqVRg/fjyOHDmi5wypvMg/DwGgfv36+H/t3XtU1HX+x/HX4C1QQEwRLygi5F3TzMxV8+5iSWkllhpqmUdTCfOW5bW13FytzOueTESTMjVLMzW84G3dFBT7JV4h8JACimbekZnfH55mm0XTteb71fk+H+fMOcz38518xeHAvOfz+bw/mZmZOnjwoKpVq6by5cubmAxWkpmZqQoVKjifT5482eXnr1KlSsrJyTEjGv4ENFIDAAvw8vKSzWbTjX7l/3rdZrNxNA4Mc9999+no0aOqWrWqXn75Zfn4+Oj9999XRkaGGjVqpHPnzpkdEQAMU65cOa1evfqmTXd37Nihrl27Kj8/3+Bk+DMw0w0YKDk5WWlpaZKkevXqqXHjxiYnglVkZGSYHQFwUbFiRR04cECVKlXSunXrNHfuXEnSxYsXVaxYMZPTwQqGDx9+W/fNmDHDzUmA69sSV61addOie+XKlbxvvIdRdAMGyM3NVc+ePbVlyxaVLVtWknT27Fm1bdtWn376qctyIsAdqlevbnYEwEW/fv3Uo0cPVapUSTabTR06dJAk/fvf/1bt2rVNTgcr2Lt3r8vz7du366GHHpK3t7fz2m97swDuNHjwYPXs2VMhISEaNGiQvLyu97suLCzUnDlz9OGHH2rp0qUmp8SdYnk5YICoqCilp6crPj5ederUkXR9f210dLTCwsKUkJBgckIAMN7y5ct1/PhxPfvss6pataokadGiRSpbtqyefPJJk9PBanx9fZWamupsXAUYbfTo0Zo2bZp8fX2dP4fp6ek6f/68hg8frmnTppmcEHeKohswgL+/vxITE/Xwww+7XP/uu+/UqVMnnT171pxgAABAEkU37g67du1SQkKCjhw5Iun6sYrPPfecmjdvbnIy/BEsLwcMYLfbixwTJkklSpSQ3W43IREAmG/jxo3auHGjcnNzi/wu/Pjjj01KBQDmad68OQW2B/IyOwBgBe3atVNMTIx++ukn57Xs7GzFxsaqffv2JiYDAHNMmjRJnTp10saNG3Xq1CmdOXPG5QEAgKdgphswwKxZsxQZGamQkBAFBwdLko4fP6769etryZIlJqcDAOPNmzdPcXFx6tOnj9lRYFH79+93ee5wOHTw4EGdP3/e5XrDhg2NjAXAA7GnGzCIw+FQYmKiDh48KEmqU6eOs1svYJScnByNGDHCuaT3v/8EcE43jHL//ffru+++U82aNc2OAovy8vKSzWYr8ntQkvO6zWbj9yKAP4yiGwAsJCIiQllZWRoyZIjzqKbfomM0jDJ69GiVKVNG48aNMzsKLCozM/O27uPIRQB/FEU34EYzZ8685T3FixdXUFCQWrZsqcDAQANSwcp8fX21bds2Pfjgg2ZHgcXFxMQoPj5eDRs2VMOGDYs0m5wxY4ZJyQAA+HOxpxtwo/fee++W99jtdp0+fVp2u11LlixR9+7dDUgGqwoODr7hUkrAaPv373d++PN///d/5oYBgLsE28A8EzPdwF3Abrdr6tSpWrx4sdLS0syOAw+2YcMGTZ8+XfPnz1dISIjZcQAAwG+wDcwzUXQDd4ns7Gw9+OCDysvLMzsKPFhAQIAuXryoa9euycfHp8iS3vz8fJOSAdcbTq5bt04LFizQ8uXLzY4DAIZjG5hnYnk5cJeoUqUKBTfc7v333zc7AlBERkaGPv74Y8XFxSkvL4+THQBYFtvAPBMz3QAAwHBXrlzR8uXLtWDBAm3fvl2FhYX6xz/+oRdffFF+fn5mxwMAU7ANzDNRdAOARV2+fFlXr151uUaxA3dLTk7WggULlJCQoLCwMPXp00dRUVGqWrWqUlNTVbduXbMjwmJoXIW7CdvAPBPLywHAQi5cuKDRo0dr2bJlOn36dJFx3lzC3R555BENHTpUu3btUq1atcyOA6hv377KysrSuHHjbti4CjAS28A8E0U3YICUlBSVKFFCDRo0kCR9+eWXWrhwoerWrauJEyeqZMmSJieEVYwaNUqbN2/W3Llz1adPH82ePVvZ2dmaP3++pk6danY8WED79u21YMEC5ebmqk+fPurcuTNFDky1fft2GlfhrhEdHW12BLiBl9kBACsYOHCgDh8+LElKT09Xz5495ePjo88//1yjRo0yOR2sZPXq1ZozZ46efvppFS9eXK1atdKbb76pt99+W5988onZ8WAB69ev1w8//KBatWpp0KBBqlSpkmJiYiSJ4humoHEV7laXL1/WuXPnXB64N1F0AwY4fPiw8xP0zz//XK1bt9bSpUsVFxenFStWmBsOlpKfn6/Q0FBJ1/dv/7o3rGXLltq6dauZ0WAhwcHBGj9+vDIyMrR48WLl5eWpePHievLJJzV27FilpKSYHREW8v7772vMmDH68ccfzY4C6MKFCxoyZIgCAwNVunRpBQQEuDxwb6LoBgzgcDhkt9slSYmJierSpYuk6288T506ZWY0WExoaKgyMjIkSbVr19ayZcskXZ8BL1u2rInJYFUdO3bU0qVL9dNPP2no0KH65ptv9PDDD5sdCxYSFRWlLVu2qGbNmvL19VW5cuVcHoCRRo0apU2bNmnu3LkqVaqUPvroI02aNEmVK1dWfHy82fFwh+heDhigXbt2Cg4OVocOHfTiiy/qwIEDCgsLU1JSkqKjo/l0HYZ57733VKxYMQ0bNkyJiYnq2rWrHA6HCgoKNGPGDOcyX8BMKSkpatKkidkxYBGLFi363XH22MJI1apVU3x8vNq0aSM/Pz+lpKQoLCxMixcvVkJCgtauXWt2RNwBim7AAPv371evXr2UlZWl4cOHa8KECZKkoUOH6vTp01q6dKnJCWFVmZmZSk5OVlhYmBo2bGh2HAAALK1MmTI6cOCAqlWrpqpVq2rlypVq1qyZMjIy1KBBA50/f97siLgDdC8HDNCwYUN9//33Ra5PmzZNxYoVMyERcF316tVVvXp1s2MAwF3h8uXLunr1qss1Pz8/k9LAin7dBlatWjXnNrBmzZqxDewex55uwCBnz57VRx99pNdff93ZvOrAgQPKzc01ORmswm636+OPP9YTTzyh+vXrq0GDBoqMjFR8fDydewFYFo2rcDfp16+fUlNTJUljxozR7Nmzdd999yk2NlYjR440OR3uFMvLAQPs379f7du3V9myZfXjjz/q0KFDCg0N1ZtvvqmsrCwaY8DtHA6HunbtqrVr16pRo0aqXbu2HA6H0tLS9P333ysyMlKrVq0yOyYAGO6VV17R5s2b9dZbb6lPnz6aPXu2srOzNX/+fE2dOlW9evUyOyIsjG1gnoGiGzBAhw4d1KRJE7377rvy9fVVamqqQkNDtXPnTj3//PM0UoPbLVy4UDExMfryyy/Vtm1bl7FNmzbpqaee0qxZs/TCCy+YlBAAzEHjKgDuxvJywAC7d+/WwIEDi1yvUqWKTp48aUIiWE1CQoLGjh1bpOCWrnfXHzNmjD755BMTkgGuxo4dq/79+5sdAxaSn5+v0NBQSdf3b/+6Baxly5baunWrmdFgMWwD81wU3YABSpUqpXPnzhW5fvjwYVWoUMGERLCa/fv3669//etNxyMiIpx7yAB3Sk9P/903j9nZ2az+gaF+bVwlydm4ShKNq2Aoh8OhyMhIvfTSS8rOzlaDBg1Ur149ZWZmqm/fvurWrZvZEfEHUHQDBoiMjNTkyZNVUFAgSbLZbMrKytLo0aP19NNPm5wOVpCfn6+KFSvedLxixYo6c+aMgYlgVeHh4crLy3M+j4qKUk5OjvP5okWLtGnTJjOiwaJoXIW7QVxcnLZu3aqNGzdq7969SkhI0KeffqrU1FQlJiZq06ZN9AC6h7GnGzDAzz//rGeeeUZ79uzRL7/8osqVK+vkyZN69NFHtXbtWpUuXdrsiPBwxYoV08mTJ2+6siInJ0eVK1dWYWGhwclgNV5eXjp58qQCAwMlyaXPBXA3oHEVzNCpUyfndq8befvtt5WUlKT169cbnAx/Bs7pBgzg7++vb7/9Vtu3b9f+/ft1/vx5NWnSRB06dDA7GizC4XCob9++KlWq1A3Hr1y5YnAiALg7Va9eXf7+/iwth6H279+vd99996bjERERmjlzpoGJ8Gei6AYM1LJlS7Vs2dLsGLCg6OjoW95D53IYwWazyWazFbkGmOXvf/+7QkJCFBUVJUnq0aOHVqxYoaCgIOcxi4C7sQ3Ms7G8HHCT/+XTyGHDhrkxCQDcPby8vBQREeFcdbF69Wq1a9euyDablStXmhEPFlSjRg198sknatGihb799lv16NFDn332mZYtW6asrCxt2LDB7IiwALaBeTaKbsBNatSocVv32Ww2paenuzkNANwd+vXrd1v3LVy40M1JgOu8vb11+PBhBQcHKyYmRpcvX9b8+fN1+PBhPfLII8wuwhD//YHkf7ty5YrWrVtH0X2PYnk54Ca/Hj8CAPgPimncbQICAnT8+HEFBwdr3bp1+tvf/ibpei8MChwYhW1gno2iG3CzgoIC1a5dW2vWrFGdOnXMjgMAAH6je/fuev755xUeHq7Tp08rIiJCkrR3716FhYWZnA5WwQeSno2iG3CzEiVK6PLly2bHAAAAN/Dee+8pJCREx48f17vvvqsyZcpIkk6cOKHBgwebnA6AJ2BPN2CAt99+W4cPH9ZHH32k4sX5rAsAAACwCopuwADdunXTxo0bVaZMGTVo0IAuvQAA3CXi4+N/d5x9tAD+KIpuwAC36tbLPh4AAMwREBDg8rygoEAXL15UyZIl5ePjo/z8fJOSAfAUFN0AAMAUhw4d0ocffqi0tDRJUp06dTR06FDVqlXL5GSwuiNHjmjQoEEaOXKkOnfubHYcAPc4L7MDAAAA61mxYoXq16+v5ORkNWrUSI0aNVJKSorq16+vFStWmB0PFhceHq6pU6cqJibG7CgAPAAz3YBBli9frmXLlikrK0tXr151GUtJSTEpFQCYo2bNmurVq5cmT57scn3ChAlasmSJjh07ZlIy4Lp9+/apdevWOnfunNlRANzjaKMMGGDmzJl644031LdvX3355Zfq16+fjh07pt27d+uVV14xOx4AGO7EiRM3bFDVu3dvTZs2zYREsKqvvvrK5bnD4dCJEyc0a9Ys/eUvfzEpFQBPQtENGGDOnDn65z//qeeee05xcXEaNWqUQkNDNX78eBq0ALCkNm3aaNu2bQoLC3O5vn37drVq1cqkVLCip556yuW5zWZThQoV1K5dO02fPt2cUAA8CsvLAQP4+PgoLS1N1atXV2BgoL799ls1atRIR44cUfPmzXX69GmzIwKAoebNm6fx48erR48eat68uSRp165d+vzzzzVp0iRVrlzZeW9kZKRZMQEA+MMougEDhIaGasWKFWrcuLGaNm2qAQMGaODAgdqwYYN69uzJbDcAy/Hyur1erjabTYWFhW5OA/zHtWvXdPnyZZUpU8bsKAA8BN3LAQO0a9fOuWesX79+io2NVceOHRUVFaVu3bqZnA4AjGe322/rQcENd1m9erXi4uJcrk2ZMkVlypRR2bJl1alTJ505c8accAA8CjPdgAF+ffNYvPj1Ngqffvqpdu7cqfDwcA0cOFAlS5Y0OSEAANbStm1bPfPMM86Gpjt37lSrVq00efJk1alTR2+88YYiIiI0Y8YMk5MCuNdRdAMAAEPMnDlTL7/8su677z7NnDnzd+8dNmyYQalgVYGBgVq/fr0aN24sSRo+fLgOHDigdevWSZLWrl2rmJgYHTlyxMyYADwARTdgkLNnz+q7775Tbm6u7Ha7y9iNjs0BAE9To0YN7dmzR/fff79q1Khx0/tsNpvS09MNTAYr8vb21qFDh1StWjVJUrNmzfTss89q5MiRkqTMzEzVrVtXFy5cMDMmAA/AkWGAAVavXq1evXrp/Pnz8vPzk81mc47ZbDaKbgCWkJGRccOvATNUqVJFaWlpqlatms6fP6/U1FS99957zvHTp0/Lx8fHxIQAPAWN1AADvPbaa+rfv7/Onz+vs2fP6syZM84HncsBADDes88+q1dffVWLFy/WgAEDFBQU5Dy+TpL27NmjWrVqmZgQgKdgphswQHZ2toYNG8Yn5gAsbfjw4bd9L82r4G7jx493/n0OCgrSkiVLVKxYMed4QkKCunbtamJCAJ6CohswQOfOnbVnzx6FhoaaHQUATLN3797buu+3W3AAd/H29lZ8fPxNxzdv3mxgGgCejEZqgJv8ei63JOXl5Wny5Mnq16+fGjRooBIlSrjcGxkZaXQ8AAAAAAag6AbcxMvr9lom2Gw2FRYWujkNAAAAADNQdAMAAEN0795dcXFx8vPzU/fu3X/33pUrVxqUCgAA92JPNwAAMIS/v79zv7a/v7/JaQAAMAYz3YAbbdq0SUOGDNGuXbvk5+fnMvbzzz+rRYsWmjt3rlq3bm1SQgAAAADuRNENuFFkZKTatm2r2NjYG47PnDlTmzdv1hdffGFwMgAArGvmzJm3fe+wYcPcmASAFVB0A25UvXp1rVu3TnXq1Lnh+MGDB9WpUydlZWUZnAwAzJWTk6MRI0Zo48aNys3N1X+/HaHBJNypRo0aLs/z8vJ08eJFlS1bVpJ09uxZ+fj4KDAwUOnp6SYkBOBJ2NMNuFFOTk6R48F+q3jx4srLyzMwEQDcHfr27ausrCyNGzdOlSpV4mxuGCojI8P59dKlSzVnzhwtWLBAtWrVkiQdOnRIAwYM0MCBA82KCMCDMNMNuFHNmjU1ffp0PfXUUzccX7lypUaMGMGn6AAsx9fXV9u2bdODDz5odhRYXM2aNbV8+XI1btzY5XpycrKeeeYZlwIdAO7E7R0kDOCOdOnSRePGjdPly5eLjF26dEkTJkzQE088YUIyADBXcHBwkSXlgBlOnDiha9euFbleWFionJwcExIB8DTMdANulJOToyZNmqhYsWIaMmSIc9nawYMHNXv2bBUWFiolJUUVK1Y0OSkAGGvDhg2aPn265s+fr5CQELPjwMK6du2q7OxsffTRR2rSpImk67PcL7/8sqpUqaKvvvrK5IQA7nUU3YCbZWZmatCgQVq/fr1zVsdms6lz586aPXt2kWYuAOCpAgICXPZuX7hwQdeuXZOPj0+R/hf5+flGx4NF5eXlKTo6WuvWrXP+HF67dk2dO3dWXFycAgMDTU4I4F5H0Q0Y5MyZMzp69KgcDofCw8MVEBBgdiQAMNSiRYtu+97o6Gg3JgGKOnz4sA4ePChJql27th544AGTEwHwFBTdAAAAAAC4CUeGAQAAw9jtdk2bNk1fffWVrl69qvbt22vChAny9vY2OxosqrCwUHFxcc4z4+12u8v4pk2bTEoGwFNQdAMAAMNMmTJFEydOVIcOHeTt7a0PPvhAubm5+vjjj82OBouKiYlRXFycHn/8cdWvX58z4wH86VheDgAADBMeHq4RI0Zo4MCBkqTExEQ9/vjjunTpkry8OMkUxitfvrzi4+PVpUsXs6MA8FD8dQMAAIbJyspyKW46dOggm82mn376ycRUsLKSJUsqLCzM7BgAPBhFNwAAMMy1a9d03333uVwrUaKECgoKTEoEq3vttdf0wQcfiMWfANyF5eUAAMAwXl5eioiIUKlSpZzXVq9erXbt2ql06dLOaytXrjQjHiyoW7du2rx5s8qVK6d69eoVOTOen0UAfxSN1AAAgGFudP527969TUgCXFe2bFl169bN7BgAPBgz3QAAAAAAuAl7ugEAAAAAcBOWlwMAAMDSli9frmXLlikrK0tXr151GUtJSTEpFQBPwUw3AAAALGvmzJnq16+fKlasqL1796pZs2a6//77lZ6eroiICLPjAfAA7OkGAACAZdWuXVsTJkzQc889J19fX6Wmpio0NFTjx49Xfn6+Zs2aZXZEAPc4ZroBAABgWVlZWWrRooUkydvbW7/88oskqU+fPkpISDAzGgAPQdENAAAAywoKClJ+fr4kqVq1atq1a5ckKSMjQywIBfBnoOgGAACAZbVr105fffWVJKlfv36KjY1Vx44dFRUVxfndAP4U7OkGAACAZdntdtntdhUvfv1Qn08//VQ7d+5UeHi4Bg4cqJIlS5qcEMC9jqIbAAAAAAA3YXk5AAAAAABuQtENAAAAAICbUHQDAAAAAOAmFN0AAAAAALgJRTcAAAAsa8KECcrMzDQ7BgAPRtENAAAAy/ryyy9Vs2ZNtW/fXkuXLtWVK1fMjgTAw1B0AwAAwLL27dun3bt3q169eoqJiVFQUJAGDRqk3bt3mx0NgIfgnG4AAABAUkFBgVavXq2FCxdq/fr1ql27tl588UX17dtX/v7+ZscDcI9iphsAAACQ5HA4VFBQoKtXr8rhcCggIECzZs1ScHCwPvvsM7PjAbhHUXQDAADA0pKTkzVkyBBVqlRJsbGxaty4sdLS0pSUlKQjR45oypQpGjZsmNkxAdyjWF4OAAAAy2rQoIEOHjyoTp06acCAAeratauKFSvmcs+pU6cUGBgou91uUkoA97LiZgcAAAAAzNKjRw/1799fVapUuek95cuXp+AGcMeY6QYAAAAAwE2Y6QYAAIBlORwOLV++XJs3b1Zubm6RGe2VK1ealAyAp6DoBgAAgGW9+uqrmj9/vtq2bauKFSvKZrOZHQmAh2F5OQAAACyrXLlyWrJkibp06WJ2FAAeiiPDAAAAYFn+/v4KDQ01OwYAD0bRDQAAAMuaOHGiJk2apEuXLpkdBYCHYnk5AAAALOvSpUvq1q2bduzYoZCQEJUoUcJlPCUlxaRkADwFjdQAAABgWdHR0UpOTlbv3r1ppAbALZjpBgAAgGWVLl1a69evV8uWLc2OAsBDsacbAAAAlhUcHCw/Pz+zYwDwYBTdAAAAsKzp06dr1KhR+vHHH82OAsBDsbwcAAAAlhUQEKCLFy/q2rVr8vHxKdJILT8/36RkADwFjdQAAABgWe+//77ZEQB4OGa6AQAAAABwE2a6AQAAYHm5ubnKzc2V3W53ud6wYUOTEgHwFBTdAAAAsKzk5GRFR0crLS1N/70A1GazqbCw0KRkADwFy8sBAABgWY0aNVLNmjU1evRoVaxYUTabzWW8evXqJiUD4CkougEAAGBZvr6+2rt3r8LCwsyOAsBDcU43AAAALKt9+/ZKTU01OwYAD8ZMNwAAACzr1KlTio6OVrNmzVS/fv0i53RHRkaalAyAp6DoBgAAgGWtXr1affr00blz54qM0UgNwJ+B5eUAAACwrKFDh6p37946ceKE7Ha7y4OCG8CfgZluAAAAWJavr6/27dunmjVrmh0FgIdiphsAAACW1b17d23evNnsGAA8WHGzAwAAAABmeeCBB/T6669r+/btatCgQZFGasOGDTMpGQBPwfJyAAAAWFaNGjVuOmaz2ZSenm5gGgCeiKIbAAAAAAA3YU83AAAAAABuwp5uAAAAWMrw4cP11ltvqXTp0ho+fPjv3jtjxgyDUgHwVBTdAAAAsJS9e/eqoKDA+TUAuBN7ugEAAAAAcBNmugEAAGA53bt3v+U9xYsXV1BQkDp27KiuXbsakAqAJ6KRGgAAACzH39//lg9vb28dOXJEUVFRGj9+vNmRAdyjWF4OAAAA/I41a9Zo8ODBysrKMjsKgHsQM90AAADA72jZsqWaNm1qdgwA9yhmugEAAAAAcBNmugEAAAAAcBOKbgAAAAAA3ISiGwAAAAAAN6HoBgAAAADATSi6AQAAAABwE4puAABw244fP67+/furcuXKKlmypKpXr66YmBidPn3a7GgAANyVKLoBAMBtSU9PV9OmTXXkyBElJCTo6NGjmjdvnjZu3KhHH31U+fn5ZkeUJDkcDl27ds3sGAAASKLoBgAAt+mVV15RyZIltWHDBj322GOqVq2aIiIilJiYqOzsbL3xxhuaNWuW6tev73zNqlWrZLPZNG/ePOe1Dh066M0335QkTZw4UQ8++KAWL16skJAQ+fv7q2fPnvrll1+c99vtdr3zzjuqUaOGvL291ahRIy1fvtw5vmXLFtlsNn3zzTd66KGHVKpUKW3fvl2pqalq27atfH195efnp4ceekh79uwx4DsFAMB/UHQDAIBbys/P1/r16zV48GB5e3u7jAUFBalXr1767LPP9Nhjj+nAgQPKy8uTJCUlJal8+fLasmWLJKmgoED/+te/1KZNG+frjx07plWrVmnNmjVas2aNkpKSNHXqVOf4O++8o/j4eM2bN08//PCDYmNj1bt3byUlJbnkGDNmjKZOnaq0tDQ1bNhQvXr1UtWqVbV7924lJydrzJgxKlGihHu+QQAA3ERxswMAAIC735EjR+RwOFSnTp0bjtepU0dnzpxRYGCgypUrp6SkJD3zzDPasmWLXnvtNX3wwQeSpO+++04FBQVq0aKF87V2u11xcXHy9fWVJPXp00cbN27UlClTdOXKFb399ttKTEzUo48+KkkKDQ3V9u3bNX/+fD322GPO/87kyZPVsWNH5/OsrCyNHDlStWvXliSFh4f/ud8UAABuAzPdAADgtjkcjt8dt9lsat26tbZs2aKzZ8/qwIEDGjx4sK5cuaKDBw8qKSlJDz/8sHx8fJyvCQkJcRbcklSpUiXl5uZKko4ePaqLFy+qY8eOKlOmjPMRHx+vY8eOufzbTZs2dXk+fPhwvfTSS+rQoYOmTp1a5H4AAIxA0Q0AAG4pLCxMNptNaWlpNxxPS0tTQECAKlSooDZt2mjLli3atm2bGjduLD8/P2chnpSU5DI7LanIkm+bzSa73S5JOn/+vCTp66+/1r59+5yPAwcOuOzrlqTSpUu7PJ84caJ++OEHPf7449q0aZPq1q2rL7744g99HwAA+F9RdAMAgFu6//771bFjR82ZM0eXLl1yGTt58qQ++eQTRUVFyWazOfd1f/755869223atFFiYqJ27Njhsp/7VurWratSpUopKytLYWFhLo/g4OBbvv6BBx5QbGysNmzYoO7du2vhwoX/y/82AAB/GEU3AAC4LbNmzdKVK1fUuXNnbd26VcePH9e6devUsWNHValSRVOmTJEkNWzYUAEBAVq6dKlL0b1q1SpduXJFf/nLX2773/T19dWIESMUGxurRYsW6dixY0pJSdGHH36oRYsW3fR1ly5d0pAhQ7RlyxZlZmZqx44d2r179033pAMA4C40UgMAALclPDxce/bs0YQJE9SjRw/l5+crKChITz31lCZMmKBy5cpJur48vFWrVvr666/VsmVLSdcLcT8/P9WqVavIMvBbeeutt1ShQgW98847Sk9PV9myZdWkSRONHTv2pq8pVqyYTp8+rRdeeEE5OTkqX768unfvrkmTJt35NwAAgDtgc9yqIwoAAAAAALgjLC8HAAAAAMBNKLoBAAAAAHATim4AAAAAANyEohsAAAAAADeh6AYAAAAAwE0ougEAAAAAcBOKbgAAAAAA3ISiGwAAAAAAN6HoBgAAAADATSi6AQAAAABwE4puAAAAAADchKIbAAAAAAA3+X+Bt/7zSZSeUgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.ticker import FuncFormatter\n",
    "\n",
    "df_rep['Amount'] = pd.to_numeric(df_rep['Amount'], errors='coerce')\n",
    "\n",
    "# Step 1: Extract Data\n",
    "# Replace these with your actual DataFrame columns\n",
    "top_5_owners_rep = df_rep.groupby('Owner')['Amount'].sum().nlargest(5)\n",
    "\n",
    "# Step 2: Create the Plot\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(top_5_owners_rep.index, top_5_owners_rep.values, color='red')\n",
    "\n",
    "#add text to amount donated by the highest donor\n",
    "plt.text(0, top_5_owners_rep.values[0], f'{top_5_owners_rep.values[0]:,.0f}', \n",
    "         ha='center', va='bottom', fontsize=12, color='black')\n",
    "\n",
    "\n",
    "\n",
    "# Step 3: Rotate x-axis labels\n",
    "plt.xticks(rotation=90)\n",
    "\n",
    "# Step 4: Add Title and Labels\n",
    "plt.title('Top 5 American Sport Team Donors for the Republican Party (2016-2020)')  # Title of the plot\n",
    "plt.xlabel('Owners')  # Label for x-axis\n",
    "plt.ylabel('Amount of Money Donated (USD)')  # Label for y-axis\n",
    "\n",
    "# Step 5: Optional - Add Gridlines\n",
    "# Uncomment the following line if you want to add gridlines\n",
    "# plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7)\n",
    "\n",
    "# Step 6: Adjust Layout\n",
    "plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))\n",
    "plt.tight_layout()  # Adjust layout to avoid overlap\n",
    "\n",
    "# Step 7: Show the Plot\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4c. Bipartisan Party"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 195 entries, 17 to 2790\n",
      "Data columns (total 4 columns):\n",
      " #   Column  Non-Null Count  Dtype \n",
      "---  ------  --------------  ----- \n",
      " 0   Owner   195 non-null    object\n",
      " 1   League  195 non-null    object\n",
      " 2   Amount  195 non-null    object\n",
      " 3   Party   195 non-null    object\n",
      "dtypes: object(4)\n",
      "memory usage: 7.6+ KB\n",
      "None\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Party</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Amy Adams Strunk</td>\n",
       "      <td>NFL</td>\n",
       "      <td>10000</td>\n",
       "      <td>Bipartisan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Amy Adams Strunk</td>\n",
       "      <td>NFL</td>\n",
       "      <td>10000</td>\n",
       "      <td>Bipartisan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Amy Adams Strunk</td>\n",
       "      <td>NFL</td>\n",
       "      <td>5000</td>\n",
       "      <td>Bipartisan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Arte Moreno</td>\n",
       "      <td>MLB</td>\n",
       "      <td>10000</td>\n",
       "      <td>Bipartisan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Arte Moreno</td>\n",
       "      <td>MLB</td>\n",
       "      <td>10000</td>\n",
       "      <td>Bipartisan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Owner League Amount       Party\n",
       "17  Amy Adams Strunk    NFL  10000  Bipartisan\n",
       "18  Amy Adams Strunk    NFL  10000  Bipartisan\n",
       "19  Amy Adams Strunk    NFL   5000  Bipartisan\n",
       "25       Arte Moreno    MLB  10000  Bipartisan\n",
       "26       Arte Moreno    MLB  10000  Bipartisan"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#creating a variable for all of the bipartisan donations\n",
    "df_bipart = donation_df[donation_df[\"Party\"] == \"Bipartisan\"]\n",
    "\n",
    "print(df_bipart.info())\n",
    "\n",
    "df_bipart.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Owner\n",
       "Jimmy and Susan Haslam                   95000\n",
       "Jeremy M. Jacobs and Jerry Jacobs Jr.    65000\n",
       "Arthur J. Rooney II                      56000\n",
       "Rocky Wirtz                              50000\n",
       "Richard Childress                        35000\n",
       "Name: Amount, dtype: object"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find the top donors for the Rep party\n",
    "bipart_owners = df_bipart.groupby('Owner')['Amount'].sum()\n",
    "\n",
    "bipart_owners = bipart_owners.sort_values(ascending=False)\n",
    "\n",
    "bipart_owners.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Owner</th>\n",
       "      <th>League</th>\n",
       "      <th>Party</th>\n",
       "      <th>Amount</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>Jimmy and Susan Haslam</td>\n",
       "      <td>NFL</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>95000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Jeremy M. Jacobs and Jerry Jacobs Jr.</td>\n",
       "      <td>NHL</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>65000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Arthur J. Rooney II</td>\n",
       "      <td>NFL</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>56000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>61</th>\n",
       "      <td>Rocky Wirtz</td>\n",
       "      <td>NHL</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>50000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Mark H. Murphy (Executive Committee)</td>\n",
       "      <td>NFL</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>35000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>Terry Pegula</td>\n",
       "      <td>NHL, NFL</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Cathy Engelbert</td>\n",
       "      <td>WNBA</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>3750</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Gail Miller</td>\n",
       "      <td>NBA</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Henry and Susan Samueli</td>\n",
       "      <td>NHL</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>Neil Leibman</td>\n",
       "      <td>MLB</td>\n",
       "      <td>Bipartisan</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>76 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Owner    League       Party Amount\n",
       "36                 Jimmy and Susan Haslam       NFL  Bipartisan  95000\n",
       "31  Jeremy M. Jacobs and Jerry Jacobs Jr.       NHL  Bipartisan  65000\n",
       "3                     Arthur J. Rooney II       NFL  Bipartisan  56000\n",
       "61                            Rocky Wirtz       NHL  Bipartisan  50000\n",
       "49   Mark H. Murphy (Executive Committee)       NFL  Bipartisan  35000\n",
       "..                                    ...       ...         ...    ...\n",
       "70                           Terry Pegula  NHL, NFL  Bipartisan   5000\n",
       "9                         Cathy Engelbert      WNBA  Bipartisan   3750\n",
       "22                            Gail Miller       NBA  Bipartisan   2000\n",
       "25                Henry and Susan Samueli       NHL  Bipartisan   2000\n",
       "53                           Neil Leibman       MLB  Bipartisan   1000\n",
       "\n",
       "[76 rows x 4 columns]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Group by Owner League and Party then sum the specified columns\n",
    "top_five_bipart = df_bipart.groupby(['Owner','League', 'Party']).sum().reset_index()\n",
    "\n",
    "# Sort the entire DataFrame by 'Amount' in descending order\n",
    "top_five_bipart = top_five_bipart.sort_values(by='Amount', kind='sort', ascending=False)\n",
    "\n",
    "top_five_bipart.head(5)\n",
    "\n",
    "df_bipart = top_five_bipart\n",
    "\n",
    "df_bipart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The total Amount donated (USD) for the Bipartisan Party is $1474699.\n",
      "The mean amount is $19403.93.\n",
      "The median amount is $16666.5.\n"
     ]
    }
   ],
   "source": [
    "bipart_amount_sum = df_bipart['Amount'].sum()\n",
    "bipart_amount_mean = df_bipart['Amount'].mean().round(2)\n",
    "bipart_amount_median = df_bipart['Amount'].median()\n",
    "\n",
    "print(f'The total Amount donated (USD) for the Bipartisan Party is ${bipart_amount_sum}.\\nThe mean amount is ${bipart_amount_mean}.\\nThe median amount is ${bipart_amount_median}.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Create a bar graph for the Bipartisan Party**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/GU6VOAAAACXBIWXMAAA9hAAAPYQGoP6dpAACx3ElEQVR4nOzdd1QU198G8GfpvUhHQVCJgA1FRcSKCCq22I2JgFhiQ8UeY40l9l5iNNiwl9gi9t4FY8OuiA0UkSIgAjvvH77sz3UBd83iUp7POZwjd+7MPrsMK9+dO/eKBEEQQERERERERERKp6bqAEREREREREQlFYtuIiIiIiIiokLCopuIiIiIiIiokLDoJiIiIiIiIiokLLqJiIiIiIiICgmLbiIiIiIiIqJCwqKbiIiIiIiIqJCw6CYiIiIiIiIqJCy6iYiIiIiIiAoJi24ioi8IDAyEg4ODqmMQFQsRERFwc3ODjo4ORCIRkpKSVJJDJBJh0KBBKnns/EyaNAkikUjVMfLk4OCAwMBAVcco0Vq1aoU+ffqoOkapk5WVBTs7OyxbtkzVUagUY9FNVEyIRCK5vk6cOKGyLL///rtCx1m2bBlEIhE8PDwKKWnp8O7dO0ycOBFVq1aFvr4+zMzM4ObmhiFDhuDFixcqyZSeno5JkybJdT46ODjIdW6vWbOm0HP/V5/m1dDQQJkyZeDu7o4hQ4YgOjpa1fEK3Zs3b9ClSxfo6upi6dKlWL9+PfT19Qvt8c6dO4dJkyaprLAHZM9fHR0dODk5YeTIkUhMTFRZrrwUhdfrawQGBkq9xkZGRqhRowbmzp2LzMxMpT1OdHQ0Jk2ahJiYGKUdM9fZs2dx6NAhjB49WtJ2584djBo1Cm5ubjA0NISNjQ38/f1x5cqVPI/x/PlzdOnSBSYmJjAyMkK7du3w6NEjmX7Lly9H586dYW9vD5FI9MUPU44cOQJvb28YGxvD0NAQ7u7u2LJlyxef09OnTzF58mTUrVsXpqamMDc3R5MmTXDkyJE8+yclJaFv376wsLCAvr4+mjZtiqioKKk+b968wezZs9GoUSNYWFjAxMQE9erVyzdPZmYmRo8eDVtbW+jq6sLDwwOHDx+W6qOpqYnQ0FBMmzYN79+//+LzIioMIkEQBFWHIKIv27Bhg9T369atw+HDh7F+/Xqp9ubNm8PKyqpQs4hEIjRv3hw9e/aUaq9ZsyaqVKki93G8vLzw4sULxMTE4P79+6hUqZKyoypFVlYWxGIxtLW1VR1FRlZWFjw8PHDnzh0EBATAzc0N7969w61bt7B3715s27YNTZo0+ea5EhISYGFhgYkTJ2LSpEkF9v3777/x7t07yff//PMPNm3ahPnz58Pc3FzSXr9+fVSoUKGwIivFp78bgiAgOTkZ165dw7Zt25CWloaZM2ciNDRU1TELTUREBFq2bInDhw/Dx8en0B9vzpw5GDlyJB4/fiwzGkUkEmHgwIFYsmRJoWZwcHCAqakphg8fDgB4//49IiMjsWrVKtSsWROXLl2S9M3OzkZ2djZ0dHQKNVN+Cnq9MjMzoaamBk1NTZVkK0hgYCA2b96MVatWAfhYvO3YsQMnTpxA165dsXnzZqU8zvbt29G5c2ccP35c6e+b7du3R0ZGBg4ePChpGzFiBFavXo2OHTuibt26SE5Oxh9//IGYmBhERERI/Q69e/cOtWrVQnJyMoYPHw5NTU3Mnz8fgiDg33//hZmZmaSvg4MDUlNTUbduXRw5cgQ9evTI90PLsLAwBAcHo3nz5mjbti3U1dVx9+5dlC1bFiNGjCjwOS1ZsgSjRo1C+/bt4eXlhezsbKxbtw5RUVH466+/EBQUJOkrFovRsGFDXLt2DSNHjoS5uTmWLVuGp0+fIjIyEk5OTgCAffv2oUOHDmjVqhWaNm0KDQ0N7NixA8ePH8eECRMwefJkqQzdu3fH9u3bMXToUDg5OWHNmjW4fPkyjh8/jgYNGkj6JSUlwcrKCsuXL0evXr2+/AMjUjaBiIqlgQMHCqr6FQYgDBw48D8d49GjRwIAYefOnYKFhYUwadIkJaVTnnfv3qk6whdt3bpVACCEh4fLbMvIyBCSk5O/aZ6cnBwhIyNDeP36tQBAmDhxosLHmD17tgBAePz4sdLzFbb8fjcSEhIET09PAYCwf/9+FSSTz38959euXSsAEC5fvqykRAVnKuhcUcb7lDzKly8v+Pv7y7SPGDFCACDcu3ev0DN8Se5rWFx/twICAgR9fX2ptpycHKF27doCAOH58+f/6fgZGRlCTk6OsG3bNgGAcPz48f90vM/Fx8cLGhoawqpVq6Tar1y5IqSmpkq1JSQkCBYWFoKXl5dU+8yZMwUAwqVLlyRtt2/fFtTV1YWxY8dK9Y2JiRHEYrEgCIKgr68vBAQE5Jnr8ePHgq6urhASEvJVz+vmzZvC69evpdrev38vODs7C+XKlZNq37JliwBA2LZtm6Tt1atXgomJidC9e3dJ26NHj4SYmBipfcViseDt7S1oa2tLvR9cvHhRACDMnj1b0paRkSFUrFhR8PT0lMnbunVroWHDhl/1XIn+Kw4vJypB0tLSMHz4cNjZ2UFbWxuVK1fGnDlzIHw2oCX3Xsfw8HBUrlwZOjo6cHd3x6lTpxR6vIyMjK8eqhUeHg5TU1P4+/ujU6dOCA8Pl+kTExMDkUiEOXPmYOnSpahQoQL09PTg6+uLp0+fQhAE/PbbbyhXrhx0dXXRrl27PIdzHjhwAA0bNoS+vj4MDQ3h7++PW7duSfUJDAyEgYEBHj58iFatWsHQ0BA9evSQbPv8qpBYLMbChQtRrVo16OjowMLCAi1atJAaFhgWFgZvb29YWlpCW1sbrq6uWL58uUw+BwcHtG7dGmfOnEHdunWho6ODChUqYN26dV98HR8+fAjg46iBz+no6MDIyEjmOT569Ah+fn7Q19eHra0tpkyZInOOfM25VKVKFWhra2PFihWwsLAAAEyePFkyJPRLV7y/ZMOGDXB3d4euri7KlCmDbt264enTp1J9Tp8+LRlWqa2tDTs7OwwbNgwZGRlS/XJfi9jYWLRu3RoGBgYoW7Ysli5dCgC4ceMGvL29oa+vj/Lly2Pjxo3/KbuZmRk2b94MDQ0NTJs2TWrbq1evEBwcDCsrK+jo6KBGjRpYu3atVJ9PfxdWrlyJihUrQltbG3Xq1MHly5dlHu/YsWOSc97ExATt2rXD7du3pfrk3l8cHR2NH374AaamppIrQ3FxcQgKCkK5cuWgra0NGxsbtGvXrsBht02aNEFAQAAAoE6dOjLDWrdt2yb5+Zmbm+PHH3/E8+fPpY5R0O/h5yZNmoSRI0cCABwdHSXn2ecZ//77b1StWhXa2tqoUqUKIiIiZI71/Plz9OrVC1ZWVpJ+f/31V77PVR7W1tYAAA0NDanMn9/TLe/78ZMnTzBgwABUrlwZurq6MDMzQ+fOnWWe75o1ayASiXDy5EkMGDAAlpaWKFeu3Bdfr8/v6c7KysLkyZPh5OQEHR0dmJmZoUGDBlJDd69fv47AwEBUqFABOjo6sLa2Rq9evfDmzRupTLnP+8GDBwgMDISJiQmMjY0RFBSE9PT0r3p91dTUJFejY2JikJiYiBEjRqBatWowMDCAkZERWrZsiWvXrkntd+LECYhEImzevBm//vorypYtCz09PSxatAidO3cGADRt2lTqlq2AgACYm5sjKytLJoevry8qV65cYNb9+/cjOztbZvSHu7s7DAwMpNrMzMzQsGFDmd/X7du3o06dOqhTp46kzdnZGc2aNcPWrVul+pYvX16uuQNWrFiBnJwcTJkyBcDHq+mfv8cXpEqVKlKjkQBAW1sbrVq1wrNnz5CamiqV38rKCh06dJC0WVhYoEuXLti9e7fkNgFHR0eUL19e6pgikQjt27dHZmam1HD67du3Q11dHX379pW06ejoIDg4GOfPn5f5/6F58+Y4c+ZMkbvtg0oHjS93IaLiQBAEtG3bFsePH0dwcDDc3Nxw8OBBjBw5Es+fP8f8+fOl+p88eRJbtmxBSEgItLW1sWzZMrRo0QKXLl1C1apVv/h4a9aswbJlyyAIAlxcXPDrr7/ihx9+kDtveHg4OnToAC0tLXTv3h3Lly/H5cuXpf6g+LTvhw8fMHjwYCQmJmLWrFno0qULvL29ceLECYwePRoPHjzA4sWLMWLECKk/ltevX4+AgAD4+flh5syZSE9Px/Lly9GgQQNcvXpVqpjOzs6Gn58fGjRogDlz5kBPTy/f/MHBwVizZg1atmyJ3r17Izs7G6dPn8aFCxdQu3ZtAB/vq6tSpQratm0LDQ0N7N27FwMGDIBYLMbAgQOljvfgwQN06tQJwcHBCAgIwF9//YXAwEC4u7sXOGQ/94+TdevW4ddff/3iH1o5OTlo0aIF6tWrh1mzZiEiIgITJ05Edna25A8vRc+lY8eOYevWrRg0aBDMzc1Ro0YNLF++HP3798f3338v+SOrevXqBWYryLRp0zB+/Hh06dIFvXv3xuvXr7F48WI0atQIV69ehYmJCYCPhV16ejr69+8PMzMzXLp0CYsXL8azZ8+wbds2mdeiZcuWaNSoEWbNmoXw8HAMGjQI+vr6GDduHHr06IEOHTpgxYoV6NmzJzw9PeHo6PjVz8He3h6NGzfG8ePHkZKSAiMjI2RkZKBJkyZ48OABBg0aBEdHR2zbtg2BgYFISkrCkCFDpI6xceNGpKamol+/fhCJRJg1axY6dOiAR48eSYYFHzlyBC1btkSFChUwadIkZGRkYPHixfDy8kJUVJTMB0idO3eGk5MTpk+fLvmDu2PHjrh16xYGDx4MBwcHvHr1CocPH0ZsbGy+kwqOGzcOlStXxsqVKzFlyhQ4OjqiYsWKAD6+XwQFBaFOnTqYMWMG4uPjsXDhQpw9e1bq5wfI/3vYoUMH3Lt3T+ZWhNwPfADgzJkz2LlzJwYMGABDQ0MsWrQIHTt2RGxsrGQ4bnx8POrVqycpfi0sLHDgwAEEBwcjJSUFQ4cO/eLPNisrCwkJCQA+Di+/evUq5s2bh0aNGsl1zsjzfnz58mWcO3cO3bp1Q7ly5RATE4Ply5ejSZMmiI6OlnmdBgwYAAsLC0yYMAFpaWlo2bLlF1+vT02aNAkzZsxA7969UbduXaSkpODKlSuIiopC8+bNAQCHDx/Go0ePEBQUBGtra9y6dQsrV67ErVu3cOHCBZn3oy5dusDR0REzZsxAVFQUVq1aBUtLS8ycOfOLr1Fecj90NDMzw6NHj/D333+jc+fOcHR0RHx8PP744w80btwY0dHRsLW1ldr3t99+g5aWFkaMGIHMzEz4+voiJCQEixYtwi+//AIXFxcAgIuLC3766SesW7cOBw8eROvWrSXHiIuLw7FjxzBx4sQCc547dw5mZmYyxWR+4uLipIpZsViM69ev5zksum7dujh06BBSU1NhaGgo1/FzHTlyBM7Ozvjnn38k7++mpqYYOHAgJk+eDDW1r7s2FxcXBz09Palz8urVq6hVq5bMMevWrYuVK1fi3r17qFatWoHHBCD1uly9ehXfffed1IfLuccEgH///Rd2dnaSdnd3dwiCgHPnzkn9HIm+CVVdYiei/+bz4eV///23AECYOnWqVL9OnToJIpFIePDggaQNgABAuHLliqTtyZMngo6OjvD9999/8bHr168vLFiwQNi9e7ewfPlyoWrVqgIAYdmyZXJlv3LligBAOHz4sCAIH4eOlStXThgyZIhUv8ePHwsABAsLCyEpKUnSPnbsWAGAUKNGDSErK0vS3r17d0FLS0t4//69IAiCkJqaKpiYmAh9+vSROm5cXJxgbGws1R4QECAAEMaMGSOTNyAgQChfvrzk+2PHjgkA8hySlzukTxAEIT09XWa7n5+fUKFCBam28uXLCwCEU6dOSdpevXolaGtrC8OHD5c5xqfS09OFypUrCwCE8uXLC4GBgcLq1auF+Pj4PJ8HAGHw4MFSef39/QUtLS3JMEFFzyU1NTXh1q1bUn2VObw8JiZGUFdXF6ZNmybV78aNG4KGhoZUe16v+YwZMwSRSCQ8efJE0pb7WkyfPl3S9vbtW0FXV1cQiUTC5s2bJe137tyR+7ngC0OahwwZIgAQrl27JgiCICxYsEAAIGzYsEHS58OHD4Knp6dgYGAgpKSkCILwv98FMzMzITExUdJ39+7dAgBh7969kjY3NzfB0tJSePPmjaTt2rVrgpqamtCzZ09J28SJEwUAUkM7c18HfDZkU15hYWEyw8s/fPggWFpaClWrVhUyMjIk7fv27RMACBMmTJC0FfR7mJcvDS/X0tKSOl+vXbsmABAWL14saQsODhZsbGyEhIQEqf27desmGBsb53lOfSr39/fzLy8vL5lj5r7mn+eU5/04rxznz58XAAjr1q2TtOX+DBo0aCBkZ2dL9S/o9SpfvrzUMOQaNWrkOWz+U3ll2rRpk8z7We7z7tWrl1Tf77//XjAzMyvwMQThf8PLX79+Lbx+/Vp48OCBMH36dEEkEgnVq1cXBOHjsOacnByp/R4/fixoa2sLU6ZMkbQdP35cACBUqFBBJn9+w8tzcnKEcuXKCV27dpVqnzdvniASiYRHjx4VmL9BgwaCu7v7F5+nIAjCqVOnBJFIJIwfP17Slvt++unzyLV06VIBgHDnzp08j1fQ8HIjIyPB1NRU0NbWFsaPHy9s375d+OGHHxT6Hfzc/fv3BR0dHeGnn36SyfH5z18QBGH//v0CACEiIiLfY75580awtLSUGRpepUoVwdvbW6b/rVu3BADCihUrpNpfvHghABBmzpypyFMiUgoOLycqIf755x+oq6sjJCREqn348OEQBAEHDhyQavf09IS7u7vke3t7e7Rr1w4HDx5ETk5OgY919uxZDBkyBG3btsXPP/+MyMhIVK1aFb/88ovMMN68hIeHw8rKCk2bNgXwcehY7mQ4eT12586dYWxsLPk+d7bzH3/8UWropoeHBz58+CAZsnr48GEkJSWhe/fuSEhIkHypq6vDw8MDx48fl3ms/v37fzH/jh07IBKJ8ry68emVHV1dXcm/k5OTkZCQgMaNG+PRo0dITk6W2s/V1RUNGzaUfG9hYYHKlSvnOTPtp3R1dXHx4kXJsNE1a9YgODgYNjY2GDx4cJ4z+366jFLu1b0PHz5IZpxV9Fxq3LgxXF1dC8z5X+zcuRNisRhdunSR+jlaW1vDyclJ6uf46WuelpaGhIQE1K9fH4Ig4OrVqzLH7t27t+TfJiYmqFy5MvT19dGlSxdJe+XKlWFiYvLFn4U8coeS5g67/Oeff2BtbY3u3btL+mhqaiIkJATv3r3DyZMnpfbv2rUrTE1NJd/nnjO52V6+fIl///0XgYGBKFOmjKRf9erV0bx5c/zzzz8ymX7++Wep73V1daGlpYUTJ07g7du3/+XpAgCuXLmCV69eYcCAAVITiPn7+8PZ2Rn79++X2Uee30N5+Pj4SK62Ax9fByMjI8nrJQgCduzYgTZt2kAQBKnzy8/PD8nJyTKzK+cld8bkw4cPY9++fZg2bRpu3bqFtm3byvWeKM/78afndlZWFt68eYNKlSrBxMQkz4x9+vSBurr6Fx87PyYmJrh16xbu37+fb59PM71//x4JCQmoV68eAOSZ6fNzrWHDhnjz5g1SUlK+mCctLQ0WFhawsLBApUqV8Msvv8DT0xO7du0C8HFYc+5V1JycHLx58wYGBgaoXLlynlkCAgKk8hdETU0NPXr0wJ49e6SGTIeHh6N+/fpfHM3w5s0bqd/b/Lx69Qo//PADHB0dMWrUKEl77jmU12Seub9T8pxnn3v37h3evn2LyZMnY8qUKejYsSPCw8PRokULLFy4UOq5yiM9PR2dO3eGrq6uzGomGRkZX5VfLBajR48eSEpKwuLFi//TMXN/BrmjUoi+JRbdRCXEkydPYGtrKzO8LHeI3JMnT6Tac2cK/dR3332H9PR0vH79WqHH1tLSwqBBg5CUlITIyMgC++bk5GDz5s1o2rQpHj9+jAcPHuDBgwfw8PBAfHw8jh49KrOPvb291Pe5Bfinw8Y+bc8tFHL/WPT29pb8sZb7dejQIbx69Upqfw0NDZQrV+6Lz/fhw4ewtbWVKmrycvbsWfj4+Ejuq7WwsMAvv/wCADJF9+fPEfj4B4I8RY+xsTFmzZqFmJgYxMTEYPXq1ahcuTKWLFmC3377TaqvmpqazAzg3333HQBI7u1U9Fz6L0Ou5XH//n0IggAnJyeZn+Pt27elfo6xsbGSgtPAwAAWFhZo3LgxANnXPPde/E8ZGxujXLlyMsNijY2NlVKA5s7SnvvaPnnyBE5OTjJDLvN7rT8/T3L/iMzNlts/r3tMXVxckJCQgLS0NKn2z39+2tramDlzJg4cOAArKyvJ8Pvc4Z2KKiiTs7OzzHOU9/dQHl/6vXr9+jWSkpKwcuVKmXMrd+blz98n8mJubg4fHx/4+PjA398fv/zyC1atWoVz585JZtwuiDzvxxkZGZgwYYJkngVzc3NYWFggKSlJ5twG/vvv5ZQpU5CUlITvvvsO1apVw8iRI3H9+nWpPomJiRgyZAisrKygq6sLCwsLyePmlelL529BdHR0JB9snDp1Ck+fPsXZs2cl72disRjz58+Hk5OT1Otz/fp1pbw+PXv2REZGhqTIv3v3LiIjI/HTTz/Jtb/whXul09LS0Lp1a6SmpmL37t1S93rnfjiQ14eoufOqyPsBwqdy9/n0Q7/c7zMyMiQfVL5+/RpxcXGSr09Xm8iVk5ODbt26ITo6Gtu3b5cZzq+rq/tV+QcPHoyIiAisWrUKNWrU+E/HzP0ZyHO/O5Gy8Z5uIlKK3AL4SxOUHDt2DC9fvsTmzZvzXOYlPDwcvr6+Um35Xa3Jrz33P1axWAzg433duZMaferTq+SA9JWS/+rhw4do1qwZnJ2dMW/ePNjZ2UFLSwv//PMP5s+fL8mW60vPRV7ly5dHr1698P3336NChQoIDw/H1KlTv/p5yONr/thThFgshkgkwoEDB/J8nXL/OM3JyUHz5s2RmJiI0aNHw9nZGfr6+nj+/DkCAwPlfs2V9bPIy82bN6Gurv7VBVFhZMvr5zd06FC0adMGf//9Nw4ePIjx48djxowZOHbsGGrWrPnVjyUPZf4eyvse8eOPP0omgfvc185F0KxZMwDAqVOnMHjw4K86xqcGDx6MsLAwDB06FJ6enjA2NoZIJEK3bt1kzm3gv/9eNmrUCA8fPsTu3btx6NAhrFq1CvPnz8eKFSskI0S6dOmCc+fOYeTIkXBzc4OBgQHEYjFatGiRZ6b/cv6qq6sXuAzd9OnTMX78ePTq1Qu//fYbypQpAzU1NQwdOlQpr4+rqyvc3d2xYcMG9OzZExs2bICWlpbUqJj8mJmZFfjBwocPH9ChQwdcv34dBw8elJlXpUyZMtDW1sbLly9l9s1t+7zIlYetrS3u378vs8yopaUlgP99GFKnTh2pD8fyWgqyT58+2LdvH8LDw+Ht7S3zWDY2Ngrnnzx5MpYtW4bff/89zw83bGxsZCZjLOiYuc/n88nfiL4FFt1EJUT58uVx5MgRmclU7ty5I9n+qbyGDN67dw96enr5TqxTkNzhml/aNzw8HJaWlpJZoj+1c+dO7Nq1CytWrFBKIZc7rNTS0lKpawZXrFgRBw8eRGJiYr5Xu/fu3YvMzEzs2bNH6upOXkPaC4OpqSkqVqyImzdvSrWLxWI8evRIcnUb+PhzByCZIEvRcykvyrySULFiRQiCAEdHR6ncn7tx4wbu3buHtWvXSq0h/+lsy6oUGxuLkydPwtPTU/K6li9fHtevX4dYLJYqNBV5rT+V2//u3bsy2+7cuQNzc3Po6+vLdayKFSti+PDhGD58OO7fvw83NzfMnTsXGzZs+OpMn/8xfvfuXYWf46f+63lmYWEBQ0ND5OTkKH1d8ezsbADI86rg5+R5P96+fTsCAgIwd+5cSZ/3798jKSlJ7kyKvl5lypRBUFAQgoKC8O7dOzRq1AiTJk1C79698fbtWxw9ehSTJ0/GhAkTCnwu38L27dvRtGlTrF69Wqo9KSlJ7iLrS69Pz549ERoaipcvX2Ljxo3w9/eXa9i4s7MzduzYkec2sViMnj174ujRo9i6datkZM6n1NTUUK1aNanVMXJdvHgRFSpUUHgSNeDjxGL379/H8+fPpUZAvXjxAsD//j8PDw+XGqr9+WipkSNHIiwsDAsWLJC5ap7Lzc0Np0+flnmvu3jxIvT09GTe25cuXYpJkyZh6NChGD16dL7H/HRiyk+Pmbv9U48fPwbwv5FERN8Sh5cTlRCtWrVCTk4OlixZItU+f/58iEQitGzZUqr9/PnzUve5PX36FLt374avr2+B9wHmNfQ8NTUVCxYsgLm5udR9iZ/LyMjAzp070bp1a3Tq1Enma9CgQUhNTcWePXvkfdoF8vPzg5GREaZPn57nUi+KDqPP1bFjRwiCgMmTJ8tsy71ik/safnoFJzk5GWFhYV/1mPm5du1anvenPXnyBNHR0XkO6f30HBEEAUuWLIGmpqbkypyi51JecmetVaQgyE+HDh2grq6OyZMny1wREwRBsjxRXq+5IAhYuHDhf87wXyUmJqJ79+7IycnBuHHjJO2tWrVCXFwctmzZImnLzs7G4sWLYWBgkOcf4AWxsbGBm5sb1q5dK/Xa37x5E4cOHUKrVq2+eIz09HSZpQArVqwIQ0PDPIdyfknt2rVhaWmJFStWSO1/4MAB3L59G/7+/gofM1fuBwhfe56pq6ujY8eO2LFjh8wHVMDXv0cAHz94AyAzJDYv8rwfq6ury5z/ixcv/uIcHJ9S5PX6fNkvAwMDVKpUSfIzzOv3DQAWLFggdx5lyuv12bZtW55XQvPzpdene/fuEIlEGDJkCB49eoQff/xRruN6enri7du3ec4LMXjwYGzZsgXLli2TWk7rc506dcLly5elCu+7d+/i2LFjkqXOFNW1a1cAkPqgQiwWIywsDGXKlJH8f+7l5SW5fcLHx0eq6J49ezbmzJmDX375RWa1hc/zx8fHY+fOnZK2hIQEbNu2DW3atJG6Nzt3Jv8ePXpg3rx5BR4zJycHK1eulLRlZmYiLCwMHh4eMregRUZGQiQSwdPT80svDZHS8Uo3UQnRpk0bNG3aFOPGjUNMTAxq1KiBQ4cOYffu3Rg6dKjUZEIAULVqVfj5+UktUQMgz0LyU0uXLsXff/+NNm3awN7eHi9fvsRff/2F2NhYrF+/HlpaWvnumzsJTdu2bfPcXq9ePVhYWCA8PFzyx8B/YWRkhOXLl+Onn35CrVq10K1bN1hYWCA2Nhb79++Hl5eXTGEpj6ZNm+Knn37CokWLcP/+fclQytOnT6Np06YYNGgQfH19oaWlhTZt2qBfv3549+4d/vzzT1haWuY5xO5rHT58GBMnTkTbtm1Rr149yTrcf/31FzIzM2WGAOro6CAiIgIBAQHw8PDAgQMHsH//fvzyyy+SqxqKnkt50dXVhaurK7Zs2YLvvvsOZcqUQdWqVeVaju5zFStWxNSpUzF27FjExMSgffv2MDQ0xOPHj7Fr1y707dsXI0aMgLOzMypWrIgRI0bg+fPnMDIywo4dO5RyL7Yi7t27hw0bNkAQBKSkpODatWvYtm0b3r17h3nz5qFFixaSvn379sUff/yBwMBAREZGwsHBAdu3b8fZs2exYMGCr7p6NXv2bLRs2RKenp4IDg6WLBlmbGws11rp9+7dQ7NmzdClSxe4urpCQ0MDu3btQnx8PLp166ZwHk1NTcycORNBQUFo3LgxunfvLlkyzMHBAcOGDVP4mLlyi4Jx48ahW7du0NTURJs2beS+mg8Av//+O44fPw4PDw/06dMHrq6uSExMRFRUFI4cOSLXmr7Pnz+XjAD48OEDrl27hj/++APm5uZyDS2X5/24devWWL9+PYyNjeHq6orz58/jyJEjkqXP5KHI6+Xq6oomTZrA3d0dZcqUwZUrV7B9+3bJRIxGRkaS+/2zsrJQtmxZHDp0SHI18Vtr3bo1pkyZgqCgINSvXx83btxAeHi4zFXZgri5uUFdXR0zZ85EcnIytLW14e3tLRlubWFhgRYtWmDbtm0wMTGR+wMjf39/aGho4MiRI1JrSi9YsADLli2Dp6cn9PT0ZEaRfP/995KfzYABA/Dnn3/C398fI0aMgKamJubNmwcrKysMHz5car+9e/dK1ifPysrC9evXJbcZtW3bVnLLRLt27dCsWTPMmDEDCQkJqFGjBv7++2+cOXMGf/zxR56TlH1q165dGDVqFJycnODi4iKTv3nz5pKh6506dUK9evUQFBSE6OhomJubY9myZcjJyZE6zy9duoSePXvCzMwMzZo1Q3h4uNQx69evL/mZenh4oHPnzhg7dixevXqFSpUqYe3atZK5TT53+PBheHl5KfQ7Q6Q032iWdCJSss+XDBOEj0tkDRs2TLC1tRU0NTUFJycnYfbs2VLLWAnC/5Y12rBhg+Dk5CRoa2sLNWvWlFkmJS+HDh0SmjdvLlhbWwuampqCiYmJ4OvrKxw9evSL+7Zp00bQ0dER0tLS8u0TGBgoaGpqCgkJCZJlkj5fuih3yZdt27ZJtee1XFFufz8/P8HY2FjQ0dERKlasKAQGBkot0ZO7JE1ePl8yTBAEITs7W5g9e7bg7OwsaGlpCRYWFkLLli2FyMhISZ89e/YI1atXF3R0dAQHBwdh5syZwl9//SWzZE/58uXzXJqncePGQuPGjfN9rQRBEB49eiRMmDBBqFevnmBpaSloaGgIFhYWgr+/v3Ds2DGZ56Gvry88fPhQ8PX1FfT09AQrKyth4sSJMkvtKHou5eXcuXOCu7u7oKWlpdDyYfkta7Rjxw6hQYMGgr6+vqCvry84OzsLAwcOFO7evSvpEx0dLfj4+AgGBgaCubm50KdPH8kyUWFhYTKvxecaN24sVKlSRaY9v5/R5/DJklFqamqCiYmJULNmTWHIkCEyy6rlio+PF4KCggRzc3NBS0tLqFatmlRWQRDy/V3IfczPX9sjR44IXl5egq6urmBkZCS0adNGiI6OluqTu4xT7lJxuRISEoSBAwcKzs7Ogr6+vmBsbCx4eHgIW7du/eLzz+93UBAEYcuWLULNmjUFbW1toUyZMkKPHj2EZ8+eSfUp6PcwP7/99ptQtmxZQU1NTeq8ye/c/HxpLEH4+DMYOHCgYGdnJ2hqagrW1tZCs2bNhJUrV37x8T9fMkxNTU2wtLQUunfvLrVcmSDkv2SYPO/Hb9++lZwnBgYGgp+fn3Dnzh2Z51PQz6Cg1+vz40ydOlWoW7euYGJiIujq6grOzs7CtGnThA8fPkj6PHv2TPj+++8FExMTwdjYWOjcubNkWaZPz8n8zrXcrHktYfYpec6L9+/fC8OHDxdsbGwEXV1dwcvLSzh//rzM+2h+/3/k+vPPP4UKFSoI6urqeS4ftnXrVgGA0Ldv3wLzfK5t27ZCs2bNZJ7Xp+fO51+fvy5Pnz4VOnXqJBgZGQkGBgZC69athfv378s8VkHH/fy9JTU1VRgyZIhgbW0tef/5dAnDguT+XPP7+vy1S0xMFIKDgwUzMzNBT09PaNy4scx5mntOyJs/IyNDGDFihGBtbS1oa2sLderUyXP5saSkJEFLS0tYtWqVXM+NSNlEgqCEmWGIqFgRiUQYOHDgV13lpeIrMDAQ27dvl+seUyL6Nvh+XLzs3r0b7du3x6lTp6SWefyS06dPo0mTJrhz506es9VT4VqwYAFmzZqFhw8fFvrkn0R54T3dRERERERy+PPPP1GhQgU0aNBAof0aNmwIX19fzJo1q5CSUX6ysrIwb948/Prrryy4SWV4TzcRERERUQE2b96M69evY//+/Vi4cOFXzZx/4MCBQkhGX6KpqYnY2FhVx6BSjle6qciLjIxEixYtYGRkBENDQ/j6+uLff/+V6dekSROIRCKZr08nLfqSPXv2oFatWtDR0YG9vT0mTpwoWfblU0lJSejbty8sLCygr6+Ppk2bSs08+zXHJCIioqKpe/fuWLx4MYKDgzFgwABVxyGiYob3dFORFhUVBS8vL9jZ2aFfv34Qi8VYtmwZEhMTcenSJanlkJo0aYKHDx9ixowZUsewtbWVWRs2LwcOHIC/vz+aNGmC7t2748aNG1i6dCn69u2L5cuXS/qJxWI0bNgQ165dw8iRIyUzcD59+hSRkZFS92rJe0wiIiIiIiqZWHRTkebv74/z58/j/v37kiUeXr58ie+++w6+vr7YsWOHpG+TJk2QkJCQ51qr8qhSpQo0NTVx5coVaGh8vPPi119/xfTp0xEdHQ1nZ2cAwNatW9G1a1ds27YNnTp1AvBxLdfvvvsOLVu2xMaNGxU+JhERERERlUwcXk5F2unTp+Hj4yO1pqKNjQ0aN26Mffv25TkLc3Z2tsKzM0dHRyM6Ohp9+/aVFMfAx3UxBUHA9u3bJW3bt2+HlZUVOnToIGmzsLBAly5dsHv3bmRmZip8TCIiIiIiKpk4kVohEovFePHiBQwNDb9qwg0CMjMzoaGhgZSUFKl2TU1NfPjwARcvXkSdOnUAADk5Obh37x709fXx4cMHWFpaIiAgAKNHj4ampmaBj3Pu3DkAgIuLi9RjGRgYoGzZsrh06ZKkPTIyEtWrV5cp7KtVq4b09HRERUWhSpUqCh2TiIiIiIiKF0EQkJqaCltbW6ip5X89m8PLC9GzZ89gZ2en6hhERERERERUSJ4+fYpy5crlu51XuguRoaEhgI8/BCMjIxWnKZ5Wr16N0NBQ/PDDDxgyZAjEYjFmz56NvXv3IisrCytXrkTXrl3z3T8kJARr167FkSNHJFfE8zJr1ixMmzYNDx48gIWFhdS2li1bIjU1FWfOnAEAmJqaIigoCPPmzZPqd/LkSbRt2xbh4eFo3bq1QsckIiIiIqLiJSUlBXZ2dpK6Lz8sugtR7pByIyMjFt1fadiwYUhISMDs2bMlE5TVrl0bo0aNwrRp02BhYVHgazt27FisXbsW58+fR7NmzfLtZ2JiAgDQ0tKSOV5WVhb09fUl7bq6uhAEQaafuro6AMDMzAxGRkYKHZOIiIiIiIqnL91KzInUqMibNm0a4uPjcfr0aVy/fh2XL1+GWCwGAHz33XcF7ps7vD8xMbHAfjY2NgA+zoz+uZcvX8LW1laqb379AEj6KnJMIiIiIiIqmVh0U7FgamqKBg0aoFq1agCAI0eOoFy5cl9ccuvRo0cAIDO8+3Nubm4AgCtXrki1v3jxAs+ePZNsz+0bFRUlKfxzXbx4EXp6epIPAhQ5JhERERERlUwsuqnY2bJlCy5fvoyhQ4dKZglMSUmRLNWVSxAETJ06FQDg5+dX4DGrVKkCZ2dnrFy5Ejk5OZL25cuXQyQSSdbjBoBOnTohPj4eO3fulLQlJCRg27ZtaNOmDbS1tRU+JhERERERlUy8p5uKtFOnTmHKlCnw9fWFmZkZLly4gLCwMLRo0QJDhgyR9IuKikL37t3RvXt3VKpUCRkZGdi1axfOnj2Lvn37olatWlLHFYlEaNy4MU6cOCFpmz17Ntq2bQtfX19069YNN2/exJIlS9C7d2+4uLhI+nXq1An16tVDUFAQoqOjYW5ujmXLliEnJweTJ0+Wehx5j0lERERERCUTlwwrRCkpKTA2NkZycjInzPpKDx8+xIABAxAVFYXU1FQ4OjoiICAAoaGh0NLSkvR7/PgxRo8ejcuXLyMuLg5qampwcXFBnz590LdvX6nJDd69ewdDQ0N069YNmzZtknq8v//+G5MnT8bt27dhYWGBwMBATJgwQWad77dv32LkyJH4+++/kZGRgTp16mDOnDmoXbu2zHOQ95hERERERFR8yFvvfVXRHRsbiydPniA9PR0WFhaoUqWKZEgt/Q+L7qLpn3/+QevWrXHt2jXJPeJERERERESKkLfek3t4eUxMDJYvX47Nmzfj2bNn+LRW19LSQsOGDdG3b1907NhRcp8tUVF0/PhxdOvWjQU3EREREREVOrmudIeEhGDt2rXw8/NDmzZtULduXdja2kJXVxeJiYm4efMmTp8+jc2bN0NdXR1hYWGoU6fOt8hfpPFKNxERERERUcmk1Cvd+vr6ePToEczMzGS2WVpawtvbG97e3pg4cSIiIiLw9OlTFt1ERERERERU6nEitUJUHK50iyaLvtyJSiVhIt8aiIiIiIjyo/R7uj+VkJCAmJgYiEQiODg45HkFnIiIiIiIiKi0U2jGs1u3bqFRo0awsrKCh4cH6tatKxlefvfu3cLKSERERERERFQsyX2lOy4uDo0bN4aFhQXmzZsHZ2dnCIKA6Oho/Pnnn2jYsCFu3rwJS0vLwsxLREREREREVGzIXXTPnz8f5cuXx9mzZ6GjoyNpb9GiBfr3748GDRpg/vz5mDFjRqEEJSIiIiIiIipu5B5efvjwYYwePVqq4M6lq6uLkSNH4uDBg0oNR0RERERERFScyV10P3r0CLVq1cp3e+3atfHo0SOlhCIiIiIiIiIqCeQuulNTUwucBt3Q0BDv3r1TSigiIiIiIiKikkChJcNSU1PzHF4OfFyjjEt+ExEREREREf2P3EW3IAj47rvvCtwuEomUEoqIiIiIiIioJJC76D5+/Hhh5iAiIiIiIiIqceQuuhs3blyYOYiIiIiIiIhKHLmL7uzsbOTk5EBbW1vSFh8fjxUrViAtLQ1t27ZFgwYNCiUkERERERERUXEkd9Hdp08faGlp4Y8//gDwcVK1OnXq4P3797CxscH8+fOxe/dutGrVqtDCEhERERERERUnci8ZdvbsWXTs2FHy/bp165CTk4P79+/j2rVrCA0NxezZswslJBEREREREVFxJHfR/fz5czg5OUm+P3r0KDp27AhjY2MAQEBAAG7duqX8hERERERERETFlNxFt46ODjIyMiTfX7hwAR4eHlLb3717p9x0RERERERERMWY3EW3m5sb1q9fDwA4ffo04uPj4e3tLdn+8OFD2NraKj8hERERERERUTEl90RqEyZMQMuWLbF161a8fPkSgYGBsLGxkWzftWsXvLy8CiUkERERERERUXGk0DrdV65cweHDh2FtbY3OnTtLbXdzc0PdunWVHpCIiIiIiIiouJK76AYAV1dXuLq65rmtb9++SglEREREREREVFLIXXQvWrQoz3ZjY2N899138PT0VFooIiIiIiIiopJA7qJ7/vz5ebYnJSUhOTkZ9evXx549e1CmTBmlhSMiIiIiIiIqzuSevfzx48d5fr19+xYPHjyAWCzGr7/+WphZiYiIiIiIiIoVuYvuglSoUAG///47Dh06pIzDEREREREREZUISim6AcDe3h5xcXHKOhwRERERERFRsae0ovvGjRsoX768sg5HREREREREVOzJPZFaSkpKnu3JycmIjIzE8OHDERAQoLRgRERERERERMWd3EW3iYkJRCJRnttEIhF69+6NMWPGKC0YERERERERUXEnd9F9/PjxPNuNjIzg5OQEAwMDpYUiIiIiIiIiKgnkLrobN25cmDmIiIiIiIiIShy5JlKLjY1V6KDPnz//qjBEREREREREJYlcRXedOnXQr18/XL58Od8+ycnJ+PPPP1G1alXs2LFDrgfPycnB+PHj4ejoCF1dXVSsWBG//fYbBEGQ9BEEARMmTICNjQ10dXXh4+OD+/fvf/HYS5cuhYODA3R0dODh4YFLly5JbX///j0GDhwIMzMzGBgYoGPHjoiPj5fqExsbC39/f+jp6cHS0hIjR45Edna2XM+NiIiIiIiISK7h5dHR0Zg2bRqaN28OHR0duLu7w9bWFjo6Onj79i2io6Nx69Yt1KpVC7NmzUKrVq3kevCZM2di+fLlWLt2LapUqYIrV64gKCgIxsbGCAkJAQDMmjULixYtwtq1a+Ho6Ijx48fDz88P0dHR0NHRyfO4W7ZsQWhoKFasWAEPDw8sWLAAfn5+uHv3LiwtLQEAw4YNw/79+7Ft2zYYGxtj0KBB6NChA86ePQvg4wcC/v7+sLa2xrlz5/Dy5Uv07NkTmpqamD59ulzPj4iIiIiIiEo3kfDpZeUvyMjIwP79+3HmzBk8efIEGRkZMDc3R82aNeHn54eqVasq9OCtW7eGlZUVVq9eLWnr2LEjdHV1sWHDBgiCAFtbWwwfPhwjRowA8PGKupWVFdasWYNu3brleVwPDw/UqVMHS5YsAQCIxWLY2dlh8ODBGDNmDJKTk2FhYYGNGzeiU6dOAIA7d+7AxcUF58+fR7169XDgwAG0bt0aL168gJWVFQBgxYoVGD16NF6/fg0tLa0vPr+UlBQYGxsjOTkZRkZGCr0234poct4z0hMJE+V+ayAiIiIiKnXkrffkGl6eS1dXF506dcKCBQuwa9cuREREYMOGDRg+fLjCBTcA1K9fH0ePHsW9e/cAANeuXcOZM2fQsmVLAMDjx48RFxcHHx8fyT7Gxsbw8PDA+fPn8zzmhw8fEBkZKbWPmpoafHx8JPtERkYiKytLqo+zszPs7e0lfc6fP49q1apJCm4A8PPzQ0pKCm7duqXwcyUiIiIiIqLSR+7ZywvDmDFjkJKSAmdnZ6irqyMnJwfTpk1Djx49AABxcXEAIFX45n6fu+1zCQkJyMnJyXOfO3fuSI6rpaUFExOTfI8bFxeX5zE+zfW5zMxMZGZmSr5PSUnJ97kTERERERFRyafQlW5l27p1K8LDw7Fx40ZERUVh7dq1mDNnDtauXavKWF9txowZMDY2lnzZ2dmpOhIRERERERGpkEqL7pEjR2LMmDHo1q0bqlWrhp9++gnDhg3DjBkzAADW1tYAIDOreHx8vGTb58zNzaGurl7gPtbW1vjw4QOSkpIK7JPXMT7N9bmxY8ciOTlZ8vX06dMvvQRERERERERUgqm06E5PT4eamnQEdXV1iMViAICjoyOsra1x9OhRyfaUlBRcvHgRnp6eeR5TS0sL7u7uUvuIxWIcPXpUso+7uzs0NTWl+ty9exexsbGSPp6enrhx4wZevXol6XP48GEYGRnB1dU1z8fW1taGkZGR1BcRERERERGVXiq9p7tNmzaYNm0a7O3tUaVKFVy9ehXz5s1Dr169AAAikQhDhw7F1KlT4eTkJFkyzNbWFu3bt8/3uKGhoQgICEDt2rVRt25dLFiwAGlpaQgKCgLwcTK24OBghIaGokyZMjAyMsLgwYPh6emJevXqAQB8fX3h6uqKn376CbNmzUJcXBx+/fVXDBw4ENra2oX+2hAREREREVHxJ1fRvWfPHrkP2LZtW7n7Ll68GOPHj8eAAQPw6tUr2Nraol+/fpgwYYKkz6hRo5CWloa+ffsiKSkJDRo0QEREhNQa3U2aNIGDgwPWrFkDAOjatStev36NCRMmIC4uDm5uboiIiJCaGG3+/PlQU1NDx44dkZmZCT8/PyxbtkyyXV1dHfv27UP//v3h6ekJfX19BAQEYMqUKXI/PyIiIiIiIird5Fqn+/Mh4CKRCJ/uJhL9b63nnJwcJcaTT/ny5TF58mQEBgZ+88cuCNfppuKM63QTEREREeVPqet0i8ViydehQ4fg5uaGAwcOICkpCUlJSfjnn39Qq1YtREREKO0JyOvWrVswNjZGz549v/ljExERERERERVE4Xu6hw4dihUrVqBBgwaSNj8/P+jp6aFv3764ffu2UgN+SZUqVXD9+vVv+phERERERERE8lB49vKHDx/CxMREpt3Y2BgxMTFKiERERERERERUMihcdNepUwehoaFSa1jHx8dj5MiRqFu3rlLDERERERERERVnChfdf/31F16+fAl7e3tUqlQJlSpVgr29PZ4/f47Vq1cXRkYiIiIiIiKiYknhe7orVaqE69ev4/Dhw7hz5w4AwMXFBT4+PlKzmBMRERERERGVdgoX3cDHJcJ8fX3RqFEjaGtrs9gmIiIiIiIiyoPCw8vFYjF+++03lC1bFgYGBnj8+DEAYPz48RxeTkRERERERPQJhYvuqVOnYs2aNZg1axa0tLQk7VWrVsWqVauUGo6IiIiIiIioOFO46F63bh1WrlyJHj16QF1dXdJeo0YNyT3eRERERERERPQVRffz589RqVIlmXaxWIysrCylhCIiIiIiIiIqCRQuul1dXXH69GmZ9u3bt6NmzZpKCUVERERERERUEig8e/mECRMQEBCA58+fQywWY+fOnbh79y7WrVuHffv2FUZGIiIiIiIiomJJ4Svd7dq1w969e3HkyBHo6+tjwoQJuH37Nvbu3YvmzZsXRkYiIiIiIiKiYumr1ulu2LAhDh8+rOwsRERERERERCWKwle6K1SogDdv3si0JyUloUKFCkoJRURERERERFQSKFx0x8TEICcn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iIiIiIiKna+eSE1DQwMdOnTAtm3bMHPmTDx48AAjRoyAnZ0devbsiZcvXyozJxEREREREVGx89VF95UrVzBgwADY2Nhg3rx5GDFiBB4+fIjDhw/jxYsXaNeunTJzEhERERERERU7GoruMG/ePISFheHu3bto1aoV1q1bh1atWkFN7WP97ujoiDVr1sDBwUHZWYmIiIhIQaLJIlVHoCJKmCioOgJRqaBw0b18+XL06tULgYGBsLGxybOPpaUlVq9e/Z/DERERERERERVnChfd9+/f/2IfLS0tBAQEfFUgIiIiIiIiopLiq+7pPn36NH788Ud4enri+fPnAID169fjzJkzSg1HREREREREVJwpXHTv2LEDfn5+0NXVxdWrV5GZmQkASE5OxvTp05UekIiIiIiIiKi4Urjonjp1KlasWIE///wTmpqaknYvLy9ERUUpNRwRERERERFRcaZw0X337l00atRIpt3Y2BhJSUnKyERERERERERUIihcdFtbW+PBgwcy7WfOnEGFChWUEoqIiIiIiIioJFC46O7Tpw+GDBmCixcvQiQS4cWLFwgPD8eIESPQv3//wshIREREREREVCwpvGTYmDFjIBaL0axZM6Snp6NRo0bQ1tbGiBEjMHjw4MLISERERERERFQsKVx0i0QijBs3DiNHjsSDBw/w7t07uLq6wsDAoDDyERERERERERVbChfdubS0tODq6qrMLEREREREREQlisJFd1paGn7//XccPXoUr169glgsltr+6NEjpYUjIiIiIiIiKs4ULrp79+6NkydP4qeffoKNjQ1EIlFh5CIiIiIiIiIq9hQuug8cOID9+/fDy8urMPIQERERERERlRgKLxlmamqKMmXKFEYWIiIiIiIiohJF4aL7t99+w4QJE5Cenl4YeYiIiIiIiIhKDIWHl8+dOxcPHz6ElZUVHBwcoKmpKbU9KipKaeGIiIiIiIiIijOFi+727dsXQgwiIiIiIiKikkfhonvixImFkYOIiIiIiIioxFH4nu5ckZGR2LBhAzZs2ICrV6/+5yC///47RCIRhg4dKml7//49Bg4cCDMzMxgYGKBjx46Ij48v8DiCIGDChAmwsbGBrq4ufHx8cP/+fak+iYmJ6NGjB4yMjGBiYoLg4GC8e/dOqs/169fRsGFD6OjowM7ODrNmzfrPz5GIiIiIiIhKF4WL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Ozg4GIcOHUKnTp1Qt25diESiwshFREREREREVOwpXHTv27cP//zzD7y8vAojDxEREREREVGJofCSYWXLluV63ERERERERERyULjonjt3LkaPHo0nT54URh4iIiIiIiKiEkPh4eW1a9fG+/fvUaFCBejp6UFTU1Nqe2JiotLCERERERERERVnChfd3bt3x/PnzzF9+nRYWVlxIjUiIiIiIiKifChcdJ87dw7nz59HjRo1CiMPERERERERUYmh8D3dzs7OyMjIKIwsRERERERERCWKwkX377//juHDh+PEiRN48+YNUlJSpL6IiIiIiIiI6COFh5e3aNECANCsWTOpdkEQIBKJkJOTo5xkRERERERERMWcwkX38ePHCyMHERERERERUYmjcNHduHHjfLfdvHnzP4UhIiIiIiIiKkkUvqf7c6mpqVi5ciXq1q3LGc2JiIiIiIiIPvHVRfepU6cQEBAAGxsbzJkzB97e3rhw4YIysxEREREREREVawoNL4+Li8OaNWuwevVqpKSkoEuXLsjMzMTff/8NV1fXwspIREREREREVCzJfaW7TZs2qFy5Mq5fv44FCxbgxYsXWLx4cWFmIyIiIiIiIirW5L7SfeDAAYSEhKB///5wcnIqzExEREREREREJYLcV7rPnDmD1NRUuLu7w8PDA0uWLEFCQkJhZiMiIiIiIiIq1uQuuuvVq4c///wTL1++RL9+/bB582bY2tpCLBbj8OHDSE1NLcycRERERERERMWOwrOX6+vro1evXjhz5gxu3LiB4cOH4/fff4elpSXatm1bGBmJiIiIiIiIiqX/tE535cqVMWvWLDx79gybNm1SViYiIiIiIiKiEuE/Fd251NXV0b59e+zZs0cZhyMiIiIiIiIqEZRSdJdkS5cuhYODA3R0dODh4YFLly6pOhIREREREREVEyy6C7BlyxaEhoZi4sSJiIqKQo0aNeDn54dXr16pOhoREREREREVAyy6CzBv3jz06dMHQUFBcHV1xYoVK6Cnp4e//vpL1dGIiIiIiIioGNBQdYCi6sOHD4iMjMTYsWMlbWpqavDx8cH58+fz3CczMxOZmZmS75OTkwEAKSkphRv2v3iv6gBUVBWZ85bnKOWD5ygVdTxHqajjOUpFXZE5R/ORm08QhAL7sejOR0JCAnJycmBlZSXVbmVlhTt37uS5z4wZMzB5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Vav09ttva+TIkapTp46KFClic97X19dQGQDkDUlJSQoKCrrnqjfyPoZuuCQGGji71157TbNmzVK7du1UunTpHH8Yf/LJJ4bKgN+5ubll//q//ztqtVplsVh4TzcA3MemTZvueb5Ro0a5VAJHYiM1uKT+/ftnDzQ1atTg00U4nQULFmjRokVq27at6RTgruLi4kwnAECe1qRJkxzH/vvvpXx4mT8wdMMlMdDA2bm7u6tixYqmM4B7aty48V3P7d+/PxdLACBvunjxos336enp2r17t959912NGjXKUBXsze3+lwD5DwMNnN2gQYM0YcIE8QQQ8pIrV65o2rRpqlevnmrXrm06BwCcnp+fn81XQECAWrZsqQ8//FBvvPGG6TzYCc90wyWNGzdOCQkJmjx5MreWwyl16NBBcXFxKlasmKpXr579arvfLF261FAZkNOmTZs0Y8YMLVmyRIGBgerYsaP+8Y9/qG7duqbTACBPOnz4sMLCwnT16lXTKbADbi+HS9q8ebPi4uL03XffMdDAKRUtWlQdOnQwnQHc1ZkzZzRr1izNmDFDly9fVqdOnZSWlqavv/5a1apVM50HAHnCf/7zH5vvrVarTp8+rbFjx+rRRx81EwW7Y6UbLqlbt273PB8TE5NLJQCQ97Rv316bNm1Su3btFBERoTZt2qhAgQIqVKiQ9u7dy9ANAA/Izc1NFoslx+Nk9evX18yZM1WlShVDZbAnhm4AAPCnFCxYUP369VOfPn1UqVKl7OMM3QDw5yQlJdl87+bmpuLFi6tw4cKGiuAI3F4OAE5q8eLFWrRokZKTk3Xr1i2bc7t27TJUBdx+RGfGjBmqU6eOqlatqi5duqhz586mswAgzwkODjadgFzA7uVwWYsXL1anTp1Uv359PfbYYzZfgGkTJ05Ut27dVLJkSe3evVv16tXTQw89pISEBD399NOm8+Di6tevry+++EKnT59W7969tWDBAgUGBiorK0tr167VlStXTCcCQJ7Qr18/TZw4McfxyZMna8CAAbkfBIdg6IZLYqCBs/vss880bdo0TZo0Se7u7nrjjTe0du1a9evXT7/++qvpPECSVKRIEXXv3l2bN2/Wvn37NGjQII0dO1YlSpTQs88+azoPAJzekiVL1KBBgxzHn3zySS1evNhAERyBoRsuiYEGzi45OVlPPvmkJMnT0zN75bBL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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.ticker import FuncFormatter\n",
    "\n",
    "#change type of Amount column\n",
    "df_bipart['Amount'] = pd.to_numeric(df_bipart['Amount'], errors='coerce')\n",
    "\n",
    "\n",
    "# Step 1: Extract Data\n",
    "# Replace these with your actual DataFrame columns\n",
    "top_5_owners_bipart = df_bipart.groupby('Owner')['Amount'].sum().nlargest(5)\n",
    "\n",
    "# Step 2: Create the Plot\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(top_5_owners_bipart.index, top_5_owners_bipart.values, color='green')\n",
    "\n",
    "#add text to amount donated by the highest donor\n",
    "plt.text(0, top_5_owners_bipart.values[0], f'{top_5_owners_bipart.values[0]:,.0f}', \n",
    "         ha='center', va='bottom', fontsize=12, color='black')\n",
    "\n",
    "\n",
    "\n",
    "# Step 3: Rotate x-axis labels\n",
    "plt.xticks(rotation=90)\n",
    "\n",
    "# Step 4: Add Title and Labels\n",
    "plt.title('Top 5 American Sport Team Donors for the Bipartisan Party (2016-2020)')  # Title of the plot\n",
    "plt.xlabel('Owners')  # Label for x-axis\n",
    "plt.ylabel('Amount of Money Donated (USD)')  # Label for y-axis\n",
    "\n",
    "# Step 5: Optional - Add Gridlines\n",
    "# Uncomment the following line if you want to add gridlines\n",
    "# plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7)\n",
    "\n",
    "# Step 6: Adjust Layout\n",
    "plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))\n",
    "plt.tight_layout()  # Adjust layout to avoid overlap\n",
    "\n",
    "# Step 7: Show the Plot\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5. Analysis and Conclusion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### From the above analysis, the data shows that the Party with the most money donated from 2016-2020 by the owners of American professional sport teams is the Republican Party with $34,246,016 donated! The Democratic Party received $10,113,639 and the Bipartisan Party received only $1474699. This data shows that the both the Republican and Democratic Parties receive significant donations from Professional Sport Team owners in America and the Bipartisan does not have much support. Also, something I found interesting was the top donor for the Republican Party, \"Charles Johnson\" because of how much more he donated in comparison to the other Republican Party supporters. He was a big outlier in the Republican Party dataset and being able to see it displayed in the bar graph really highlighted that. In conclusion, this project was really fun and challenging! Although I wish I would have chosen a dataset that I found a little more interesting, it was really fun trying to figure things out and find answers to each step along the way. I am looking forward to the next project."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
