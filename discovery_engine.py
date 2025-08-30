#!/usr/bin/env python3
"""
AI Project Discovery Engine - MVP Implementation
Simple CLI that asks questions and generates projects
"""

import json
import os
from typing import Dict, List, Any

class ProjectDiscovery:
    def __init__(self):
        self.context = {}
        self.conversation_flow = {
            "start": "problem_understanding",
            "problem_understanding": "user_context", 
            "user_context": "scope_definition",
            "scope_definition": "technical_assessment",
            "technical_assessment": "complete"
        }
        self.current_stage = "start"
        
    def ask_question(self, stage: str) -> str:
        """Return the right question for each discovery stage"""
        questions = {
            "problem_understanding": "What problem are you trying to solve? Describe it in plain English.",
            "user_context": "Who would use this? How many people? Where would they access it?",
            "scope_definition": "Do you want something simple that works, or something comprehensive? Think MVP vs full solution.",
            "technical_assessment": "What tools do you currently use? Any existing systems this needs to work with?"
        }
        return questions.get(stage, "Tell me more...")
    
    def process_answer(self, answer: str) -> Dict[str, Any]:
        """Process user answer and determine next step"""
        # Store the answer
        self.context[self.current_stage] = answer
        
        # Analyze and extract insights
        insights = self._analyze_answer(answer, self.current_stage)
        self.context.update(insights)
        
        # Move to next stage
        self.current_stage = self.conversation_flow.get(self.current_stage, "complete")
        
        return {
            "stage": self.current_stage,
            "insights": insights,
            "next_question": self.ask_question(self.current_stage) if self.current_stage != "complete" else None,
            "context": self.context
        }
    
    def _analyze_answer(self, answer: str, stage: str) -> Dict[str, Any]:
        """Extract structured insights from natural language answers"""
        answer_lower = answer.lower()
        insights = {}
        
        if stage == "problem_understanding":
            # Detect project type from problem description
            if any(word in answer_lower for word in ["website", "web", "online", "browser"]):
                insights["likely_project_type"] = "web_app"
            elif any(word in answer_lower for word in ["command", "script", "automate", "terminal"]):
                insights["likely_project_type"] = "cli_tool"
            elif any(word in answer_lower for word in ["data", "analyze", "process", "csv", "database"]):
                insights["likely_project_type"] = "data_pipeline"
            else:
                insights["likely_project_type"] = "unknown"
                
        elif stage == "user_context":
            # Detect scale and access patterns
            if any(word in answer_lower for word in ["just me", "personal", "myself"]):
                insights["scale"] = "personal"
            elif any(word in answer_lower for word in ["team", "few people", "colleagues"]):
                insights["scale"] = "team"
            else:
                insights["scale"] = "public"
                
        elif stage == "scope_definition":
            # Detect MVP vs comprehensive
            if any(word in answer_lower for word in ["simple", "basic", "mvp", "quick", "minimal"]):
                insights["scope"] = "mvp"
            else:
                insights["scope"] = "comprehensive"
                
        elif stage == "technical_assessment":
            # Detect existing tech stack
            if any(word in answer_lower for word in ["python", "django", "flask"]):
                insights["preferred_stack"] = "python"
            elif any(word in answer_lower for word in ["javascript", "node", "react"]):
                insights["preferred_stack"] = "javascript"
            else:
                insights["preferred_stack"] = "any"
                
        return insights
    
    def get_project_recommendation(self) -> Dict[str, Any]:
        """Generate project recommendation based on discovered context"""
        if self.current_stage != "complete":
            return {"error": "Discovery not complete"}
            
        # This is where the magic happens - convert discovery to technical decisions
        recommendation = {
            "project_type": self.context.get("likely_project_type", "web_app"),
            "technology_stack": self._recommend_tech_stack(),
            "architecture": self._recommend_architecture(),
            "deployment": self._recommend_deployment(),
            "reasoning": self._explain_choices()
        }
        
        return recommendation
    
    def _recommend_tech_stack(self) -> str:
        """Choose optimal tech stack based on discovered requirements"""
        project_type = self.context.get("likely_project_type")
        preferred_stack = self.context.get("preferred_stack", "any")
        scope = self.context.get("scope", "mvp")
        
        if preferred_stack != "any":
            return preferred_stack
            
        # MVP-first recommendations
        if project_type == "cli_tool":
            return "python"  # Fast, simple for scripts
        elif project_type == "data_pipeline":
            return "python"  # Best data ecosystem
        elif project_type == "web_app":
            if scope == "mvp":
                return "python"  # Django/Flask for rapid prototyping
            else:
                return "javascript"  # More scalable for complex web apps
        else:
            return "python"  # Default for unknown scenarios
    
    def _recommend_architecture(self) -> str:
        """Recommend architecture pattern"""
        project_type = self.context.get("likely_project_type")
        scale = self.context.get("scale", "personal")
        
        if project_type == "cli_tool":
            return "single_script"
        elif scale == "personal":
            return "monolith"
        else:
            return "modular_monolith"
    
    def _recommend_deployment(self) -> str:
        """Recommend deployment approach"""
        scale = self.context.get("scale", "personal")
        project_type = self.context.get("likely_project_type")
        
        if project_type == "cli_tool":
            return "local_install"
        elif scale == "personal":
            return "local_server"
        else:
            return "cloud_deploy"
    
    def _explain_choices(self) -> List[str]:
        """Explain why these technical choices were made"""
        explanations = []
        
        tech_stack = self._recommend_tech_stack()
        explanations.append(f"Chose {tech_stack} because it's optimal for {self.context.get('likely_project_type')} projects")
        
        if self.context.get("scope") == "mvp":
            explanations.append("Prioritized rapid development for MVP validation")
            
        scale = self.context.get("scale")
        explanations.append(f"Architecture chosen for {scale} scale usage")
        
        return explanations

def demo_discovery():
    """Demonstrate the discovery engine"""
    print("🧠 AI Project Discovery Engine - Demo")
    print("=" * 50)
    
    discovery = ProjectDiscovery()
    
    # Simulate a discovery conversation
    print(f"\nQ: {discovery.ask_question('problem_understanding')}")
    result = discovery.process_answer("I want to build a tool that helps me track my expenses and categorize them automatically")
    
    print(f"\nQ: {result['next_question']}")
    result = discovery.process_answer("Just for me personally, I'd use it on my computer")
    
    print(f"\nQ: {result['next_question']}")
    result = discovery.process_answer("Something simple that works, I just want to get started")
    
    print(f"\nQ: {result['next_question']}")
    result = discovery.process_answer("I use Excel currently, nothing fancy")
    
    # Get recommendation
    recommendation = discovery.get_project_recommendation()
    
    print("\n🎯 PROJECT RECOMMENDATION")
    print("=" * 30)
    print(f"Project Type: {recommendation['project_type']}")
    print(f"Tech Stack: {recommendation['technology_stack']}")
    print(f"Architecture: {recommendation['architecture']}")
    print(f"Deployment: {recommendation['deployment']}")
    print("\nReasoning:")
    for reason in recommendation['reasoning']:
        print(f"  • {reason}")
    
    print(f"\n📊 Discovery Context:")
    print(json.dumps(discovery.context, indent=2))

if __name__ == "__main__":
    demo_discovery()
