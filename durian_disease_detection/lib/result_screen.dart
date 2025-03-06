import 'package:flutter/material.dart';
import 'dart:io';

class ResultScreen extends StatelessWidget {
  final Map<String, dynamic> result;
  final File imageFile;

  const ResultScreen({Key? key, required this.result, required this.imageFile}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    String disease = result['predicted_class']?.toString() ?? "ไม่ทราบ";
    String confidence = result['confidence'] is num
        ? "${(result['confidence'] as num).toStringAsFixed(2)}%"
        : "N/A";

    return Scaffold(
      appBar: AppBar(
        title: const Text("ผลการวิเคราะห์"),
        centerTitle: true,
        backgroundColor: Colors.green,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Card(
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(15.0),
              ),
              elevation: 5,
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  children: [
                    ClipRRect(
                      borderRadius: BorderRadius.circular(10.0),
                      child: Image.file(imageFile, height: 250, fit: BoxFit.cover),
                    ),
                    const SizedBox(height: 20),
                    Text("\u{1F4C8} โรคที่พบ:",
                        style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.green)),
                    Text(disease,
                        style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.red)),
                    const SizedBox(height: 10),
                    Text("\u{1F4CA} ความมั่นใจ:",
                        style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.blue)),
                    Text(confidence,
                        style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w500, color: Colors.black)),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton.icon(
              icon: const Icon(Icons.replay, size: 24),
              label: const Text("วิเคราะห์ใหม่", style: TextStyle(fontSize: 18)),
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                backgroundColor: Colors.green,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              onPressed: () => Navigator.pop(context),
            ),
          ],
        ),
      ),
    );
  }
}
