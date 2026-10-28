\# Literature Review



\## Paper 1: Challenges and Solutions for Sustainable ICT: The Role of File Storage



\*\*Authors:\*\* L. Mersico, H. Abroshan, E. Sanchez-Velazquez, et al.  

\*\*Year:\*\* 2024  

\*\*Journal:\*\* Sustainability  

\*\*Volume:\*\* 16  

\*\*Issue:\*\* 18  

\*\*Article Number:\*\* 8043  



\### 1. Objective

The paper discusses the challenges of achieving sustainability in Information and Communication Technology (ICT), focusing on the role of file storage.



\### 2. Problem Addressed

The increasing amount of digital data creates challenges related to storage requirements, resource consumption, and sustainability. Efficient file storage is important for reducing the environmental impact of ICT systems.



\### 3. Proposed Approach

The paper examines sustainability challenges associated with ICT and discusses potential solutions, emphasizing the importance of file storage practices in improving sustainability.



\### 4. Key Contribution

The paper highlights the relationship between file storage and sustainable ICT. It provides background for understanding why efficient storage management is important.



\### 5. Limitations

The PPT's literature review entry does not specify the paper's exact limitations. These must be verified from the full research paper before being stated.



\### 6. Relevance to Our Project

Our project, \*An Integrated Distributed Framework for Automated Lifecycle Classification and Redundancy Mitigation in Large-Scale Repositories\*, focuses on identifying digital waste and improving storage efficiency. This paper provides sustainability-related background for our project.



\### 7. Research Gap

The PPT's entry does not establish a specific research gap for this paper. We need to examine the full paper before identifying any gap it leaves unresolved.



\### 8. Reference

Mersico, L., Abroshan, H., Sanchez-Velazquez, E., et al. (2024). Challenges and Solutions for Sustainable ICT: The Role of File Storage. \*Sustainability, 16\*(18), Article 8043.



\## Paper 2: Deep Contrastive Learning-Based Redundancy Elimination for Similar Data in Cloud Storage Systems



\*\*Authors:\*\* Ling Xiao, Qinbao Fang, and Shihao Feng  

\*\*Year:\*\* 2026  

\*\*Journal:\*\* Journal of King Saud University – Computer and Information Sciences  

\*\*Volume:\*\* 38  

\*\*Article Number:\*\* 607  

\*\*DOI:\*\* 10.1007/s44443-026-01042-5



\### 1. Objective

The paper aims to improve redundancy elimination in cloud storage by accurately identifying similar data blocks and improving storage efficiency.



\### 2. Problem Addressed

Traditional redundancy-elimination techniques may struggle to identify similar data blocks when their contents contain small modifications. Computational overhead from similarity searches can also reduce processing efficiency.



\### 3. Proposed Approach

The authors propose DCLC, a deep contrastive learning-based redundancy-elimination method. It uses a Transformer-based context-aware model to learn data-block representations, a locality-aware caching mechanism to reduce repeated searches, and multi-reference delta encoding to exploit redundancy across similar blocks.



\### 4. Key Contribution

The paper combines context-aware similarity detection, efficient candidate retrieval, and multi-reference delta encoding. In the evaluated workloads, the authors report throughput improvements of 4.18× to 59.58× and a maximum 248% improvement in overall compression ratio compared with representative existing approaches.



\### 5. Limitations and Future Work

The authors identify the need for more memory-efficient embedding indexes and vector-retrieval mechanisms as an area for future work. The reported results should be interpreted in the context of the datasets and methods evaluated in the paper.



\### 6. Relevance to Our Project

This paper is relevant to our project because it investigates methods for reducing redundant data in cloud storage. Its redundancy-elimination approach can be compared with our proposed framework, which combines lifecycle classification with redundancy mitigation.



\### 7. Research Gap

DCLC focuses on identifying similar data blocks and eliminating redundancy. Our project additionally aims to classify data according to its lifecycle and identify potentially obsolete data. This creates a useful comparison between specialized redundancy elimination and an integrated lifecycle-management framework.



\### 8. Reference

Xiao, L., Fang, Q., \& Feng, S. (2026). Deep contrastive learning-based redundancy elimination for similar data in cloud storage systems. \*Journal of King Saud University – Computer and Information Sciences, 38\*, Article 607. https://doi.org/10.1007/s44443-026-01042-5



\## Paper 3: Cloud Storage Tier Optimization Through Storage Object Classification



\*\*Authors:\*\* Akif Quddus Khan, Mihhail Matskin, Radu Prodan, Christoph Bussler, Dumitru Roman, and Ahmet Soylu  

\*\*Year:\*\* 2024  

\*\*Journal:\*\* Computing  

\*\*Volume:\*\* 106  

\*\*Issue:\*\* 11  

\*\*Pages:\*\* 3389–3418  

\*\*DOI:\*\* 10.1007/s00607-024-01281-2



\### 1. Objective

The paper aims to optimize cloud storage costs by classifying storage objects and assigning them to suitable storage tiers according to their characteristics and access patterns.



\### 2. Problem Addressed

Keeping all data in a single storage tier may be inefficient because data objects have different access frequencies, sizes, and ages. An unsuitable storage tier can increase costs or affect data access performance.



\### 3. Proposed Approach

The authors propose two approaches: rule-based classification and game theory-based classification. Both approaches consider object size, access frequency, and age to determine suitable storage tiers. The four tiers are Premium, Hot, Cold, and Archive. The approaches are evaluated using fully synthetic and semi-synthetic datasets with static and dynamic access patterns.



\### 4. Key Contribution

The paper presents two lightweight, platform-independent approaches for cloud storage-tier optimization. The authors report that the approaches can substantially reduce storage costs while remaining computationally feasible.



\### 5. Limitations and Future Work

The authors identify further work in cost modelling, including network usage, data migration costs, and penalties for moving objects before minimum storage-duration requirements. They also propose evaluating additional Big Data and IoT workloads and developing a practical tool integrated with cloud storage APIs.



\### 6. Relevance to Our Project

This paper is relevant because it demonstrates how data characteristics and access patterns can guide automated storage-management decisions. Our project similarly uses data characteristics to classify lifecycle categories, but additionally focuses on identifying digital waste and mitigating redundancy.



\### 7. Research Gap

The paper focuses on classifying storage objects into tiers to optimize cloud storage costs. Our project extends the comparison to an integrated framework that combines lifecycle classification with redundancy mitigation. This distinction provides a basis for evaluating how the two approaches address different storage-management objectives.



\### 8. Reference

Khan, A. Q., Matskin, M., Prodan, R., Bussler, C., Roman, D., \& Soylu, A. (2024). Cloud storage tier optimization through storage object classification. \*Computing, 106\*(11), 3389–3418. https://doi.org/10.1007/s00607-024-01281-2



\## Paper 4: Unveiling Key Performance Indicators for the Energy Efficiency of Cloud Data Storage



\*\*Authors:\*\* Pouyeh Banijamali, Iffat Fatima, Patricia Lago, and Ilja Heitlager  

\*\*Year:\*\* 2024  

\*\*Conference:\*\* 2024 IEEE 21st International Conference on Software Architecture Companion (ICSA-C)  

\*\*Pages:\*\* 222–229  

\*\*DOI:\*\* 10.1109/ICSA-C63560.2024.00047



\### 1. Objective

The paper aims to identify measurable key performance indicators (KPIs) for monitoring and improving the energy efficiency of cloud data storage.



\### 2. Problem Addressed

Cloud providers may report overall data-centre energy efficiency without sufficient transparency about individual components and functions. This makes it difficult for organisations to evaluate and optimise the energy efficiency of their storage systems.



\### 3. Proposed Approach

The authors conducted an exploratory study with Schuberg Philis, an IT provider in the Netherlands. They examined cloud-provider data and metrics from academic literature, then developed three KPIs using an existing KPI framework and the organisation's sustainability roadmap. Experts from the organisation reviewed the proposed indicators.



\### 4. Key Contribution

The paper proposes three KPIs: energy consumption, storage capacity utilisation, and capacity per watt. It also identifies actions associated with these indicators to support organisational sustainability targets.



\### 5. Limitations and Future Work

The study was conducted in collaboration with one organisation, so its findings should be interpreted within that context. The work provides a foundation for developing similar approaches for other practitioners and sustainability settings.



\### 6. Relevance to Our Project

Our project aims to identify digital waste through lifecycle classification and redundancy mitigation. The proposed KPIs provide a potential basis for evaluating storage utilisation and sustainability. However, any energy-saving claims would require separate measurement or estimation.



\### 7. Research Gap

This paper focuses on measuring and monitoring the energy efficiency of cloud data storage. Our project instead focuses on automated lifecycle classification and redundancy mitigation. Comparing these approaches helps distinguish sustainability measurement from automated storage-management techniques.



\### 8. Reference

Banijamali, P., Fatima, I., Lago, P., \& Heitlager, I. (2024). Unveiling Key Performance Indicators for the Energy Efficiency of Cloud Data Storage. In \*Proceedings of the 2024 IEEE 21st International Conference on Software Architecture Companion (ICSA-C)\* (pp. 222–229). https://doi.org/10.1109/ICSA-C63560.2024.00047



\## Paper 5: To Store or Not: Online Cost Optimization for Running Big Data Jobs on the Cloud



\*\*Authors:\*\* Xiankun Fu, Li Pan, and Shijun Liu  

\*\*Year:\*\* 2024  

\*\*Journal:\*\* Future Generation Computer Systems  

\*\*Volume:\*\* 156  

\*\*Pages:\*\* 42–52  

\*\*DOI:\*\* 10.1016/j.future.2024.03.003



\### 1. Objective

The paper aims to reduce the cost of running big data jobs in cloud environments by deciding which intermediate data should be stored for potential reuse by subsequent jobs.



\### 2. Problem Addressed

Storing intermediate results can reduce repeated computation, but retaining unnecessary data increases storage costs. Existing storage strategies may fail to distinguish between data with different reuse patterns.



\### 3. Proposed Approach

The authors propose two online algorithms: SUM, a deterministic algorithm, and RSUM, a randomized algorithm. Both determine whether intermediate data should be stored without requiring prior knowledge of future workloads. The authors analyse their competitive ratios and evaluate their algorithms using big data workloads and an Alibaba Cloud environment.



\### 4. Key Contribution

The paper provides theoretical guarantees for its storage-decision algorithms and demonstrates their potential to reduce the cost of running cloud-based big data jobs under common pricing schemes.



\### 5. Limitations and Future Work

The approach focuses on online decisions about retaining intermediate results for reuse. Its stated scope does not establish a complete framework for repository-wide lifecycle classification and redundancy mitigation.



\### 6. Relevance to Our Project

This paper is relevant because it demonstrates how storage decisions can improve efficiency and reduce costs. Our project takes a broader approach by classifying data according to its lifecycle and combining classification with redundancy mitigation.



\### 7. Research Gap

The paper focuses on deciding whether intermediate data generated by big data jobs should be retained for reuse. Our project aims to integrate lifecycle classification and redundancy mitigation across large-scale repositories. This distinction provides a basis for comparing selective intermediate-data retention with broader automated data lifecycle management.



\### 8. Reference

Fu, X., Pan, L., \& Liu, S. (2024). To store or not: Online cost optimization for running big data jobs on the cloud. \*Future Generation Computer Systems, 156\*, 42–52. https://doi.org/10.1016/j.future.2024.03.003



\## Paper 6: Cloud Storage Cost: A Taxonomy and Survey



\*\*Authors:\*\* Akif Quddus Khan, Mihhail Matskin, Radu Prodan, Christoph Bussler, Dumitru Roman, and Ahmet Soylu

\*\*Year:\*\* 2024

\*\*Journal:\*\* World Wide Web

\*\*Volume:\*\* 27

\*\*Issue:\*\* 4

\*\*Article Number:\*\* 36

\*\*DOI:\*\* 10.1007/s11280-024-01273-4



\### 1. Objective

The paper aims to explain the complex cost structure of cloud storage and help organisations make informed decisions about cloud storage selection and cost optimisation.



\### 2. Problem Addressed

Cloud storage costs involve several components, including data storage, replication, transactions, and network usage. Different cloud providers have different pricing structures, making it difficult to compare services and select cost-effective storage options.



\### 3. Proposed Approach

The authors develop a taxonomy of cloud storage costs and examine quality-of-service factors that influence storage decisions. They analyse cost components, compare cloud providers under different scenarios, and discuss trade-offs involving storage, computation, caching, and network usage.



\### 4. Key Contribution

The paper presents a structured taxonomy of cloud storage costs and examines how cost, performance, availability, reliability, and security affect cloud storage selection and optimisation.



\### 5. Limitations and Future Work

The paper discusses challenges in existing cost-optimisation approaches, including limited practical implementation and evaluation in real-world scenarios. It highlights the need for flexible approaches that account for different user requirements and trade-offs between cost and quality of service.



\### 6. Relevance to Our Project

Our project aims to identify digital waste through lifecycle classification and redundancy mitigation. This paper provides background on the cost implications of storing and transferring data. Reducing unnecessary data may reduce storage requirements, although actual savings depend on the storage environment and associated processing costs.



\### 7. Research Gap

This paper focuses on cloud storage cost structures, cost trade-offs, and storage-provider selection. Our project focuses on automated lifecycle classification and redundancy mitigation. This provides a basis for comparing storage-cost analysis with an automated approach to managing unnecessary data.



\### 8. Reference

Khan, A. Q., Matskin, M., Prodan, R., Bussler, C., Roman, D., \& Soylu, A. (2024). Cloud storage cost: A taxonomy and survey. \*World Wide Web, 27\*(4), Article 36. https://doi.org/10.1007/s11280-024-01273-4



\## Paper 7: Leveraging Data Deduplication Approaches in the Cloud Storage: A Succinct Review



\*\*Authors:\*\* Anjuli Goel and Chander Prabha

\*\*Year:\*\* 2025

\*\*Journal:\*\* Procedia Computer Science

\*\*Volume:\*\* 259

\*\*Pages:\*\* 1640–1651

\*\*DOI:\*\* 10.1016/j.procs.2025.04.119



\### 1. Objective



The paper reviews data-deduplication approaches used in cloud storage, focusing particularly on indexing techniques for identifying duplicate data.



\### 2. Problem Addressed



Cloud storage systems handle increasing amounts of data, and duplicate copies can waste storage space and increase storage and network costs. Data deduplication helps identify redundant content and retain unique copies while supporting backup and storage management.



\### 3. Proposed Approach



The paper presents a review of existing data-deduplication techniques, with particular attention to indexing approaches. The deduplication process involves four main stages: chunking, fingerprinting, indexing, and writing. Indexing is particularly important because it helps identify matching data chunks.



\### 4. Key Contribution



The paper provides an overview of data-deduplication approaches in cloud storage and discusses indexing techniques used to identify redundant data. It explains how deduplication can help reduce storage requirements, data transfers, and energy consumption.



\### 5. Limitations and Future Work



The accessible abstract does not establish a specific list of limitations identified by the authors. The full paper must be examined before stating the authors' explicit limitations or future-work directions.



\### 6. Relevance to Our Project



Our project aims to identify digital waste through lifecycle classification and redundancy mitigation. This paper provides background on how duplicate data can be identified and removed. Deduplication complements lifecycle classification because the two techniques address different aspects of storage management.



\### 7. Research Gap



The paper reviews approaches for identifying duplicate data in cloud storage, particularly through indexing techniques. Our project aims to integrate lifecycle classification with redundancy mitigation in large-scale repositories. This provides a basis for comparing specialised deduplication techniques with an integrated data-lifecycle management framework.



\### 8. Reference



Goel, A., \& Prabha, C. (2025). Leveraging data deduplication approaches in the cloud storage: A succinct review. \*Procedia Computer Science, 259\*, 1640–1651. https://doi.org/10.1016/j.procs.2025.04.119



\## Paper 8: dualDup: A Secure and Reliable Cloud Storage Framework to Deduplicate the Encrypted Data and Key



\*\*Authors:\*\* Vikas Chouhan, Sateesh K. Peddoju, and Rajkumar Buyya

\*\*Year:\*\* 2022

\*\*Journal:\*\* Journal of Information Security and Applications

\*\*Volume:\*\* 69

\*\*Article Number:\*\* 103265

\*\*DOI:\*\* 10.1016/j.jisa.2022.103265



\### 1. Objective



The paper proposes dualDup, a cloud storage framework designed to eliminate duplicate encrypted data while maintaining the security and reliability of both data and encryption keys.



\### 2. Problem Addressed



Cloud storage providers cannot easily identify identical files when users upload encrypted data. Existing approaches also face reliability challenges when data and encryption keys depend on a single storage server.



\### 3. Proposed Approach



The authors combine DupLESS with erasure coding to support secure deduplication and reliability. The framework distributes data fragments and encryption-key fragments across separate storage servers. A Trusted Third Party helps coordinate deduplication and reduce unnecessary data transfers. The authors implement the framework in Python using a Dropbox data-centre environment and evaluate its security and performance.



\### 4. Key Contribution



The paper combines secure deduplication, data and key reliability, privacy protection, and storage recovery. The authors report an average storage overhead of 66.66% when using Reed–Solomon (3,2) coding and analyse protection against insider and outsider adversaries.



\### 5. Limitations



The paper focuses on secure deduplication and reliable storage of encrypted data and keys. Its stated scope does not establish a complete lifecycle-classification system for identifying active, rarely accessed, or potentially obsolete data.



\### 6. Relevance to Our Project



Our project aims to identify digital waste and mitigate redundancy through lifecycle classification and redundancy management. This paper provides a relevant example of deduplication combined with security and reliability mechanisms.



\### 7. Research Gap



The paper focuses on secure duplicate elimination and reliable storage of encrypted data and keys. Our project aims to integrate lifecycle classification with redundancy mitigation across large-scale repositories. This provides a basis for comparing secure deduplication with broader automated data-lifecycle management.



\### 8. Reference



Chouhan, V., Peddoju, S. K., \& Buyya, R. (2022). dualDup: A secure and reliable cloud storage framework to deduplicate the encrypted data and key. \*Journal of Information Security and Applications, 69\*, Article 103265. https://doi.org/10.1016/j.jisa.2022.103265





\## Paper 9: Data Deduplication and Integrity Check Scheme Based on Unique Tags in Edge Cloud Computing



\*\*Authors:\*\* Sevuga Pandian Asirvatham and Gomathi Muthusamy

\*\*Year:\*\* 2024

\*\*Journal:\*\* Ingénierie des Systèmes d’Information

\*\*Volume:\*\* 29

\*\*Issue:\*\* 6

\*\*Pages:\*\* 2197–2207

\*\*DOI:\*\* 10.18280/isi.290610



\### 1. Objective



The paper proposes a method for identifying and eliminating duplicate data in edge-cloud storage while checking data integrity and addressing security concerns.



\### 2. Problem Addressed



Edge-cloud environments may store duplicate data across distributed servers. Encryption can make deduplication more difficult, while resource-constrained edge servers make data processing and integrity verification challenging.



\### 3. Proposed Approach



The authors propose a scheme combining Threshold Similarity Measures (TSM), Cluster Index-Based Sliding Window Hashing (CISWH), Checksum Selective Indexing Chunking (CSIC), Prefetching Local Index Caching (PLIC), and Unique Tag Deduplication Integrity Check (UTDIC). These techniques support similarity detection, data segmentation, indexing, caching, duplicate verification, and integrity checking.



\### 4. Key Contribution



The paper combines edge-cloud deduplication with integrity verification. The authors report 97.9% precision, 98.8% recall, and 43.2% storage optimisation performance in their evaluation.



\### 5. Limitations and Future Work



The paper focuses on edge-cloud deduplication and integrity verification rather than a complete lifecycle-classification workflow. The authors identify improving deduplication performance through indexing as a direction for future work.



\### 6. Relevance to Our Project



Our project aims to identify digital waste through lifecycle classification and redundancy mitigation. This paper provides an example of combining duplicate detection with integrity checking, which is relevant to the redundancy-mitigation component of our framework.



\### 7. Research Gap



The paper focuses on deduplication and integrity verification in edge-cloud environments. Our project aims to integrate lifecycle classification with redundancy mitigation across large-scale repositories. This provides a basis for comparing secure duplicate detection with integrated data-lifecycle management.



\### 8. Reference



Asirvatham, S. P., \& Muthusamy, G. (2024). Data deduplication and integrity check scheme based on unique tags in edge cloud computing. \*Ingénierie des Systèmes d’Information, 29\*(6), 2197–2207. https://doi.org/10.18280/isi.290610





\## Paper 10: Cloud Storage Auditing and Data Sharing with Data Deduplication and Private Information Protection for Cloud-Based EMR



\*\*Authors:\*\* Jingze Yu, Wenting Shen, and Xi Zhang

\*\*Year:\*\* 2024

\*\*Journal:\*\* Computers \& Security

\*\*Volume:\*\* 144

\*\*Article Number:\*\* 103932

\*\*DOI:\*\* 10.1016/j.cose.2024.103932



\### 1. Objective



The paper proposes a cloud storage scheme that combines data deduplication, integrity auditing, and protection of patients' private information when electronic medical records (EMRs) are shared with researchers.



\### 2. Problem Addressed



Cloud-based medical records can contain duplicate data blocks, creating storage redundancy. Records may also be modified or deleted without the owner's knowledge, and sharing them can expose sensitive patient information. The proposed scheme aims to address redundancy, integrity, and privacy together.



\### 3. Proposed Approach



The scheme uses data blinding to conceal private information, a sanitizer to process records, and authenticator transformation to support integrity verification after sanitization. It also implements block-level deduplication so that duplicate data blocks need not be stored repeatedly. A Third-Party Auditor (TPA) checks record integrity, while proof-of-ownership mechanisms support deduplication verification.



\### 4. Key Contribution



The main contribution is integrating block-level deduplication with privacy-preserving data sharing and integrity auditing. The authors report that their security analysis and performance evaluation support the security and efficiency of the proposed scheme. No single numerical improvement percentage is stated here because it is not provided in the article's abstract.



\### 5. Limitations and Scope



The scheme focuses on cloud-based electronic medical records and secure data sharing. It does not provide a general lifecycle-classification system for identifying active, rarely accessed, or potentially obsolete files.



\### 6. Relevance to Our Project



Our project aims to combine automated data-lifecycle classification with redundancy mitigation in large-scale repositories. This paper provides a relevant example of integrating duplicate-block removal with other storage requirements, particularly data integrity and privacy.



\### 7. Research Gap



The paper focuses on secure medical-record sharing, privacy protection, integrity auditing, and deduplication. Our project aims to integrate redundancy mitigation with lifecycle-based storage decisions across large-scale repositories. This provides a basis for exploring storage-management methods that consider both redundancy and data lifecycle.



\### 8. Reference



Yu, J., Shen, W., \& Zhang, X. (2024). Cloud storage auditing and data sharing with data deduplication and private information protection for cloud-based EMR. \*Computers \& Security, 144\*, 103932. https://doi.org/10.1016/j.cose.2024.103932



\## Paper 11: Improving Anomaly Detection in the HDFS Dataset with Novel Machine Learning Models and Techniques



\*\*Authors:\*\* Mohammed Bekkouche and Sidi Mohammed Benslimane

\*\*Year:\*\* 2025

\*\*Journal:\*\* Computer Science Journal of Moldova

\*\*Volume:\*\* 33, Issue 3 (99)

\*\*Pages:\*\* 322–351

\*\*DOI:\*\* 10.56415/csjm.v33.16



\### 1. Objective



The paper investigates machine learning techniques for improving anomaly detection in Hadoop Distributed File System (HDFS) logs. It evaluates supervised and unsupervised methods on reduced and complete versions of the HDFS dataset.



\### 2. Problem Addressed



Existing supervised methods can perform poorly on the reduced HDFS dataset, while many unsupervised techniques struggle across both dataset versions. These differences motivate the development and evaluation of improved anomaly-detection approaches.



\### 3. Proposed Approach



The authors investigate Incremental Principal Component Analysis (IPCA), K-Means combined with Isolation Forest, an autoencoder combined with clustering, and a hybrid Support Vector Machine (SVM) and Decision Tree classifier. They also evaluate SMOTE for class imbalance, Word2Vec and TF-IDF feature representations, and temporal features based on time gaps between log entries.



\### 4. Key Findings



The study reports improved recall and F1-score from Incremental PCA compared with traditional PCA on the reduced dataset. The K-Means and Isolation Forest combination improves anomaly detection, while the autoencoder-plus-clustering approach achieves a recall of 1.0 on the complete HDFS dataset. The authors also report improvements from combining SVM and Decision Tree, using SMOTE, incorporating temporal features, and applying Word2Vec in several evaluated configurations.



\### 5. Limitations and Scope



The study focuses on anomaly detection in HDFS logs rather than storage lifecycle classification or redundancy mitigation. Its findings concern the evaluated datasets, feature representations, and anomaly-detection models.



\### 6. Relevance to Our Project



Our project focuses on automated lifecycle classification and redundancy mitigation in large-scale repositories. This paper provides relevant background on machine learning, feature engineering, and the analysis of distributed-system data. However, anomaly detection and lifecycle classification are different tasks.



\### 7. Research Gap



The paper concentrates on identifying anomalous HDFS log patterns. Our project aims to combine lifecycle classification with redundancy mitigation to support storage management. A potential research direction is to use repository metadata and access patterns to support lifecycle-aware storage decisions.



\### 8. Reference



Bekkouche, M., \& Benslimane, S. M. (2025). Improving anomaly detection in the HDFS dataset with novel machine learning models and techniques. \*Computer Science Journal of Moldova, 33\*(3), 322–351. https://doi.org/10.56415/csjm.v33.16



\## Paper 12: ADAPT: An Effective Data-Aware Multicloud Data Placement Framework



\*\*Authors:\*\* John Agyekum, Somnath Mazumdar, and Christoph Scheich

\*\*Year:\*\* 2025

\*\*Journal:\*\* Cluster Computing

\*\*Volume:\*\* 28

\*\*Article Number:\*\* 825

\*\*DOI:\*\* 10.1007/s10586-025-05546-z



\### 1. Objective



The paper proposes ADAPT (Adaptive Data Placement Framework), a machine learning-based framework designed to reduce storage costs and improve data availability across multiple cloud providers. It recommends storage locations based on data characteristics, access requirements, cloud pricing, latency, and user preferences.



\### 2. Problem Addressed



Multicloud storage management introduces challenges such as varying storage costs, vendor lock-in, data access latency, availability, and geographical storage restrictions. Inefficient data placement can increase costs and reduce application performance.



\### 3. Proposed Approach



The authors evaluate four classification models: Decision Tree, Random Forest, XGBoost, and Support Vector Machine (SVM). XGBoost performs best in their evaluation and is integrated into the ADAPT framework. The framework uses Apache Spark and Spring Boot and includes modules for monitoring data access, estimating storage costs, recommending data placement, and prefetching files.



\### 4. Key Findings



The authors report that XGBoost improves cost efficiency by 6.58%–24.26% in the evaluated scenarios. Their prototype demonstrates machine learning-based storage-placement recommendations across cloud providers. The framework also uses access patterns and geographical information to support data prefetching and availability.



\### 5. Limitations and Future Work



The authors identify the need to support additional storage options, including cold and archive tiers; consider inter-cloud data-transfer costs; develop more comprehensive training datasets; introduce monitoring and feedback mechanisms; and investigate security concerns in multicloud environments. The suitability of different ML models may also vary by scenario.



\### 6. Relevance to Our Project



Our project focuses on automated lifecycle classification and redundancy mitigation in large-scale repositories. ADAPT provides relevant evidence that machine learning can classify storage-related decisions using data characteristics and access requirements. However, its main focus is multicloud data placement rather than duplicate-data elimination.



\### 7. Research Gap



ADAPT optimises storage placement, cost, and availability across multiple cloud providers. Our project aims to integrate lifecycle classification with redundancy mitigation. A potential research direction is to combine lifecycle-aware classification with duplicate-data detection so that storage decisions account for both data usage and redundant copies.



\### 8. Reference



Agyekum, J., Mazumdar, S., \& Scheich, C. (2025). ADAPT: An effective data-aware multicloud data placement framework. \*Cluster Computing, 28\*, Article 825. https://doi.org/10.1007/s10586-025-05546-z



\## Paper 13: Towards Optimizing Storage Costs on the Cloud



\*\*Authors:\*\* Koyel Mukherjee, Raunak Shah, Shiv Kumar Saini, Karanpreet Singh, Khushi, Harsh Kesarwani, Kavya Barnwal, and Ayush Chauhan

\*\*Year:\*\* 2023

\*\*Conference:\*\* 2023 IEEE 39th International Conference on Data Engineering (ICDE)

\*\*Pages:\*\* 2919–2932

\*\*DOI:\*\* 10.1109/ICDE55515.2023.00223



\### 1. Objective



The paper proposes SCOPe, a unified optimisation pipeline for reducing cloud storage and data-access costs while maintaining the required performance and latency.



\### 2. Problem Addressed



Cloud data lakes can incur unnecessary costs when data is placed in unsuitable storage tiers, compression algorithms are selected without considering dataset characteristics, or data is partitioned according to ingestion batches rather than access patterns.



\### 3. Proposed Approach



SCOPe combines three components: storage-tier optimisation, compression-performance prediction, and access-pattern-aware data partitioning. The framework selects storage tiers and compression schemes using temporal access predictions and estimates of compression performance. It also formulates data partitioning as an optimisation problem that considers partition sizes and reading costs.



\### 4. Key Findings



The authors evaluate their methods using TPC-H data and enterprise datasets ranging from gigabytes to petabytes. They report cost savings of approximately 50%–83% compared with platform baselines on the evaluated enterprise data-lake datasets. The paper also provides theoretical analysis, bounds, and computational-hardness results for its optimisation problems.



\### 5. Limitations and Scope



The paper focuses on cloud storage-tier selection, compression, partitioning, and cost optimisation. It does not directly provide a complete lifecycle-classification and duplicate-data-elimination framework for large-scale repositories.



\### 6. Relevance to Our Project



Our project aims to combine automated lifecycle classification with redundancy mitigation. SCOPe demonstrates the importance of using data characteristics and access patterns to make storage decisions. Its optimisation approach provides relevant background for designing efficient repository-management strategies.



\### 7. Research Gap



SCOPe focuses on storage-tier optimisation, compression, and access-aware partitioning. Our project aims to integrate lifecycle classification with redundancy mitigation. A potential research direction is to combine lifecycle-aware classification, duplicate-data detection, and storage optimisation within a unified distributed framework.



\### 8. Reference



Mukherjee, K., Shah, R., Saini, S. K., Singh, K., Khushi, Kesarwani, H., Barnwal, K., \& Chauhan, A. (2023). Towards optimizing storage costs on the cloud. In \*2023 IEEE 39th International Conference on Data Engineering (ICDE)\* (pp. 2919–2932). https://doi.org/10.1109/ICDE55515.2023.00223



\## Paper 14: R2D2: Reducing Redundancy and Duplication in Data Lakes



\*\*Authors:\*\* Raunak Shah, Koyel Mukherjee, Atharv Tyagi, Sai Keerthana Karnam, Dhruv Joshi, Shivam Bhosale, and Subrata Mitra

\*\*Year:\*\* 2023

\*\*Journal:\*\* Proceedings of the ACM on Management of Data

\*\*Volume:\*\* 1, Issue 4

\*\*Article:\*\* 268, 25 pages

\*\*DOI:\*\* 10.1145/3626762



\### 1. Objective



The paper proposes R2D2, a framework for identifying and reducing redundant datasets in large enterprise data lakes. It addresses dataset containment, where one dataset's contents are already contained within another dataset, and aims to reduce storage and maintenance costs.



\### 2. Problem Addressed



Enterprise data lakes may contain datasets with overlapping or duplicated information. This increases storage requirements and maintenance overhead. Exhaustively comparing all dataset pairs is expensive, while deleting redundant datasets without considering future access can introduce reconstruction costs.



\### 3. Proposed Approach



R2D2 uses a three-stage hierarchical pipeline. First, a Schema Graph Builder identifies potential containment relationships using dataset schemas. Second, Min-Max Pruning removes unlikely relationships using column minimum and maximum values. Third, Content-Level Pruning examines dataset contents to further eliminate incorrect containment candidates.



After identifying containment relationships, the framework optimises which datasets can be deleted while considering storage, maintenance, reconstruction costs, and latency constraints.



\### 4. Technologies Used



The authors implement the system using Apache Spark on Azure Databricks for enterprise data stored in ADLS Gen2. They also evaluate the framework on open-source datasets using AWS infrastructure.



\### 5. Key Findings



The authors report that R2D2 can process an enterprise data lake at the terabyte scale in approximately five hours. Their experiments cover enterprise and open-source datasets. The framework aims to reduce redundancy while accounting for the costs of accessing and reconstructing deleted datasets.



\### 6. Limitations and Scope



R2D2 focuses on dataset containment and cost-aware redundancy reduction. It does not itself provide a complete automated lifecycle-classification system that categorises stored data according to usage, age, or lifecycle stage.



\### 7. Relevance to Our Project



Our project aims to integrate automated lifecycle classification with redundancy mitigation in large-scale repositories. R2D2 provides a relevant foundation for detecting redundant datasets and making cost-aware deletion decisions. Its distributed implementation also demonstrates the use of Apache Spark for large-scale data analysis.



\### 8. Research Gap



R2D2 concentrates on dataset containment, redundancy detection, and cost-aware deletion and reconstruction. Our project aims to combine redundancy mitigation with automated lifecycle classification. A potential research direction is to integrate lifecycle classification, redundancy detection, and storage-management decisions within one distributed framework.



\### 9. Reference



Shah, R., Mukherjee, K., Tyagi, A., Karnam, S. K., Joshi, D., Bhosale, S., \& Mitra, S. (2023). R2D2: Reducing redundancy and duplication in data lakes. \*Proceedings of the ACM on Management of Data, 1\*(4), Article 268. https://doi.org/10.1145/3626762





\## Paper 15: Unbalanced Big Data-Compatible Cloud Storage Method Based on Redundancy Elimination Technology



\*\*Author:\*\* Tingting Yu

\*\*Year:\*\* 2022

\*\*Journal:\*\* Scientific Programming

\*\*Article ID:\*\* 1371778

\*\*Length:\*\* 10 pages

\*\*DOI:\*\* 10.1155/2022/1371778



\### 1. Objective



The paper proposes a cloud storage method that combines data classification, compression, encryption, and redundancy elimination. Its objective is to improve storage efficiency, reduce duplicate data, and lower the storage space required for large datasets.



\### 2. Problem Addressed



Large-scale storage systems face challenges involving duplicate data, processing efficiency, imbalanced datasets, and data security. Traditional storage approaches may retain redundant files or blocks, increasing storage requirements and management overhead.



\### 3. Proposed Approach



The author develops a big-data collection and storage framework based on Hadoop and NoSQL technologies. The collected data are classified and processed, compressed using Huffman coding, and encrypted to improve data security. A deduplication algorithm identifies duplicate data objects so that redundant copies can be replaced by references to unique copies. A cloud platform manages the processed data and supports storage-resource allocation.



\### 4. Key Findings



The proposed method is evaluated using six datasets from the UCI Machine Learning Repository. The author reports a higher deduplication rate, faster duplicate-data removal, and lower storage-space requirements than the two comparison methods. The study combines classification, compression, encryption, and deduplication in a single storage-management approach.



\### 5. Limitations and Scope



The paper focuses on processing and storing unbalanced big data through classification, compression, encryption, and redundancy elimination. It does not describe a complete lifecycle-classification system based on file age, access frequency, or obsolescence.



\### 6. Relevance to Our Project



Our project aims to integrate automated lifecycle classification with redundancy mitigation in large-scale repositories. This paper provides a relevant foundation for combining data classification with deduplication and storage optimisation. Its approach also illustrates how multiple storage-management operations can be integrated into one pipeline.



\### 7. Research Gap



The paper combines data classification, compression, encryption, and redundancy elimination. Our project aims to integrate automated lifecycle classification with redundancy mitigation. A potential research direction is to combine lifecycle-based storage decisions with duplicate-data detection to improve repository storage efficiency.



\### 8. Reference



Yu, T. (2022). Unbalanced big data-compatible cloud storage method based on redundancy elimination technology. \*Scientific Programming, 2022\*, Article 1371778. https://doi.org/10.1155/2022/1371778











