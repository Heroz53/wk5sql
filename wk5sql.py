from tabulate import tabulate

# Data for the comparison table
data = [
    ["MySQL", "Open-Source", "Small to medium-sized businesses, startups, developers",
     "Widely used, strong community support, fast read operations, support for replication",
     "Easy to set up and use, large community and resources"],
    
    ["PostgreSQL", "Open-Source", "Enterprises, data analysts, developers",
     "Advanced SQL compliance, extensible, support for JSON and XML, strong ACID compliance",
     "Moderate learning curve, robust documentation"],
    
    ["Microsoft SQL Server", "Commercial", "Enterprises, businesses requiring integration with Microsoft products",
     "High performance, integration with Microsoft ecosystem, strong BI tools, excellent support",
     "Relatively easy for users familiar with Microsoft products, comprehensive support"],
    
    ["Oracle Database", "Commercial", "Large enterprises, financial institutions, businesses requiring high security and reliability",
     "High availability, scalability, advanced security features, robust transaction management",
     "Complex setup, steep learning curve, extensive support"],
    
    ["Node.js", "Open-Source (JavaScript runtime, not a traditional database server)",
     "Web developers, startups, companies building scalable network applications",
     "Non-blocking I/O, event-driven architecture, npm ecosystem, real-time capabilities",
     "Easy for JavaScript developers, requires understanding of asynchronous programming"]
]

# Headers for the table
headers = ["Database Server", "Type", "Target Audience", "Key Features", "Ease of Use"]

# Print the table
print(tabulate(data, headers, tablefmt="github"))
