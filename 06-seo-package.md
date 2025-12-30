# EPYC Courier Service — Complete SEO Package

---

## PAGE TITLES & META DESCRIPTIONS

### Homepage
```html
<title>EPYC Courier Service | 24/7 Same-Day Delivery | Los Angeles & Southern California</title>
<meta name="description" content="Southern California's trusted same-day courier service. Medical specimen delivery, legal documents, commercial packages. HIPAA compliant, GPS tracking, proof of delivery. Call (818) 217-0070.">
```

### Medical Courier Page
```html
<title>Medical Courier Service Los Angeles | HIPAA Compliant Specimen Delivery | EPYC</title>
<meta name="description" content="HIPAA compliant medical courier in Los Angeles & Southern California. Laboratory specimen transport, pharmaceutical delivery, medical equipment. STAT delivery within 60 minutes. Call (818) 217-0070.">
```

### Legal Courier Page
```html
<title>Legal Courier Service Los Angeles | Court Filing & Document Delivery | EPYC</title>
<meta name="description" content="Legal courier service in Los Angeles & Southern California. Court filings, process serving, attorney document delivery. We know every courthouse. Rush service available. Call (818) 217-0070.">
```

### Commercial Delivery Page
```html
<title>Commercial Courier Service Los Angeles | Same-Day Business Delivery | EPYC</title>
<meta name="description" content="Commercial courier and same-day business delivery in Los Angeles & Southern California. Packages, documents, prototypes, bank deposits. GPS tracking. Call (818) 217-0070.">
```

### About Us Page
```html
<title>About EPYC Courier Service | Los Angeles Same-Day Delivery Company</title>
<meta name="description" content="Learn about EPYC Courier Service — Southern California's trusted same-day delivery company. Professional drivers, HIPAA compliant, 24/7 service. Serving LA, Orange County, and San Diego.">
```

### Contact Page
```html
<title>Contact EPYC Courier Service | Get a Quote | (818) 217-0070</title>
<meta name="description" content="Contact EPYC Courier Service for same-day delivery in Los Angeles & Southern California. Request a quote online or call (818) 217-0070. 24/7 emergency service available.">
```

### Service Areas - Los Angeles
```html
<title>Los Angeles Courier Service | Same-Day Delivery LA | EPYC Courier</title>
<meta name="description" content="Same-day courier service in Los Angeles. Medical, legal, and commercial delivery throughout LA County. Downtown, Hollywood, Westside, Valley, and more. Call (818) 217-0070.">
```

### Service Areas - Orange County
```html
<title>Orange County Courier Service | Same-Day Delivery OC | EPYC Courier</title>
<meta name="description" content="Same-day courier service in Orange County. Medical, legal, and commercial delivery. Anaheim, Irvine, Santa Ana, Newport Beach. Call (818) 217-0070.">
```

### Service Areas - San Diego
```html
<title>San Diego Courier Service | Same-Day Delivery SD | EPYC Courier</title>
<meta name="description" content="Same-day courier service in San Diego County. Medical, legal, and commercial delivery. Downtown SD, La Jolla, North County. Call (818) 217-0070.">
```

---

## SCHEMA.ORG STRUCTURED DATA

### LocalBusiness Schema (Homepage)
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://epyccs.com/#organization",
  "name": "EPYC Courier Service",
  "alternateName": "EPYC CS",
  "description": "Southern California's trusted same-day courier service specializing in medical, legal, and commercial delivery.",
  "url": "https://epyccs.com",
  "telephone": "(818) 217-0070",
  "email": "admin@epyccs.com",
  "image": "https://epyccs.com/images/epyc-logo.png",
  "logo": "https://epyccs.com/images/epyc-logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "",
    "addressLocality": "Los Angeles",
    "addressRegion": "CA",
    "postalCode": "",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 34.0522,
    "longitude": -118.2437
  },
  "areaServed": [
    {
      "@type": "County",
      "name": "Los Angeles County"
    },
    {
      "@type": "County",
      "name": "Orange County"
    },
    {
      "@type": "County",
      "name": "San Diego County"
    },
    {
      "@type": "County",
      "name": "Riverside County"
    },
    {
      "@type": "County",
      "name": "San Bernardino County"
    }
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
      "opens": "00:00",
      "closes": "23:59"
    }
  ],
  "priceRange": "$$",
  "paymentAccepted": ["Cash", "Credit Card", "Invoice"],
  "currenciesAccepted": "USD",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Courier Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Medical Courier Service",
          "description": "HIPAA compliant medical specimen and pharmaceutical delivery"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Legal Courier Service",
          "description": "Court filing and legal document delivery"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Commercial Delivery",
          "description": "Same-day business package delivery"
        }
      }
    ]
  },
  "sameAs": [
    "https://www.facebook.com/epyccs",
    "https://www.instagram.com/epyccs",
    "https://www.linkedin.com/company/epyccs",
    "https://www.yelp.com/biz/epyc-courier-service"
  ]
}
```

### Service Schema (for each service page)
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Medical Courier Service",
  "provider": {
    "@type": "LocalBusiness",
    "name": "EPYC Courier Service",
    "telephone": "(818) 217-0070"
  },
  "areaServed": {
    "@type": "State",
    "name": "California"
  },
  "description": "HIPAA compliant medical specimen transport, pharmaceutical delivery, and medical equipment courier service.",
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "priceSpecification": {
      "@type": "PriceSpecification",
      "priceCurrency": "USD"
    }
  }
}
```

### FAQ Schema (for FAQ sections)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What areas does EPYC Courier Service cover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "EPYC Courier Service covers all of Southern California including Los Angeles County, Orange County, San Diego County, and the Inland Empire (Riverside and San Bernardino Counties)."
      }
    },
    {
      "@type": "Question",
      "name": "Is EPYC Courier Service HIPAA compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, EPYC Courier Service is fully HIPAA compliant. Our medical courier drivers are trained in HIPAA and OSHA protocols for safe handling of medical specimens and protected health information."
      }
    },
    {
      "@type": "Question",
      "name": "How fast can EPYC deliver?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "EPYC offers STAT delivery within 60 minutes, Rush delivery in 1-2 hours, and Same-Day delivery within 4 hours. 24/7 emergency service is available."
      }
    },
    {
      "@type": "Question",
      "name": "Does EPYC offer real-time tracking?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, all EPYC deliveries include real-time GPS tracking, ETA updates, and proof of delivery with signature capture and photo confirmation."
      }
    }
  ]
}
```

---

## TARGET KEYWORDS BY PAGE

### Homepage (Primary)
- courier service los angeles
- same day delivery southern california
- los angeles courier
- southern california courier service
- 24/7 courier service

### Homepage (Secondary)
- rush delivery los angeles
- on demand courier la
- package delivery same day
- local courier service

### Medical Courier (Primary)
- medical courier los angeles
- HIPAA compliant courier
- laboratory specimen delivery
- medical specimen transport
- pharmaceutical courier

### Medical Courier (Secondary)
- stat medical delivery
- hospital courier service
- lab courier los angeles
- medical delivery service

### Legal Courier (Primary)
- legal courier los angeles
- court filing service
- process serving los angeles
- legal document delivery
- attorney courier service

### Legal Courier (Secondary)
- court runner los angeles
- legal messenger service
- same day court filing
- document service los angeles

### Commercial (Primary)
- commercial courier los angeles
- business delivery service
- same day package delivery
- corporate courier service
- on demand delivery la

---

## OPEN GRAPH & SOCIAL TAGS

```html
<!-- Facebook / Open Graph -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://epyccs.com/">
<meta property="og:title" content="EPYC Courier Service | 24/7 Same-Day Delivery">
<meta property="og:description" content="Southern California's trusted same-day courier service. Medical, legal, and commercial delivery. HIPAA compliant. Call (818) 217-0070.">
<meta property="og:image" content="https://epyccs.com/images/epyc-social-share.jpg">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="https://epyccs.com/">
<meta name="twitter:title" content="EPYC Courier Service | 24/7 Same-Day Delivery">
<meta name="twitter:description" content="Southern California's trusted same-day courier service. Medical, legal, and commercial delivery.">
<meta name="twitter:image" content="https://epyccs.com/images/epyc-social-share.jpg">
```

---

## TECHNICAL SEO CHECKLIST

### Must-Have:
- [ ] SSL Certificate (HTTPS)
- [ ] Mobile-responsive design
- [ ] Fast page load speed (<3 seconds)
- [ ] XML sitemap submitted to Google
- [ ] Google Business Profile claimed & optimized
- [ ] Yelp Business Page created
- [ ] Schema markup implemented
- [ ] Alt text on all images
- [ ] Clean URL structure
- [ ] 404 error page

### Google Business Profile Optimization:
- [ ] Accurate business name
- [ ] Phone number: (818) 217-0070
- [ ] Service area defined (LA, OC, SD, IE)
- [ ] Business categories: Courier Service, Delivery Service, Medical Courier
- [ ] Business hours: 24/7
- [ ] Photos uploaded (vehicles, team, deliveries)
- [ ] Services listed with descriptions
- [ ] Regular posts with updates
- [ ] Respond to all reviews

---

## CONTENT CALENDAR (Blog Ideas)

### Month 1:
1. "How to Choose a Medical Courier Service in Los Angeles"
2. "Understanding HIPAA Compliance for Medical Deliveries"
3. "Court Filing Deadlines: What Every Paralegal Should Know"

### Month 2:
1. "Same-Day Delivery: How It Works in Southern California"
2. "Medical Specimen Transport: Chain of Custody Explained"
3. "Top 5 Questions to Ask Your Courier Service"

### Month 3:
1. "Legal Courier vs. Process Server: What's the Difference?"
2. "Why Your Business Needs a Reliable Courier Partner"
3. "LA Traffic Tips: How Professional Couriers Beat the Clock"

---

## LOCAL CITATIONS TO BUILD

### Priority Directories:
1. Google Business Profile
2. Yelp
3. Apple Maps
4. Bing Places
5. Facebook Business
6. LinkedIn Company Page
7. Yellow Pages
8. Foursquare/Swarm
9. MapQuest
10. Better Business Bureau

### Industry-Specific:
1. Expertise.com
2. Clutch.co
3. Thumbtack
4. Bark.com
5. HomeAdvisor (for local services)
